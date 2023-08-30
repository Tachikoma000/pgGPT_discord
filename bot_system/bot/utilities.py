import os
import logging
import re
import asyncio
# import discord
import nextcord as discord
from .config import bot, user_timestamps, BASE_URL, logger

def format_code_for_discord(response: str) -> str:
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
    for i in range(max_retries):
        try:
            await interaction.followup.send(message)  # Updated this line
            return  # If successful, exit the function
        except discord.errors.NotFound:
            if i < max_retries - 1:  # If not the last retry attempt
                await asyncio.sleep(2 ** i)  # Exponential backoff: wait for 2^i seconds
            else:
                logger.error("Failed to send message after max retries.")

