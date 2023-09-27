import os
from .bot.config import bot
from .bot.handlers import (
    on_ready, help_command, query_subgraph_command, 
    ask_ai_command, search_subgraph_command,
    get_api_key, handle_interaction, handle_ai_interaction, 
    handle_subgraph_search
)

def run_main():
    """
    Entry point function to start the Discord bot.
    
    This function:
    1. Retrieves the bot token from the environment variables.
    2. Starts the bot using the retrieved token.
    3. Handles graceful shutdown of the bot on keyboard interrupts.
    """
    
    # Retrieve the Discord bot token from environment variables
    TOKEN = os.getenv('DISCORD_BOT_TOKEN')
    
    # Check if the bot token is available
    if not TOKEN:
        raise ValueError("Missing bot token! Set it using the BOT_TOKEN environment variable.")
    
    try:
        # Start the bot using the token
        bot.run(TOKEN)
    except KeyboardInterrupt:
        # Handle graceful shutdown on keyboard interrupts (e.g., Ctrl+C)
        print("Shutting down gracefully...")
        bot.loop.run_until_complete(bot.close())
