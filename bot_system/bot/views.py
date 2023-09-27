import os
import logging
import asyncio
from .config import bot, user_timestamps, BASE_URL, logger
import nextcord as discord

class EntitySelectionView(discord.ui.View):
    """
    A Discord UI View for selecting an entity from the provided list.
    
    Attributes:
        entities (list): List of entities to choose from.
        interaction (discord.Interaction): The Discord interaction context.
        handler (object): Handler that contains methods to process entity data.
    """
    
    def __init__(self, entities, interaction, handler):
        """
        Initialize the EntitySelectionView.
        
        Args:
            entities (list): List of entities to choose from.
            interaction (discord.Interaction): The Discord interaction context.
            handler (object): Handler that contains methods to process entity data.
        """
        super().__init__(timeout=300.0)  # Set timeout for 300 seconds
        self.entities = entities
        self.interaction = interaction
        self.handler = handler
        for idx, entity in enumerate(entities):
            button = discord.ui.Button(label=entity, custom_id=f"entity_{entity}", style=discord.ButtonStyle.primary)
            button.callback = self.entity_button_callback
            self.add_item(button)
    
    async def entity_button_callback(self, interaction: discord.Interaction):
        """
        Callback function executed when an entity button is pressed.
        
        Args:
            interaction (discord.Interaction): The Discord interaction context.
        """
        user = interaction.user
        try:
            entity_name = interaction.data["custom_id"].split("_")[1]
            fields = self.handler.introspect_schema()[entity_name]
            df = self.handler.run_query(entity_name, fields)

            filename = f"{entity_name}_query_result.csv"
            self.handler.query_to_csv(df, filename)
            
            # Check if the file size is larger than the Discord upload limit (8MB)
            file_size = os.path.getsize(filename)
            if file_size > 8 * 1024 * 1024:  # 8MB in bytes
                await interaction.response.send_message(f"The file for {entity_name} is too large to send on Discord. Please try a different entity or reduce the queried data.")
                os.remove(filename)
                return
            
            await interaction.response.send_message(f"Here's the query result for entity: {entity_name}", file=discord.File(filename))
            os.remove(filename)
            self.stop()  # Stop this view from listening to further interactions

        except discord.errors.NotFound:
            error_message = ("Sorry, there was an issue processing your request. "
                            "Please try pressing the button again. If the problem persists, contact the bot administrator.")
            
            max_retries = 3
            for attempt in range(1, max_retries + 1):
                try:
                    await interaction.followup.send(error_message, ephemeral=True)  # Using followup since the initial interaction might have expired
                    break
                except discord.errors.NotFound:
                    if attempt == max_retries:
                        logger.error("Failed to send followup message after max retries due to expired or unknown interaction.")
                        try:
                            # Attempt to DM the user if all retries fail
                            if user.dm_channel is None:
                                await user.create_dm()
                            await user.dm_channel.send(error_message)
                        except Exception as e:
                            logger.error(f"Failed to DM the user: {e}")
                    else:
                        await asyncio.sleep(2 ** attempt)  # Exponential backoff: wait for 2^attempt seconds
                except Exception as e:
                    logger.error(f"Failed to send followup message on attempt {attempt}: {e}")

        except Exception as e:
            # Log any other unexpected errors
            logger.error(f"Unexpected error: {e}")