```python
from subgrounds import Subgrounds
from datetime import datetime
from subgrounds.subgraph import SyntheticField
import pandas as pd

# Initialize Subgrounds and load the subgraph
sg = Subgrounds()
stargate_eth = sg.load_subgraph("https://api.thegraph.com/subgraphs/name/messari/stargate-ethereum")

# Define the query and field paths
usage_metrics_daily_snapshots = stargate_eth.Query.usageMetricsDailySnapshots(first=1000)

# Create the datetime synthetic field
stargate_eth.UsageMetricsDailySnapshot.datetime = SyntheticField(
    lambda timestamp: str(datetime.fromtimestamp(timestamp)),
    SyntheticField.FLOAT,
    stargate_eth.UsageMetricsDailySnapshot.timestamp,
)

# Field paths for each category
cumulative_metrics_fields = [
    usage_metrics_daily_snapshots.cumulativeLiquidityDepositCount,
    usage_metrics_daily_snapshots.cumulativeLiquidityWithdrawCount,
    usage_metrics_daily_snapshots.cumulativeMessageReceivedCount,
    usage_metrics_daily_snapshots.cumulativeMessageSentCount,
    usage_metrics_daily_snapshots.cumulativeTransactionCount,
    usage_metrics_daily_snapshots.cumulativeTransferInCount,
    usage_metrics_daily_snapshots.cumulativeTransferOutCount,
    usage_metrics_daily_snapshots.cumulativeUniqueLiquidityProviders,
    usage_metrics_daily_snapshots.cumulativeUniqueMessageSenders,
    usage_metrics_daily_snapshots.cumulativeUniqueTransferReceivers,
    usage_metrics_daily_snapshots.cumulativeUniqueTransferSenders,
    usage_metrics_daily_snapshots.cumulativeUniqueUsers,
]

daily_metrics_fields = [
    usage_metrics_daily_snapshots.dailyActiveLiquidityProviders,
    usage_metrics_daily_snapshots.dailyActiveMessageSenders,
    usage_metrics_daily_snapshots.dailyActiveTransferReceivers,
    usage_metrics_daily_snapshots.dailyActiveTransferSenders,
    usage_metrics_daily_snapshots.dailyActiveUsers,
    usage_metrics_daily_snapshots.dailyLiquidityDepositCount,
    usage_metrics_daily_snapshots.dailyLiquidityWithdrawCount,
    usage_metrics_daily_snapshots.dailyMessageReceivedCount,
    usage_metrics_daily_snapshots.dailyMessageSentCount,
    usage_metrics_daily_snapshots.dailyTransactionCount,
    usage_metrics_daily_snapshots.dailyTransferInCount,
    usage_metrics_daily_snapshots.dailyTransferOutCount,
]

snapshot_info_fields = [
    usage_metrics_daily_snapshots.day,
    usage_metrics_daily_snapshots.id,
    usage_metrics_daily_snapshots.datetime,  # Use the synthetic field for datetime
    usage_metrics_daily_snapshots.timestamp,
]

protocol_metrics_fields = [
    usage_metrics_daily_snapshots.totalCanonicalRouteCount,
    usage_metrics_daily_snapshots.totalPoolCount,
    usage_metrics_daily_snapshots.totalPoolRouteCount,
    usage_metrics_daily_snapshots.totalSupportedTokenCount,
    usage_metrics_daily_snapshots.totalWrappedRouteCount,
]

# Execute the query and store the results in a DataFrame
cumulative_metrics_df = sg.query_df(cumulative_metrics_fields)
daily_metrics_df = sg.query_df(daily_metrics_fields)
snapshot_info_df = sg.query_df(snapshot_info_fields)
protocol_metrics_df = sg.query_df(protocol_metrics_fields)

```
```python
# Initialize Subgrounds and load the subgraph
sg = Subgrounds()
stargate_eth = sg.load_subgraph("https://api.thegraph.com/subgraphs/name/messari/stargate-ethereum")

# Define the query and field paths
pools_query = stargate_eth.Query.pools(first=1000)

# Field paths for each category
snapshot_fields = [
    pools_query._lastDailySnapshotTimestamp,
    pools_query._lastHourlySnapshotTimestamp,
]

creation_fields = [
    pools_query.createdBlockNumber,
    pools_query.createdTimestamp,
]

cumulative_metrics_fields = [
    pools_query.cumulativeProtocolSideRevenueUSD,
    pools_query.cumulativeSupplySideRevenueUSD,
    pools_query.cumulativeTotalRevenueUSD,
    pools_query.cumulativeVolumeIn,
    pools_query.cumulativeVolumeInUSD,
    pools_query.cumulativeVolumeOut,
    pools_query.cumulativeVolumeOutUSD,
]

identity_fields = [
    pools_query.id,
    pools_query.name,
    pools_query.symbol,
    pools_query.type,
]

liquidity_fields = [
    pools_query.inputTokenBalance,
    pools_query.outputTokenSupply,
    pools_query.stakedOutputTokenAmount,
]

rewards_fields = [
    pools_query.rewardTokenEmissionsAmount,
    pools_query.rewardTokenEmissionsUSD,
]

volume_fields = [
    pools_query.netVolume,
    pools_query.netVolumeUSD,
    pools_query.outputTokenPriceUSD,
]

value_locked_fields = [
    pools_query.totalValueLockedUSD,
]

# Execute the query and store the results in DataFrames
snapshot_df = sg.query_df(snapshot_fields)
creation_df = sg.query_df(creation_fields)
cumulative_metrics_df = sg.query_df(cumulative_metrics_fields)
identity_df = sg.query_df(identity_fields)
liquidity_df = sg.query_df(liquidity_fields)
rewards_df = sg.query_df(rewards_fields)
volume_df = sg.query_df(volume_fields)
value_locked_df = sg.query_df(value_locked_fields)
```
```python
print("Cumulative Metrics:")
cumulative_metrics_df
```
```python
print("Snapshot Information:")
snapshot_info_df
```
```python
print("Snapshot Fields:")
snapshot_df
```
```python
print("Creation Fields:")
creation_df
```
```python
print("Cumulative Metrics Fields:")
cumulative_metrics_df
```
```python
print("Identity Fields:")
identity_df
```
```python
print("Liquidity Fields:")
liquidity_df
```
```python
print("Rewards Fields:")
rewards_df
```
```python
print("Volume Fields:")
volume_df
```
```python
print("Total Value Locked Fields:")
value_locked_df
```


---

