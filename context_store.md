# Subgrounds docs

[
    {
        "id": "subgrounds-intro",
        "title": "Subgrounds",
        "description": "The Subgrounds class provides the top level API and most users will be using this class exclusively. This class is used to load (i.e.: introspect) GraphQL APIs (subgraph or vanilla GraphQL APIs) as well as execute querying operations. Moreover, this class is meant to be used as a singleton, i.e.: initialized once and reused throughout a project.",
        "tags": ["Subgrounds", "API", "GraphQL", "Singleton"],
        "code_examples": [
            {
                "id": "loading-subgraph-and-api",
                "description": "This code demonstrates how to initialize the Subgrounds object and load a GraphQL API. It loads a subgraph and a vanilla GraphQL API using their API URLs.",
                "tags": ["Initialization", "Loading", "API"],
                "code": "from subgrounds import Subgrounds\n\n# Initialize Subgrounds\nsg = Subgrounds()\n\n# Load a subgraph using its API URL\naave_v2 = sg.load_subgraph('https://api.thegraph.com/subgraphs/name/messari/aave-v2-ethereum')\n\n# Load a vanilla GraphQL API using its API URL\nsnapshot = sg.load_api('https://hub.snapshot.org/graphql')"
            }
        ]
    },
    {
        "id": "getting-data",
        "title": "Getting the Data",
        "description": "Once you load in your subgraphs (or vanilla APIs), you can start gathering data via Subgrounds.query.",
        "tags": ["Data", "Subgraphs", "APIs", "Querying"],
        "code_examples": [
            {
                "id": "gathering-aave-market-names",
                "description": "This code gathers the names of the latest markets in Aave.",
                "tags": ["Aave", "Markets", "Names"],
                "code": "sg.query([aave_v2.Query.markets.name])"
            },
            {
                "id": "gathering-snapshot-proposals",
                "description": "This code gathers the titles and scores of the latest proposals from snapshot.",
                "tags": ["Snapshot", "Proposals", "Titles", "Scores"],
                "code": "sg.query([snapshot.Query.proposals.title, snapshot.Query.proposals.scores_total,])"
            }
        ]
    },
    {
        "id": "querying",
        "title": "Querying",
        "description": "Subgrounds provides 3 main ways to query data, which provide different data structures and typing: Subgrounds.query, Subgrounds.query_json, and Subgrounds.query_df. Each has its own result types and usage cases.",
        "tags": ["Querying", "Data Structures", "Typing"],
        "code_examples": [
            {
                "id": "query-methods-setup",
                "description": "This code sets up the examples for the three query methods using the Aave V2 data from Ethereum.",
                "tags": ["Query Methods", "Setup", "Aave V2", "Ethereum"],
                "code": "from subgrounds import Subgrounds\n\nsg = Subgrounds()\naave_v2 = sg.load_subgraph('https://api.thegraph.com/subgraphs/name/messari/aave-v2-ethereum')\n\naave_markets = aave_v2.Query.markets(\n    first=3,\n    orderBy=aave_v2.Market.totalValueLockedUSD,\n    orderDirection='desc',\n    where=[aave_v2.Market.createdBlockNumber > 14720000]\n)"
            },
            {
                "id": "query-example",
                "description": "This code demonstrates the use of the query method. A list of names and a matching list TVL values gets returned.",
                "tags": ["Query Method", "Names", "TVL Values"],
                "code": "sg.query([aave_markets.name, aave_markets.totalValueLockedUSD,])"
            },
            {
                "id": "query-json-example",
                "description": "This code demonstrates the use of the query_json method. A more complex JSON data structure gets returned.",
                "tags": ["Query_JSON Method", "JSON Data Structure"],
                "code": "sg.query_json([aave_markets.name, aave_markets.totalValueLockedUSD,])"
            },
            {
                "id": "query-df-example",
                "description": "This code demonstrates the use of the query_df method. A simple pandas.DataFrame gets returned.",
                "tags": ["Query_DF Method", "Pandas DataFrame"],
                "code": "sg.query_df([aave_markets.name, aave_markets.totalValueLockedUSD,])"
            }
        ]
    }
]

[
    {
        "id": "synthetic-fields-intro",
        "title": "Synthetic Fields",
        "description": "One of Subgrounds' unique features is the ability to define schema-based (i.e.: pre-querying) transformations using SyntheticFields. They can be created using Python arithmetic operators on relative FieldPaths and must be added to the entity which they enhance. Once added to an entity, SyntheticFields can be queried just like regular GraphQL fields.",
        "tags": ["Subgrounds", "SyntheticFields", "FieldPaths", "GraphQL"],
        "code_examples": [
            {
                "id": "synthetic-field-swap-price",
                "description": "This code demonstrates how to create a simple SyntheticField to calculate the swap price of Swap events stored on the Sushiswap subgraph.",
                "tags": ["SyntheticField", "Swap Price", "Sushiswap", "Subgraph"],
                "code": "from subgrounds import Subgrounds\n\nsg = Subgrounds()\n\nsushiswap = sg.load_subgraph('https://api.thegraph.com/subgraphs/name/sushiswap/exchange')\nswap = sushiswap.Swap\n\nswap.price1 = (abs(swap.amount0Out - swap.amount0In) / abs(swap.amount1Out - swap.amount1In))\n\nweth_usdc = sushiswap.Query.pair(id='0x397ff1542f962076d0bfe58ea045ffa2d347aca0')\n\nlast_10_swaps = weth_usdc.swaps(orderBy=swap.timestamp, orderDirection='desc', first=10)\n\nsg.query_df([last_10_swaps.timestamp, last_10_swaps.price1])"
            },
            {
                "id": "complex-synthetic-field-datetime",
                "description": "This code demonstrates how to create a complex SyntheticField using the constructor. It creates a SyntheticField on the Swap entity called datetime, which will format the timestamp field into something more human readable.",
                "tags": ["SyntheticField", "Datetime", "Human Readable"],
                "code": "from datetime import datetime\nfrom subgrounds.subgraph import SyntheticField\n\nswap.datetime = SyntheticField(f=lambda timestamp: str(datetime.fromtimestamp(timestamp)), type_=SyntheticField.STRING, deps=swap.timestamp,)\n\nlast_10_swaps = sushiswap.Query.swaps(orderBy=swap.timestamp, orderDirection='desc', first=10,)\n\nsg.query_df([last_10_swaps.datetime, last_10_swaps.pair.token0.symbol, last_10_swaps.pair.token1.symbol,])"
            }
        ]
    },
    {
        "id": "helpers-intro",
        "title": "Helpers",
        "description": "There are several common instances of SyntheticFields we see in the wild. We've added some helper constructors for ease of use.",
        "tags": ["Helpers", "SyntheticFields"],
        "code_examples": [
            {
                "id": "helper-datetime-of-timestamp",
                "description": "This helper constructor makes it easy to convert timestamps into datetime.datetime objects.",
                "tags": ["Helper", "Datetime", "Timestamp"],
                "code": "swap.datetime = SyntheticField.datetime_of_timestamp(swap.timestamp)"
            },
            {
                "id": "helper-map",
                "description": "This helper constructor makes it easy to convert timestamps into datetime.datetime objects.",
                "tags": ["Helper", "Map"],
                "code": "swap.datetime = SyntheticField.datetime_of_timestamp(swap.timestamp)"
            }
        ]
    }
]

