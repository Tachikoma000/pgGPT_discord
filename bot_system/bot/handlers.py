"""
The provided code integrates a bot that performs various tasks on Discord. It primarily interacts with an AI service and subgraphs to query and retrieve data, 
then presents this information to users on Discord. The bot can handle interactions, fetch information from APIs, and manage the rate limits of user requests. 
Here's a brief summary of the modules and classes:

1. **Modules**:
    - Essential libraries like `os`, `time`, `logging`, etc.
    - `motor.motor_asyncio`: For asynchronous MongoDB operations.
    - `llm_system.pgGPT_v2`: An AI system for handling language queries.
    - `nextcord`: A Discord API wrapper.
    - Other utility modules specific to this project.

2. **Classes**:
    - `EntitySelectionView`: Represents a UI view for selecting entities from a list.
    - `EntityButton`: Represents a button associated with an entity.
    
3. **Functions**:
    - `check_embed_length()`: Checks the length of a Discord embed message.
    - Event handlers (`on_ready`, `help_command`, etc.): Handles specific bot events.
    - `get_api_key()`: Gets the API key from the user.
    - `handle_interaction()`: Handles the interaction for querying a subgraph.
    - `handle_ai_interaction()`: Interacts with the AI system to get a response.
    - `handle_subgraph_search()`: Searches subgraphs based on a keyword.

Developers should be aware of the rate-limiting mechanism which prevents users from making rapid successive requests. They should also note the 
event-driven nature of Discord bots, where specific events trigger specific functions.

Environment variables and other configurations are assumed to be imported from other modules, like `config`.
"""

import os
import io
import time
import logging
import datetime
import motor.motor_asyncio
from .constants import API_KEY_TIMEOUT
from llm_system.pgGPT_v2 import AILangChainV2
from .config import bot, user_timestamps, BASE_URL, logger
from .utilities import send_with_retry
from .views import EntitySelectionView
from .features.graphql_query.graphql_handler import GraphQLHandler
from .features.subgraph_catalog.mongo_handler import MongoHandler
import nextcord as discord
from nextcord.ui import View, Button
from nextcord import ButtonStyle
from nextcord.ext import commands

# ===================== Globals ======================

# Initialize logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)  # Set the logging level to DEBUG for detailed logs

formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s')
file_handler = logging.FileHandler('./loggers/pggpt_discord_bot.log')  # Save logs to file
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

# Initialize the AI language chain service
ai_service = AILangChainV2()

# ===================== Classes ======================

class EntitySelectionView(View):
    """Represents a UI view where users can select entities from a list."""
    def __init__(self, entities, interaction, handler):
        super().__init__(timeout=None)
        self.interaction = interaction
        self.handler = handler
        for entity in entities:
            self.add_item(EntityButton(label=entity, style=ButtonStyle.primary, handler=handler))

    async def on_timeout(self):
        """Send a message if the user takes too long to select an entity."""
        await self.interaction.followup.send("You took too long to select an entity. Please restart the query process if you wish to continue.", ephemeral=True)

class EntityButton(Button):
    """Represents a button associated with an entity."""
    def __init__(self, *, handler, **kwargs):
        super().__init__(**kwargs)
        self.handler = handler

    async def callback(self, interaction):
        """Callback for when the button is clicked."""
        fields = self.handler.introspect_schema().get(self.label, [])
        df = self.handler.run_query(self.label, fields)
        
        # Convert the dataframe to a CSV in-memory
        csv_buffer = io.StringIO()
        df.to_csv(csv_buffer, index=False)
        csv_buffer.seek(0)  # Move the cursor to the beginning of the file

        # Send the in-memory CSV as a file
        await interaction.response.send_message("Your query results:", file=discord.File(csv_buffer, filename=f"{self.label}.csv"))

# ===================== Helper Functions ======================

def check_embed_length(embed):
    """Checks the length of a Discord embed message to ensure it meets Discord's limits."""
    total_length = 0
    total_length += len(embed.author.name) if embed.author else 0
    total_length += len(embed.title) if embed.title else 0
    total_length += len(embed.description) if embed.description else 0
    total_length += len(embed.footer.text) if embed.footer else 0
    for field in embed.fields:
        total_length += len(field.name) + len(field.value)
    return total_length

def is_rate_limited(user_id):
    """Check if a user is rate limited."""
    if user_id in user_timestamps and time.time() - user_timestamps[user_id] < 1.0:
        return True
    user_timestamps[user_id] = time.time()
    return False