```python
from datetime import datetime
from subgrounds.subgraph import SyntheticField
from subgrounds import Subgrounds
import pandas as pd

# Initialize Subgrounds
sg = Subgrounds()

# Load a subgraph using its API URL
balancer_v2 = sg.load_subgraph('https://api.thegraph.com/subgraphs/name/messari/balancer-v2-ethereum')

# Create a SyntheticField on the LiquidityPool entity called `datetime`, which will format the createdTimestamp field into a human readable datetime string.
balancer_v2.LiquidityPool.datetime = SyntheticField(
    lambda timestamp: str(datetime.fromtimestamp(int(timestamp))),
    SyntheticField.FLOAT,
    balancer_v2.LiquidityPool.createdTimestamp
)

# Create a FieldPath object for the required fields in the liquidityPools entity.
# Specify options to sort the data by createdTimestamp in descending order and limit the number of results to 100.
liquidity_pools_query = balancer_v2.Query.liquidityPools(
    orderBy=balancer_v2.LiquidityPool.createdTimestamp, 
    orderDirection='desc', 
    first=100
)

# Field paths for each category
pool_identity_fields = [
    liquidity_pools_query._poolId,
    liquidity_pools_query.name,
    liquidity_pools_query.symbol,
    liquidity_pools_query.isSingleSided,
]

pool_metrics_fields = [
    liquidity_pools_query.createdBlockNumber,
    liquidity_pools_query.createdTimestamp,
    liquidity_pools_query.datetime,
    liquidity_pools_query.totalValueLockedUSD,
]

pool_revenue_fields = [
    liquidity_pools_query.cumulativeProtocolSideRevenueUSD,
    liquidity_pools_query.cumulativeSupplySideRevenueUSD,
    liquidity_pools_query.cumulativeTotalRevenueUSD,
]

pool_volume_fields = [
    liquidity_pools_query.cumulativeVolumeUSD,
    liquidity_pools_query.outputTokenPriceUSD,
]

pool_balances_fields = [
    liquidity_pools_query.inputTokenBalances,
    liquidity_pools_query.inputTokenWeights,
    liquidity_pools_query.outputTokenSupply,
    liquidity_pools_query.stakedOutputTokenAmount,
]

pool_rewards_fields = [
    liquidity_pools_query.rewardTokenEmissionsAmount,
    liquidity_pools_query.rewardTokenEmissionsUSD,
]

# Concatenate all field paths
liquidity_pools_fields = (
    pool_identity_fields
    + pool_metrics_fields
    + pool_revenue_fields
    + pool_volume_fields
    + pool_balances_fields
    + pool_rewards_fields
)

# Execute the query and store the results in a DataFrame
liquidity_pools_df = sg.query_df(liquidity_pools_fields)

# Print the results
print("Liquidity Pools:")
print(liquidity_pools_df)
```
```python
from datetime import datetime
from subgrounds.subgraph import SyntheticField
from subgrounds import Subgrounds

# Initialize Subgrounds and load the subgraph
sg = Subgrounds()
subgraph_url = 'https://api.thegraph.com/subgraphs/name/messari/lido-ethereum'
subgraph = sg.load_subgraph(subgraph_url)

# Create a SyntheticField on the FinancialsDailySnapshot entity called `datetime`, which will format the timestamp field into a human readable datetime string.
subgraph.FinancialsDailySnapshot.datetime = SyntheticField(
    lambda timestamp: str(datetime.fromtimestamp(int(timestamp))),
    SyntheticField.FLOAT,
    subgraph.FinancialsDailySnapshot.timestamp
)

# Define the query and field paths
financials_query = subgraph.Query.financialsDailySnapshots(first=1000)

# Field paths for each category
protocol_revenue_fields = [
    financials_query.cumulativeProtocolSideRevenueUSD,
    financials_query.dailyProtocolSideRevenueUSD,
]

supply_revenue_fields = [
    financials_query.cumulativeSupplySideRevenueUSD,
    financials_query.dailySupplySideRevenueUSD,
]

total_revenue_fields = [
    financials_query.cumulativeTotalRevenueUSD,
    financials_query.dailyTotalRevenueUSD,
]

volume_fields = [
    # financials_query.cumulativeVolumeUSD,
    # financials_query.dailyVolumeUSD,
]

value_locked_fields = [
    financials_query.protocolControlledValueUSD,
    financials_query.totalValueLockedUSD,
]

identity_fields = [
    financials_query.blockNumber,
    financials_query.id,
    financials_query.timestamp,
]

# Concatenate all field paths
financials_fields = (
    protocol_revenue_fields
    + supply_revenue_fields
    + total_revenue_fields
    + volume_fields
    + value_locked_fields
    + identity_fields
)

# Execute the query and store the results in a DataFrame
financials_df = sg.query_df(financials_fields)

# Print the results
print("Financials Daily Snapshots:")
print(financials_df)
```
```python
from subgrounds import Subgrounds

# Initialize Subgrounds and load the subgraph
sg = Subgrounds()
subgraph_url = 'https://api.thegraph.com/subgraphs/name/messari/balancer-v2-ethereum'
subgraph = sg.load_subgraph(subgraph_url)

# Define the query and field paths
metrics_query = subgraph.Query.usageMetricsDailySnapshots(first=1000)

# Field paths for each category
block_and_id_fields = [
    metrics_query.blockNumber,
    metrics_query.id,
    metrics_query.timestamp,
]

user_activity_fields = [
    metrics_query.cumulativeUniqueUsers,
    metrics_query.dailyActiveUsers,
]

transaction_count_fields = [
    metrics_query.dailyDepositCount,
    metrics_query.dailySwapCount,
    metrics_query.dailyTransactionCount,
    metrics_query.dailyWithdrawCount,
]

pool_count_field = [
    metrics_query.totalPoolCount,
]

# Concatenate all field paths
metrics_fields = (
    block_and_id_fields
    + user_activity_fields
    + transaction_count_fields
    + pool_count_field
)

# Execute the query and store the results in a DataFrame
metrics_df = sg.query_df(metrics_fields)

# Print the results
print("Usage Metrics Daily Snapshots:")
print(metrics_df)

```


---

```python

```


---

# Uniswap v3 Analysis



## Querying Financials Daily Snapshots

This code section retrieves information about the latest financial snapshot of a specific Uniswap v3 subgraph. It does the following:

- Imports necessary libraries for Subgrounds and environment variables

- Loads environment variables from a `.env` file

- Creates a `Subgrounds` object for interacting with subgraphs

- Loads a specific Uniswap v3 subgraph with a given API endpoint

- Queries the `financialsDailySnapshots` endpoint with specific filter criteria

- Converts the query results to a Pandas dataframe and extracts the first row

- View the result



## Querying Liquidity Pools

This code section retrieves information about the liquidity pools of a specific Uniswap v3 subgraph. It does the following:

- Queries the `liquidityPools` endpoint with specific filter criteria

- Converts the query results to a Pandas dataframe and extracts the first row

- Stores the resulting Pandas series in `res2`



## Querying dexAmmProtocols

This code section retrieves information about the decentralized exchange automated market maker (DEX AMM) protocols of a specific Uniswap v3 subgraph. It does the following:

- Queries the `dexAmmProtocols` endpoint with specific filter criteria

- Converts the query results to a Pandas dataframe and extracts the first row

- Stores the resulting Pandas series in `res3`



## Querying Pools Daily Snapshots

This code section retrieves information about a specific liquidity pool on a Uniswap v3 subgraph. It does the following:

- Queries the `liquidityPoolDailySnapshots` endpoint with specific filter criteria

- Queries multiple fields from the resulting data and stores it in a JSON object

- Prints the resulting JSON object






