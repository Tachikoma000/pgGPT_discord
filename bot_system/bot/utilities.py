import os
import logging
import re
import asyncio
import nextcord as discord
from .config import bot, user_timestamps, BASE_URL, logger

def format_code_for_discord(response: str) -> str:
    """
    Format given strings that match common Python code patterns with Discord markdown for code blocks.
    
    Args:
        response (str): The input string potentially containing Python code snippets.
    
    Returns:
        str: The formatted string with detected Python code snippets wrapped in Discord markdown for code blocks.
    """
    
    # Using regex to detect patterns that might be Python code
    code_patterns = [
        (r'(\w+\s*=\s*\w+\.[\s\S]+?\))', r'```python\n\1\n```'),  # Assignments
        (r'(for\s+\w+\s+in[\s\S]+?:)', r'```python\n\1\n```'),   # For loops
        (r'(if\s+\w+[\s\S]+?:)', r'```python\n\1\n```'),         # If conditions
        (r'(\w+\(\))', r'```python\n\1\n```'),                   # Function calls
        (r'(\[\w+\.\w+\])', r'```python\n\1\n```')               # Array or list indexing
    ]
    
    for pattern, replacement in code_patterns:
        response = re.sub(pattern, replacement, response)
    
    return response

async def send_with_retry(interaction, message, max_retries=3):
    """
    Asynchronously send a message using a Discord interaction. 
    If unsuccessful, it will retry up to the specified maximum retries.
    
    Args:
        interaction (discord.Interaction): The Discord interaction context.
        message (str): The message to send.
        max_retries (int, optional): Maximum number of retries. Defaults to 3.
    
    Returns:
        None: If the message was successfully sent or max retries was reached.
    """
    
    for i in range(max_retries):
        try:
            await interaction.followup.send(message)
            return  # If successful, exit the function
        except discord.errors.NotFound:
            if i < max_retries - 1:  # If not the last retry attempt
                await asyncio.sleep(2 ** i)  # Exponential backoff: wait for 2^i seconds
            else:
                logger.error("Failed to send message after max retries.")
