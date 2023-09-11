import requests
from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport
import pandas as pd
import logging

# Initialize logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)  # Set the logging level to DEBUG for detailed logs

formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s')
file_handler = logging.FileHandler('pggpt_graph_handler.log')  # Save logs to file
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

class GraphQLHandler:
    # This handler will be responsible for interacting with the Subgraph URL and executing GraphQL queries. 
    def __init__(self, subgraph_url, api_key=None, deployment=False):
        logger.info(f"Initializing GraphQLHandler with subgraph_url: {subgraph_url} and deployment: {deployment}")
        self.subgraph_url = subgraph_url
        self.api_key = api_key
        self.deployment = deployment
        self.subgraph_id = subgraph_url.split('/')[-1]  # Extracts the subgraph ID from the URL
        self.client = self.setup_client()

    def setup_client(self):
        headers = {
            "Content-Type": "application/json",
        }
        if self.api_key:
            headers["Playgrounds-Api-Key"] = self.api_key
            logger.debug("API key provided for GraphQL client setup.")

        url = f"https://api.playgrounds.network/v1/proxy/subgraphs/id/{self.subgraph_id}"
        if self.deployment:
            url = f"https://api.playgrounds.network/v1/proxy/deployments/id/{self.subgraph_id}"

        logger.debug(f"Setting up GraphQL client with URL: {url}")
        transport = RequestsHTTPTransport(
            url=url,
            headers=headers,
            use_json=True,
        )
        client = Client(transport=transport, fetch_schema_from_transport=True)
        return client

    def introspect_schema(self):
        logger.info("Initiating schema introspection.")
        introspection_query = gql(
            """
            query {
                __schema {
                    types {
                        name
                        fields {
                            name
                            type {
                                kind
                                name
                                fields {
                                    name
                                }
                            }
                        }
                    }
                }
            }
            """
        )
        result = self.client.execute(introspection_query)
        schema = {}
        for type_ in result['__schema']['types']:
            if type_['name'] != '__schema':
                entity_name = type_['name']
                fields = self._get_fields(type_)
                if fields:
                    schema[entity_name] = fields
        logger.debug("Schema introspection completed.")
        return schema

    def _get_fields(self, type_):
        fields = []
        for f in (type_.get('fields') or []):
            if f['name'] != '__typename' and not (f['name'].endswith('_filter') or f['name'].endswith('_orderBy') or f['name'].islower()):
                fields.append(f['name'])
                if f.get('type') and f['type'].get('fields'):
                    fields.extend(self._get_fields(f['type']))
        return fields

    def run_query(self, entity, fields):
        logger.info(f"Executing GraphQL query for entity: {entity}")
        entity = entity[0].lower() + entity[1:] + 's'
        fields_str = ", ".join(fields)
        query_str = f"""
        query {{
            {entity} {{
                {fields_str}
            }}
        }}
        """
        query = gql(query_str)
        result = self.client.execute(query)
        df = pd.DataFrame(result[entity])
        logger.debug(f"Query for entity: {entity} completed.")
        return df

    def query_to_csv(self, df, filename):
        logger.info(f"Saving query results to CSV file: {filename}")
        df.to_csv(filename, index=False)
        logger.debug(f"Query results saved to {filename}.")