```python
# Import the Subgrounds library
from subgrounds import Subgrounds
from dotenv import load_dotenv
import os

load_dotenv()
graph_api_key = os.getenv('GRAPH_API_KEY')

# Create a new Subgrounds object
sg = Subgrounds()

# Load the Uniswap v3 subgraph using a specific API endpoint
uni = sg.load_subgraph(f'https://gateway.thegraph.com/api/{graph_api_key}/subgraphs/id/ELUcwgpm14LKPLrBRuVvPvNKHQ9HvwmtKgKSH6123cr7')
# b2f94294e72881a7cdfe13eaba5709f4
# Query the financialsDailySnapshots endpoint with a specified order, limit, and filter criteria
latest_snapshots = uni.Query.financialsDailySnapshots(
  orderBy=uni.FinancialsDailySnapshot.timestamp,
  orderDirection='desc',
  first=1,
)

# Convert the query results to a Pandas dataframe and extract the first row
res = sg.query_df(latest_snapshots).squeeze()

# Print the result
res
```
```python
# This code queries the liquidityPools endpoint of a specific Uniswap v3 subgraph to retrieve information about the liquidity pools that exist on the network

# Create a query object for the liquidityPools endpoint that specifies that the first result should be returned, the results should be sorted in descending order by the total value locked in USD, and the order should be descending.
pools = uni.Query.liquidityPools(
  first=1,
  orderBy=uni.LiquidityPool.totalValueLockedUSD,
  orderDirection='desc'
)

# Execute the query, convert the results into a Pandas dataframe, and extract the first row as a Pandas series.
res2 = sg.query_df(pools).squeeze()

# Store the resulting Pandas series in res2.
res2
```
```python
# This code queries the dexAmmProtocols endpoint of a specific Uniswap v3 subgraph to retrieve information about the decentralized exchange automated market maker (DEX AMM) protocols that exist on the network.

# Create a query object for the dexAmmProtocols endpoint that specifies that the first result should be returned.
protocol = uni.Query.dexAmmProtocols(
  first=1
)

# Execute the query, convert the results into a Pandas dataframe, and extract the first row as a Pandas series.
res3 = sg.query_df(protocol).squeeze()

# Store the resulting Pandas series in res3.
res3

```
```python
# Query the liquidity pool daily snapshots with specified filter criteria
lp = uni.Query.liquidityPoolDailySnapshots(
    first=1,
    orderBy=uni.LiquidityPoolDailySnapshot.timestamp,
    orderDirection='desc',
    where=[uni.LiquidityPoolDailySnapshot.pool == '0x88e6a0c2ddd26feeb64f039a2c41296fcb3f5640']
)

# Query multiple fields from the resulting data and store in a JSON object
res4 = sg.query_json([
    lp.id,
    lp.pool.name,
    lp.blockNumber,
    lp.totalValueLockedUSD,
    lp.cumulativeSupplySideRevenueUSD,
    lp.dailySupplySideRevenueUSD,
    lp.cumulativeProtocolSideRevenueUSD,
    lp.dailyTotalRevenueUSD,
    lp.dailyVolumeUSD,
    lp.cumulativeVolumeUSD,
    lp.outputTokenSupply,
    lp.outputTokenPriceUSD,
    lp.stakedOutputTokenAmount,
    lp.inputTokenBalances,
    lp.inputTokenWeights,
    lp.rewardTokenEmissionsAmount,
    lp.rewardTokenEmissionsUSD,
    lp.dailyVolumeByTokenAmount,
    lp.dailyVolumeByTokenUSD,
    lp.protocol.cumulativeProtocolSideRevenueUSD,
    lp.protocol.cumulativeSupplySideRevenueUSD,
    lp.protocol.cumulativeTotalRevenueUSD,
    lp.protocol.protocolControlledValueUSD,
    lp.protocol.totalPoolCount,
    lp.protocol.totalValueLockedUSD,
    lp.pool.outputToken.lastPriceUSD,
    lp.pool.outputToken.name,
])

# Print the resulting JSON object
res4

```
```python

```


---

# AAVE v3 Mainnet



**What is Aave?**



Aave is a decentralized finance protocol that allows people to lend and borrow cryptocurrencies. 

Lenders earn interest by depositing digital assets into specially created liquidity pools. Borrowers can then use their crypto as collateral to take out a flash loan using this liquidity.



**What does this example cover?**



In this example, we utilize the Subgrounds library to interact with the AAVE v3 Ethereum subgraph and fetch data related to its various usage metrics and lending protocols. This example explains how to load a subgraph, query it, handle and transform the data returned, and even visualize it. The detailed breakdown is as follows:



- Importing Libraries: The subgrounds library is imported for handling decentralized subgraphs, and pandas is used for handling data manipulation.



- Subgrounds Initialization: A Subgrounds object is instantiated using the `Playgrounds API key`.



- Loading AAVE v3 Subgraph: The AAVE v3 subgraph is loaded by passing its ID to a URL string and calling `sg.load_subgraph()`.



- Querying Subgraph: A `UsageMetricsDailySnapshot` query is performed on the subgraph, where the first 10 entries are fetched in descending order.



- Data Extraction: The extracted data, including `timestamp`, `daily active borrowers`, and `daily active depositors`, are fetched into a DataFrame using `sg.query_df()`.



- Converting Timestamps: Two methods are demonstrated for converting timestamp data to a more human-readable format using the `SyntheticField` object and the `datetime.fromtimestamp()` function.



- Querying Lending Protocols: Queries are performed on the `lendingProtocols` entity of the AAVE v3 subgraph, fetching all fields and specific fields. The returned data are then fetched into a DataFrame.



- SyntheticField for Custom Metrics: SyntheticField objects are created to calculate custom metrics, such as the `borrow-deposit ratio`, `user engagement metrics` for borrowed funds, and average values for borrow, deposit, and liquidation per user.



- Fetching Market Daily Snapshots: Queries are performed on the marketDailySnapshots entity of the subgraph, fetching specific market rates, converting timestamps, and restructuring the DataFrame using the pivot() function.



- Data Visualization: The data are plotted using plotly, showcasing interest rates over time and daily active users against datetime.



In conclusion, this code snippet effectively demonstrates how to utilize the Subgrounds library to interact with Ethereum subgraphs and process, manipulate, and visualize the extracted data. It's a useful guide for anyone looking to interact with Ethereum subgraphs and create custom metrics for data analysis.

About AAVE:



Aave is a decentralized finance protocol that allows people to lend and borrow cryptocurrencies. 



Lenders earn interest by depositing digital assets into specially created liquidity pools. 



Borrowers can then use their crypto as collateral to take out a flash loan using this liquidity.



Aave V3, introducing important new risk mitigation features and improved capital efficiency



V3 was designed with a flexible architecture for increased composability, and made it possible to build a variety of innovative features on top of the protocol such as new risk management tools that provide additional security and stability. 



Examples include Supply and Borrow Caps and Risk and Listing Admins. Aave V3 also improves capital efficiency and decentralized liquidity while lowering gas fees 25 percent.

