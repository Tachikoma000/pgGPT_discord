import os
import time
import logging
import datetime
import motor.motor_asyncio
import traceback 
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

ai_service = AILangChainV2()

class EntitySelectionView(View):
    def __init__(self, entities, interaction, handler):
        super().__init__(timeout=None)
        self.interaction = interaction
        self.handler = handler
        for entity in entities:
            self.add_item(EntityButton(label=entity, style=ButtonStyle.primary, handler=handler))

    async def on_timeout(self):
        await self.interaction.followup.send("You took too long to select an entity. Please restart the query process if you wish to continue.", ephemeral=True)

class EntityButton(Button):
    def __init__(self, *, handler, **kwargs):
        super().__init__(**kwargs)
        self.handler = handler

    async def callback(self, interaction):
        fields = self.handler.introspect_schema().get(self.label, [])
        df = self.handler.run_query(self.label, fields)
        filename = f"{self.label}.csv"
        df.to_csv(filename, index=False)
        await interaction.response.send_message("Your query results:", file=discord.File(filename))
        
def check_embed_length(embed):
    total_length = 0
    total_length += len(embed.author.name) if embed.author else 0
    total_length += len(embed.title) if embed.title else 0
    total_length += len(embed.description) if embed.description else 0
    total_length += len(embed.footer.text) if embed.footer else 0
    for field in embed.fields:
        total_length += len(field.name) + len(field.value)
    return total_length

@bot.event
async def on_ready():
    logger.info(f"We have logged in as {bot.user}")

@bot.slash_command(name="help", description="Shows a list of all commands and their descriptions")
async def help_command(int: discord.Interaction):
    commands = {
        "hello": "Create a new thread for conversation",
        "query_subgraph": "Create a new thread for querying subgraph"
    }
    description = "\n".join(f"/{name}: {desc}" for name, desc in commands.items())
    await int.response.send_message(description)

@bot.slash_command(name="query_subgraph", description="Create a new thread for querying subgraph")
async def query_subgraph_command(int: discord.Interaction, subgraph_id: str):
    bot.loop.create_task(handle_interaction(int, subgraph_id, type='subgraph'))

@bot.slash_command(name="ask_ai", description="Ask a question to Playgrounds Ai")
async def ask_ai_command(int: discord.Interaction, question: str):
    bot.loop.create_task(handle_ai_interaction(int, question))
    
@bot.slash_command(name="search_subgraph", description="Search for relevant subgraphs based on a keyword")
async def search_subgraph_command(int: discord.Interaction, query: str):
    bot.loop.create_task(handle_subgraph_search(int, query))


async def get_api_key(int: discord.Interaction):
    user = int.user
    if user.dm_channel is None:
        await user.create_dm()
    await user.dm_channel.send('Please send your Playgrounds API key in this channel.')
    def check(m):
        return m.channel == user.dm_channel and m.author == user
    try:
        message = await bot.wait_for('message', check=check, timeout=60.0)
    except asyncio.TimeoutError:
        await user.dm_channel.send('You did not reply in time, please try again.')
    else:
        await user.dm_channel.send('API key received!')
        return message.content
    