async def get_api_key(int: discord.Interaction):
    """Gets the API key from the user via DM."""
    user = int.user
    logger.debug(f"Initiating API key retrieval for user {user.id} ({user.name})")
    
    if user.dm_channel is None:
        await user.create_dm()
    await user.dm_channel.send('Please send your Playgrounds API key in this channel.')
    def check(m):
        return m.channel == user.dm_channel and m.author == user
    try:
        message = await bot.wait_for('message', check=check, timeout=60.0)
    except asyncio.TimeoutError:
        logger.warning(f"Timeout error for user {user.id} ({user.name}) while waiting for API key.")
        await user.dm_channel.send('You did not reply in time, please try again.')
    else:
        logger.info(f"API key received from user {user.id} ({user.name})")
        await user.dm_channel.send('API key received!')
        return message.content

async def create_and_send_embed(int, type, subgraph_id):
    """Create and send an embed based on the interaction type and subgraph ID."""
    user = int.user
    embed = discord.Embed(
        description=f"<@{user.id}> wants to use {int.data['name']} command! 🤖💬",
        color=discord.Color.green(),
    )
    if type == 'hello':
        embed.add_field(name=user.name, value=subgraph_id)
    else:
        embed.add_field(name="Subgraph ID", value=subgraph_id)
    response = await int.followup.send(embed=embed)
    return await int.channel.fetch_message(response.id)

async def create_thread_for_interaction(int, response):
    """Create a thread based on the interaction and return it."""
    user = int.user
    return await response.create_thread(
        name=f"{int.data['name']} by {user.name}"
    )

# ===================== Bot Event Handlers ======================

@bot.event
async def on_ready():
    """Event handler for when the bot is ready."""
    logger.info(f"We have logged in as {bot.user}")
    
# ===================== Bot Commands ======================

@bot.slash_command(name="help", description="Shows a list of all commands and their descriptions")
async def help_command(int: discord.Interaction):
    """Displays a list of available bot commands."""
    commands = {
        "hello": "Create a new thread for conversation",
        "query_subgraph": "Create a new thread for querying subgraph"
    }
    description = "\n".join(f"/{name}: {desc}" for name, desc in commands.items())
    await int.response.send_message(description)

@bot.slash_command(name="query_subgraph", description="Create a new thread for querying subgraph")
async def query_subgraph_command(int: discord.Interaction, subgraph_id: str):
    """Creates a new thread to query a subgraph."""
    bot.loop.create_task(handle_interaction(int, subgraph_id, type='subgraph'))

@bot.slash_command(name="ask_ai", description="Ask a question to Playgrounds Ai")
async def ask_ai_command(int: discord.Interaction, question: str):
    """Creates a new conversation with RAG LLM Query Engine."""
    bot.loop.create_task(handle_ai_interaction(int, question))
    
@bot.slash_command(name="search_subgraph", description="Search for relevant subgraphs based on a keyword")
async def search_subgraph_command(int: discord.Interaction, query: str):
    """Creates a new thread to search for a subgraph."""
    bot.loop.create_task(handle_subgraph_search(int, query))


# ===================== Main Functions - Respond to commands ======================

async def handle_subgraph_query(int, subgraph_id):
    """Handle the subgraph querying process."""
    api_key = await get_api_key(int)
    if not api_key:
        return
    await int.followup.send("API key received!")
    
    subgraph_url = BASE_URL.format(api_key, subgraph_id)
    handler = GraphQLHandler(subgraph_url, api_key)

    schema = handler.introspect_schema()
    entities = list(schema.keys())
    
    view = EntitySelectionView(entities, int, handler)
    await int.followup.send(f"Select an entity from the buttons below:", view=view)
    await view.wait()