[
    {
        "id": "arguments-intro",
        "title": "Arguments",
        "description": "Some FieldPaths can be parameterized with certain arguments such as specific token ids, sorting by certain fields, etc. These arguments can be configured by calling said function.",
        "tags": ["Arguments", "FieldPaths", "Subgrounds"],
        "code_examples": [
            {
                "id": "load-curve-subgraph",
                "description": "This code shows how to load a curve subgraph using Subgrounds.",
                "tags": ["Subgrounds", "Curve Subgraph"],
                "code": "from subgrounds.subgrounds import Subgrounds\n\nsg = Subgrounds()\n\ncurve = sg.load_subgraph('https://api.thegraph.com/subgraphs/name/messari/curve-finance-ethereum')"
            },
            {
                "id": "analyzing-curve-pool-data",
                "description": "This code shows how to analyze curve pool data via the curve.Query.pools FieldPath by using arguments to configure the query.",
                "tags": ["Curve Pool Data", "FieldPath", "Arguments"],
                "code": "curve_pools = curve.Query.liquidityPools(first=10, orderBy=curve.LiquidityPool.totalValueLockedUSD, orderDirection='desc', where=[curve.LiquidityPool.createdBlockNumber > 14720000])\n\nsg.query_df([curve_pools.outputToken.name, curve_pools.totalValueLockedUSD,])"
            },
            {
                "id": "raw-form-arguments",
                "description": "This code shows how to supply argument values in their raw form, without the use of relative FieldPaths.",
                "tags": ["Arguments", "Raw Form", "FieldPaths"],
                "code": "curve_pools = curve.Query.liquidityPools(first=10, orderBy='totalValueLockedUSD', orderDirection='desc', where={'createdBlockNumber_gt': 14720000})"
            },
            {
                "id": "relative-form-arguments",
                "description": "This code shows how to supply argument values in their relative form, with the use of FieldPaths.",
                "tags": ["Arguments", "Relative Form", "FieldPaths"],
                "code": "curve_pools = curve.Query.liquidityPools(first=10, orderBy=curve.LiquidityPool.totalValueLockedUSD, orderDirection='desc', where=[curve.LiquidityPool.createdBlockNumber > 14720000])"
            }
        ]
    },
    {
        "id": "merging-intro",
        "title": "Merging",
        "description": "When passing a list of FieldPaths to any Subgrounds.query function, Subgrounds will merge them into a single query. This is only true if the FieldPaths originate from the same subgraph.",
        "tags": ["Merging", "FieldPaths", "Subgrounds"],
        "code_examples": [
            {
                "id": "most-traded-pools-query",
                "description": "In this query, we are taking the top 4 curve pools by cumulative volume and analyzes the top 3 days by daily total revenue.",
                "tags": ["Curve Pools", "Query", "FieldPaths"],
                "code": "from subgrounds import Subgrounds\n\nsg = Subgrounds()\n\ncurve = sg.load_subgraph('https://api.thegraph.com/subgraphs/name/messari/curve-finance-ethereum')\n\nmost_traded_pools = curve.Query.liquidityPools(orderBy=curve.LiquidityPool.cumulativeVolumeUSD, orderDirection='desc', first=4,)\n\nmost_traded_snapshots = most_traded_pools.dailySnapshots(orderBy=curve.LiquidityPoolDailySnapshot.dailyTotalRevenue, orderDirection='desc', first=3,)\n\nsg.query_df([most_traded_pools.name, most_traded_snapshots.dailyVolumeUSD, most_traded_snapshots.dailyTotalRevenueUSD,])"
            }
        ]
    }
]

[
    {
        "id": "contrib-plotly-intro",
        "title": "Contrib - Plotly",
        "description": "The Subgrounds Plotly Wrapper is an extension of the Plotly components to understand and work seamlessly with the Subgrounds library. It provides a convenient way to visualize data fetched from subgraphs using Plotly, by wrapping Plotly's trace components with additional functionality.",
        "tags": ["Subgrounds", "Plotly", "Data Visualization"],
        "code_examples": [
            {
                "id": "getting-started-subgrounds-plotly",
                "description": "This example demonstrates how to get started with the Subgrounds Plotly Wrapper. It shows how to import the necessary components, load a subgraph, and create a Figure instance with appropriate traces.",
                "tags": ["Subgrounds", "Plotly", "Getting Started"],
                "code": "from subgrounds import Subgrounds\nfrom subgrounds.contrib.plotly import Figure, Indicator\n\nsg = Subgrounds()\naave_v2 = sg.load_subgraph('https://api.thegraph.com/subgraphs/name/messari/aave-v2-ethereum')\n\nFigure(subgrounds=sg, traces=[Indicator(value=pair.token0Price),])"
            },
            {
                "id": "simple-indicator-example",
                "description": "This example shows how to create a simple Indicator using the Subgrounds Plotly Wrapper.",
                "tags": ["Subgrounds", "Plotly", "Indicator"],
                "code": "from subgrounds import Subgrounds\nfrom subgrounds.contrib.plotly import Figure, Indicator\n\nsg = Subgrounds()\naave_v2 = sg.load_subgraph('https://api.thegraph.com/subgraphs/name/messari/aave-v2-ethereum')\n\nFigure(subgrounds=sg, traces=[Indicator(value=pair.token0Price),])"
            },
            {
                "id": "scatter-and-bar-plots-example",
                "description": "This example demonstrates how to create Scatter and Bar plots using Subgrounds and the Plotly Wrapper. It shows how to load a subgraph, fetch data for the past 30 days, create synthetic fields, create Scatter and Bar traces, and create Figure instances to display them.",
                "tags": ["Subgrounds", "Plotly", "Scatter", "Bar", "Data Visualization"],
                "code": "from datetime import datetime\n\nimport pandas as pd\n\nfrom subgrounds import FieldPath, Subgrounds, SyntheticField\nfrom subgrounds.contrib.plotly import Figure, Scatter, Bar\n\nsg = Subgrounds()\n\nlido_activity = sg.load_subgraph('https://api.thegraph.com/subgraphs/name/messari/lido-ethereum')\n\nusage_daily_snapshot_30days = lido_activity.Query.usageMetricsDailySnapshots(orderBy=lido_activity.UsageMetricsDailySnapshot.timestamp, orderDirection='desc', first=30,)\n\ndaily_snapshot = lido_activity.UsageMetricsDailySnapshot\n\ndaily_snapshot.datetime = SyntheticField.datetime_of_timestamp(daily_snapshot.timestamp)\n\ntrace = Scatter(x=usage_daily_snapshot_30days.datetime, y=usage_daily_snapshot_30days.dailyActiveUsers,)\n\nfig = Figure(subgrounds=sg, traces=trace, layout=dict(title='Daily Active Users vs Datetime', xaxis=dict(title='Datetime'), yaxis=dict(title='Daily Active Users'),),)\n\ntrace2 = Bar(x=usage_daily_snapshot_30days.datetime, y=usage_daily_snapshot_30days.dailyTransactionCount,)\n\nfig2 = Figure(subgrounds=sg, traces=trace2, layout=dict(title='Daily Transaction Count', xaxis=dict(title='Datetime'), yaxis=dict(title='Daily Transaction Count'),),)\n\nfig.figure.show()\n\nfig2.figure.show()"
            }
        ],
        "resources": [
            {
                "name": "Plotly Docs",
                "url": "https://plotly.com/python/"
            }
        ]
    }
]

[
    {
        "id": "custom-strategies-intro",
        "title": "Custom Strategies",
        "description": "Subgrounds allows developers to create their own pagination strategy by creating a class that implements the PaginationStrategy protocol. The class's constructor should accept a SchemaMeta argument which represents the schema of the subgraph API that the query is directed to and a Document argument which represents the query to be paginated on.",
        "tags": ["Subgrounds", "PaginationStrategy"],
        "code_examples": [
            {
                "id": "pagination-strategy-protocol",
                "description": "This is an example of a class that implements the PaginationStrategy protocol.",
                "tags": ["Subgrounds", "PaginationStrategy"],
                "code": "class PaginationStrategy(Protocol):\n    def __init__(\n        self,\n        schema: SchemaMeta,\n        document: Document\n    ) -> None: ...\n\n    def step(\n        self,\n        page_data: Optional[dict[str, Any]] = None\n    ) -> Tuple[Document, dict[str, Any]]: ..."
            },
            {
                "id": "pagination-over-query-document",
                "description": "This is the algorithm used by Subgrounds to paginate over a query document given a pagination strategy.",
                "tags": ["Subgrounds", "PaginationStrategy"],
                "code": "def paginate(\n    schema: SchemaMeta,\n    doc: Document,\n    pagination_strategy: Type[PaginationStrategy]\n) -> dict[str, Any]:\n    try:\n        strategy = pagination_strategy(schema, doc)\n\n        data: dict[str, Any] = {}\n\n        next_page_doc, variables = strategy.step(page_data=None)\n\n        while True:\n            try:\n                page_data = client.query(\n                    url=next_page_doc.url,\n                    query_str=next_page_doc.graphql,\n                    variables=next_page_doc.variables | variables\n                )\n\n                data = merge(data, page_data)\n\n                next_page_doc, variables = strategy.step(page_data=page_data)\n            \n            except StopPagination:\n                break\n            \n            except Exception as exn:\n                raise PaginationError(exn.args[0], strategy)\n\n        return data\n\n    except SkipPagination:\n        return client.query(doc.url, doc.graphql, variables=doc.variables)"
            }
        ]
    },
    {
        "id": "contrib-intro",
        "title": "Contrib",
        "description": "Contrib is a niche concept in some libraries that represent extra or contributed content to a library that may not fit in the main package. For us, `subgrounds.contrib` represents extra features and ideas with `subgrounds` that generally builds upon the core part of `subgrounds`.",
        "tags": ["Subgrounds", "Contrib"],
        "resources": [
            {
                "name": "Relevant Stackoverflow post",
                "url": "https://softwareengineering.stackexchange.com/questions/252053/whats-in-the-contrib-folder"
            }
        ],
        "subsections": [
            {
                "id": "contrib-plotly",
                "title": "Plotly",
                "description": "Originally located in `plotly_wrappers`, `subgrounds.contrib.plotly` contains helpful wrappers on `plotly` objects that allow you to use FieldPaths directly without creating a pandas.DataFrame.",
                "tags": ["Subgrounds", "Contrib", "Plotly"]
            },
            {
                "id": "contrib-dash",
                "title": "Dash",
                "description": "Originally located in `subgrounds.dash_wrappers`, `subgrounds.contrib.dash` contains helpful wrappers on `dash` objects that allow you to use other wrapped visualization objects (currently `subgrounds.contrib.plotly`) in `dash` apps without creating DataFrames.",
                "tags": ["Subgrounds", "Contrib", "Dash"]
            },
            {
                "id": "contrib-warning",
                "title": "Warning",
                "description": "The `contrib` subpackage of `subgrounds` does not follow the same semver patterns that `subgrounds` does. This is purely a place for us to experiment with new ideas, including enriching popular libraries with `subgrounds`.",
                "tags": ["Subgrounds", "Contrib"]
            }
        ]
    }
]

