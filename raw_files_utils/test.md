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
