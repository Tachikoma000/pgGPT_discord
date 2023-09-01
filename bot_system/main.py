import os
from .bot.config import bot
from .bot.handlers import (on_ready, help_command, query_subgraph_command, ask_ai_command, search_subgraph_command,
                           get_api_key, handle_interaction, handle_ai_interaction, handle_subgraph_search)

def run_main():
    TOKEN = os.getenv('DISCORD_BOT_TOKEN')
    if not TOKEN:
        raise ValueError("Missing bot token! Set it using the BOT_TOKEN environment variable.")
    
    try:
        bot.run(TOKEN)
    except KeyboardInterrupt:
        print("Shutting down gracefully...")
        bot.loop.run_until_complete(bot.close())