```python
## Playgrounds Gateway setup - visit app.playgrounds.network to get an api key to query decentralized subgraphs

# Import subgrounds
from subgrounds import Subgrounds

# Instantiate subgrounds and insert Playgrounds API key into header
sg = Subgrounds.from_pg_key("PGA_API_KEY")

# Insert desired subgraph id from decentralized subgraph. Find in subgraph url
aave_v3_id = "SUBGRAPH_ID"
```
```python
# Load subgraph using playgrounds proxy endpoint 
aave_v3 = sg.load_subgraph(f"https://api.playgrounds.network/v1/proxy/subgraphs/id/{aave_v3_id}")
```
```python
# How to query subgraphs with subgrounds
# Subgrounds allows the same arguments as you normally use on graphql

usage_metrics_daily = aave_v3.Query.usageMetricsDailySnapshots(
    first = 10,
    orderDirection = 'desc'
)

q_df_ex = sg.query_df([
    usage_metrics_daily.timestamp,
    usage_metrics_daily.dailyActiveBorrowers,
    usage_metrics_daily.dailyActiveDepositors,
])
```
```python
q_df_ex
```
```python
from subgrounds.subgraph import SyntheticField
from datetime import datetime

usage_metrics_daily = aave_v3.UsageMetricsDailySnapshot

# Method 1
usage_metrics_daily.d_t = SyntheticField(
    f=lambda timestamp: str(datetime.fromtimestamp(timestamp)),
    type_=SyntheticField.STRING,
    deps=usage_metrics_daily.timestamp,
)

# Method 2: This helper constructor makes it easy to convert timestamps into datetime objects.
usage_metrics_daily.datetime = SyntheticField.datetime_of_timestamp(usage_metrics_daily.timestamp)

usage_metrics_daily = aave_v3.Query.usageMetricsDailySnapshots(
    first = 100,
    orderDirection = 'desc'
)

sg.query_df([
    usage_metrics_daily.datetime,
    usage_metrics_daily.d_t,
    usage_metrics_daily.dailyActiveBorrowers,
    usage_metrics_daily.dailyActiveDepositors,
    usage_metrics_daily.dailyActiveLiquidatees,
    usage_metrics_daily.dailyActiveLiquidators,
])
```
Let's play with synthetic fields some more and create some interesting transformations. That we can query as if regular GraphQL fields. 



SyntheticFields can created using the constructor, allowing for much more complex transformations.

```python

# Query lending protocols entitty and fields from subgraph
# Here we are querying all of the fields in the lending protocols

aave_lending = aave_v3.Query.lendingProtocols()
aave_overview = sg.query_df(aave_lending)
aave_overview.squeeze()
```
```python
# Query lending protocols entitty and specific fields 

aave_lending = aave_v3.Query.lendingProtocols()
aave_overview = sg.query_df([
    aave_lending.name,
    aave_lending.type,
    aave_lending.cumulativeBorrowUSD,
    aave_lending.cumulativeDepositUSD,
    aave_lending.cumulativeLiquidateUSD,
    aave_lending.cumulativePositionCount,
    aave_lending.cumulativeProtocolSideRevenueUSD,
    aave_lending.cumulativeSupplySideRevenueUSD,
    aave_lending.cumulativeTotalRevenueUSD,
    aave_lending.cumulativeUniqueUsers,
    aave_lending.cumulativeUniqueBorrowers,
    aave_lending.cumulativeUniqueDepositors,
    aave_lending.cumulativeUniqueLiquidatees,
    aave_lending.cumulativeUniqueLiquidators,
])
aave_overview.squeeze()
```
```python
from subgrounds.subgraph import SyntheticField

# Borrow_Deposit_Ratio: Calculate borrow deposit ratio by dividing the total borrow by the total deposit
aave_v3.LendingProtocol.borrow_dep_ratio = SyntheticField(
    lambda x, y: x/y,
    SyntheticField.FLOAT,
    [aave_v3.LendingProtocol.totalBorrowBalanceUSD,
    aave_v3.LendingProtocol.totalDepositBalanceUSD],
)

sg.query([aave_lending.totalBorrowBalanceUSD,
          aave_lending.totalDepositBalanceUSD,
          aave_lending.borrow_dep_ratio])
```
```python
# User Engagement Metrics: You can calculate the proportion of users who have ever borrowed,
# by dividing each of the cumulativeUnique...
# fields by cumulativeUniqueUsers

aave_v3.LendingProtocol.user_engagement_borrowed = (
    abs(aave_v3.LendingProtocol.cumulativeUniqueBorrowers)
/abs(aave_v3.LendingProtocol.cumulativeUniqueUsers)
)

sg.query_df([aave_lending.cumulativeUniqueBorrowers,
             aave_lending.cumulativeUniqueUsers,
             aave_lending.user_engagement_borrowed])
```
```python
# Average Borrow, Deposit, and Liquidation Values: cumulativeBorrowUSD divided by cumulativeUniqueBorrowers,
# cumulativeDepositUSD divided by cumulativeUniqueDepositors, and cumulativeLiquidateUSD divided by 
# cumulativeUniqueLiquidatees will give you the average amount borrowed, deposited, and liquidated per user.

# Average borrow
aave_v3.LendingProtocol.avg_borrow_per_user = SyntheticField(
    lambda x, y: x/y,
    SyntheticField.FLOAT,
    [aave_v3.LendingProtocol.cumulativeBorrowUSD,
    aave_v3.LendingProtocol.cumulativeUniqueBorrowers],
)

# Average deposit
aave_v3.LendingProtocol.avg_deposit_per_user = SyntheticField(
    lambda x, y: x/y,
    SyntheticField.FLOAT,
    [aave_v3.LendingProtocol.cumulativeDepositUSD,
    aave_v3.LendingProtocol.cumulativeUniqueDepositors],
)

# Average liqudation per user
aave_v3.LendingProtocol.avg_liquidation_per_user = SyntheticField(
    lambda x, y: x/y,
    SyntheticField.FLOAT,
    [aave_v3.LendingProtocol.cumulativeLiquidateUSD,
    aave_v3.LendingProtocol.cumulativeUniqueLiquidatees],
)

sg.query_df([aave_lending.avg_borrow_per_user,
          aave_lending.avg_deposit_per_user,
          aave_lending.avg_liquidation_per_user])
```
```python
import pandas as pd
steth_market_id = '0x0b925ed163218f6662a35e0f0371ac234f9e9371'

snapshots = aave_v3.Query.marketDailySnapshots(
    first=100,
    orderBy=aave_v3.MarketDailySnapshot.timestamp,
    orderDirection='desc',
    where={
        'market':steth_market_id
    }
)

df = sg.query_df([
    snapshots.timestamp,
    snapshots.rates.rate,
    snapshots.rates.side,
    snapshots.rates.type
])

df['side_type'] = df['marketDailySnapshots_rates_side'] +'-' +  df['marketDailySnapshots_rates_type']
df2 = df[['marketDailySnapshots_timestamp', 'marketDailySnapshots_rates_rate', 'side_type']]
df2 = df2.pivot(index='marketDailySnapshots_timestamp',columns='side_type').droplevel(level=0, axis=1)
df2.index = pd.to_datetime(df2.index, unit='s')
df2
```
```python
import plotly.express as px
fig = px.line(df2, x=df2.index, y="BORROWER-STABLE", title='STETH Interest Rates')
fig.show()
```
```python
from subgrounds.contrib.plotly import Figure, Scatter

# Create the Scatter trace with appropriate field paths
trace = Scatter(
    x=usage_metrics_daily.datetime,
    y=usage_metrics_daily.dailyActiveUsers,
)

# Create the Figure instance with the trace and display it
fig = Figure(
    subgrounds=sg,
    traces=trace,
    layout=dict(
        title="Daily Active Users vs Datetime",
        xaxis=dict(title="Datetime"),
        yaxis=dict(title="Daily Active Users")
    ),
)
fig.figure.show()
```


