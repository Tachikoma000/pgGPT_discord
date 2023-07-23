import discord
from discord.ext import commands
from ai_system import setup_chat_engine
import logging
from discord import File
from graphql_handler import GraphQLHandler
import asyncio
import os

logger = logging.getLogger(__name__)

chat_engine = setup_chat_engine()

async def get_api_key(ctx):
    if ctx.author.dm_channel is None:
        await ctx.author.create_dm()

    await ctx.author.dm_channel.send('Please send your API key in this channel.')

    def check(m):
        return m.channel == ctx.author.dm_channel and m.author == ctx.author

    try:
        message = await ctx.bot.wait_for('message', check=check, timeout=60.0)
    except asyncio.TimeoutError:
        await ctx.author.dm_channel.send('You did not reply in time, please try again.')
    else:
        await ctx.author.dm_channel.send('API key received!')
        return message.content

def setup(bot):
    @bot.command(name='start')
    async def start(ctx):
        thread = await ctx.channel.start_thread(name="Test Thread")
        await thread.send("Hello, world!")

    @bot.command(name='ask')
    async def ask(ctx, *, question):
        try:
            response = chat_engine.chat(question)
            response_text = response.response
            await ctx.send(response_text)
        except discord.DiscordException as e:
            logger.error(f"An Discord error occurred: {e}")
            await ctx.send("An error occurred while processing your request. Please try again.")
        except Exception as e:
            logger.error(f"An unexpected error occurred: {e}")
            await ctx.send("An unexpected error occurred. Please try again later.")
            
    @bot.command(name='query')
    async def query(ctx, subgraph_id: str, deployment: bool=False):
        api_key = await get_api_key(ctx)

        handler = GraphQLHandler(subgraph_id, api_key, deployment)
        
        loading_messages = [
            "Reading Subgraph...",
            "Understanding schema...",
            "Identifying entities and fields...",
            "Preparing interaction..."
        ]
        
        for msg in loading_messages:
            await ctx.send(msg)
            await asyncio.sleep(1)  # sleep for 1 second

        schema = handler.introspect_schema()

        # Get a list of entities from the schema
        entities = list(schema.keys())

        # Format entities list as bullet points
        formatted_entities = "\n- ".join(entities)

        # Send a message with the list of entities
        # Send a message with the list of entities
        await ctx.send(f"Awesome! Here are the exciting entities we discovered:\n- {formatted_entities}\n\nPlease reply with the name of the entity you want to query. We recommend copy-pasting to avoid spelling mistakes!")

        # Wait for the user to reply with an entity
        entity = await ctx.bot.wait_for('message', check=lambda m: m.author == ctx.author, timeout=60.0)

        # Check if the chosen entity is valid
        if entity.content not in entities:
            await ctx.send("Invalid entity. Please try again.")
            return

        # Get the fields for the selected entity from the schema
        fields = schema[entity.content]

        # Format fields list as bullet points
        formatted_fields = "\n- ".join(fields)

        # Send a message with the list of fields for the chosen entity
        # Send a message with the list of fields for the chosen entity
        await ctx.send(f"Great choice! Here are the available fields for {entity.content}:\n- {formatted_fields}\n\nPlease reply with the name of the field you want to query. Copy-pasting is a good idea to avoid spelling mistakes!")

        # Wait for the user to reply with a field
        field = await ctx.bot.wait_for('message', check=lambda m: m.author == ctx.author, timeout=60.0)

        # Check if the chosen field is valid
        if field.content not in fields:
            await ctx.send("Invalid field. Please try again.")
            return

        # Now we have the entity and field the user wants to query
        # You can use these to build your GraphQL query
        df = handler.run_query(entity.content, [field.content])

        # Save the query result to a csv file
        filename = f"{entity.content}_{field.content}_query_result.csv"
        handler.query_to_csv(df, filename)

        # Send the csv file back to the user
        await ctx.send(file=discord.File(filename))
        
        # Delete the file
        os.remove(filename)

    @bot.event
    async def on_ready():
        print("Everything's all ready to go~")
        print("Registered commands: ", [command.name for command in bot.commands])

    @bot.event
    async def on_message(message):
        print("The message's content was", message.content)
        await bot.process_commands(message)

    @bot.command()
    async def ping(ctx):
        latency = bot.latency
        await ctx.send(latency)

    @bot.command()
    async def echo(ctx, *, content:str):
        await ctx.send(content)
