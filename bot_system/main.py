import os
from .bot.config import bot
from .bot.handlers import on_ready, help_command, query_subgraph_command, ask_ai_command, get_api_key, handle_interaction, handle_ai_interaction

def run_main():
    TOKEN = os.getenv('DISCORD_BOT_TOKEN')
    if not TOKEN:
        raise ValueError("Missing bot token! Set it using the BOT_TOKEN environment variable.")
    bot.run(TOKEN)