async def handle_interaction(int: discord.Interaction, subgraph_id: str, type: str):
    """Handles the interaction for querying a subgraph."""
    logger.info(f"Handling interaction for user {int.user.id} ({int.user.name}) for subgraph {subgraph_id} with type {type}")
    
    await int.response.defer()

    if is_rate_limited(int.user.id):
        return

    if not isinstance(int.channel, discord.TextChannel):
        return

    response = await create_and_send_embed(int, type, subgraph_id)

    if not int.guild:
        await int.followup.send("This command can only be used within a server.", ephemeral=True)
        return

    thread = await create_thread_for_interaction(int, response)

    async with thread.typing():
        if type == 'hello':
            await thread.send(f"{int.command.name} command activated, {subgraph_id}!")
        else:
            initial_message = (f"Hello {int.user.mention},\n\n"
                               "You have started a **subgraph query**.\n\n"
                               "Step 1: I have sent you a private message asking for your Playgrounds API key. Please respond there.\n\n"
                               "Step 2: Once I have received your API key, I will fetch a list of entities from the specified subgraph. \n\n"
                               "Step 3: You will then need to send the name of the entity you wish to query. \n\n"
                               "Step 4: I will run the query and return the result in a CSV file.")
            await thread.send(initial_message)
            await handle_subgraph_query(int, subgraph_id)

async def handle_ai_interaction(int, question):
    """Interacts with the AI system to get a response."""
    logger.info(f"AI interaction started for user {int.user.id} ({int.user.name}) with question: {question}")
    try:
        await int.response.defer()
        global ai_service
        
        logger.debug(f"Querying AI service with question: {question}")
        response = ai_service.ask(question)
        logger.debug(f"AI response: {response}")

        if not response:
            logger.warning(f"No response received from AI for user {int.user.id} ({int.user.name})")
            await int.followup.send("Error occurred while processing your request.")
            return
        
        await int.followup.send(response)  # Send the AI's response as plain text
        
    except discord.errors.HTTPException as e:
        if "Must be 1024 or fewer in length" in str(e):
            logger.error(f"AI response too long for Discord's limits for user {int.user.id} ({int.user.name})")
            await int.followup.send("My response is too long for Discord's limits. Please refine your question or ask in parts.")
        else:
            logger.exception(f"HTTPException for user {int.user.id} ({int.user.name}): {e}")
            await int.followup.send("An unexpected error occurred. Please try again later.")
            
    except discord.errors.NotFound:
        logger.error("Failed to send message due to expired or unknown interaction.")
    except Exception as e:
        logger.exception(f"Unexpected error for user {int.user.id} ({int.user.name}): {e}")
        await int.followup.send("An unexpected error occurred. Please try again later.")

async def handle_subgraph_search(int: discord.Interaction, query: str):
    """Searches subgraphs based on a keyword."""
    logger.info(f"Subgraph search started for user {int.user.id} ({int.user.name}) with query: {query}")
    
    await int.response.defer()
    
    if is_rate_limited(int.user.id):
        return

    if not isinstance(int.channel, discord.TextChannel):
        logger.warning("Interaction not in a TextChannel. Aborting for user {int.user.id} ({int.user.name})")
        return

    # Use the refactored function to create and send embed
    response = await create_and_send_embed(int, 'search', query)

    # Use the refactored function to create a thread
    thread = await create_thread_for_interaction(int, response)

    async with thread.typing():
        try:
            # Initialize the MongoDB handler service
            mongo_service = MongoHandler()
            
            # Perform a general search in MongoDB using the given query
            logger.debug(f"Performing MongoDB search for query: {query}")
            items = mongo_service.perform_general_search(query)
            logger.debug(f"Found {len(items)} items from MongoDB search for query: {query}")

            # If more than 5 results are found
            if len(items) > 5:
                # Display the results 
                results = mongo_service.display_results(items)
                # Iterate through the results and send them as embeds in the thread
                for name, description, url in results:
                    embed = discord.Embed(title=name, description=description, url=url)
                    await thread.send(embed=embed)
                # Save the results to a CSV file
                csv_file_path = mongo_service.save_to_csv(items)
                # Send the CSV file to the thread
                await thread.send("I found a lot of subgraphs, here's a csv file with all of their urls:", file=discord.File(csv_file_path))
                # Remove the CSV file from the server after sending
                os.remove(csv_file_path)
            else:
                # If 5 or fewer results are found, display them directly
                results = mongo_service.display_results(items)
                # Iterate through the results and send them as embeds in the thread
                for name, description, url in results:
                    embed = discord.Embed(title=name, description=description, url=url)
                    await thread.send(embed=embed)
        except Exception as e:
            # Log the unexpected error
            logger.exception(f"Unexpected error during subgraph search for user {int.user.id} ({int.user.name}): {e}")
            # Notify the user about the failure in the search process
            await int.followup.send(f"Failed to search subgraphs: {str(e)}", ephemeral=True)