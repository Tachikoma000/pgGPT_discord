# Subgrounds docs

## Working with Subgrounds: Loading APIs, Data Gathering, and Querying
Section 1: Introduction to Subgrounds
Introduction:
The Subgrounds class provides the top-level API, and it is primarily the class users interact with. Subgrounds is used to load (i.e., introspect) GraphQL APIs, whether they're subgraph or vanilla GraphQL APIs, as well as execute querying operations. Subgrounds is designed to be a singleton, meaning it's initialized once and reused throughout a project.

Example 1: Initializing and Loading Subgraph & API:
The following code shows how to initialize a Subgrounds object and load a GraphQL API. It demonstrates loading a subgraph and a vanilla GraphQL API using their respective API URLs.

```python
from subgrounds import Subgrounds

# Initialize Subgrounds
sg = Subgrounds()

# Load a subgraph using its API URL
aave_v2 = sg.load_subgraph('https://api.thegraph.com/subgraphs/name/messari/aave-v2-ethereum')

# Load a vanilla GraphQL API using its API URL
snapshot = sg.load_api('https://hub.snapshot.org/graphql')
```

Section 2: Gathering Data with Subgrounds
Introduction:
Once your subgraphs (or vanilla APIs) are loaded, data gathering can be initiated via the Subgrounds.query function.

Example 1: Gathering Aave Market Names:
The following code collects the names of the most recent markets in Aave.

```python
sg.query([aave_v2.Query.markets.name])
```

Example 2: Gathering Snapshot Proposals:
This code retrieves the titles and scores of the latest proposals from snapshot.

```python
sg.query([snapshot.Query.proposals.title, snapshot.Query.proposals.scores_total,])
```

Section 3: Querying with Subgrounds
Introduction:
Subgrounds provides three main querying methods that provide different data structures and types: Subgrounds.query, Subgrounds.query_json, and Subgrounds.query_df. Each method has its own result types and use cases.

Example 1: Setup for Query Methods:
This code sets up examples for the three query methods using the Aave V2 data from Ethereum.

```python
from subgrounds import Subgrounds

sg = Subgrounds()
aave_v2 = sg.load_subgraph('https://api.thegraph.com/subgraphs/name/messari/aave-v2-ethereum')

aave_markets = aave_v2.Query.markets(
    first=3,
    orderBy=aave_v2.Market.totalValueLockedUSD,
    orderDirection='desc',
    where=[aave_v2.Market.createdBlockNumber > 14720000]
)
```

Example 2: Query Method:
This code shows how to use the query method, returning a list of names and matching TVL values.

```python
sg.query([aave_markets.name, aave_markets.totalValueLockedUSD,])
```

Example 3: Query_JSON Method:
This code shows how to use the query_json method, returning a more complex JSON data structure.

```python
sg.query_json([aave_markets.name, aave_markets.totalValueLockedUSD,])
```

Example 4: Query_DF Method:
This code shows how to use the query_df method, returning a simple pandas.DataFrame.

```python
sg.query_df([aave_markets.name, aave_markets.totalValueLockedUSD,])
```

### Utilizing SyntheticFields and Helpers with Subgrounds
Section 1: Synthetic Fields in Subgrounds
Introduction:
One of the distinctive features of Subgrounds is its ability to define schema-based transformations (pre-querying) using SyntheticFields. SyntheticFields can be created using Python arithmetic operators on relative FieldPaths and must be added to the entity they enhance. Once attached to an entity, SyntheticFields can be queried like regular GraphQL fields.

Example 1: Synthetic Field for Swap Price:
The following code demonstrates how to create a simple SyntheticField to calculate the swap price of Swap events stored on the Sushiswap subgraph.

```python
Copy code
from subgrounds import Subgrounds

sg = Subgrounds()

sushiswap = sg.load_subgraph('https://api.thegraph.com/subgraphs/name/sushiswap/exchange')
swap = sushiswap.Swap

swap.price1 = (abs(swap.amount0Out - swap.amount0In) / abs(swap.amount1Out - swap.amount1In))

weth_usdc = sushiswap.Query.pair(id='0x397ff1542f962076d0bfe58ea045ffa2d347aca0')

last_10_swaps = weth_usdc.swaps(orderBy=swap.timestamp, orderDirection='desc', first=10)

sg.query_df([last_10_swaps.timestamp, last_10_swaps.price1])
```

Example 2: Complex Synthetic Field for Datetime:
This code demonstrates how to create a complex SyntheticField using the constructor. It creates a SyntheticField on the Swap entity called datetime, which formats the timestamp field into a more human-readable form.

