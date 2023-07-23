import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
intents.guilds = True
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print("Everything's all ready to go~")

@bot.event
async def on_message(message):
    print("The message's content was", message.content)
    await bot.process_commands(message)

@bot.command()
async def ping(ctx):
    '''
    This text will be shown in the help command
    '''
    # Get the latency of the bot
    latency = bot.latency  # Included in the Discord.py library
    # Send it to the user
    await ctx.send(latency)

@bot.command()
async def echo(ctx, *, content:str):
    await ctx.send(content)

def get_bot():
    return bot
