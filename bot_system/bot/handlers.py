import os
import time
import logging
# import discord
import motor.motor_asyncio
import traceback 
from llm_system.pgGPT import AILangChain
from .config import bot, user_timestamps, BASE_URL, logger
from .utilities import send_with_retry
# from .views import FeedbackForm
from .views import EntitySelectionView
from .features.graphql_query.graphql_handler import GraphQLHandler
from .features.subgraph_catalog.mongo_handler import MongoHandler
import nextcord as discord
from nextcord.ext import commands


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
    try:
        # Rate limit
        user_id = int.user.id
        if user_id in user_timestamps and time.time() - user_timestamps[user_id] < 1.0:
            return
        user_timestamps[user_id] = time.time()
        
        if not isinstance(int.channel, discord.TextChannel):
            return

        user = int.user
        # logger.info(f"{int.data.name} command by {user} {subgraph_id}")
        try:
            embed = discord.Embed(
                description=f"<@{user.id}> wants to use {int.data['name']} command! 🤖💬",
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

        thread = await response.create_thread(
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
        # Here's the enhanced error logging
        logger.exception(f"Unexpected error: {e}")
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
        logger.error("Failed to send message due to expired or unknown interaction.")
        
async def handle_subgraph_search(int: discord.Interaction, query: str):
    logger.info(f"Received subgraph search command with query: {query}")
    
    # Defer the response immediately
    await int.response.defer()

    try:
        # Rate limit
        user_id = int.user.id
        if user_id in user_timestamps and time.time() - user_timestamps[user_id] < 1.0:
            logger.warning(f"Rate limit exceeded for user ID: {user_id}")
            return
        user_timestamps[user_id] = time.time()

        if not isinstance(int.channel, discord.TextChannel):
            logger.warning("Interaction not in a TextChannel. Aborting.")
            return

        mongo_service = MongoHandler()
        logger.info(f"Searching MongoDB with query: {query}")
        items = mongo_service.perform_general_search(query)
        logger.info(f"Found {len(items)} results for query: {query}")

        if len(items) > 5:
            logger.info("Displaying top 5 results in Discord.")
            # Display the results in an embed for Discord
            results = mongo_service.display_results(items)
            for name, description, url in results:
                embed = discord.Embed(title=name, description=description, url=url)
                await int.followup.send(embed=embed)
            
            logger.info("Saving all results to CSV.")
            # Save all results to CSV
            message = mongo_service.save_to_csv(items)
            await int.followup.send(message)

        else:
            logger.info(f"Displaying all {len(items)} results in Discord.")
            # Display the results in an embed for Discord
            results = mongo_service.display_results(items)
            for name, description, url in results:
                embed = discord.Embed(title=name, description=description, url=url)
                await int.followup.send(embed=embed)

    except Exception as e:
        logger.exception(f"Unexpected error during subgraph search: {e}")
        await int.followup.send(f"Failed to search subgraphs: {str(e)}", ephemeral=True)