```python
from datetime import datetime
from subgrounds.subgraph import SyntheticField

swap.datetime = SyntheticField(f=lambda timestamp: str(datetime.fromtimestamp(timestamp)), type_=SyntheticField.STRING, deps=swap.timestamp,)

last_10_swaps = sushiswap.Query.swaps(orderBy=swap.timestamp, orderDirection='desc', first=10,)

sg.query_df([last_10_swaps.datetime, last_10_swaps.pair.token0.symbol, last_10_swaps.pair.token1.symbol,])
```

Section 2: Helper Constructors in Subgrounds
Introduction:
Several common instances of SyntheticFields are found in practice. To facilitate their use, some helper constructors have been added.

Example 1: Datetime of Timestamp Helper:
This helper constructor simplifies the conversion of timestamps into datetime.datetime objects.

```python
swap.datetime = SyntheticField.datetime_of_timestamp(swap.timestamp)
```

Example 2: Map Helper:
This helper constructor also simplifies the conversion of timestamps into datetime.datetime objects.

```python
swap.datetime = SyntheticField.datetime_of_timestamp(swap.timestamp)
```

### Configuring Arguments and Merging FieldPaths with Subgrounds
#### Configuring Arguments in FieldPaths

Introduction:
FieldPaths in Subgrounds can be parameterized with specific arguments such as token ids, sorting fields, etc. You can configure these arguments by calling the related function.

Example 1: Loading a Curve Subgraph:
The following example shows how to load a curve subgraph using Subgrounds.

```python
from subgrounds.subgrounds import Subgrounds

sg = Subgrounds()

curve = sg.load_subgraph('https://api.thegraph.com/subgraphs/name/messari/curve-finance-ethereum')
```

Example 2: Analyzing Curve Pool Data:
This code demonstrates how to analyze curve pool data using the curve.Query.pools FieldPath, and how arguments can be used to configure the query.

```python
curve_pools = curve.Query.liquidityPools(first=10, orderBy=curve.LiquidityPool.totalValueLockedUSD, orderDirection='desc', where=[curve.LiquidityPool.createdBlockNumber > 14720000])

sg.query_df([curve_pools.outputToken.name, curve_pools.totalValueLockedUSD,])
```

Example 3: Supplying Argument Values in Raw Form:
This code illustrates how to provide argument values in their raw form, without the use of relative FieldPaths.

```python
curve_pools = curve.Query.liquidityPools(first=10, orderBy='totalValueLockedUSD', orderDirection='desc', where={'createdBlockNumber_gt': 14720000})
```

Example 4: Supplying Argument Values in Relative Form:
This code shows how to provide argument values in their relative form, with the use of FieldPaths.

```python
curve_pools = curve.Query.liquidityPools(first=10, orderBy=curve.LiquidityPool.totalValueLockedUSD, orderDirection='desc', where=[curve.LiquidityPool.createdBlockNumber > 14720000])
```

Section 2: Merging FieldPaths in Subgrounds
Introduction:
When you pass a list of FieldPaths to any Subgrounds.query function, Subgrounds will merge them into a single query, given that the FieldPaths come from the same subgraph.

Example: Querying Most Traded Pools:
In this query, we retrieve the top 4 curve pools by cumulative volume and analyze the top 3 days by daily total revenue.

```python
from subgrounds import Subgrounds

sg = Subgrounds()

curve = sg.load_subgraph('https://api.thegraph.com/subgraphs/name/messari/curve-finance-ethereum')

most_traded_pools = curve.Query.liquidityPools(orderBy=curve.LiquidityPool.cumulativeVolumeUSD, orderDirection='desc', first=4,)

most_traded_snapshots = most_traded_pools.dailySnapshots(orderBy=curve.LiquidityPoolDailySnapshot.dailyTotalRevenue, orderDirection='desc', first=3,)

sg.query_df([most_traded_pools.name, most_traded_snapshots.dailyVolumeUSD, most_traded_snapshots.dailyTotalRevenueUSD,])
```

### Subgrounds Plotly Wrapper

Introduction:
The Subgrounds Plotly Wrapper is a powerful extension that allows Plotly components to work seamlessly with the Subgrounds library. It offers a user-friendly method to visualize data retrieved from subgraphs using Plotly. The wrapper achieves this by augmenting Plotly's trace components with added functionality.

Example 1: Getting Started with Subgrounds Plotly Wrapper:
The example below illustrates how to initialize the Subgrounds Plotly Wrapper. It demonstrates the import process for the necessary components, how to load a subgraph, and create a Figure instance with appropriate traces.
```python
from subgrounds import Subgrounds
from subgrounds.contrib.plotly import Figure, Indicator

sg = Subgrounds()
aave_v2 = sg.load_subgraph('https://api.thegraph.com/subgraphs/name/messari/aave-v2-ethereum')

Figure(subgrounds=sg, traces=[Indicator(value=pair.token0Price),])
```