---

```python
## Gateway setup
from subgrounds import Subgrounds
sg = Subgrounds.from_pg_key("PGA_API_KEY")
subgraph_id = "GELTrjPJYEzxyp6Y2CtEaYpGHcJNrJA6i5Ci4KfJSEsf"
```
```python
fraxlend_subgraph = sg.load_subgraph(f"https://api.playgrounds.network/v1/proxy/subgraphs/id/{subgraph_id}")
```
```python
fraxlendFactories = fraxlend_subgraph.Query.fraxlendFactories()
fraxlend_overview = sg.query_df([
    fraxlendFactories.id,
    fraxlendFactories.totalTVLValue,
    fraxlendFactories.totalBorrowedValue,
    fraxlendFactories.totalCollateralLockedValue,
    fraxlendFactories.positionCount,
    fraxlendFactories.pairCount,
    fraxlendFactories.assetTokenCount,
    fraxlendFactories.collateralTokenCount, 
])
fraxlend_overview.head()
```
```python
users = fraxlend_subgraph.Query.users(
    first = 10
)
user_metrics = sg.query_df([
    users.address,
    users.id,
])
```
```python
positions = users.positions(
    first =10
)
position_metrics = sg.query_df([
    positions.block,
    positions.timestamp,
    positions.id,
    positions.borrowedAssetShare,
    positions.depositedCollateralAmount,
    positions.lentAssetShare,
])
```
```python
pairs = fraxlend_subgraph.Query.pairs(
    first = 10
)
pairs_metrics = sg.query_df([
    pairs.address,
    # pairs.borrowerWhitelistActive,
    pairs.id,
    # pairs.lenderWhitelistActive,
    # pairs.liquidationFee,
    # pairs.maturity,
    # pairs.maxLTV,
    # pairs.name,
    # pairs.symbol,
    # pairs.collateral,
    pairs.dailyHistory(first = 10),
])
```


---

## Subgrounds Tutorials: Lido Exploration





This code demonstrates how to use the Subgrounds library to interact with a specific subgraph, in this case, the Lido Ethereum subgraph, and fetch usage metrics for a given period (last 30 days).



1. Import the necessary libraries: The code begins by importing the required Python libraries, including `datetime` from the standard library, and `SyntheticField` and `Subgrounds` from the `subgrounds` library. It also imports `pandas` for handling data as DataFrames.

   

2. Initialize Subgrounds: The `Subgrounds` object is initialized as `sg`. This object serves as the main entry point for interacting with different subgraphs and fetching data using GraphQL queries.

   

3. Load Lido Ethereum subgraph: The Lido Ethereum subgraph is loaded using its API URL. This returns a `Subgraph` object named `lido_activity`, which is used to interact with the Lido Ethereum subgraph.

   

4. Query usage metrics daily snapshots: The code constructs a query to fetch the `usageMetricsDailySnapshots` entity from the Lido Ethereum subgraph. It specifies ordering options to sort the data by timestamp in descending order and limits the number of results to 30, effectively fetching the last 30 days of data.

   

5. Create a SyntheticField for human-readable timestamps: A `SyntheticField` named `datetime` is created for the `UsageMetricsDailySnapshot` entity. This field takes the original `timestamp` field, converts it to a human-readable format using the `datetime.fromtimestamp()` function, and stores it as a float. This makes it easier to read and understand the timestamp data.

   

6. Fetch data and store it in a DataFrame: The `sg.query_df()` function is used to execute the query and fetch the data. It takes a list of the fields to be fetched (timestamp, daily active users, cumulative unique users, and daily transaction count) and returns a pandas DataFrame containing the data.



The primary focus of this code is to demonstrate how the Subgrounds library can be used to interact with a subgraph (Lido Ethereum subgraph) and fetch specific data using queries. This data can then be processed, manipulated, and analyzed using other Python libraries like pandas.


```python
from datetime import datetime
from subgrounds.subgraph import SyntheticField
from subgrounds import Subgrounds
import pandas as pd

# Initialize Subgrounds
sg = Subgrounds()

# Load a subgraph using its API URL
lido_activity = sg.load_subgraph('https://api.thegraph.com/subgraphs/name/messari/lido-ethereum')

# Create a FieldPath object for the required fields in the financialsDailySnapshots entity.
# Specify options to sort the data by timestamp in descending order and limit the number of results to 30.
usage_daily_snapshot_30days = lido_activity.Query.usageMetricsDailySnapshots(
    orderBy=lido_activity.UsageMetricsDailySnapshot.timestamp, 
    orderDirection='desc', 
    first=30
)

# Create a SyntheticField on the Swap entity called `timestamp`, which will format the timestamp field into something more human readable
lido_activity.UsageMetricsDailySnapshot.datetime = SyntheticField(
  lambda timestamp: str(datetime.fromtimestamp(timestamp)),
  SyntheticField.FLOAT,
  lido_activity.UsageMetricsDailySnapshot.timestamp
)

sg.query_df([
    usage_daily_snapshot_30days.datetime,
    usage_daily_snapshot_30days.dailyActiveUsers,
    usage_daily_snapshot_30days.cumulativeUniqueUsers,
    usage_daily_snapshot_30days.dailyTransactionCount
])
```
```python

```


---

## Subgrounds Tutorials: Lido Exploration





This code demonstrates how to use the Subgrounds library to interact with a specific subgraph, in this case, the Lido Ethereum subgraph, and fetch finanThis code demonstrates how to use the Subgrounds library to interact with a specific subgraph, in this case, the Lido Ethereum subgraph, and fetch financial data for a given period (last 30 days).



1. Import the necessary libraries: The code starts by importing the required Python libraries, including datetime from the standard library, and `SyntheticField` and `Subgrounds` from the `subgrounds` library. It also imports `pandas` for handling data as DataFrames.



2. Initialize Subgrounds: The `Subgrounds` object is initialized as `sg`. This object serves as the main entry point for interacting with different subgraphs and fetching data using GraphQL queries.



3. Load Lido Ethereum subgraph: The Lido Ethereum subgraph is loaded using its API URL. This returns a `Subgraph` object named `lido_activity`, which is used to interact with the Lido Ethereum subgraph.



4. Query financials daily snapshots: The code constructs a query to fetch the `financialsDailySnapshots` entity from the Lido Ethereum subgraph. It specifies ordering options to sort the data by timestamp in descending order and limits the number of results to 30, effectively fetching the last 30 days of data.



5. Create a SyntheticField for human-readable timestamps: A `SyntheticField` named `datetime` is created for the `FinancialsDailySnapshot` entity. This field takes the original timestamp field, converts it to a human-readable format using the `datetime.fromtimestamp()` function, and stores it as a float. This makes it easier to read and understand the timestamp data.



