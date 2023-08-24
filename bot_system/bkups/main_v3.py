# Import required libraries
import os
import re
import time
import asyncio
import logging
import discord
from dotenv import load_dotenv
from .bot.features.graphql_query.graphql_handler import GraphQLHandler
from llm_system.pgGPT import AILangChain

# Load environment variables
load_dotenv()

# Set up logging
logging.basicConfig(
    format="[%(asctime)s] [%(filename)s:%(lineno)d] %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

# Constants
BASE_URL = "https://gateway.thegraph.com/api/{}/subgraphs/id/{}"

# Initialize discord client with specific intents
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

# Initialize command tree for discord client
tree = discord.app_commands.CommandTree(client)

# Rate limiting dictionary
user_timestamps = {}

# Declare a global dictionary to manage user sessions:
user_selections = {}

# --------------------------------- Utility Functions ---------------------------------

def format_code_for_discord(response: str) -> str:
    # Using regex to detect patterns that might be Python code
    code_patterns = [
        (r'(\w+\s*=\s*\w+\.[\s\S]+?\))', r'```python\n\1\n```'),  # Assignments
        (r'(for\s+\w+\s+in[\s\S]+?:)', r'```python\n\1\n```'),   # For loops
        (r'(if\s+\w+[\s\S]+?:)', r'```python\n\1\n```'),         # If conditions
        (r'(\w+\(\))', r'```python\n\1\n```'),                   # Function calls
        (r'(\[\w+\.\w+\])', r'```python\n\1\n```')               # Array or list indexing
    ]
    
    for pattern, replacement in code_patterns:
        response = re.sub(pattern, replacement, response)
    
    return response

async def send_message_with_retry(interaction, content=None, embed=None, view=None, max_retries=3):
    """
    A utility function to send a message with retry upon NotFound exception.
    """
    for i in range(max_retries):
        try:
            await interaction.response.send_message(content=content, embed=embed, view=view)
            break  # If the message is sent successfully, break out of the loop
        except discord.errors.NotFound:
            if i < max_retries - 1:  # Not the last retry
                await asyncio.sleep(2 ** i)  # Exponential backoff
            else:
                # If all retries failed, log the error
                logger.error("Failed to send message after maximum retries.")
                
# --------------------------------- Special Views ---------------------------------

class EntitySelectionView(discord.ui.View):
    """A View for selecting an entity from the provided list."""
    
    def __init__(self, entities, interaction, handler):
        super().__init__(timeout=120.0)  # Set timeout for 120 seconds, for example
        self.entities = entities
        self.interaction = interaction
        self.handler = handler
        for idx, entity in enumerate(entities):
            button = discord.ui.Button(label=entity, custom_id=f"entity_{entity}", style=discord.ButtonStyle.primary)
            button.callback = self.entity_button_callback
            self.add_item(button)
    
    async def entity_button_callback(self, interaction: discord.Interaction):
        logger.info(f"Entity button pressed by user {interaction.user.name} for entity {entity_name}.")
        try:
            entity_name = interaction.data["custom_id"].split("_")[1]
            fields = list(handler.introspect_schema()[entity_name])  # Get fields for the chosen entity
            user_selections[interaction.user.id] = {'entity': entity_name, 'fields': []}
            
            # Create a new view for field selection and send it
            field_view = FieldSelectionView(fields, interaction, handler, entity_name)
            await interaction.response.send_message(f"Select fields for entity {entity_name}:", view=field_view)

        except discord.errors.NotFound:
            # Error message to inform the user about the issue
            error_message = ("Sorry, there was an issue processing your request. "
                            "Please try pressing the button again. If the problem persists, contact the bot administrator.")
            
            max_retries = 3
            for attempt in range(1, max_retries + 1):
                try:
                    await interaction.followup.send(error_message, ephemeral=True)  # Using followup since the initial interaction might have expired
                    break  # If successful, exit the loop
                except discord.errors.NotFound:
                    if attempt == max_retries:
                        print("Failed to send followup message after max retries due to expired or unknown interaction.")
                        try:
                            # Attempt to DM the user if all retries fail
                            if user.dm_channel is None:
                                await user.create_dm()
                            await user.dm_channel.send(error_message)
                        except Exception as e:
                            print(f"Failed to DM the user: {e}")
                    else:
                        await asyncio.sleep(2 ** attempt)  # Exponential backoff: wait for 2^attempt seconds
                except Exception as e:
                    print(f"Failed to send followup message on attempt {attempt}: {e}")

        except Exception as e:
            # General error handling for other unforeseen issues
            print(f"Unexpected error: {e}")
            
class FieldSelectionView(discord.ui.View):
    def __init__(self, fields, interaction, handler, entity_name):
        super().__init__(timeout=120.0)
        self.fields = fields
        self.interaction = interaction
        self.handler = handler
        self.entity_name = entity_name
        for field in fields:
            button = discord.ui.Button(label=field, custom_id=f"field_{field}", style=discord.ButtonStyle.secondary)
            button.callback = self.field_button_callback
            self.add_item(button)
    
    async def field_button_callback(self, interaction: discord.Interaction):
        logger.info(f"Field button pressed by user {interaction.user.name} for field {field_name}.")
        field_name = interaction.data["custom_id"].split("_")[1]
        user_selections[interaction.user.id]['fields'].append(field_name)
        
        # Check if the field has subfields
        subfields = handler._get_fields(self.entity_name, field_name)
        if subfields:
            subfield_view = SubfieldSelectionView(subfields, interaction, handler, field_name)
            await interaction.response.send_message(f"Select subfields for {field_name}:", view=subfield_view)
        else:
            # If no subfields, store the selection and let the user continue
            user_selections[interaction.user.id]['fields'].append(field_name)
            
class SubfieldSelectionView(discord.ui.View):
    def __init__(self, subfields, interaction, handler, field_name):
        super().__init__(timeout=120.0)
        self.subfields = subfields
        self.interaction = interaction
        self.handler = handler
        self.field_name = field_name
        for subfield in subfields:
            button = discord.ui.Button(label=subfield, custom_id=f"subfield_{subfield}", style=discord.ButtonStyle.secondary)
            button.callback = self.subfield_button_callback
            self.add_item(button)
    
    async def subfield_button_callback(self, interaction: discord.Interaction):
        logger.info(f"Subfield button pressed by user {interaction.user.name} for subfield {subfield_name}.")
        subfield_name = interaction.data["custom_id"].split("_")[1]
        
        # Append the selected subfield to the user's selection
        user_selections[interaction.user.id]['fields'].append(f"{self.field_name}.{subfield_name}")

        # You can either allow the user to select multiple subfields or proceed immediately after one subfield selection.
        # If you want the user to proceed immediately:
        # await interaction.response.send_message(f"Subfield {subfield_name} selected. You can proceed to the next step or select another subfield.")
        # If you want to allow multiple subfield selections, you can simply acknowledge the button press:
        await interaction.response.send_message(f"Subfield {subfield_name} selected. Select another subfield or proceed to the next step.")


class QuerySubmitView(discord.ui.View):
    def __init__(self, selections, handler):
        super().__init__(timeout=120.0)
        self.selections = selections
        self.handler = handler
        submit_button = discord.ui.Button(label="Submit", custom_id="submit_query", style=discord.ButtonStyle.success)
        submit_button.callback = self.submit_button_callback
        self.add_item(submit_button)
    
    async def submit_button_callback(self, interaction: discord.Interaction):
        # Construct and execute the GraphQL query using selections
        df = self.handler.run_query(self.selections['entity'], self.selections['fields'])
        filename = f"{self.selections['entity']}_query_result.csv"
        self.handler.query_to_csv(df, filename)
        await interaction.response.send_message(f"Query result for {self.selections['entity']}:", file=discord.File(filename))

# --------------------------------- Event and Command Handlers ---------------------------------

@client.event
async def on_ready():
    logger.info(f"We have logged in as {client.user}")
    await tree.sync()


@tree.command(name="help", description="Shows a list of all commands and their descriptions")
async def help_command(int: discord.Interaction):
    commands = {
        "hello": "Create a new thread for conversation",
        "query_subgraph": "Create a new thread for querying subgraph"
    }
    description = "\n".join(f"/{name}: {desc}" for name, desc in commands.items())
    await int.response.send_message(description)

@tree.command(name="query_subgraph", description="Create a new thread for querying subgraph")
@discord.app_commands.checks.has_permissions(send_messages=True)
@discord.app_commands.checks.has_permissions(view_channel=True)
@discord.app_commands.checks.bot_has_permissions(send_messages=True)
@discord.app_commands.checks.bot_has_permissions(view_channel=True)
@discord.app_commands.checks.bot_has_permissions(manage_threads=True)
async def query_subgraph_command(int: discord.Interaction, subgraph_id: str):
    try:
        await int.response.send_message("Processing your request...")
        
        api_key = await get_api_key(int)
        logger.info(f"Received API key from user {int.user.name}.")

        subgraph_url = BASE_URL.format(api_key, subgraph_id)
        handler = GraphQLHandler(subgraph_url, api_key)
        
        entities = list(handler.introspect_schema().keys())
        
        view = EntitySelectionView(entities, int, handler)
        await int.followup.send(f"Select an entity from the buttons below:", view=view)

    except Exception as e:
        await int.followup.send(f"An error occurred: {e}", ephemeral=True)

@tree.command(name="ask_ai", description="Ask a question to the AI")
@discord.app_commands.checks.has_permissions(send_messages=True)
@discord.app_commands.checks.has_permissions(view_channel=True)
@discord.app_commands.checks.bot_has_permissions(send_messages=True)
@discord.app_commands.checks.bot_has_permissions(view_channel=True)
@discord.app_commands.checks.bot_has_permissions(manage_threads=True)
async def ask_ai_command(int: discord.Interaction, question: str):
    client.loop.create_task(handle_ai_interaction(int, question))

async def get_api_key(int: discord.Interaction):
    user = int.user
    if user.dm_channel is None:
        await user.create_dm()
    await user.dm_channel.send('Please send your Playgrounds API key in this channel.')
    def check(m):
        return m.channel == user.dm_channel and m.author == user
    try:
        message = await client.wait_for('message', check=check, timeout=60.0)
    except asyncio.TimeoutError:
        await user.dm_channel.send('You did not reply in time, please try again.')
    else:
        await user.dm_channel.send('API key received!')
        return message.content
    
async def handle_interaction(int: discord.Interaction, subgraph_id: str, type: str):
    try:
        # Rate limit
        user_id = int.user.id
        if user_id in user_timestamps and time.time() - user_timestamps[user_id] < 1.0:
            return
        user_timestamps[user_id] = time.time()
        
        if not isinstance(int.channel, discord.TextChannel):
            return

        user = int.user
        logger.info(f"{int.command.name} command by {user} {subgraph_id}")
        try:
            embed = discord.Embed(
                description=f"<@{user.id}> wants to use {int.command.name} command! 🤖💬",
                color=discord.Color.green(),
            )
            if type == 'hello':
                embed.add_field(name=user.name, value=subgraph_id)
            else:
                embed.add_field(name="Subgraph ID", value=subgraph_id)
            await int.response.send_message(embed=embed)
            response = await int.original_response()
        except Exception as e:
            logger.exception(e)
            await int.response.send_message(
                f"Failed to start chat {str(e)}", ephemeral=True
            )
            return


        logger.info(f"Attempting to create a thread for user {user.name} with command {int.command.name}.")
        thread = await response.create_thread(
            logger.info(f"Successfully created a thread for user {user.name} with command {int.command.name}."),
            name=f"{int.command.name} by {user.name}",
            slowmode_delay=1,
            reason="interaction-command",
            auto_archive_duration=60,
        )
        async with thread.typing():
            if type == 'hello':
                await thread.send(f"{int.command.name} command activated, {subgraph_id}!")
            else:
                initial_message = (f"Hello {user.mention},\n\n"
                                   "You have started a **subgraph query**.\n\n"
                                   "**Step 1:** I have sent you a private message asking for your Playgrounds API key. Please respond there.\n\n"
                                   "**Step 2:** Once I have received your API key, I will fetch a list of entities from the specified subgraph. \n\n"
                                   "**Step 3:** You will then need to send the name of the entity you wish to query. \n\n"
                                   "**Step 4:** I will run the query and return the result in a CSV file.")
                await thread.send(initial_message)
                api_key = await get_api_key(int)
                await thread.send("API key received!")  # Don't reveal the API key

                # Insert the API key into the URL
                subgraph_url = BASE_URL.format(api_key, subgraph_id)

                # Create GraphQLHandler instance with the subgraph URL and API key
                handler = GraphQLHandler(subgraph_url, api_key)

                # Introspect the subgraph
                schema = handler.introspect_schema()

                # Get the list of entities
                entities = list(schema.keys())
                logger.info(f"Introspected {len(entities)} entities: {', '.join(entities)}")

                # Return the list of entities to the user as buttons
                view = EntitySelectionView(entities, int, handler)
                await thread.send(f"Select an entity from the buttons below:", view=view)
                
                # The EntitySelectionView will handle the button presses and stop listening after a button is pressed
                await view.wait()  # Wait for the view to stop listening

    # More specific exception handling
    except discord.Forbidden:
        logger.exception("Bot lacks permissions to perform an action")
        await int.followup.send(
            "The bot lacks permissions to perform an action.", ephemeral=True
        )
        
    except Exception as e:
        logger.exception(e)
        await int.followup.send(
            f"Failed to start chat {str(e)}", ephemeral=True
        )

async def handle_ai_interaction(int: discord.Interaction, question: str):
    try:
        # Immediate feedback to user
        await int.response.send_message("Processing your request...")
        
        # The rest of your AI processing
        ai_service = AILangChain()
        response = ai_service.ask(question)
        response_parts = response[0][1].split("```")  # Splitting the response at code blocks
        
        # Filtering out empty strings and reconstructing the code blocks
        response_parts = [f"```{part} ```" if i%2 == 1 else part for i, part in enumerate(response_parts) if part.strip()]
        
        # Create an embed for a structured response
        embed = discord.Embed(color=discord.Color.blue())
        embed.set_author(name=f"Question by @{int.user.name}", icon_url=int.user.display_avatar.url)
        embed.add_field(name="**Question:**", value=f"```{question}```", inline=False)
        
        for part in response_parts:
            title = "**Response:**" if "```" not in part else ""  # Using the title only for text responses
            embed.add_field(name=title, value=part, inline=False)
        
        # Send the AI's response as an embed
        await int.followup.send(embed=embed)

    except discord.errors.NotFound:
        # Log the error and potentially retry
        print("Failed to send message due to expired or unknown interaction.")


# --------------------------------- Main Execution ---------------------------------

def run_main():
    TOKEN = os.getenv('DISCORD_BOT_TOKEN')
    if not TOKEN:
        raise ValueError("Missing bot token! Set it using the BOT_TOKEN environment variable.")
    client.run(TOKEN)