# Subgrounds code examples

[
    {
        "id": "standard-query-example",
        "code": "```python\nfrom subgrounds.subgrounds import Subgrounds\nsg = Subgrounds()\ncurve = sg.load_subgraph('https://api.thegraph.com/subgraphs/name/messari/curve-finance-ethereum')\ncurve_pools = curve.Query.liquidityPools(first=10,orderBy=curve.LiquidityPool.totalValueLockedUSD,orderDirection=\"desc\",where=[curve.LiquidityPool.createdBlockNumber > 14720000])\nsg.query_df([curve_pools.outputToken.name,curve_pools.totalValueLockedUSD,])```",
        "tags": ["standard-query", "fieldpath", "orderby", "orderdirection", "where-condition", "first-integer"],
        "description": "A standard Subgrounds query that loads a subgraph, queries for specific liquidity pools with set conditions, and retrieves data from those pools."
    },
    {
        "id": "nested-query-example",
        "code": "```python\nfrom subgrounds import Subgrounds\nsg = Subgrounds()\ncurve = sg.load_subgraph('https://api.thegraph.com/subgraphs/name/messari/curve-finance-ethereum')\nmost_traded_pools = curve.Query.liquidityPools(orderBy=curve.LiquidityPool.cumulativeVolumeUSD,orderDirection='desc',first=4,)\nmost_traded_snapshots = most_traded_pools.dailySnapshots(orderBy=curve.LiquidityPoolDailySnapshot.dailyTotalRevenue,orderDirection='desc',first=3,)\nsg.query_df([most_traded_pools.name,most_traded_snapshots.dailyVolumeUSD,most_traded_snapshots.dailyTotalRevenueUSD,])```",
        "tags": ["nested-query", "fieldpath", "orderby", "orderdirection", "first-integer"],
        "description": "A nested Subgrounds query that loads a subgraph, retrieves data from the most traded pools, and further queries for the snapshots of these pools."
    },
    {
        "id": "synthetic-field-example",
        "code": "```python\nfrom subgrounds import Subgrounds\nsg = Subgrounds()\nsushiswap = sg.load_subgraph('https://api.thegraph.com/subgraphs/name/sushiswap/exchange')\nswap = sushiswap.Swap\nswap.price1 = (abs(swap.amount0Out - swap.amount0In) / abs(swap.amount1Out - swap.amount1In))\nweth_usdc = sushiswap.Query.pair(id='0x397ff1542f962076d0bfe58ea045ffa2d347aca0')\nlast_10_swaps = weth_usdc.swaps(orderBy=swap.timestamp,orderDirection='desc',first=10)\nsg.query_df([last_10_swaps.timestamp,last_10_swaps.price1])```",
        "tags": ["synthetic-field", "fieldpath", "orderby", "orderdirection", "first-integer"],
        "description": "A Subgrounds query that uses a synthetic field to calculate swap prices. It retrieves the last 10 swaps of a specific pair and queries for the timestamps and calculated prices."
    },
    {
        "id": "synthetic-field-helper-example",
        "code": "```python\nfrom subgrounds.subgraph import SyntheticField\nswap.datetime = SyntheticField.datetime_of_timestamp(swap.timestamp)```",
        "tags": ["synthetic-field-helper"],
        "description": "An example of using a synthetic field helper in Subgrounds to convert a timestamp to a human-readable datetime."
    }
]

{
    "id": "usage-metrics-query-example",
    "code": "```python\nfrom subgrounds import Subgrounds\nfrom datetime import datetime\nfrom subgrounds.subgraph import SyntheticField\nimport pandas as pd\n\n# Initialize Subgrounds and load the subgraph\nsg = Subgrounds()\nstargate_eth = sg.load_subgraph(\"https://api.thegraph.com/subgraphs/name/messari/stargate-ethereum\")\n\n# Define the query and field paths\nusage_metrics_daily_snapshots = stargate_eth.Query.usageMetricsDailySnapshots(first=1000)\n\n# Create the datetime synthetic field\nstargate_eth.UsageMetricsDailySnapshot.datetime = SyntheticField(\n    lambda timestamp: str(datetime.fromtimestamp(timestamp)),\n    SyntheticField.FLOAT,\n    stargate_eth.UsageMetricsDailySnapshot.timestamp,\n)\n\n# Field paths for each category\ncumulative_metrics_fields = [...]\ndaily_metrics_fields = [...]\nsnapshot_info_fields = [...]\nprotocol_metrics_fields = [...]\n\n# Execute the query and store the results in a DataFrame\ncumulative_metrics_df = sg.query_df(cumulative_metrics_fields)\ndaily_metrics_df = sg.query_df(daily_metrics_fields)\nsnapshot_info_df = sg.query_df(snapshot_info_fields)\nprotocol_metrics_df = sg.query_df(protocol_metrics_fields)```",
    "tags": ["subgrounds", "query", "synthetic-field", "dataframe"],
    "description": "This example demonstrates how to query usage metrics using Subgrounds. It also showcases the usage of synthetic fields and the extraction of data into pandas DataFrames."
}

{
    "id": "pool-data-query-example",
    "code": "```python\n# Initialize Subgrounds and load the subgraph\nsg = Subgrounds()\nstargate_eth = sg.load_subgraph(\"https://api.thegraph.com/subgraphs/name/messari/stargate-ethereum\")\n\n# Define the query and field paths\npools_query = stargate_eth.Query.pools(first=1000)\n\n# Field paths for each category\nsnapshot_fields = [...]\ncreation_fields = [...]\ncumulative_metrics_fields = [...]\nidentity_fields = [...]\nliquidity_fields = [...]\nrewards_fields = [...]\nvolume_fields = [...]\nvalue_locked_fields = [...]\n\n# Execute the query and store the results in DataFrames\nsnapshot_df = sg.query_df(snapshot_fields)\ncreation_df = sg.query_df(creation_fields)\ncumulative_metrics_df = sg.query_df(cumulative_metrics_fields)\nidentity_df = sg.query_df(identity_fields)\nliquidity_df = sg.query_df(liquidity_fields)\nrewards_df = sg.query_df(rewards_fields)\nvolume_df = sg.query_df(volume_fields)\nvalue_locked_df = sg.query_df(value_locked_fields)```",
    "tags": ["subgrounds", "query", "dataframe"],
    "description": "This example demonstrates how to query pool data using Subgrounds. It extracts multiple categories of data into pandas DataFrames."
}