6. Fetch data and store it in a DataFrame: The `sg.query_df()` function is used to execute the query and fetch the data. It takes a list of the fields to be fetched (timestamp, cumulative protocol-side revenue, cumulative total revenue, cumulative supply-side revenue, daily protocol-side revenue, daily total revenue, daily supply-side revenue, total value locked, and protocol-controlled value) and returns a pandas DataFrame containing the data.



The main focus of this code is to demonstrate how the Subgrounds library can be used to interact with a subgraph (Lido Ethereum subgraph) and fetch specific financial data using queries. This data can then be processed, manipulated, and analyzed using other Python libraries like pandas.


```python
from datetime import datetime
from subgrounds.subgraph import SyntheticField
from subgrounds import Subgrounds
import pandas as pd

# Initialize Subgrounds
sg = Subgrounds()

# Load a subgraph using its API URL
lido_activity = sg.load_subgraph('https://api.thegraph.com/subgraphs/name/messari/lido-ethereum')

# Create a FieldPath object for the required fields in the financialsDailySnapshots entity.
# Specify options to sort the data by timestamp in descending order and limit the number of results to 30.
financials_daily_snapshot_30days = lido_activity.Query.financialsDailySnapshots(
    orderBy=lido_activity.FinancialsDailySnapshot.timestamp, 
    orderDirection='desc', 
    first=30
)

# Create a SyntheticField on the Swap entity called `timestamp`, which will format the timestamp field into something more human readable
lido_activity.FinancialsDailySnapshot.datetime = SyntheticField(
  lambda timestamp: str(datetime.fromtimestamp(timestamp)),
  SyntheticField.FLOAT,
  lido_activity.FinancialsDailySnapshot.timestamp
)

sg.query_df([
    financials_daily_snapshot_30days.datetime,
    financials_daily_snapshot_30days.cumulativeProtocolSideRevenueUSD,
    financials_daily_snapshot_30days.cumulativeTotalRevenueUSD,
    financials_daily_snapshot_30days.cumulativeSupplySideRevenueUSD,
    financials_daily_snapshot_30days.dailyProtocolSideRevenueUSD,
    financials_daily_snapshot_30days.dailyTotalRevenueUSD,
    financials_daily_snapshot_30days.dailySupplySideRevenueUSD,
    financials_daily_snapshot_30days.totalValueLockedUSD,
    financials_daily_snapshot_30days.protocolControlledValueUSD
])
```
```python

```


---

## Subgrounds Tutorials: Lido Exploration





This code demonstrates how to use the Subgrounds library to interact with the Lido Ethereum subgraph and fetch specific financial data for a particular pool with the pool's ID. The data is then processed, manipulated, and displayed in a human-readable format.



- Import the necessary libraries: The code starts by importing the required Python libraries, including `datetime` from the standard library, and `SyntheticField` and `Subgrounds` from the `subgrounds` library. It also imports `pandas` and `numpy` for handling data as DataFrames and performing numerical operations.



- Initialize Subgrounds: The `Subground`s object is initialized as `sg`. This object serves as the main entry point for interacting with different subgraphs and fetching data using GraphQL queries.



- Load Lido Ethereum subgraph: The Lido Ethereum subgraph is loaded using its API URL. This returns a `Subgraph` object named `lido_pool_stETH`, which is used to interact with the Lido Ethereum subgraph.



- Query pool data: The code constructs a query to fetch the `pools` entity from the Lido Ethereum subgraph. It specifies ordering options to sort the data by `createdTimestamp` in descending order and limits the number of results to 30. The `where` clause filters the results to only include the pool with the specified ID.



- Create a SyntheticField for human-readable timestamps: A `SyntheticField` named `datetime` is created for the `Pool` entity. This field takes the original `createdTimestamp` field, converts it to a human-readable format using the `datetime.fromtimestamp()` function, and stores it as a float. This makes it easier to read and understand the timestamp data.



- Create a SyntheticField for decimal conversion: A `SyntheticField` named `inputTokenBalance_decimalConv` is created for the `Pool` entity. This field takes the original `inputTokenBalances` field, divides it by 10^18 to convert it to a decimal representation, and stores it as a float.



- Fetch data and store it in a DataFrame: The `sg.query_df()` function is used to execute the query and fetch the data. It takes a list of the fields to be fetched (created timestamp, cumulative protocol-side revenue, cumulative supply-side revenue, cumulative total revenue, input token balance, output token supply, and total value locked) and returns a pandas DataFrame containing the data.



- Squeeze the DataFrame: The `pool_summary` DataFrame is squeezed using the `squeeze()` function, which turns it into a pandas Series named `squeezed_pool_summary`.



- Format the data: A custom function named `format_decimal()` is defined to format the numbers in the Series to a specified number of decimal places. The `squeezed_pool_summary` Series is then passed through this function, resulting in a new Series named `decimal_pool_summary` with formatted numbers.



- Print the resulting Series: The `decimal_pool_summary` Series is printed to display the fetched and formatted financial data.



The main focus of this code is to demonstrate how the Subgrounds library can be used to interact with a subgraph (Lido Ethereum subgraph) and fetch specific financial data for a particular pool using queries. This data can then be processed, manipulated, and displayed in a human-readable format using other Python libraries like pandas and numpy.






```python
from datetime import datetime
from subgrounds.subgraph import SyntheticField
from subgrounds import Subgrounds
import pandas as pd
import numpy as np

# Initialize Subgrounds
sg = Subgrounds()

# Load a subgraph using its API URL
lido_pool_stETH = sg.load_subgraph('https://api.thegraph.com/subgraphs/name/messari/lido-ethereum')

# Create a FieldPath object for the required fields in the financialsDailySnapshots entity.
# Specify options to sort the data by timestamp in descending order and limit the number of results to 30.
lido_pool_stETH_pool_summary = lido_pool_stETH.Query.pools(
    orderBy=lido_pool_stETH.Pool.createdTimestamp, 
    orderDirection='desc', 
    first=30,
    where=[
        lido_pool_stETH.Pool.id == "0xae7ab96520DE3A18E5e111B5EaAb095312D7fE84"
    ]
)

# Create a SyntheticField on the Swap entity called `timestamp`, which will format the timestamp field into something more human readable
lido_pool_stETH.Pool.datetime = SyntheticField(
  lambda createdTimestamp: str(datetime.fromtimestamp(createdTimestamp)),
  SyntheticField.FLOAT,
  lido_pool_stETH.Pool.createdTimestamp
)

# Create a SyntheticField on the Swap entity called `timestamp`, which will format the timestamp field into something more human readable
lido_pool_stETH.Pool.inputTokenBalance_decimalConv = SyntheticField(
  lambda x: x[0] / (10**18) if type(x) is list else x / (10**18),
  SyntheticField.FLOAT,
  lido_pool_stETH.Pool.inputTokenBalances
)

lido_pool_stETH.Pool.outputTokenSupply_decimalConv = SyntheticField(
  lambda x: x[0] / (10**18) if type(x) is list else x / (10**18),
  SyntheticField.FLOAT,
  lido_pool_stETH.Pool.outputTokenSupply
)

# lido_pool_stETH.Pool.inputTokenBalance_decimalConv = lido_pool_stETH.Pool.inputTokenBalances / (10**18)

pool_summary = sg.query_df([
    lido_pool_stETH_pool_summary.createdTimestamp,
    lido_pool_stETH_pool_summary.cumulativeProtocolSideRevenueUSD,
    lido_pool_stETH_pool_summary.cumulativeSupplySideRevenueUSD,
    lido_pool_stETH_pool_summary.cumulativeTotalRevenueUSD,
    lido_pool_stETH_pool_summary.inputTokenBalance_decimalConv,
    lido_pool_stETH_pool_summary.outputTokenSupply_decimalConv,
    lido_pool_stETH_pool_summary.totalValueLockedUSD
])
pool_creation = sg.query_df([
  lido_pool_stETH_pool_summary.datetime,
])

# squeezed_pool_summary = pool_summary.astype('float64').squeeze()
squeezed_pool_summary = pool_summary.squeeze()
squeezed_pool_creation = pool_creation.squeeze()

def format_decimal(number, decimal_places=4):
    return f"{number:.{decimal_places}f}"

# Assuming your squeezed DataFrame is named 'squeezed_pool_summary'
decimal_pool_summary = squeezed_pool_summary.apply(format_decimal)

# Print the resulting Series
print(f"Pool creation date and time: {squeezed_pool_creation}")
print("Pool summary:")
print(decimal_pool_summary)
```
```python

```


