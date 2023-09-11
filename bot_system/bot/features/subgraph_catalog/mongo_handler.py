"""
This module facilitates interactions with a MongoDB collection that stores metadata for a catalog.
The primary use of this module is to search the catalog based on a given query and retrieve relevant entries.

The MongoHandler class handles the primary operations:
1. Connects to the MongoDB instance using connection details from environment variables.
2. Searches the catalog collection using a range of filters.
3. Formats and restricts the search results, then saves them to a CSV file.
4. Displays a limited number of search results.

To use this module, ensure the environment variable 'MONGO_URL' is set correctly. The MongoDB collection is expected to 
contain specific fields as used in this module. If the database schema changes, this module will need updates accordingly.
"""

import os
from dotenv import load_dotenv
from pymongo import MongoClient
import pandas as pd
import logging

# =============== Logging Configuration ================

# Initialize logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)  # Set the logging level to DEBUG for detailed logs

formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s')
file_handler = logging.FileHandler('pggpt_mongo_handler.log')  # Save logs to file
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

# =============== Main Class ================

class MongoHandler:
    def __init__(self):
        """Initializes the MongoDB client and sets up the database and collection."""
        load_dotenv()
        MONGO_URL = os.environ.get('MONGO_URL')
        if not MONGO_URL:
            logger.error("Missing MongoDB URL!")
            raise ValueError("Missing MongoDB URL!")
        
        self.client = MongoClient(MONGO_URL)
        self.db = self.client.dev
        self.collection = self.db.catalog_ingestion_metadata
        logger.info("MongoHandler initialized successfully.")

    def perform_general_search(self, query: str) -> list:
        """Searches the catalog collection using a range of filters based on the given query."""
        query_filters = {
            "$or": [
                {"description.value": query},
                {"name.value": query},
                {"url": query},
                {"tags": query},
                {"location_metadata.subgraph_id": query},
                {"location_metadata.owner_address": query},
                {"location_metadata.author": query},
                {'location_metadata.name': query}
            ]
        }
        logger.info(f"Performing general search with query: {query}")
        return list(self.collection.find(query_filters))

    def save_to_csv(self, items: list) -> None:
        """Saves the given list of items to a CSV file."""
        df = pd.DataFrame(items, columns=["location_metadata", "description", "url"])
        df['name'] = df['location_metadata'].apply(lambda x: x.get('name', ''))
        df['description'] = df['description'].apply(lambda x: x[0].get('value', '') if isinstance(x, list) else '')
        df.drop(columns=['location_metadata'], inplace=True)
        
        filename = "search_results.csv"
        df.to_csv(filename, index=False)
        logger.info(f"Search results saved to {filename}")
        return filename

    def display_results(self, items) -> list:
        """Formats and returns a limited number of search results."""
        results = []
        for item in items[:5]:  # Display only first 5
            name = item.get("location_metadata", {}).get("name", item.get("name", [{}])[0].get("value", ""))
            description = item.get("description", [{}])[0].get("value", "")
            url = item.get("url", "")
            results.append((name, description, url))
        logger.debug(f"Display results: {results}")
        return results
