# Import required libraries
import discord
from discord import Message as DiscordMessage
import logging
from bot.features.graphql_query.graphql_handler import GraphQLHandler
import asyncio
import os
import validators
import time
from dotenv import load_dotenv

load_dotenv()

# Set up logging
logging.basicConfig(
    format="[%(asctime)s] [%(filename)s:%(lineno)d] %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

# Base URL for the subgraph API
BASE_URL = "https://gateway.thegraph.com/api/{}/subgraphs/id/{}"

# Create a discord client with specific intents
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

# Create a command tree for the discord client
tree = discord.app_commands.CommandTree(client)

# Initialize a dictionary for rate limiting
user_timestamps = {}

# Function to get API key from a user through direct message
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

# Event that runs when the bot has connected to discord
@client.event
async def on_ready():
    logger.info(f"We have logged in as {client.user}")
    await tree.sync()

# Command to start a conversation thread
@tree.command(name="hello", description="Create a new thread for conversation")
@discord.app_commands.checks.has_permissions(send_messages=True)
@discord.app_commands.checks.has_permissions(view_channel=True)
@discord.app_commands.checks.bot_has_permissions(send_messages=True)
@discord.app_commands.checks.bot_has_permissions(view_channel=True)
@discord.app_commands.checks.bot_has_permissions(manage_threads=True)
async def hello_command(int: discord.Interaction, username: str):
    client.loop.create_task(handle_interaction(int, username, type='hello'))

# Command to query a subgraph and return the result in a new thread
@tree.command(name="query_subgraph", description="Create a new thread for querying subgraph")
@discord.app_commands.checks.has_permissions(send_messages=True)
@discord.app_commands.checks.has_permissions(view_channel=True)
@discord.app_commands.checks.bot_has_permissions(send_messages=True)
@discord.app_commands.checks.bot_has_permissions(view_channel=True)
@discord.app_commands.checks.bot_has_permissions(manage_threads=True)
async def query_subgraph_command(int: discord.Interaction, subgraph_id: str): # Changed from subgraph_url to subgraph_id
    client.loop.create_task(handle_interaction(int, subgraph_id, type='subgraph')) # Changed from subgraph_url to subgraph_id

# Function to handle interactions from the commands
async def handle_interaction(int: discord.Interaction, subgraph_id: str, type: str): # Changed from input_data to subgraph_id
    try:
        # Rate limit
        user_id = int.user.id
        if user_id in user_timestamps and time.time() - user_timestamps[user_id] < 1.0:
            return
        user_timestamps[user_id] = time.time()
        
        if not isinstance(int.channel, discord.TextChannel):
            return

        user = int.user
        logger.info(f"{int.command.name} command by {user} {subgraph_id}") # Changed from input_data to subgraph_id
        try:
            embed = discord.Embed(
                description=f"<@{user.id}> wants to use {int.command.name} command! 🤖💬",
                color=discord.Color.green(),
            )
            if type == 'hello':
                embed.add_field(name=user.name, value=subgraph_id) # Changed from input_data to subgraph_id
            else:
                embed.add_field(name="Subgraph ID", value=subgraph_id) # Changed from input_data to subgraph_id
            await int.response.send_message(embed=embed)
            response = await int.original_response()
        except Exception as e:
            logger.exception(e)
            await int.response.send_message(
                f"Failed to start chat {str(e)}", ephemeral=True
            )
            return

        thread = await response.create_thread(
            name=f"{int.command.name} by {user.name}",
            slowmode_delay=1,
            reason="interaction-command",
            auto_archive_duration=60,
        )
        async with thread.typing():
            if type == 'hello':
                await thread.send(f"{int.command.name} command activated, {subgraph_id}!") # Changed from input_data to subgraph_id
                    
            else:
                initial_message = f"Hello {user.mention},\n\n" \
                                "You have started a **subgraph query**.\n\n" \
                                "**Step 1:** I have sent you a private message asking for your Playgrounds API key. Please respond there.\n\n" \
                                "**Step 2:** Once I have received your API key, I will fetch a list of entities from the specified subgraph. \n\n" \
                                "**Step 3:** You will then need to send the name of the entity you wish to query. \n\n" \
                                "**Step 4:** I will run the query and return the result in a CSV file."
                await thread.send(initial_message)
                api_key = await get_api_key(int)
                await thread.send("API key received!")  # Don't reveal the API key

                # Insert the API key into the URL
                subgraph_url = BASE_URL.format(api_key, subgraph_id) # Changed from input_data to subgraph_id

                # Create GraphQLHandler instance with the subgraph URL and API key
                handler = GraphQLHandler(subgraph_url, api_key)

                # Introspect the subgraph
                schema = handler.introspect_schema()

                # Get the list of entities
                entities = list(schema.keys())

                # Return the list of entities to the user
                await thread.send(f"The entities in the subgraph are:\n- " + "\n- ".join(entities))

                # Continuously listen for new messages in the thread
                while True:
                    entity_msg = await client.wait_for('message', check=lambda m: m.channel == thread and m.author == user)
                    entity_name = entity_msg.content

                    if entity_name in entities:
                        fields = schema[entity_name]
                        df = handler.run_query(entity_name, fields)

                        filename = f"{entity_name}_query_result.csv"
                        handler.query_to_csv(df, filename)

                        await thread.send(file=discord.File(filename))
                        os.remove(filename)
                    else:
                        await thread.send(f"Invalid entity name: {entity_name}. Please try again.")
                        
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

# New help command
@tree.command(name="help", description="Shows a list of all commands and their descriptions")
async def help_command(int: discord.Interaction):
    commands = {
        "hello": "Create a new thread for conversation",
        "query_subgraph": "Create a new thread for querying subgraph",
        # Add all other commands here
    }
    description = "\n".join(f"/{name}: {desc}" for name, desc in commands.items())
    await int.response.send_message(description)

# Run the discord bot
TOKEN = os.getenv('DISCORD_BOT_TOKEN')
if not TOKEN:
    raise ValueError("Missing bot token! Set it using the BOT_TOKEN environment variable.")
client.run(TOKEN)