---

## Subgrounds Tutorials: RocketPool_Snapshot



In this example, we are using  SyntheticFields to create new fields that do not exist in the original data source. These new fields are calculated based on existing fields in the financialsDailySnapshots entity.



First, we create a FieldPath object to query the required fields from the financialsDailySnapshots entity, sorted by timestamp in descending order and limited to the last 30 entries.



Next, we create a synthetic field `datetime` in the FinancialsDailySnapshot entity to convert the timestamp field into a human-readable format.



Then, we define three more synthetic fields. 



- `revDiffRevenueUSD30` calculates the difference in revenue between the dailyProtocolSideRevenueUSD and dailySupplySideRevenueUSD fields over the past 30 days. 



- `avgDailyRevenueUSD30` calculates the average of the dailyProtocolSideRevenueUSD and dailySupplySideRevenueUSD fields over the past 30 days.



- `revenueMargin30` calculates the percentage change in revenue between the dailyProtocolSideRevenueUSD and dailySupplySideRevenueUSD fields over the past 30 days.



Finally, we query the required fields, including the newly created synthetic fields, and flatten the data into a single DataFrame for analysis.

```python
from datetime import datetime
from subgrounds.subgraph import SyntheticField
from subgrounds import Subgrounds
import pandas as pd

# Initialize Subgrounds
sg = Subgrounds()

# Load a subgraph using its API URL
financials_daily_snapshots = sg.load_subgraph('https://api.thegraph.com/subgraphs/name/messari/rocket-pool-ethereum')

# Create a FieldPath object for the required fields in the financialsDailySnapshots entity.
# Specify options to sort the data by timestamp in descending order and limit the number of results to 30.
financials_daily_snapshot_30days = financials_daily_snapshots.Query.financialsDailySnapshots(
    orderBy=financials_daily_snapshots.FinancialsDailySnapshot.timestamp, 
    orderDirection='desc', 
    first=30
)

# Create a SyntheticField on the Swap entity called `timestamp`, which will format the timestamp field into something more human readable
financials_daily_snapshots.FinancialsDailySnapshot.datetime = SyntheticField(
  lambda timestamp: str(datetime.fromtimestamp(timestamp)),
  SyntheticField.FLOAT,
  financials_daily_snapshots.FinancialsDailySnapshot.timestamp
)

# Define a synthetic field to calculate the daily revenue difference for the past 30 days
financials_daily_snapshots.FinancialsDailySnapshot.revDiffRevenueUSD30 = SyntheticField(
    lambda x, y: abs(x - y),
    SyntheticField.FLOAT,
    [financials_daily_snapshots.FinancialsDailySnapshot.dailyProtocolSideRevenueUSD,
    financials_daily_snapshots.FinancialsDailySnapshot.dailySupplySideRevenueUSD],
)

# the average daily revenue
financials_daily_snapshots.FinancialsDailySnapshot.avgDailyRevenueUSD30 = SyntheticField(
    lambda x, y: (x + y) / 2,
    SyntheticField.FLOAT,
    [financials_daily_snapshots.FinancialsDailySnapshot.dailyProtocolSideRevenueUSD,
    financials_daily_snapshots.FinancialsDailySnapshot.dailySupplySideRevenueUSD],
)

# Create a SyntheticField for the percentage change in daily revenue over the past 30 days
financials_daily_snapshots.FinancialsDailySnapshot.revenueMargin30  = SyntheticField(
    lambda x, y: x / y,
    SyntheticField.FLOAT,
    [financials_daily_snapshots.FinancialsDailySnapshot.dailyProtocolSideRevenueUSD,
    financials_daily_snapshots.FinancialsDailySnapshot.dailySupplySideRevenueUSD],
)


# Query data flattened to a single DataFrame
sg.query_df([
    financials_daily_snapshot_30days.timestamp,
    financials_daily_snapshot_30days.datetime,
    financials_daily_snapshot_30days.blockNumber,
    financials_daily_snapshot_30days.cumulativeProtocolSideRevenueUSD,
    financials_daily_snapshot_30days.cumulativeProtocolSideRevenueUSD,
    financials_daily_snapshot_30days.cumulativeSupplySideRevenueUSD,
    financials_daily_snapshot_30days.cumulativeTotalRevenueUSD,
    financials_daily_snapshot_30days.dailyProtocolSideRevenueUSD,
    financials_daily_snapshot_30days.dailySupplySideRevenueUSD,
    financials_daily_snapshot_30days.dailyTotalRevenueUSD,
    financials_daily_snapshot_30days.revDiffRevenueUSD30,
    financials_daily_snapshot_30days.avgDailyRevenueUSD30,
    financials_daily_snapshot_30days.revenueMargin30,

])
```
```python

```


---

## Subgrounds Tutorials: RocketPool  x Lido Exploration



This code demonstrates how to use the Subgrounds library to analyze and compare revenue and usage data for two DeFi protocols, Lido and Rocket Pool. The Subgrounds library provides an easy-to-use interface to fetch and manipulate data from The Graph, a decentralized protocol for indexing and querying data from blockchains like Ethereum.





In the code, we first import the necessary libraries, such as `Subgrounds`, `SyntheticField`, `datetime`, and `panda`s. We then initialize a `Subground`s instance, which is used to interact with subgraphs from The Graph. We load the Lido and Rocket Pool subgraphs using their API URLs by calling the `load_subgraph` method. This allows us to query data from these subgraphs easily. 





For protocol `revenue analysis`, we query the `financials daily snapshots` for both protocols and fetch the latest snapshot to compare the `cumulative supply-side`, `protocol-side`, and `total revenue`. We store the comparison in a pandas DataFrame and print it out. 





For protocol usage analysis, we query the usage metrics daily snapshots for both protocols and fetch the data for the past 30 days. We convert the timestamp field to a human-readable format using the `apply` method on the pandas DataFrame. We then calculate the daily and hourly transaction counts and active user counts for both protocols, store the results in DataFrames, and print them out.





 Throughout the code, Subgrounds is used to load subgraphs, query data from the subgraphs, and fetch the queried data in pandas DataFrames, making it easy to manipulate and analyze the data.