Example 2: Creating a Simple Indicator:
This example guides you through the creation of a simple Indicator using the Subgrounds Plotly Wrapper.
```python
from subgrounds import Subgrounds
from subgrounds.contrib.plotly import Figure, Indicator

sg = Subgrounds()
aave_v2 = sg.load_subgraph('https://api.thegraph.com/subgraphs/name/messari/aave-v2-ethereum')

Figure(subgrounds=sg, traces=[Indicator(value=pair.token0Price),])
```

Example 3: Generating Scatter and Bar Plots:
This example demonstrates the creation of Scatter and Bar plots using Subgrounds and the Plotly Wrapper. The process involves loading a subgraph, fetching data for the past 30 days, creating synthetic fields, generating Scatter and Bar traces, and finally, constructing Figure instances to display the plots.
```python
from datetime import datetime

import pandas as pd

from subgrounds import FieldPath, Subgrounds, SyntheticField
from subgrounds.contrib.plotly import Figure, Scatter, Bar

sg = Subgrounds()

lido_activity = sg.load_subgraph('https://api.thegraph.com/subgraphs/name/messari/lido-ethereum')

usage_daily_snapshot_30days = lido_activity.Query.usageMetricsDailySnapshots(orderBy=lido_activity.UsageMetricsDailySnapshot.timestamp, orderDirection='desc', first=30,)

daily_snapshot = lido_activity.UsageMetricsDailySnapshot

daily_snapshot.datetime = SyntheticField.datetime_of_timestamp(daily_snapshot.timestamp)

trace = Scatter(x=usage_daily_snapshot_30days.datetime, y=usage_daily_snapshot_30days.dailyActiveUsers,)

fig = Figure(subgrounds=sg, traces=trace, layout=dict(title='Daily Active Users vs Datetime', xaxis=dict(title='Datetime'), yaxis=dict(title='Daily Active Users'),),)

trace2 = Bar(x=usage_daily_snapshot_30days.datetime, y=usage_daily_snapshot_30days.dailyTransactionCount,)

fig2 = Figure(subgrounds=sg, traces=trace2, layout=dict(title='Daily Transaction Count', xaxis=dict(title='Datetime'), yaxis=dict(title='Daily Transaction Count'),),)

fig.figure.show()

fig2.figure.show()
```
Additional Resources:
For more detailed information, consider visiting the Plotly Docs.

### Custom Pagination Strategies

Subgrounds offers the ability for developers to define their own pagination strategies. This is done by creating a class that adheres to the PaginationStrategy protocol. The class constructor should accept two arguments: a SchemaMeta and a Document. SchemaMeta represents the schema of the targeted subgraph API, while the Document represents the specific query to be paginated.

Example 1: Implementing the PaginationStrategy Protocol:
The example below demonstrates a class implementing the PaginationStrategy protocol:

```python
class PaginationStrategy(Protocol):
    def __init__(
        self,
        schema: SchemaMeta,
        document: Document
    ) -> None: ...

    def step(
        self,
        page_data: Optional[dict[str, Any]] = None
    ) -> Tuple[Document, dict[str, Any]]: ...
```

Example 2: Paginating Over a Query Document:
Subgrounds uses a specific algorithm to paginate over a query document based on the provided pagination strategy. This algorithm is outlined in the following example:

```python
def paginate(
    schema: SchemaMeta,
    doc: Document,
    pagination_strategy: Type[PaginationStrategy]
) -> dict[str, Any]:
    try:
        strategy = pagination_strategy(schema, doc)

        data: dict[str, Any] = {}

        next_page_doc, variables = strategy.step(page_data=None)

        while True:
            try:
                page_data = client.query(
                    url=next_page_doc.url,
                    query_str=next_page_doc.graphql,
                    variables=next_page_doc.variables | variables
                )

                data = merge(data, page_data)

                next_page_doc, variables = strategy.step(page_data=page_data)
            
            except StopPagination:
                break
            
            except Exception as exn:
                raise PaginationError(exn.args[0], strategy)

        return data

    except SkipPagination:
        return client.query(doc.url, doc.graphql, variables=doc.variables)
```

# Subgrounds code examples
## The following are Subgrounds query examples and show how to create subgrounds code

