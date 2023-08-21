import nextcord as discord
from .bot_commands import get_bot

intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