```python
from subgrounds import Subgrounds
from subgrounds.subgraph import SyntheticField
from datetime import datetime
import pandas as pd

# Initialize Subgrounds
sg = Subgrounds()

# Load subgraphs for Lido and rocketPool
lido_subgraph = sg.load_subgraph('https://api.thegraph.com/subgraphs/name/messari/lido-ethereum')
rocketPool_subgraph = sg.load_subgraph('https://api.thegraph.com/subgraphs/name/messari/rocket-pool-ethereum')

# Query financials daily snapshots for both protocols (sorted by timestamp)
lido_financials = lido_subgraph.Query.financialsDailySnapshots(orderBy=lido_subgraph.FinancialsDailySnapshot.timestamp, orderDirection='desc')
rocketPool_financials = rocketPool_subgraph.Query.financialsDailySnapshots(orderBy=rocketPool_subgraph.FinancialsDailySnapshot.timestamp, orderDirection='desc')

# Fetch the latest financials snapshot for both protocols
lido_financials_latest = sg.query_df([
    lido_financials.cumulativeSupplySideRevenueUSD, 
    lido_financials.cumulativeProtocolSideRevenueUSD, 
    lido_financials.cumulativeTotalRevenueUSD]).iloc[0]
    
rocketPool_financials_latest = sg.query_df([
    rocketPool_financials.cumulativeSupplySideRevenueUSD, 
    rocketPool_financials.cumulativeProtocolSideRevenueUSD, 
    rocketPool_financials.cumulativeTotalRevenueUSD]).iloc[0]

# Compare cumulative supply-side, protocol-side, and total revenue for both protocols
revenue_comparison = pd.DataFrame({'Lido': lido_financials_latest, 'rocketPool': rocketPool_financials_latest})
print(revenue_comparison)
```
## Subgrounds Tutorials: RocketPool  x Lido Exploration - Continued



This code uses the Subgrounds library to interact with the Lido and Rocket Pool subgraphs and fetch usage metrics daily snapshots for both protocols over the past 30 days. Here's a step-by-step explanation of the code:



- Import required libraries: Subgrounds, SyntheticField, datetime, and pandas.



- Initialize Subgrounds with `sg = Subgrounds()`.



- Load Lido and Rocket Pool subgraphs using their respective API URLs.



- Query the usage metrics daily snapshots for both protocols, ordering by timestamp in descending order, and limit the results to the last 30 days.



- Fetch the usage metrics for the past 30 days for both protocols by querying the daily timestamp, daily transaction count, and daily active users.



- Combine the results from both protocols into two separate DataFrames: `lido_usage_30` and `rocket_pool_usage_30`.



The code also includes commented-out sections for styling the DataFrames and displaying them in a more visually appealing format. To use this functionality, you can uncomment the sections that define the `style_dataframe` function, format the timestamps in the DataFrames, and style and display the resulting DataFrames.




```python
from subgrounds import Subgrounds
from subgrounds.subgraph import SyntheticField
from datetime import datetime
import pandas as pd

# Initialize Subgrounds
sg = Subgrounds()

# Load subgraphs for Lido and rocketPool_subgraph
lido_subgraph = sg.load_subgraph('https://api.thegraph.com/subgraphs/name/messari/lido-ethereum')
rocketPool_subgraph = sg.load_subgraph('https://api.thegraph.com/subgraphs/name/messari/rocket-pool-ethereum')

# Query usage metrics daily snapshots for both protocols (sorted by timestamp)
lido_usage = lido_subgraph.Query.usageMetricsDailySnapshots(
    orderBy=lido_subgraph.UsageMetricsDailySnapshot.timestamp,
    orderDirection='desc',
    first=30)

rocket_pool_usage = rocketPool_subgraph.Query.usageMetricsDailySnapshots(
    orderBy=rocketPool_subgraph.UsageMetricsDailySnapshot.timestamp, 
    orderDirection='desc',
    first=30)

# Fetch usage metrics for the past 30 days for both protocols
lido_usage_30days = sg.query_df([
    lido_usage.timestamp,
    lido_usage.dailyTransactionCount, 
    lido_usage.dailyActiveUsers])
    
rocket_pool_usage_30days = sg.query_df([
    rocket_pool_usage.timestamp,
    rocket_pool_usage.dailyTransactionCount, 
    rocket_pool_usage.dailyActiveUsers])


[lido_usage_30,rocket_pool_usage_30] = sg.query_df([
    lido_usage.timestamp, 
    lido_usage.dailyTransactionCount, 
    lido_usage.dailyActiveUsers,
    rocket_pool_usage.timestamp,
    rocket_pool_usage.dailyTransactionCount, 
    rocket_pool_usage.dailyActiveUsers
])
rocket_pool_usage_30
```
```python
lido_usage_30
```
```python

```
```python

```


---

Introduce getting started with Gateway to:

1. Create new account and log in to Playgrounds App

2. Walkthrough the app homepage

3. Show how to generate Playgrounds Proxy Api Key

4. Show how to load Playgrounds Proxy Api Key into Subgrounds

5. Copy Aave v3 subgraph id and load it into Subgrounds

6. Perform basic query on Aave v3 subgraph, showcasing we are querying decentralized subgraph

## Gateway setup and basics



To query a decentralized network subgraph with id subgraph-id, 

you can make a POST request to the Playgrounds proxy endpoint:



`https://api.playgrounds.network/v1/proxy/subgraphs/id/[subgraph-id]`



The POST request itself will have to contain the Playgrounds API key you generated earlier as the value of the Playgrounds-Api-Token header. The rest of the request will be the same as the request you would usually make to the Graph's decentralized network. 



Let's try an example of Playgrounds Gateway request sent using curl in terminal!



```curl https://api.playgrounds.network/v1/proxy/subgraphs/id/ELUcwgpm14LKPLrBRuVvPvNKHQ9HvwmtKgKSH6123cr7 \

    -H 'Content-Type: application/json' \

    -H 'Playgrounds-Api-Key: PG_API_KEY' \

    -d '{"query":"{protocols {id}}"}'```



The endpoint mirrors the Graph decentralized network gateway endpoint:



`https://gateway.thegraph.com/api/[api-key]/subgraphs/id/[subgraph-id]`



Key difference is the API key is not part of the URL



`https://api.playgrounds.network/v1/proxy/subgraphs/id/[subgraph-id]`


```python
# Import subgrounds
from subgrounds import Subgrounds

# Instantiate subgrounds and insert Playgrounds API key into header
sg = Subgrounds.from_pg_key("pg-AqAFS8G3TN3Kagdgw2MrGjFvDGUgxImS")

# Insert desired subgraph id from decentralized subgraph. Find in subgraph url
uniswap_id = "ELUcwgpm14LKPLrBRuVvPvNKHQ9HvwmtKgKSH6123cr7"
```
```python
subgraph = sg.load_subgraph(
    f"https://api.playgrounds.network/v1/proxy/subgraphs/id/{uniswap_id}")

sg.query_df([
    subgraph.Query.tokens.id,
    subgraph.Query.tokens.symbol,
])
```


---