async def handle_interaction(int: discord.Interaction, subgraph_id: str, type: str):
    # Defer the interaction immediately
    await int.response.defer()
    try:
        # Rate limit
        user_id = int.user.id
        if user_id in user_timestamps and time.time() - user_timestamps[user_id] < 1.0:
            return
        user_timestamps[user_id] = time.time()
        
        if not isinstance(int.channel, discord.TextChannel):
            return

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
        response = await int.channel.fetch_message(response.id)

        if not int.guild:
            await int.followup.send("This command can only be used within a server.", ephemeral=True)
            return

        thread = await response.create_thread(
            name=f"{int.data['name']} by {user.name}",
            # slowmode_delay=1,
            # reason="interaction-command",
            # auto_archive_duration=60,
        )
        
        async with thread.typing():
            if type == 'hello':
                await thread.send(f"{int.command.name} command activated, {subgraph_id}!")
            else:
                initial_message = (f"Hello {user.mention},\n\n"
                                   "You have started a **subgraph query**.\n\n"
                                   "Step 1: I have sent you a private message asking for your Playgrounds API key. Please respond there.\n\n"
                                   "Step 2: Once I have received your API key, I will fetch a list of entities from the specified subgraph. \n\n"
                                   "Step 3: You will then need to send the name of the entity you wish to query. \n\n"
                                   "Step 4: I will run the query and return the result in a CSV file.")
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
                
                # Return the list of entities to the user as buttons
                view = EntitySelectionView(entities, int, handler)
                await thread.send(f"Select an entity from the buttons below:", view=view)

                # The EntitySelectionView will handle the button presses and stop listening after a button is pressed
                await view.wait()  # Wait for the view to stop listening

    except discord.Forbidden:
        logger.exception("Bot lacks permissions to perform an action")
        await int.followup.send("The bot lacks permissions to perform an action.", ephemeral=True)

    except Exception as e:
        logger.exception(e)
        logger.exception(f"Unexpected error: {e}")
        await int.followup.send(f"Failed to start chat {str(e)}", ephemeral=True)

async def handle_ai_interaction(int, question):
    try:
        await int.response.defer()
        global ai_service
        response = ai_service.ask(question)
        print(f"AI response: {response}")

        if not response:
            await int.followup.send("Error occurred while processing your request.")
            return
        
        await int.followup.send(response)  # Send the AI's response as plain text
    except discord.errors.HTTPException as e:
        if "Must be 1024 or fewer in length" in str(e):
            await int.followup.send("My response is too long for Discord's limits. Please refine your question or ask in parts.")
        else:
            await int.followup.send("An unexpected error occurred. Please try again later.")
    except discord.errors.NotFound:
        logger.error("Failed to send message due to expired or unknown interaction.")
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        await int.followup.send("An unexpected error occurred. Please try again later.")

async def handle_subgraph_search(int: discord.Interaction, query: str):
    await int.response.defer()
    try:
        user_id = int.user.id
        if user_id in user_timestamps and time.time() - user_timestamps[user_id] < 1.0:
            logger.warning(f"Rate limit exceeded for user ID: {user_id}")
            return
        user_timestamps[user_id] = time.time()

        if not isinstance(int.channel, discord.TextChannel):
            logger.warning("Interaction not in a TextChannel. Aborting.")
            return

        user = int.user

        # Set up the embed message
        embed = discord.Embed(title="Subgraph Search Initiated 🔍", color=discord.Color.blue())
        embed.set_author(name=int.user.name, icon_url=int.user.display_avatar.url)
        embed.description = f"Searching subgraph catalog for all subgraphs related to: **{query}**\n\nPlease open this thread to view the subgraphs I find."
        embed.set_footer(text="Requested on")
        embed.timestamp = datetime.datetime.utcnow()
        response = await int.followup.send(embed=embed)
        response = await int.channel.fetch_message(response.id)

        # Create the thread
        thread = await response.create_thread(
            name=f"{int.data['name']} by {user.name}",
            auto_archive_duration=60,
        )

        async with thread.typing():
            mongo_service = MongoHandler()
            items = mongo_service.perform_general_search(query)

            if len(items) > 5:
                results = mongo_service.display_results(items)
                for name, description, url in results:
                    embed = discord.Embed(title=name, description=description, url=url)
                    await thread.send(embed=embed)
                csv_file_path = mongo_service.save_to_csv(items)
                await thread.send("I found a lot of subgraphs, here's a csv file with all of their urls:", file=discord.File(csv_file_path))
                os.remove(csv_file_path)
            else:
                results = mongo_service.display_results(items)
                for name, description, url in results:
                    embed = discord.Embed(title=name, description=description, url=url)
                    await thread.send(embed=embed)

    except Exception as e:
        logger.exception(f"Unexpected error during subgraph search: {e}")
        await int.followup.send(f"Failed to search subgraphs: {str(e)}", ephemeral=True)

