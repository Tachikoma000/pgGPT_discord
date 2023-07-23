import discord
from discord.ext import commands
from bot_commands import setup

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
intents.guilds = True

def get_bot():
    bot = commands.Bot(command_prefix='$', intents=intents)
    setup(bot)
    return bot
