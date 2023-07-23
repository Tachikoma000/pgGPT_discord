import os
import logging
from bot_setup import get_bot
from dotenv import load_dotenv

import discord
print("Discord.py version:", discord.__version__)


load_dotenv()

logging.basicConfig(level=logging.ERROR)
logging.getLogger('discord').setLevel(logging.ERROR)
logging.getLogger('discord.client').setLevel(logging.ERROR)  # add this line
logging.getLogger('discord.gateway').setLevel(logging.ERROR)  # and this line
logger = logging.getLogger(__name__)

bot = get_bot()

token = os.getenv("BOT_TOKEN")
if not token:
    raise ValueError("Missing bot token! Set it using the BOT_TOKEN environment variable.")
bot.run(token)
