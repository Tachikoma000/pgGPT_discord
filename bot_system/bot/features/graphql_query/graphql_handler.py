import requests
from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport
import pandas as pd

class GraphQLHandler:
    # This handler will be responsible for interacting with the Subgraph URL and executing GraphQL queries. 
    def __init__(self, subgraph_url, api_key=None, deployment=False):
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

        url = f"https://api.playgrounds.network/v1/proxy/subgraphs/id/{self.subgraph_id}"
        if self.deployment:
            url = f"https://api.playgrounds.network/v1/proxy/deployments/id/{self.subgraph_id}"

        transport = RequestsHTTPTransport(
            url=url,
            headers=headers,
            use_json=True,
        )
        client = Client(transport=transport, fetch_schema_from_transport=True)
        return client

    def introspect_schema(self):
        # Schema Introspection
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
                # Ignore system types and types related to a specific entity
                if not (entity_name.startswith('_') or entity_name.endswith('_filter') or entity_name.endswith('_orderBy') or entity_name.islower()):
                    fields = self._get_fields(type_)
                    if fields:
                        schema[entity_name] = fields
        return schema

    def _get_fields(self, type_):
        fields = []
        for f in (type_.get('fields') or []):
            # Ignore system fields and fields related to a specific entity
            if f['name'] != '__typename' and not (f['name'].endswith('_filter') or f['name'].endswith('_orderBy') or f['name'].islower()):
                fields.append(f['name'])
                if f.get('type') and f['type'].get('fields'):
                    fields.extend(self._get_fields(f['type']))
        return fields

    def run_query(self, entity, fields):
        # Convert the entity name to camelCase and pluralize it
        entity = entity[0].lower() + entity[1:] + 's'

        # Construct the query string
        fields_str = ", ".join(fields)
        query_str = f"""
        query {{
            {entity} {{
                {fields_str}
            }}
        }}
        """

        # Convert the query string to a gql object
        query = gql(query_str)

        # Execute the query
        result = self.client.execute(query)
        
        # Convert the result to a DataFrame
        df = pd.DataFrame(result[entity])

        return df

    def query_to_csv(self, df, filename):
        df.to_csv(filename, index=False)