{
    "id": "printing-data-example",
    "code": "```python\nprint(\"Cumulative Metrics:\")\ncumulative_metrics_df\n\nprint(\"Snapshot Information:\")\nsnapshot_info_df\n\nprint(\"Snapshot Fields:\")\nsnapshot_df\n\nprint(\"Creation Fields:\")\ncreation_df\n\nprint(\"Cumulative Metrics Fields:\")\ncumulative_metrics_df\n\nprint(\"Identity Fields:\")\nidentity_df\n\nprint(\"Liquidity Fields:\")\nliquidity_df\n\nprint(\"Rewards Fields:\")\nrewards_df\n\nprint(\"Volume Fields:\")\nvolume_df\n\nprint(\"Total Value Locked Fields:\")\nvalue_locked_df```",
    "tags": ["subgrounds", "print", "dataframe"],
    "description": "This example demonstrates how to print various data fields queried from Subgrounds into pandas DataFrames."
}

{
    "id": "liquidity-pool-data-query-example",
    "code": "```python\nfrom datetime import datetime\nfrom subgrounds.subgraph import SyntheticField\nfrom subgrounds import Subgrounds\nimport pandas as pd\n\n# Initialize Subgrounds and load the subgraph\nsg = Subgrounds()\nbalancer_v2 = sg.load_subgraph('https://api.thegraph.com/subgraphs/name/messari/balancer-v2-ethereum')\n\n# Create a SyntheticField on the LiquidityPool entity called `datetime`\nbalancer_v2.LiquidityPool.datetime = SyntheticField(\n    lambda timestamp: str(datetime.fromtimestamp(int(timestamp))),\n    SyntheticField.FLOAT,\n    balancer_v2.LiquidityPool.createdTimestamp\n)\n\n# Define the query and field paths\nliquidity_pools_query = balancer_v2.Query.liquidityPools(orderBy=balancer_v2.LiquidityPool.createdTimestamp, orderDirection='desc', first=100)\n\n# Field paths for each category\npool_identity_fields = [...]\npool_metrics_fields = [...]\npool_revenue_fields = [...]\npool_volume_fields = [...]\npool_balances_fields = [...]\npool_rewards_fields = [...]\n\n# Concatenate all field paths\nliquidity_pools_fields = (pool_identity_fields + pool_metrics_fields + pool_revenue_fields + pool_volume_fields + pool_balances_fields + pool_rewards_fields)\n\n# Execute the query and store the results in a DataFrame\nliquidity_pools_df = sg.query_df(liquidity_pools_fields)\n\n# Print the results\nprint(\"Liquidity Pools:\")\nprint(liquidity_pools_df)```",
    "tags": ["subgrounds", "query", "synthetic-field", "dataframe"],
    "description": "This example demonstrates how to query liquidity pool data using Subgrounds. It also showcases the usage of synthetic fields, sorting and limiting results, and the extraction of data into pandas DataFrames."
}

{
    "id": "financials-daily-snapshots-query-example",
    "code": "```python\nfrom datetime import datetime\nfrom subgrounds.subgraph import SyntheticField\nfrom subgrounds import Subgrounds\n\n# Initialize Subgrounds and load the subgraph\nsg = Subgrounds()\nsubgraph_url = 'https://api.thegraph.com/subgraphs/name/messari/lido-ethereum'\nsubgraph = sg.load_subgraph(subgraph_url)\n\n# Create a SyntheticField on the FinancialsDailySnapshot entity called `datetime`\nsubgraph.FinancialsDailySnapshot.datetime = SyntheticField(\n    lambda timestamp: str(datetime.fromtimestamp(int(timestamp))),\n    SyntheticField.FLOAT,\n    subgraph.FinancialsDailySnapshot.timestamp\n)\n\n# Define the query and field paths\nfinancials_query = subgraph.Query.financialsDailySnapshots(first=1000)\n\n# Field paths for each category\nprotocol_revenue_fields = [...]\nsupply_revenue_fields = [...]\ntotal_revenue_fields = [...]\nvolume_fields = [...]\nvalue_locked_fields = [...]\nidentity_fields = [...]\n\n# Concatenate all field paths\nfinancials_fields = (protocol_revenue_fields + supply_revenue_fields + total_revenue_fields + volume_fields + value_locked_fields + identity_fields)\n\n# Execute the query and store the results in a DataFrame\nfinancials_df = sg.query_df(financials_fields)\n\n# Print the results\nprint(\"Financials Daily Snapshots:\")\nprint(financials_df)```",
    "tags": ["subgrounds", "query", "synthetic-field", "dataframe"],
    "description": "This example demonstrates how to query financials daily snapshots using Subgrounds. It also showcases the usage of synthetic fields and the extraction of data into pandas DataFrames."
}

{
    "id": "usage-metrics-daily-snapshots-query-example",
    "code": "```python\nfrom subgrounds import Subgrounds\n\n# Initialize Subgrounds and load the subgraph\nsg = Subgrounds()\nsubgraph_url = 'https://api.thegraph.com/subgraphs/name/messari/balancer-v2-ethereum'\nsubgraph = sg.load_subgraph(subgraph_url)\n\n# Define the query and field paths\nmetrics_query = subgraph.Query.usageMetricsDailySnapshots(first=1000)\n\n# Field paths for each category\nblock_and_id_fields = [\n    metrics_query.blockNumber,\n    metrics_query.id,\n    metrics_query.timestamp,\n]\n\nuser_activity_fields = [\n    metrics_query.cumulativeUniqueUsers,\n    metrics_query.dailyActiveUsers,\n]\n\ntransaction_count_fields = [\n    metrics_query.dailyDepositCount,\n    metrics_query.dailySwapCount,\n    metrics_query.dailyTransactionCount,\n    metrics_query.dailyWithdrawCount,\n]\n\npool_count_field = [\n    metrics_query.totalPoolCount,\n]\n\n# Concatenate all field paths\nmetrics_fields = (\n    block_and_id_fields\n    + user_activity_fields\n    + transaction_count_fields\n    + pool_count_field\n)\n\n# Execute the query and store the results in a DataFrame\nmetrics_df = sg.query_df(metrics_fields)\n\n# Print the results\nprint(\"Usage Metrics Daily Snapshots:\")\nprint(metrics_df)```",
    "tags": ["subgrounds", "query", "dataframe"],
    "description": "This example demonstrates how to query usage metrics daily snapshots using Subgrounds. It also showcases how to query different categories of data, and the extraction of data into pandas DataFrames."
}

{
    "id": "uniswap-v3-financials-daily-snapshots-query-example",
    "code": "```python\n# Import the Subgrounds library\nfrom subgrounds import Subgrounds\nfrom dotenv import load_dotenv\nimport os\n\nload_dotenv()\ngraph_api_key = os.getenv('GRAPH_API_KEY')\n\n# Create a new Subgrounds object\nsg = Subgrounds()\n\n# Load the Uniswap v3 subgraph using a specific API endpoint\nuni = sg.load_subgraph(f'https://gateway.thegraph.com/api/{graph_api_key}/subgraphs/id/ELUcwgpm14LKPLrBRuVvPvNKHQ9HvwmtKgKSH6123cr7')\n\n# Query the financialsDailySnapshots endpoint with a specified order, limit, and filter criteria\nlatest_snapshots = uni.Query.financialsDailySnapshots(\n  orderBy=uni.FinancialsDailySnapshot.timestamp,\n  orderDirection='desc',\n  first=1,\n)\n\n# Convert the query results to a Pandas dataframe and extract the first row\nres = sg.query_df(latest_snapshots).squeeze()\n\n# Print the result\nres```",
    "tags": ["subgrounds", "query", "dataframe"],
    "description": "This example demonstrates how to query the latest financials daily snapshots from a Uniswap v3 subgraph using Subgrounds. It shows how to load the subgraph with an API key, filter and order query results, and convert results into a pandas DataFrame."
}

{
    "id": "uniswap-v3-liquidity-pools-query-example",
    "code": "```python\n# This code queries the liquidityPools endpoint of a specific Uniswap v3 subgraph to retrieve information about the liquidity pools that exist on the network\n\n# Create a query object for the liquidityPools endpoint that specifies that the first result should be returned, the results should be sorted in descending order by the total value locked in USD, and the order should be descending.\npools = uni.Query.liquidityPools(\n  first=1,\n  orderBy=uni.LiquidityPool.totalValueLockedUSD,\n  orderDirection='desc'\n)\n\n# Execute the query, convert the results into a Pandas dataframe, and extract the first row as a Pandas series.\nres2 = sg.query_df(pools).squeeze()\n\n# Store the resulting Pandas series in res2.\nres2```",
    "tags": ["subgrounds", "query", "dataframe"],
    "description": "This example demonstrates how to query information about the liquidity pools from a Uniswap v3 subgraph using Subgrounds. It illustrates how to sort query results, convert them into a pandas DataFrame, and extract the first row as a series."
}

