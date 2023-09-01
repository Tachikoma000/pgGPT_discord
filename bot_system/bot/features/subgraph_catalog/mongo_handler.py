import os
from dotenv import load_dotenv
from pymongo import MongoClient
import pandas as pd

class MongoHandler:
    def __init__(self):
        load_dotenv()
        MONGO_URL = os.environ.get('MONGO_URL')
        if not MONGO_URL:
            raise ValueError("Missing MongoDB URL!")
        
        self.client = MongoClient(MONGO_URL)
        self.db = self.client.dev
        self.collection = self.db.catalog_ingestion_metadata

    def perform_general_search(self, query: str) -> list:
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
        return list(self.collection.find(query_filters))

    def save_to_csv(self, items: list) -> None:
        # Restrict the dataframe to specific columns
        df = pd.DataFrame(items, columns=["location_metadata", "description", "url"])
        # Extract nested data from columns
        df['name'] = df['location_metadata'].apply(lambda x: x.get('name', ''))
        df['description'] = df['description'].apply(lambda x: x[0].get('value', '') if isinstance(x, list) else '')
        df.drop(columns=['location_metadata'], inplace=True)
        filename = "search_results.csv"
        df.to_csv("search_results.csv", index=False)
        return filename

    def display_results(self, items) -> list:
        results = []
        for item in items[:5]:  # Display only first 5
            name = item.get("location_metadata", {}).get("name", item.get("name", [{}])[0].get("value", ""))
            description = item.get("description", [{}])[0].get("value", "")
            url = item.get("url", "")
            results.append((name, description, url))
        return results