### Standard query example
This example shows how to load a subgraph and perform a query with a condition.
```python
from subgrounds.subgrounds import Subgrounds

sg = Subgrounds()

# Replace with your subgraph url
subgraph_url = 'your_subgraph_url_here'
subgraph = sg.load_subgraph(subgraph_url)

# Replace with your conditions and fields to fetch
query_result = subgraph.Query.your_query_here(
    first=10,
    orderBy=subgraph.YourField.your_field_here,
    orderDirection="desc",
    where=[subgraph.YourField.your_field_here > your_value_here]
)

dataframe = sg.query_df([query_result.your_field_here, query_result.your_field_here])
```

### Nested Query
This example shows how to perform a nested query.
```python
from subgrounds import Subgrounds

sg = Subgrounds()

# Replace with your subgraph url
subgraph_url = 'your_subgraph_url_here'
subgraph = sg.load_subgraph(subgraph_url)

# Replace with your conditions and fields to fetch
query_result = subgraph.Query.your_query_here(
    orderBy=subgraph.YourField.your_field_here,
    orderDirection='desc',
    first=10,
)

nested_query_result = query_result.your_nested_query_here(
    orderBy=subgraph.YourNestedField.your_nested_field_here,
    orderDirection='desc',
    first=10,
)

dataframe = sg.query_df([
    query_result.your_field_here,
    nested_query_result.your_nested_field_here,
    nested_query_result.your_nested_field_here
])
```

### Synthetic Field
This example shows how to create a synthetic field.
```python
from subgrounds import Subgrounds

sg = Subgrounds()

# Replace with your subgraph url
subgraph_url = 'your_subgraph_url_here'
subgraph = sg.load_subgraph(subgraph_url)

# Replace with your synthetic field computation
subgraph.YourEntity.your_synthetic_field = (
    abs(subgraph.YourEntity.your_field_here - subgraph.YourEntity.your_field_here) 
    / abs(subgraph.YourEntity.your_field_here - subgraph.YourEntity.your_field_here)
)

# Replace with your conditions and fields to fetch
query_result = subgraph.Query.your_query_here(
    orderBy=subgraph.YourField.your_field_here,
    orderDirection='desc',
    first=10
)

dataframe = sg.query_df([query_result.your_field_here, query_result.your_synthetic_field])
```

### Gateway setup with Subgrounds:
```python
from subgrounds import Subgrounds
sg = Subgrounds.from_pg_key("YOUR_PG_API_KEY")
desired_subgraph_id = "YOUR_SUBGRAPH_ID"
```

### Loading a subgraph using a proxy endpoint:
```python
desired_subgraph = sg.load_subgraph(f"https://api.yourdomain.com/v1/proxy/subgraphs/id/{desired_subgraph_id}")
```

### Using a synthetic field helper to convert a timestamp to datetime:
```python
from subgrounds.subgraph import SyntheticField
specific_entity.timestamp_field = SyntheticField.datetime_of_timestamp(specific_entity.timestamp)
```
### Using SyntheticFields in subgraph queries:
```python
from subgrounds.subgraph import SyntheticField
from datetime import datetime

some_query = your_subgraph.YourQuery

some_query.synth_field = SyntheticField(
    f=lambda timestamp: str(datetime.fromtimestamp(timestamp)),
    type_=SyntheticField.STRING,
    deps=some_query.timestamp,
)

some_query.datetime = SyntheticField.datetime_of_timestamp(some_query.timestamp)

some_query = your_subgraph.Query.your_query_method(
    first = 100,
    orderDirection = 'desc'
)

sg.query_df([
    some_query.datetime,
    some_query.synth_field,
    some_query.some_field,
    some_query.some_other_field,
])
```

### Creating SyntheticFields:
```python
from subgrounds.subgraph import SyntheticField

your_subgraph.YourEntity.new_synthetic_field = SyntheticField(
    lambda x, y: x/y,
    SyntheticField.FLOAT,
    [your_subgraph.YourEntity.field_x, your_subgraph.YourEntity.field_y],
)

sg.query([your_entity.field_x, your_entity.field_y, your_entity.new_synthetic_field])

your_subgraph.YourEntity.another_synthetic_field = (
    abs(your_subgraph.YourEntity.field_a) / abs(your_subgraph.YourEntity.field_b)
)

sg.query_df([your_entity.field_a, your_entity.field_b, your_entity.another_synthetic_field])
```

In these examples, you'd replace YOUR_PG_API_KEY, YOUR_SUBGRAPH_ID, yourdomain.com, specific_entity, your_subgraph, YourQuery, your_query_method, some_field, some_other_field, YourEntity, field_x, field_y, field_a, and field_b with the actual values you'd use in your code.