{
    "id": "uniswap-v3-dexAmmProtocols-query-example",
    "code": "```python\n# This code queries the dexAmmProtocols endpoint of a specific Uniswap v3 subgraph to retrieve information about the decentralized exchange automated market maker (DEX AMM) protocols that exist on the network.\n\n# Create a query object for the dexAmmProtocols endpoint that specifies that the first result should be returned.\nprotocol = uni.Query.dexAmmProtocols(\n  first=1\n)\n\n# Execute the query, convert the results into a Pandas dataframe, and extract the first row as a Pandas series.\nres3 = sg.query_df(protocol).squeeze()\n\n# Store the resulting Pandas series in res3.\nres3```",
    "tags": ["subgrounds", "query", "dataframe"],
    "description": "This example demonstrates how to query information about the DEX AMM protocols from a Uniswap v3 subgraph using Subgrounds. It explains how to create a query object, execute the query, and convert the results into a pandas DataFrame."
}

{
    "id": "uniswap-v3-pools-daily-snapshots-query-example",
    "code": "```python\n# Query the liquidity pool daily snapshots with specified filter criteria\nlp = uni.Query.liquidityPoolDailySnapshots(\n    first=1,\n    orderBy=uni.LiquidityPoolDailySnapshot.timestamp,\n    orderDirection='desc',\n    where=[uni.LiquidityPoolDailySnapshot.pool == '0x88e6a0c2ddd26feeb64f039a2c41296fcb3f5640']\n)\n\n# Query multiple fields from the resulting data and store in a JSON object\nres4 = sg.query_json([\n    lp.id,\n    lp.pool.name,\n    lp.blockNumber,\n    lp.totalValueLockedUSD,\n    lp.cumulativeSupplySideRevenueUSD,\n    lp.dailySupplySideRevenueUSD,\n    lp.cumulativeProtocolSideRevenueUSD,\n    lp.dailyTotalRevenueUSD,\n    lp.dailyVolumeUSD,\n    lp.cumulativeVolumeUSD,\n    lp.outputTokenSupply,\n    lp.outputTokenPriceUSD,\n    lp.stakedOutputTokenAmount,\n    lp.inputTokenBalances,\n    lp.inputTokenWeights,\n    lp.rewardTokenEmissionsAmount,\n    lp.rewardTokenEmissionsUSD,\n    lp.dailyVolumeByTokenAmount,\n    lp.dailyVolumeByTokenUSD,\n    lp.protocol.cumulativeProtocolSideRevenueUSD,\n    lp.protocol.cumulativeSupplySideRevenueUSD,\n    lp.protocol.cumulativeTotalRevenueUSD,\n    lp.protocol.protocolControlledValueUSD,\n    lp.protocol.totalPoolCount,\n    lp.protocol.totalValueLockedUSD,\n    lp.pool.outputToken.lastPriceUSD,\n    lp.pool.outputToken.name,\n])\n\n# Print the resulting JSON object\nres4```",
    "tags": ["subgrounds", "query", "json"],
    "description": "This example demonstrates how to query daily snapshots of liquidity pools from a Uniswap v3 subgraph using Subgrounds. It also showcases how to filter query results, query multiple fields, and store the resulting data in a JSON object."
}

{
    "id": "playgrounds-gateway-setup-example",
    "code": "```python\n# Import subgrounds\nfrom subgrounds import Subgrounds\n\n# Instantiate subgrounds and insert Playgrounds API key into header\nsg = Subgrounds.from_pg_key(\"PGA_API_KEY\")\n\n# Insert desired subgraph id from decentralized subgraph. Find in subgraph url\naave_v3_id = \"SUBGRAPH_ID\"```",
    "tags": ["subgrounds", "api", "gateway"],
    "description": "This example demonstrates how to set up a gateway using the Subgrounds library and the Playgrounds API. It includes inserting the API key into the Subgrounds instance and specifying the ID of the subgraph to be queried."
}

{
    "id": "loading-subgraph-playgrounds-proxy-example",
    "code": "```python\n# Load subgraph using playgrounds proxy endpoint \naave_v3 = sg.load_subgraph(f\"https://api.playgrounds.network/v1/proxy/subgraphs/id/{aave_v3_id}\")```",
    "tags": ["subgrounds", "proxy", "subgraph"],
    "description": "This example shows how to load a subgraph using the Playgrounds proxy endpoint with the Subgrounds library. It specifies the URL of the subgraph to be queried."
}

{
    "id": "querying-subgraphs-subgrounds-example",
    "code": "```python\n# How to query subgraphs with subgrounds\n# Subgrounds allows the same arguments as you normally use on graphql\n\nusage_metrics_daily = aave_v3.Query.usageMetricsDailySnapshots(\n    first = 10,\n    orderDirection = 'desc'\n)\n\nq_df_ex = sg.query_df([\n    usage_metrics_daily.timestamp,\n    usage_metrics_daily.dailyActiveBorrowers,\n    usage_metrics_daily.dailyActiveDepositors,\n])```",
    "tags": ["subgrounds", "query", "graphql"],
    "description": "This example demonstrates how to query a subgraph using the Subgrounds library. It uses the same arguments as you would normally use on GraphQL and converts the query results to a pandas DataFrame."
}

{
    "id": "displaying-query-results-example",
    "code": "```python\nq_df_ex```",
    "tags": ["subgrounds", "dataframe"],
    "description": "This example shows how to display the results of a query as a pandas DataFrame using the Subgrounds library."
}

{
    "id": "using-synthetic-fields-example",
    "code": "```python\nfrom subgrounds.subgraph import SyntheticField\nfrom datetime import datetime\n\nusage_metrics_daily = aave_v3.UsageMetricsDailySnapshot\n\n# Method 1\nusage_metrics_daily.d_t = SyntheticField(\n    f=lambda timestamp: str(datetime.fromtimestamp(timestamp)),\n    type_=SyntheticField.STRING,\n    deps=usage_metrics_daily.timestamp,\n)\n\n# Method 2: This helper constructor makes it easy to convert timestamps into datetime objects.\nusage_metrics_daily.datetime = SyntheticField.datetime_of_timestamp(usage_metrics_daily.timestamp)\n\nusage_metrics_daily = aave_v3.Query.usageMetricsDailySnapshots(\n    first = 100,\n    orderDirection = 'desc'\n)\n\nsg.query_df([\n    usage_metrics_daily.datetime,\n    usage_metrics_daily.d_t,\n    usage_metrics_daily.dailyActiveBorrowers,\n    usage_metrics_daily.dailyActiveDepositors,\n    usage_metrics_daily.dailyActiveLiquidatees,\n    usage_metrics_daily.dailyActiveLiquidators,\n])```",
    "tags": ["subgrounds", "synthetic-field", "graphql"],
    "description": "This example demonstrates how to create and use SyntheticFields in subgraph queries. SyntheticFields allow for the transformation and manipulation of data during the querying process. This code shows two methods of converting timestamps into datetime objects and querying different usage metrics."
}

{
    "id": "query-all-fields-lending-protocols-example",
    "code": "```python\n# Query lending protocols entitty and fields from subgraph\n# Here we are querying all of the fields in the lending protocols\n\naave_lending = aave_v3.Query.lendingProtocols()\naave_overview = sg.query_df(aave_lending)\naave_overview.squeeze()```",
    "tags": ["subgrounds", "query", "lending-protocols"],
    "description": "This example shows how to query all fields in the lending protocols entity from a subgraph using the Subgrounds library. It converts the query results to a pandas DataFrame and uses the squeeze method to reduce the DataFrame dimensionality."
}

{
    "id": "query-specific-fields-lending-protocols-example",
    "code": "```python\n# Query lending protocols entitty and specific fields \n\naave_lending = aave_v3.Query.lendingProtocols()\naave_overview = sg.query_df([\n    aave_lending.name,\n    aave_lending.type,\n    aave_lending.cumulativeBorrowUSD,\n    aave_lending.cumulativeDepositUSD,\n    aave_lending.cumulativeLiquidateUSD,\n    aave_lending.cumulativePositionCount,\n    aave_lending.cumulativeProtocolSideRevenueUSD,\n    aave_lending.cumulativeSupplySideRevenueUSD,\n    aave_lending.cumulativeTotalRevenueUSD,\n    aave_lending.cumulativeUniqueUsers,\n    aave_lending.cumulativeUniqueBorrowers,\n    aave_lending.cumulativeUniqueDepositors,\n    aave_lending.cumulativeUniqueLiquidatees,\n    aave_lending.cumulativeUniqueLiquidators,\n])\naave_overview.squeeze()```",
    "tags": ["subgrounds", "query", "lending-protocols"],
    "description": "This example shows how to query specific fields in the lending protocols entity from a subgraph using the Subgrounds library. It specifies the fields to be queried, converts the query results to a pandas DataFrame, and uses the squeeze method to reduce the DataFrame dimensionality."
}

{
    "id": "creating-synthetic-fields-example",
    "code": "```python\nfrom subgrounds.subgraph import SyntheticField\n\n# Borrow_Deposit_Ratio: Calculate borrow deposit ratio by dividing the total borrow by the total deposit\naave_v3.LendingProtocol.borrow_dep_ratio = SyntheticField(\n    lambda x, y: x/y,\n    SyntheticField.FLOAT,\n    [aave_v3.LendingProtocol.totalBorrowBalanceUSD,\n    aave_v3.LendingProtocol.totalDepositBalanceUSD],\n)\n\nsg.query([aave_lending.totalBorrowBalanceUSD,\n          aave_lending.totalDepositBalanceUSD,\n          aave_lending.borrow_dep_ratio])\n\n# User Engagement Metrics: You can calculate the proportion of users who have ever borrowed,\n# by dividing each of the cumulativeUnique...\n# fields by cumulativeUniqueUsers\n\naave_v3.LendingProtocol.user_engagement_borrowed = (\n    abs(aave_v3.LendingProtocol.cumulativeUniqueBorrowers)\n/abs(aave_v3.LendingProtocol.cumulativeUniqueUsers)\n)\n\nsg.query_df([aave_lending.cumulativeUniqueBorrowers,\n             aave_lending.cumulativeUniqueUsers,\n             aave_lending.user_engagement_borrowed])\n\n# Average Borrow, Deposit, and Liquidation Values: cumulativeBorrowUSD divided by cumulativeUniqueBorrowers

{
    "id": "query-market-daily-snapshots-example",
    "code": "```python\nimport pandas as pd\nsteth_market_id = '0x0b925ed163218f6662a35e0f0371ac234f9e9371'\n\nsnapshots = aave_v3.Query.marketDailySnapshots(\n    first=100,\n    orderBy=aave_v3.MarketDailySnapshot.timestamp,\n    orderDirection='desc',\n    where={\n        'market':steth_market_id\n    }\n)\n\ndf = sg.query_df([\n    snapshots.timestamp,\n    snapshots.rates.rate,\n    snapshots.rates.side,\n    snapshots.rates.type\n])\n\ndf['side_type'] = df['marketDailySnapshots_rates_side'] +'-' +  df['marketDailySnapshots_rates_type']\ndf2 = df[['marketDailySnapshots_timestamp', 'marketDailySnapshots_rates_rate', 'side_type']]\ndf2 = df2.pivot(index='marketDailySnapshots_timestamp',columns='side_type').droplevel(level=0, axis=1)\ndf2.index = pd.to_datetime(df2.index, unit='s')\ndf2```",
    "tags": ["subgrounds", "query", "market-daily-snapshots", "data-manipulation"],
    "description": "This example demonstrates how to query market daily snapshots from a subgraph, manipulate the queried data, and convert the timestamps into datetime format."
}

{
    "id": "plotting-data-plotly-example",
    "code": "```python\nimport plotly.express as px\nfig = px.line(df2, x=df2.index, y=\"BORROWER-STABLE\", title='STETH Interest Rates')\nfig.show()```",
    "tags": ["plotly", "data-visualization"],
    "description": "This example shows how to visualize data using Plotly. Here, a line plot is created to represent STETH Interest Rates over time."
}

{
    "id": "plotting-data-subgrounds-example",
    "code": "```python\nfrom subgrounds.contrib.plotly import Figure, Scatter\n\n# Create the Scatter trace with appropriate field paths\ntrace = Scatter(\n    x=usage_metrics_daily.datetime,\n    y=usage_metrics_daily.dailyActiveUsers,\n)\n\n# Create the Figure instance with the trace and display it\nfig = Figure(\n    subgrounds=sg,\n    traces=trace,\n    layout=dict(\n        title=\"Daily Active Users vs Datetime\",\n        xaxis=dict(title=\"Datetime\"),\n        yaxis=dict(title=\"Daily Active Users\")\n    ),\n)\nfig.figure.show()```",
    "tags": ["subgrounds", "plotly", "data-visualization"],
    "description": "This example shows how to use the Subgrounds library with Plotly to visualize data. Here, a scatter plot is created to represent the number of daily active users over time."
}

{
    "id": "loading-subgraph-example",
    "code": "```python\n## Gateway setup\nfrom subgrounds import Subgrounds\nsg = Subgrounds.from_pg_key(\"PGA_API_KEY\")\nsubgraph_id = \"GELTrjPJYEzxyp6Y2CtEaYpGHcJNrJA6i5Ci4KfJSEsf\"\n\nfraxlend_subgraph = sg.load_subgraph(f\"https://api.playgrounds.network/v1/proxy/subgraphs/id/{subgraph_id}\")```",
    "tags": ["subgrounds", "loading-subgraph"],
    "description": "This example shows how to setup a gateway and load a specific subgraph using the Subgrounds library."
}

{
    "id": "querying-specific-fields-example",
    "code": "```python\nfraxlendFactories = fraxlend_subgraph.Query.fraxlendFactories()\nfraxlend_overview = sg.query_df([\n    fraxlendFactories.id,\n    fraxlendFactories.totalTVLValue,\n    fraxlendFactories.totalBorrowedValue,\n    fraxlendFactories.totalCollateralLockedValue,\n    fraxlendFactories.positionCount,\n    fraxlendFactories.pairCount,\n    fraxlendFactories.assetTokenCount,\n    fraxlendFactories.collateralTokenCount, \n])\nfraxlend_overview.head()```",
    "tags": ["subgrounds", "query", "fraxlend-factories"],
    "description": "This example shows how to query specific fields from a 'fraxlendFactories' entity of a subgraph using the Subgrounds library and convert the query results into a pandas DataFrame."
}

{
    "id": "querying-user-metrics-example",
    "code": "```python\nusers = fraxlend_subgraph.Query.users(\n    first = 10\n)\nuser_metrics = sg.query_df([\n    users.address,\n    users.id,\n])```",
    "tags": ["subgrounds", "query", "user-metrics"],
    "description": "This example shows how to query user metrics from a 'users' entity of a subgraph using the Subgrounds library and convert the query results into a pandas DataFrame."
}

{
    "id": "querying-position-metrics-example",
    "code": "```python\npositions = users.positions(\n    first =10\n)\nposition_metrics = sg.query_df([\n    positions.block,\n    positions.timestamp,\n    positions.id,\n    positions.borrowedAssetShare,\n    positions.depositedCollateralAmount,\n    positions.lentAssetShare,\n])```",
    "tags": ["subgrounds", "query", "position-metrics"],
    "description": "This example shows how to query position metrics from a 'positions' entity of a subgraph using the Subgrounds library and convert the query results into a pandas DataFrame."
}

{
    "id": "querying-pair-metrics-example",
    "code": "```python\npairs = fraxlend_subgraph.Query.pairs(\n    first = 10\n)\npairs_metrics = sg.query_df([\n    pairs.address,\n    pairs.id,\n    pairs.dailyHistory(first = 10),\n])```",
    "tags": ["subgrounds", "query", "pair-metrics"],
    "description": "This example shows how to query pair metrics from a 'pairs' entity of a subgraph using the Subgrounds library and convert the query results into a pandas DataFrame."
}

{
    "id": "querying-usage-metrics-example",
    "code": "```python\nfrom datetime import datetime\nfrom subgrounds.subgraph import SyntheticField\nfrom subgrounds import Subgrounds\nimport pandas as pd\n\n# Initialize Subgrounds\nsg = Subgrounds()\n\n# Load a subgraph using its API URL\nlido_activity = sg.load_subgraph('https://api.thegraph.com/subgraphs/name/messari/lido-ethereum')\n\n# Create a FieldPath object for the required fields in the financialsDailySnapshots entity.\n# Specify options to sort the data by timestamp in descending order and limit the number of results to 30.\nusage_daily_snapshot_30days = lido_activity.Query.usageMetricsDailySnapshots(\n    orderBy=lido_activity.UsageMetricsDailySnapshot.timestamp, \n    orderDirection='desc', \n    first=30\n)\n\n# Create a SyntheticField on the Swap entity called `timestamp`, which will format the timestamp field into something more human readable\nlido_activity.UsageMetricsDailySnapshot.datetime = SyntheticField(\n  lambda timestamp: str(datetime.fromtimestamp(timestamp)),\n  SyntheticField.FLOAT,\n  lido_activity.UsageMetricsDailySnapshot.timestamp\n)\n\nsg.query_df([\n    usage_daily_snapshot_30days.datetime,\n    usage_daily_snapshot_30days.dailyActiveUsers,\n    usage_daily_snapshot_30days.cumulativeUniqueUsers,\n    usage_daily_snapshot_30days.dailyTransactionCount\n])```",
    "tags": ["subgrounds", "query", "usage-metrics"],
    "description": "This example shows how to query usage metrics from 'usageMetricsDailySnapshots' entity and format timestamp field into something more human readable using the Subgrounds library."
}

{
    "id": "querying-financial-metrics-example",
    "code": "```python\nfrom datetime import datetime\nfrom subgrounds.subgraph import SyntheticField\nfrom subgrounds import Subgrounds\nimport pandas as pd\n\n# Initialize Subgrounds\nsg = Subgrounds()\n\n# Load a subgraph using its API URL\nlido_activity = sg.load_subgraph('https://api.thegraph.com/subgraphs/name/messari/lido-ethereum')\n\n# Create a FieldPath object for the required fields in the financialsDailySnapshots entity.\n# Specify options to sort the data by timestamp in descending order and limit the number of results to 30.\nfinancials_daily_snapshot_30days = lido_activity.Query.financialsDailySnapshots(\n    orderBy=lido_activity.FinancialsDailySnapshot.timestamp, \n    orderDirection='desc', \n    first=30\n)\n\n# Create a SyntheticField on the Swap entity called `timestamp`, which will format the timestamp field into something more human readable\nlido_activity.FinancialsDailySnapshot.datetime = SyntheticField(\n  lambda timestamp: str(datetime.fromtimestamp(timestamp)),\n  SyntheticField.FLOAT,\n  lido_activity.FinancialsDailySnapshot.timestamp\n)\n\nsg.query_df([\n    financials_daily_snapshot_30days.datetime,\n    financials_daily_snapshot_30days.cumulativeProtocolSideRevenueUSD,\n    financials_daily_snapshot_30days.cumulativeTotalRevenueUSD,\n    financials_daily_snapshot_30days.cumulativeSupplySideRevenueUSD,\n    financials_daily_snapshot_30days.dailyProtocolSideRevenueUSD,\n    financials_daily_snapshot_30days.dailyTotalRevenueUSD,\n    financials_daily_snapshot_30days.dailySupplySideRevenueUSD,\n    financials_daily_snapshot_30days.totalValueLockedUSD,\n    financials_daily_snapshot_30days.protocolControlledValueUSD\n])```",
    "tags": ["subgrounds", "query", "financial-metrics"],
    "description": "This example shows how to query financial metrics from 'financialsDailySnapshots' entity and format timestamp field into something more human readable using the Subgrounds library."
}

{
    "id": "querying-pool-summary-example",
    "code": "```python\nfrom datetime import datetime\nfrom subgrounds.subgraph import SyntheticField\nfrom subgrounds import Subgrounds\nimport pandas as pd\nimport numpy as np\n\n# Initialize Subgrounds\nsg = Subgrounds()\n\n# Load a subgraph using its API URL\nlido_pool_stETH = sg.load_subgraph('https://api.thegraph.com/subgraphs/name/messari/lido-ethereum')\n\n# Create a FieldPath object for the required fields in the financialsDailySnapshots entity.\n# Specify options to sort the data by timestamp in descending order and limit the number of results to 30.\nlido_pool_stETH_pool_summary = lido_pool_stETH.Query.pools(\n    orderBy=lido_pool_stETH.Pool.createdTimestamp, \n    orderDirection='desc', \n    first=30,\n    where=[\n        lido_pool_stETH.Pool.id == \"0xae7ab96520DE3A18E5e111B5EaAb095312D7fE84\"\n    ]\n)\n\n# Create a SyntheticField on the Swap entity called `timestamp`, which will format the timestamp field into something more human readable\nlido_pool_stETH.Pool.datetime = SyntheticField(\n  lambda createdTimestamp: str(datetime.fromtimestamp(createdTimestamp)),\n  SyntheticField.FLOAT,\n  lido_pool_stETH.Pool.createdTimestamp\n)\n\n# Create a SyntheticField on the Swap entity called `timestamp`, which will format the timestamp field into something more human readable\nlido_pool_stETH.Pool.inputTokenBalance_decimalConv = SyntheticField(\n  lambda x: x[0] / (10**18) if type(x) is list else x / (10**18),\n  SyntheticField.FLOAT,\n  lido_pool_stETH.Pool.inputTokenBalances\n)\n\nlido_pool_stETH.Pool.outputTokenSupply_decimalConv = SyntheticField(\n  lambda x: x[0] / (10**18) if type(x) is list else x / (10**18),\n  SyntheticField.FLOAT,\n  lido_pool_stETH.Pool.outputTokenSupply\n)\n\n# lido_pool_stETH.Pool.inputTokenBalance_decimalConv = lido_pool_stETH.Pool.inputTokenBalances / (10**18)\n\npool_summary = sg.query_df([\n    lido_pool_stETH_pool_summary.createdTimestamp,\n    lido_pool_stETH_pool_summary.cumulativeProtocolSideRevenueUSD,\n    lido_pool_stETH_pool_summary.cumulativeSupplySideRevenueUSD,\n    lido_pool_stETH_pool_summary.cumulativeTotalRevenueUSD,\n    lido_pool_stETH_pool_summary.inputTokenBalance_decimalConv,\n    lido_pool_stETH_pool_summary.outputTokenSupply_decimalConv,\n    lido_pool_stETH_pool_summary.totalValueLockedUSD\n])\npool_creation = sg.query_df([\n  lido_pool_stETH_pool_summary.datetime,\n])\n\n# squeezed_pool_summary = pool_summary.astype('float64').squeeze()\nsqueezed_pool_summary = pool_summary.squeeze()\nsqueezed_pool_creation = pool_creation.squeeze()\n\ndef format_decimal(number, decimal_places=4):\n    return f\"{number:.{decimal_places}f}\"\n\n# Assuming your squeezed DataFrame is named 'squeezed_pool_summary'\ndecimal_pool_summary = squeezed_pool_summary.apply(format_decimal)\n\n# Print the resulting Series\nprint(f\"Pool creation date and time: {squeezed_pool_creation}\")\nprint(\"Pool summary:\")\nprint(decimal_pool_summary)\n```",
    "tags": ["subgrounds", "query", "pool-summary"],
    "description": "This example shows how to query a specific pool summary and format the results using the Subgrounds library."
}

{
    "id": "querying-financial-metrics-calculate-additional-metrics-example",
    "code": "```python\nfrom datetime import datetime\nfrom subgrounds.subgraph import SyntheticField\nfrom subgrounds import Subgrounds\nimport pandas as pd\n\n# Initialize Subgrounds\nsg = Subgrounds()\n\n# Load a subgraph using its API URL\nfinancials_daily_snapshots = sg.load_subgraph('https://api.thegraph.com/subgraphs/name/messari/rocket-pool-ethereum')\n\n# Create a FieldPath object for the required fields in the financialsDailySnapshots entity.\n# Specify options to sort the data by timestamp in descending order and limit the number of results to 30.\nfinancials_daily_snapshot_30days = financials_daily_snapshots.Query.financialsDailySnapshots(\n    orderBy=financials_daily_snapshots.FinancialsDailySnapshot.timestamp, \n    orderDirection='desc', \n    first=30\n)\n\n# Create a SyntheticField on the Swap entity called `timestamp`, which will format the timestamp field into something more human readable\nfinancials_daily_snapshots.FinancialsDailySnapshot.datetime = SyntheticField(\n  lambda timestamp: str(datetime.fromtimestamp(timestamp)),\n  SyntheticField.FLOAT,\n  financials_daily_snapshots.FinancialsDailySnapshot.timestamp\n)\n\n# Define a synthetic field to calculate the daily revenue difference for the past 30 days\nfinancials_daily_snapshots.FinancialsDailySnapshot.revDiffRevenueUSD30 = SyntheticField(\n    lambda x, y: abs(x - y),\n    SyntheticField.FLOAT,\n    [financials_daily_snapshots.FinancialsDailySnapshot.dailyProtocolSideRevenueUSD,\n    financials_daily_snapshots.FinancialsDailySnapshot.dailySupplySideRevenueUSD],\n)\n\n# the average daily revenue\nfinancials_daily_snapshots.FinancialsDailySnapshot.avgDailyRevenueUSD30 = SyntheticField(\n    lambda x, y: (x + y) / 2,\n    SyntheticField.FLOAT,\n    [financials_daily_snapshots.FinancialsDailySnapshot.dailyProtocolSideRevenueUSD,\n    financials_daily_snapshots.FinancialsDailySnapshot.dailySupplySideRevenueUSD],\n)\n\n# Create a SyntheticField for the percentage change in daily revenue over the past 30 days\nfinancials_daily_snapshots.FinancialsDailySnapshot.revenueMargin30  = SyntheticField(\n    lambda x, y: x / y,\n    SyntheticField.FLOAT,\n    [financials_daily_snapshots.FinancialsDailySnapshot.dailyProtocolSideRevenueUSD,\n    financials_daily_snapshots.FinancialsDailySnapshot.dailySupplySideRevenueUSD],\n)\n\n\n# Query data flattened to a single DataFrame\nsg.query_df([\n    financials_daily_snapshot_30days.datetime,\n    financials_daily_snapshot_30days.cumulativeProtocolSideRevenueUSD,\n    financials_daily_snapshot_30days.cumulativeTotalRevenueUSD,\n    financials_daily_snapshot_30days.cumulativeSupplySideRevenueUSD,\n    financials_daily_snapshot_30days.dailyProtocolSideRevenueUSD,\n    financials_daily_snapshot_30days.dailyTotalRevenueUSD,\n    financials_daily_snapshot_30days.dailySupplySideRevenueUSD,\n    financials_daily_snapshot_30days.totalValueLockedUSD,\n    financials_daily_snapshot_30days.protocolControlledValueUSD,\n    financials_daily_snapshot_30days.revDiffRevenueUSD30,\n    financials_daily_snapshot_30days.avgDailyRevenueUSD30,\n    financials_daily_snapshot_30days.revenueMargin30\n])```",
    "tags": ["subgrounds", "query", "financial-metrics", "calculation"],
    "description": "This example shows how to query financial metrics, calculate additional metrics such as revenue differences, averages, and percentage changes using the Subgrounds library."
}

{
    "id": "comparing-financial-metrics-between-protocols-example",
    "code": "```python\nfrom subgrounds import Subgrounds\nfrom subgrounds.subgraph import SyntheticField\nfrom datetime import datetime\nimport pandas as pd\n\n# Initialize Subgrounds\nsg = Subgrounds()\n\n# Load subgraphs for Lido and rocketPool\nlido_subgraph = sg.load_subgraph('https://api.thegraph.com/subgraphs/name/messari/lido-ethereum')\nrocketPool_subgraph = sg.load_subgraph('https://api.thegraph.com/subgraphs/name/messari/rocket-pool-ethereum')\n\n# Query financials daily snapshots for both protocols (sorted by timestamp)\nlido_financials = lido_subgraph.Query.financialsDailySnapshots(orderBy=lido_subgraph.FinancialsDailySnapshot.timestamp, orderDirection='desc')\nrocketPool_financials = rocketPool_subgraph.Query.financialsDailySnapshots(orderBy=rocketPool_subgraph.FinancialsDailySnapshot.timestamp, orderDirection='desc')\n\n# Fetch the latest financials snapshot for both protocols\nlido_financials_latest = sg.query_df([\n    lido_financials.cumulativeSupplySideRevenueUSD, \n    lido_financials.cumulativeProtocolSideRevenueUSD, \n    lido_financials.cumulativeTotalRevenueUSD]).iloc[0]\n    \nrocketPool_financials_latest = sg.query_df([\n    rocketPool_financials.cumulativeSupplySideRevenueUSD, \n    rocketPool_financials.cumulativeProtocolSideRevenueUSD, \n    rocketPool_financials.cumulativeTotalRevenueUSD]).iloc[0]\n\n# Compare cumulative supply-side, protocol-side, and total revenue for both protocols\nrevenue_comparison = pd.DataFrame({'Lido': lido_financials_latest, 'rocketPool': rocketPool_financials_latest})\nprint(revenue_comparison)\n```",
    "tags": ["subgrounds", "query", "financial-metrics", "comparison"],
    "description": "This example shows how to compare financial metrics between Lido and Rocket Pool protocols using the Subgrounds library."
}

{
    "id": "comparing-usage-metrics-between-protocols-example",
    "code": "```python\nfrom subgrounds import Subgrounds\nfrom subgrounds.subgraph import SyntheticField\nfrom datetime import datetime\nimport pandas as pd\n\n# Initialize Subgrounds\nsg = Subgrounds()\n\n# Load subgraphs for Lido and rocketPool\nlido_subgraph = sg.load_subgraph('https://api.thegraph.com/subgraphs/name/messari/lido-ethereum')\nrocketPool_subgraph = sg.load_subgraph('https://api.thegraph.com/subgraphs/name/messari/rocket-pool-ethereum')\n\n# Query usage metrics daily snapshots for both protocols (sorted by timestamp)\nlido_usage = lido_subgraph.Query.usageMetricsDailySnapshots(\n    orderBy=lido_subgraph.UsageMetricsDailySnapshot.timestamp,\n    orderDirection='desc',\n    first=30)\n\nrocket_pool_usage = rocketPool_subgraph.Query.usageMetricsDailySnapshots(\n    orderBy=rocketPool_subgraph.UsageMetricsDailySnapshot.timestamp, \n    orderDirection='desc',\n    first=30)\n\n# Fetch usage metrics for the past 30 days for both protocols\nlido_usage_30days = sg.query_df([\n    lido_usage.timestamp,\n    lido_usage.dailyTransactionCount, \n    lido_usage.dailyActiveUsers])\n    \nrocket_pool_usage_30days = sg.query_df([\n    rocket_pool_usage.timestamp,\n    rocket_pool_usage.dailyTransactionCount, \n    rocket_pool_usage.dailyActiveUsers])\n\n[lido_usage_30,rocket_pool_usage_30] = sg.query_df([\n    lido_usage.timestamp, \n    lido_usage.dailyTransactionCount, \n    lido_usage.dailyActiveUsers,\n    rocket_pool_usage.timestamp,\n    rocket_pool_usage.dailyTransactionCount, \n    rocket_pool_usage.dailyActiveUsers\n])\nrocket_pool_usage_30\nlido_usage_30\n```",
    "tags": ["subgrounds", "query", "usage-metrics", "comparison"],
    "description": "This example shows how to compare usage metrics between Lido and Rocket Pool protocols over the past 30 days using the Subgrounds library."
}

{
    "id": "gateway-setup-and-basics-example",
    "code": "```python\n# Import subgrounds\nfrom subgrounds import Subgrounds\n\n# Instantiate subgrounds and insert Playgrounds API key into header\nsg = Subgrounds.from_pg_key('pg-AqAFS8G3TN3Kagdgw2MrGjFvDGUgxImS')\n\n# Insert desired subgraph id from decentralized subgraph. Find in subgraph url\nuniswap_id = 'ELUcwgpm14LKPLrBRuVvPvNKHQ9HvwmtKgKSH6123cr7'\n\nsubgraph = sg.load_subgraph(\n    f'https://api.playgrounds.network/v1/proxy/subgraphs/id/{uniswap_id}')\n\nsg.query_df([\n    subgraph.Query.tokens.id,\n    subgraph.Query.tokens.symbol,\n])\n```",
    "tags": ["subgrounds", "gateway", "setup", "basics"],
    "description": "This example demonstrates how to set up Gateway using Subgrounds library. It shows how to create a new Subgrounds instance using a Playgrounds API key, load a subgraph from the decentralized network, and perform a basic query on the loaded subgraph."
}

