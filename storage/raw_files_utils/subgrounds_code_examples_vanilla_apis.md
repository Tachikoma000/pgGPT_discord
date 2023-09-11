```python
from datetime import datetime
import time
from datetime import date
from subgrounds.subgraph import SyntheticField, FieldPath
from subgrounds.subgrounds import Subgrounds
import pandas as pd
import  os as os
import duckdb as db
import seaborn as sns
import matplotlib.pyplot as plt
import datetime as dt
```
```python
sg = Subgrounds()
snapshot = sg.load_api('https://hub.snapshot.org/graphql')
```
```python
snapshot.Proposal.datetime = SyntheticField(
  lambda timestamp: str(datetime.fromtimestamp(timestamp)),
  SyntheticField.STRING,
  snapshot.Proposal.end,
)
```
```python
spacename = 'olympusdao.eth'

# based on their url, for example "curve.eth" for  https://snapshot.org/#/curve.eth
print  (spacename)
```
```python
proposals = snapshot.Query.proposals(
  orderBy='created',
  orderDirection='desc',
  first=1000,
  where=[
    snapshot.Proposal.space == spacename, ##'fuse.eth',
    snapshot.Proposal.state == 'closed'
    ##snapshot.Proposal.title == 'OIP-18: Reward rate framework and reduction',
  ]
)

```
```python
proposals_snapshots = sg.query_df([
    proposals.title,
    proposals.created,
    proposals.id,
    proposals.start,
    proposals.end,
    proposals.votes
])

proposals_snapshots['createdDate']=(pd.to_datetime(proposals_snapshots['proposals_created'],unit='s'))
proposals_snapshots['startDate']=(pd.to_datetime(proposals_snapshots['proposals_start'],unit='s'))
proposals_snapshots['endDate']=(pd.to_datetime(proposals_snapshots['proposals_end'],unit='s'))
proposals_snapshots.head(10)
```
```python
total_snapshots = len(proposals_snapshots)
print(total_snapshots)
```
```python
proposals_choices = sg.query(proposals.choices)
proposals_choices = pd.DataFrame(proposals_choices)
proposals_choices.head(100)
```
proposals_choices = sg.query(proposals.choices)

proposals_choices = pd.DataFrame(proposals_choices, columns = ['option_1', 'option_2', 'option_3', 'option_4', 'option_5','option_6','option_7'])

proposals_choices.head(100)

```python
olympus_governance_view = pd.DataFrame()
olympus_governance_view = pd.concat([proposals_snapshots,proposals_choices], axis=1)
olympus_governance_view.head(5)
```
```python
len(olympus_governance_view)
```
```python
olympus_governance_view.drop_duplicates()
```
```python
len(olympus_governance_view)
```
```python
##this captures the ENTIRE list of people who voted
voteTicker = 0
totalProposals = len(olympus_governance_view)
voteslist = pd.DataFrame()
votesDb = pd.DataFrame()
voteListLength = 1000
datediff = 0
now=0
daysAgo=0
daysLimit = 90
datediff=0
epochlimit = (90*86400)
ut = time.time()
limitTimestamp = int(ut - epochlimit)
limitDate = datetime.fromtimestamp(limitTimestamp)
limitDate = limitDate.strftime('%m-%d-%Y')
exit = False

while int(datediff) < int(daysLimit):
    proposal_id = olympus_governance_view.iloc[voteTicker,2]
    skipValue = (voteTicker)*(1000)
    vote_tracker = snapshot.Query.votes(
        #orderBy = 'created',
        #orderDirection='asc',
        first=1000,
        where=[
          snapshot.Vote.proposal == proposal_id
          #snapshot.Vote.created > limitTimestamp
        ]
    )
    voting_snapshots = sg.query_df([
    vote_tracker.id,
    vote_tracker.voter,
    vote_tracker.created,
    vote_tracker.choice,
    vote_tracker.vp
    ])


    voting_snapshots['proposals_id']= olympus_governance_view.iloc[voteTicker,2]
    #voteDate = votesDb.iat[voteTicker,4]

    votesDb=pd.concat([voting_snapshots, votesDb])
    votesDb['createdDate']=(pd.to_datetime(votesDb['votes_created'],unit='s'))
    then = votesDb.iat[voteTicker,6]
    now = datetime.now()
    delta = now-then
    datediff = delta.days
    votesDbLength = len(votesDb)
    voteListLength = len(voting_snapshots)
    recordTimestamp1 = votesDb.iat[voteTicker,2]
    recordTimestamp = dt.datetime.fromtimestamp( recordTimestamp1 )
    now = (int(dt.datetime.utcnow().timestamp()))
    #datediff=abs(int(now) - recordTimestamp1)

    if int(datediff) > int(daysLimit):
        exit
    if voteTicker== totalProposals:
        exit

    print('ticker', voteTicker, 'proposal',proposal_id, 'records:',voteListLength, 'DB size:',votesDbLength, '    -days ago:', datediff, '     -date', then, '    -exit?', exit )
    #print(proposal_id, voteDate, datediff)
    voteTicker = voteTicker+1

votesDb.drop_duplicates
print("Done. Total Records collected: ", votesDbLength)
```
```python
votesDb.head(100)
```
```python
votesDb.rename(columns={"createdDate": "voteDate"}, inplace = True)
votesDb.drop_duplicates(inplace=True)
votesDb.drop_duplicates()
votesDb.head(10000)
```
```python
#olympus_governance_view.rename(columns={"createdDate": "voteDate"}, inplace = True)
olympus_governance_view.head(200)
```
```python
governance_data = pd.merge(votesDb, olympus_governance_view, how='inner', left_on='proposals_id', right_on='proposals_id')
governance_data.head(10)
```
```python
crunch_data = db.query("select "
                           "A.proposals_id"
                       "    ,A.startDate "
                       "    ,A.proposals_title "
                       "    ,A.votes_voter "
                       "    ,A.votes_vp "
                       "    ,A.voteDate "
                           ",sum(A.votes_vp) over (Partition by proposals_id  order by votes_vp desc, voteDate asc) as cumulative_vp "
                           ",sum(A.votes_vp) over (Partition by proposals_id) as total_vp "
                           ",(votes_vp::decimal/sum(votes_vp::decimal) over (Partition by proposals_id)) as percentage_of_total_vp "
                           ",((sum(A.votes_vp) over (Partition by proposals_id  order by votes_vp desc, voteDate asc))::decimal/sum(votes_vp::decimal) over (Partition by proposals_id)) as cum_percentage_of_total_vp "
                       ",round((sum(A.votes_vp) over (Partition by proposals_id  order by votes_vp desc, voteDate asc))::decimal/sum(votes_vp::decimal) over (Partition by proposals_id)) as cum_percentage_of_total_vp_stepped "
                           ",row_number() over (Partition by proposals_id order by votes_vp desc, voteDate asc) as proposal_voter_rank "

                           ",(count(*) over (Partition by proposals_id))::decimal total_voters "

                           ",(count(*) over (Partition by proposals_id  order by votes_vp desc, voteDate asc))::decimal/(count(*) over (Partition by proposals_id))::decimal percentage_voters_counted "

                           ",round(100*(count(*) over (Partition by proposals_id  order by votes_vp desc, voteDate asc))::decimal/(count(*) over (Partition by proposals_id)))::decimal percentage_voters_counted_stepped "
                       "from "
                       "    governance_data  A "
                       #"where   to_timestamp((votes_Created::bigint))<'2023-01-01' "
                       ""
                       "Group by "
                           "A.proposals_id"
                       "    ,A.startDate "
                       "    ,A.proposals_title "
                       "    ,A.votes_voter "
                       "    ,A.votes_vp "
                       "    ,A.voteDate "
                       ""
                       "Order by "
                       "    A.startDate  asc "
                       "    , votes_vp desc "
                       "    , voteDate asc"
                       "").df()


crunch_data.insert(0, 'DAO', spacename)
crunch_data.drop_duplicates
crunch_data.head(100)

```
```python
#leaders = crunch_data.loc[crunch_data['proposal_voter_rank'] <=3]
#leader_count = leaders.votes_voter.nunique()
#leader_count
#DONT ASK ME WHY THIS DIDNT WORK. HAVE TO DO IT THE UGLY WAY

leader_ranks = db.query("with leader_ranks as "
                        "(Select distinct "
                        "   B.proposals_id"
                        "   ,B.votes_voter"
                        "   ,B.proposal_voter_rank "
                        "   ,(B.proposal_voter_rank +1) as leader_rank "
                        "From "
                        "   (select "
                               "proposals_id"
                               ",votes_voter "
                               ",votes_choice"
                               ",votes_vp"
                               ",votes_created  "
                               ",sum(votes_vp) over (Partition by proposals_id  order by votes_vp desc, votes_created asc) as cumulative_vp"
                               ",sum(votes_vp) over (Partition by proposals_id) as total_vp"
                               ",(votes_vp::decimal/sum(votes_vp::decimal) over (Partition by proposals_id)) as percentage_of_total_vp "
                               ",((sum(votes_vp) over (Partition by proposals_id  order by votes_vp desc, votes_created asc))::decimal/sum(votes_vp::decimal) over (Partition by proposals_id)) as cum_percentage_of_total_vp "
                           "    ,round((sum(votes_vp) over (Partition by proposals_id  order by votes_vp desc, votes_created asc))::decimal/sum(votes_vp::decimal) over (Partition by proposals_id)) as cum_percentage_of_total_vp_stepped "
                               ",row_number() over (Partition by proposals_id order by votes_vp desc, votes_created asc) as proposal_voter_rank "
                               ",count(votes_voter) over (Partition by proposals_id  order by votes_vp desc, votes_created asc) total_voters "
                               ",(count(*) over (Partition by proposals_id  order by votes_vp desc, votes_created asc))::decimal/(count(*) over (Partition by proposals_id))::decimal percentage_voters_counted "
                               ",round(100*(count(*) over (Partition by proposals_id  order by votes_vp desc, votes_created asc))::decimal/(count(*) over (Partition by proposals_id)))::decimal percentage_voters_counted_stepped "
                           "from "
                           "    governance_data  "
                               ""
                           "Group by "
                           "    proposals_id"
                           "    ,votes_voter"
                           "    ,votes_choice"
                           "    , votes_vp "
                           "    , votes_created "
                           ""
                           "Order by "
                           "    proposals_id "
                           "    ,votes_vp desc "
                           "    , votes_created asc) B "
                        "where "
                        "   B.cum_percentage_of_total_vp<=0.5) "
                        ""
                        "Select "
                        "   *"
                        "From crunch_data A"
                        "   Join leader_ranks B on A.proposal_voter_rank = B.leader_rank and A.proposals_id = B.proposals_id"
                        ""
                    ).df()
leader_ranks

```
```python
dao_members = crunch_data.groupby('DAO').votes_voter.nunique()
dao_members = dao_members.iloc[0]
leader_count =leader_ranks.votes_voter.nunique()
elite = round((leader_count)/(dao_members),4)

print(dao_members, "{0:.2%}".format(elite))

```
```python
curve_data = db.query(
    "SELECT "
    "   percentage_voters_counted_stepped "
    "   ,percentage_voters_counted "
    "   ,cum_percentage_of_total_vp "
    "   ,SUBSTRING(proposals_title,2,7) proposal "
    "FROM crunch_data "
    "union all "
    "select "
    "   percentage_voters_counted_stepped "
    "   , avg(percentage_voters_counted) avg_percentage_voters_counted "
    "   , avg(cum_percentage_of_total_vp) avg_percentage_of_total_vp "
    "   ,'Grand Average' as proposal "
    "from crunch_data "
    " group by 1 "
     ).df()

curve_data.head(200)


```
```python
file = input('Selet a folder to save output') ##enter your file path here - the file is in the repo "summary_stats.csv".
```
```python
path =file+'/'+spacename+'_olympus_governance_data_'+str(date.today().strftime("%b-%d-%Y"))+'.csv'
governance_data.to_csv(path, index = False)
```
```python
path =file+'/'+spacename+'_olympus_crunch_data_'+str(date.today().strftime("%b-%d-%Y"))+'.csv'
crunch_data.to_csv(path, index = False)
```
```python
path =file+'/'+spacename+'_olympus_curve_data_'+str(date.today().strftime("%b-%d-%Y"))+'.csv'
curve_data.to_csv(path, index = False)
```
```python
plt.rc("figure", figsize=(40, 20))
#sns.set_style("whitegrid")
plt.rc("font", size=25)
data_means = crunch_data.groupby("percentage_voters_counted_stepped")["cum_percentage_of_total_vp","percentage_voters_counted"].agg("mean").reset_index()
##print(data_means)
plot_title = spacename + ' snapshots % of vote along population with Average as X'

ax=sns.scatterplot(data=crunch_data, hue = "proposals_id",y="cum_percentage_of_total_vp",x="percentage_voters_counted_stepped").set(title=plot_title,xlabel='% of voters',ylabel='% of voting power')
chart = sns.scatterplot(data=data_means,x="percentage_voters_counted_stepped",y="cum_percentage_of_total_vp",zorder=3, s=800,marker='X',color = 'orange')
plt.legend(bbox_to_anchor=(1.02, 0.99), loc='upper left', borderaxespad=0)
#and save the chart file, too
print(chart)
plt.savefig(file+'\\'+spacename+' vote power distribution.png',transparent =False,  dpi=100)
```


---

```python
from datetime import datetime as dt
import time
from datetime import date
from subgrounds.subgraph import SyntheticField, FieldPath
from subgrounds.subgrounds import Subgrounds
import pandas as pd
import  os as os
import duckdb as db
import seaborn as sns
import matplotlib.pyplot as plt
```
```python
sg = Subgrounds()
snapshot = sg.load_api('https://hub.snapshot.org/graphql')
```
```python
snapshot.Proposal.datetime = SyntheticField(
  lambda timestamp: str(datetime.fromtimestamp(timestamp)),
  SyntheticField.STRING,
  snapshot.Proposal.end,
)
```
```python
spacename = input('Enter space name')
```
```python
daysLimit = int(input('How many days in the past do you want to go?'))
```
```python
proposals = snapshot.Query.proposals(
  orderBy='created',
  orderDirection='desc',
  first=1000,
  where=[
    snapshot.Proposal.space == spacename, ##'fuse.eth',
    snapshot.Proposal.state == 'closed'
    ##snapshot.Proposal.title == 'OIP-18: Reward rate framework and reduction',
  ]
)

```
```python
proposals_snapshots = sg.query_df([
    proposals.title,
    proposals.created,
    proposals.id,
    proposals.start,
    proposals.end,
    proposals.votes
])

proposals_snapshots['createdDate']=(pd.to_datetime(proposals_snapshots['proposals_created'],unit='s'))
proposals_snapshots['startDate']=(pd.to_datetime(proposals_snapshots['proposals_start'],unit='s'))
proposals_snapshots['endDate']=(pd.to_datetime(proposals_snapshots['proposals_end'],unit='s'))
proposals_snapshots.head(10)
```
```python
total_snapshots = len(proposals_snapshots)
print(total_snapshots)
```
```python
proposals_choices = sg.query(proposals.choices)
proposals_choices = pd.DataFrame(proposals_choices)
proposals_choices.head(100)
```
proposals_choices = sg.query(proposals.choices)

proposals_choices = pd.DataFrame(proposals_choices, columns = ['option_1', 'option_2', 'option_3', 'option_4', 'option_5','option_6','option_7'])

proposals_choices.head(100)

```python
olympus_governance_view = pd.DataFrame()
olympus_governance_view = pd.concat([proposals_snapshots,proposals_choices], axis=1)
olympus_governance_view.head(5)
```
```python
len(olympus_governance_view)
```
```python
olympus_governance_view.drop_duplicates()
```
```python
len(olympus_governance_view)
```
```python
##this captures the ENTIRE list of people who voted
voteTicker = 0
totalProposals = len(olympus_governance_view)
voteslist = pd.DataFrame()
votesDb = pd.DataFrame()
voteListLength = 1000
datediff = 0
now=0
daysAgo=0
#daysLimit = 90
datediff=0
epochlimit = (90*86400)
ut = time.time()
limitTimestamp = int(ut - epochlimit)
limitDate = datetime.fromtimestamp(limitTimestamp)
limitDate = limitDate.strftime('%m-%d-%Y')

while int(datediff) < int(daysLimit):
    proposal_id = olympus_governance_view.iloc[voteTicker,2]
    skipValue = (voteTicker)*(1000)
    vote_tracker = snapshot.Query.votes(
        #orderBy = 'created',
        #orderDirection='asc',
        first=1000,
        where=[
          snapshot.Vote.proposal == proposal_id
          #snapshot.Vote.created > limitTimestamp
        ]
    )
    voting_snapshots = sg.query_df([
    vote_tracker.id,
    vote_tracker.voter,
    vote_tracker.created,
    vote_tracker.choice,
    vote_tracker.vp
    ])


    voting_snapshots['proposals_id']= olympus_governance_view.iloc[voteTicker,2]
    #voteDate = votesDb.iat[voteTicker,4]

    votesDb=pd.concat([voting_snapshots, votesDb])
    votesDb['createdDate']=(pd.to_datetime(votesDb['votes_created'],unit='s'))
    then = votesDb.iat[voteTicker,6]
    now = datetime.now()
    delta = now-then
    datediff = delta.days
    votesDbLength = len(votesDb)
    voteListLength = len(voting_snapshots)
    recordTimestamp1 = votesDb.iat[voteTicker,2]
    recordTimestamp = dt.fromtimestamp( recordTimestamp1 )
    now = (int(dt.utcnow().timestamp()))
    #datediff=abs(int(now) - recordTimestamp1)

    print('ticker', voteTicker, 'proposal',proposal_id, 'records:',voteListLength, 'DB size:',votesDbLength, '    -days ago:', datediff, '     -date', then, '    -exit?', exit )
    #print(proposal_id, voteDate, datediff)
    voteTicker = voteTicker+1

votesDb.drop_duplicates
print("Done. Total Records collected: ", votesDbLength)
```
```python
votesDb.head(100)
```
```python
votesDb.rename(columns={"createdDate": "voteDate"}, inplace = True)
votesDb.drop_duplicates(inplace=True)
votesDb.drop_duplicates()
votesDb.head(10000)
```
```python
#olympus_governance_view.rename(columns={"createdDate": "voteDate"}, inplace = True)
olympus_governance_view.head(200)
```
```python
governance_data = pd.merge(votesDb, olympus_governance_view, how='inner', left_on='proposals_id', right_on='proposals_id')
governance_data.head(10)
```
```python
crunch_data = db.query("select "
                           "A.proposals_id"
                       "    ,A.startDate "
                       "    ,A.proposals_title "
                       "    ,A.votes_voter "
                       "    ,A.votes_vp "
                       "    ,A.voteDate "
                           ",sum(A.votes_vp) over (Partition by proposals_id  order by votes_vp desc, voteDate asc) as cumulative_vp "
                           ",sum(A.votes_vp) over (Partition by proposals_id) as total_vp "
                           ",(votes_vp::decimal/sum(votes_vp::decimal) over (Partition by proposals_id)) as percentage_of_total_vp "
                           ",((sum(A.votes_vp) over (Partition by proposals_id  order by votes_vp desc, voteDate asc))::decimal/sum(votes_vp::decimal) over (Partition by proposals_id)) as cum_percentage_of_total_vp "
                       ",round((sum(A.votes_vp) over (Partition by proposals_id  order by votes_vp desc, voteDate asc))::decimal/sum(votes_vp::decimal) over (Partition by proposals_id)) as cum_percentage_of_total_vp_stepped "
                           ",row_number() over (Partition by proposals_id order by votes_vp desc, voteDate asc) as proposal_voter_rank "

                           ",(count(*) over (Partition by proposals_id))::decimal total_voters "

                           ",(count(*) over (Partition by proposals_id  order by votes_vp desc, voteDate asc))::decimal/(count(*) over (Partition by proposals_id))::decimal percentage_voters_counted "

                           ",round(100*(count(*) over (Partition by proposals_id  order by votes_vp desc, voteDate asc))::decimal/(count(*) over (Partition by proposals_id)))::decimal percentage_voters_counted_stepped "
                       "from "
                       "    governance_data  A "
                       #"where   to_timestamp((votes_Created::bigint))<'2023-01-01' "
                       ""
                       "Group by "
                           "A.proposals_id"
                       "    ,A.startDate "
                       "    ,A.proposals_title "
                       "    ,A.votes_voter "
                       "    ,A.votes_vp "
                       "    ,A.voteDate "
                       ""
                       "Order by "
                       "    A.startDate  asc "
                       "    , votes_vp desc "
                       "    , voteDate asc"
                       "").df()


crunch_data.insert(0, 'DAO', spacename)
crunch_data.drop_duplicates
crunch_data.head(100)

```
```python
#leaders = crunch_data.loc[crunch_data['proposal_voter_rank'] <=3]
#leader_count = leaders.votes_voter.nunique()
#leader_count
#DONT ASK ME WHY THIS DIDNT WORK. HAVE TO DO IT THE UGLY WAY

leader_ranks = db.query("with leader_ranks as "
                        "(Select distinct "
                        "   B.proposals_id"
                        "   ,B.votes_voter"
                        "   ,B.proposal_voter_rank "
                        "   ,(B.proposal_voter_rank +1) as leader_rank "
                        "From "
                        "   (select "
                               "proposals_id"
                               ",votes_voter "
                               ",votes_choice"
                               ",votes_vp"
                               ",votes_created  "
                               ",sum(votes_vp) over (Partition by proposals_id  order by votes_vp desc, votes_created asc) as cumulative_vp"
                               ",sum(votes_vp) over (Partition by proposals_id) as total_vp"
                               ",(votes_vp::decimal/sum(votes_vp::decimal) over (Partition by proposals_id)) as percentage_of_total_vp "
                               ",((sum(votes_vp) over (Partition by proposals_id  order by votes_vp desc, votes_created asc))::decimal/sum(votes_vp::decimal) over (Partition by proposals_id)) as cum_percentage_of_total_vp "
                           "    ,round((sum(votes_vp) over (Partition by proposals_id  order by votes_vp desc, votes_created asc))::decimal/sum(votes_vp::decimal) over (Partition by proposals_id)) as cum_percentage_of_total_vp_stepped "
                               ",row_number() over (Partition by proposals_id order by votes_vp desc, votes_created asc) as proposal_voter_rank "
                               ",count(votes_voter) over (Partition by proposals_id  order by votes_vp desc, votes_created asc) total_voters "
                               ",(count(*) over (Partition by proposals_id  order by votes_vp desc, votes_created asc))::decimal/(count(*) over (Partition by proposals_id))::decimal percentage_voters_counted "
                               ",round(100*(count(*) over (Partition by proposals_id  order by votes_vp desc, votes_created asc))::decimal/(count(*) over (Partition by proposals_id)))::decimal percentage_voters_counted_stepped "
                           "from "
                           "    governance_data  "
                               ""
                           "Group by "
                           "    proposals_id"
                           "    ,votes_voter"
                           "    ,votes_choice"
                           "    , votes_vp "
                           "    , votes_created "
                           ""
                           "Order by "
                           "    proposals_id "
                           "    ,votes_vp desc "
                           "    , votes_created asc) B "
                        "where "
                        "   B.cum_percentage_of_total_vp<=0.5) "
                        ""
                        "Select "
                        "   *"
                        "From crunch_data A"
                        "   Join leader_ranks B on A.proposal_voter_rank = B.leader_rank and A.proposals_id = B.proposals_id"
                        ""
                    ).df()
leader_ranks

```
```python
dao_members = crunch_data.groupby('DAO').votes_voter.nunique()
dao_members = dao_members.iloc[0]
leader_count =leader_ranks.votes_voter.nunique()
elite = round((leader_count)/(dao_members),4)

print(dao_members, "{0:.2%}".format(elite))

```
```python
curve_data = db.query(
    "select "
    "   percentage_voters_counted_stepped "
    "   , avg(percentage_voters_counted) avg_percentage_voters_counted "
    "   , avg(cum_percentage_of_total_vp) avg_percentage_of_total_vp "
    "   ,'Grand Average' as proposal "
    "from crunch_data "
    " group by 1 "
    "UNION ALL "
    "SELECT "
    "   percentage_voters_counted_stepped "
    "   ,percentage_voters_counted "
    "   ,cum_percentage_of_total_vp "
    "   ,proposals_id "
    "FROM crunch_data "
     ).df()

curve_data.head(200)


```
```python
file = input('Selet a folder to save output') ##enter your file path here - the file is in the repo "summary_stats.csv".
```
```python
path =file+'/'+spacename+'_olympus_governance_data_'+str(date.today().strftime("%b-%d-%Y"))+'.csv'
governance_data.to_csv(path, index = False)
```
```python
path =file+'/'+spacename+'_olympus_crunch_data_'+str(date.today().strftime("%b-%d-%Y"))+'.csv'
crunch_data.to_csv(path, index = False)
```
```python
path =file+'/'+spacename+'_olympus_curve_data_'+str(date.today().strftime("%b-%d-%Y"))+'.csv'
curve_data.to_csv(path, index = False)
```
```python
plt.rc("figure", figsize=(40, 20))
#sns.set_style("whitegrid")
plt.rc("font", size=25)
data_means = crunch_data.groupby("percentage_voters_counted_stepped")["cum_percentage_of_total_vp","percentage_voters_counted"].agg("mean").reset_index()
##print(data_means)
plot_title = spacename + ' snapshots % of vote along population with Average as X'

ax=sns.scatterplot(data=crunch_data, hue = "proposals_id",y="cum_percentage_of_total_vp",x="percentage_voters_counted_stepped").set(title=plot_title,xlabel='% of voters',ylabel='% of voting power')
chart = sns.scatterplot(data=data_means,x="percentage_voters_counted_stepped",y="cum_percentage_of_total_vp",zorder=3, s=800,marker='X',color = 'orange')
plt.legend(bbox_to_anchor=(1.02, 0.99), loc='upper left', borderaxespad=0)
#and save the chart file, too
print(chart)
plt.savefig(file+'\\'+spacename+' vote power distribution.png',transparent =False,  dpi=100)
```
```python

```


---

```python
#Snapshot diver allows you to pull a single election's data from Snapshot. Bugs? Ping me on Twitter @edgecaser.

from datetime import datetime
from datetime import date
from subgrounds.subgraph import SyntheticField, FieldPath
from subgrounds.subgrounds import Subgrounds

import pandas as pd
import duckdb as db
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

st.set_page_config(layout="wide")

st.markdown("""
<style>
.bigger-font {
    font-size:18px !important;
}
.biggest-font {
    font-size:20px !important;
}

</style>
""", unsafe_allow_html=True)

st.write('# Snapshot Diver')
st.write('### By @Edgecaser')

st.markdown('<p class="bigger-font">This tool will help you pull the detailed results of any Proposal for a Single DAO within Snapshot.</p>', unsafe_allow_html=True)

st.markdown('<p class="bigger-font">DAO stands for Decentralized Autonomous Organization, a bottoms-up team or organization. These are run by votes recorded on the Blockchain.</p>', unsafe_allow_html=True)

st.markdown('<p class="bigger-font">Some DAOs voting power has a 1:1 correlation with their token holdings. Others use different schemes that distribute voting power in different ways, all the way down to one-wallet-one-vote. </p>', unsafe_allow_html=True)


st.markdown('<p class="bigger-font"> If you are interested in analyzing a DAO\'s governance power patterns across all its proposals, visit Snapshot Surfer </p>', unsafe_allow_html=True)
st.markdown('[Snapshot Surfer](https://edgecaser-snapshotsurfer-snapshotsurfer-yyutu2.streamlitapp.com/)')


#instructions
st.markdown(
    '<p class="bigger-font">To use this tool, you will need to know the name space of the DAO you are looking for. For example, OlympusDAO has a url like https://snapshot.org/#/olympusdao.eth. Therefore, write olympusdao.eth when queried to get its data.</p>',
    unsafe_allow_html=True)
st.write('')

st.markdown(
    '<p class="bigger-font">Once you have entered a spacename, you will see the choices of proposals available to analyze.</p>',
    unsafe_allow_html=True)
st.write('')


spacename = st.text_input('Where to pull from? Type your selection then press START',help='Which space, eg: curve.eth')

if len(spacename)>=3:

    sg = Subgrounds()
    snapshot = sg.load_api('https://hub.snapshot.org/graphql')

    snapshot.Proposal.datetime = SyntheticField(
      lambda timestamp: str(datetime.fromtimestamp(timestamp)),
      SyntheticField.STRING,
      snapshot.Proposal.end,
    )

    proposals = snapshot.Query.proposals(
      orderBy='created',
      orderDirection='desc',
      first=10000,

      where=[
        snapshot.Proposal.space == spacename, ##'fuse.eth',
        snapshot.Proposal.state == 'closed'
        ##snapshot.Proposal.title == 'OIP-18: Reward rate framework and reduction',
      ]
    )

    proposals_snapshots = sg.query_df([
        proposals.title,
        proposals.id,
        proposals.body,
        proposals.scores_total,
        proposals.created
    ])


    #test
    proposals_choices = sg.query(proposals.choices)

    proposals_choices = pd.DataFrame(proposals_choices)

    dao_governance_view = pd.concat([proposals_snapshots, proposals_choices], axis=1)

    #remove duplicates
    dao_governance_view_clean = dao_governance_view.copy(deep=True)

    dao_governance_view_clean = db.query("select  to_timestamp(proposals_created) as proposal_date,*  "
                                         "from dao_governance_view_clean order by proposals_created desc").df()

    dao_governance_view_clean.insert(0, 'DAO', spacename)

    st.write('Directory of proposals available:',dao_governance_view_clean)


    #st.write(snapshots.head(10))

    shape = dao_governance_view_clean.shape
    number_of_choices = shape[1]-6

    number_of_columns = shape[1]

    st.write('columns:',number_of_columns,' number of choices:', number_of_choices)


    snapshots = db.query("select distinct proposals_title, proposals_body from dao_governance_view_clean  ").df()

    choice = ''

    choice = (st.selectbox('Select Proposal and press START',snapshots,1))
    choiceOG = choice

    if st.button('START'):
        #st.write(choice)

        choicedf = pd.DataFrame(columns=['proposals_title'])

        #st.write(choicedf)


        row = pd.DataFrame({'proposals_title': [choice]})

        #st.write(row)

        choice = choicedf.append(row,ignore_index=True)

        st.write(choice)

        propid = db.query("select distinct dao_governance_view_clean.proposals_id from dao_governance_view_clean join choice on dao_governance_view_clean.proposals_title = choice.proposals_title").df()

        proposal_id=propid.iloc[0,0]

        row_data = db.query("select * from dao_governance_view_clean join choice on dao_governance_view_clean.proposals_title = choice.proposals_title").df()


        vote_tracker = snapshot.Query.votes(
            orderBy='created',
            orderDirection='desc',
            first=10000,
            where=[
                snapshot.Vote.proposal == proposal_id
            ]
        )

        voting_snapshots_list = sg.query_df([
            vote_tracker.id,
            vote_tracker.voter,
            vote_tracker.created,
            vote_tracker.choice,
            vote_tracker.vp
        ])


        #generate a list of choices made per voter
        options = dao_governance_view_clean
        options.drop(options.columns[[0, 1, 2,3,4,5]], axis=1, inplace=True)

        choice_list = db.query("select distinct votes_voter, votes_choice, votes_created from voting_snapshots_list order by votes_created desc").df()


        # add an empty column for the choice text to choice_list
        choice_list.insert(2, 'vote_text', '')

        # now we add the actual body, row by row,  using the vote choice number as the lookup index in dao_governance_view_clean (accounting for the first 6 columns

        shape = choice_list.shape
        number_of_voters = shape[0]-1

        st.write('total voters:', number_of_voters)

        z = 0
        while z<=number_of_voters:
            choice_val = choice_list.iloc[z,1]
            position = 6+ choice_val
            choice_text = row_data.iloc[0,position]

            choice_list.at[z,'vote_text']=choice_text
            z=z+1


        choice_table = db.query("select distinct votes_voter,votes_choice,vote_text from choice_list").df()

        voting_snapshots_list = voting_snapshots_list.merge(choice_list, left_on=['votes_voter'], right_on=['votes_voter'], how='left')

        voting_snapshots_list.rename(columns={'votes_created_x': 'votes_created', 'votes_choice_x': 'votes_choice'}, inplace=True)

        voting_snapshots_list.drop(['votes_created_y','votes_choice_y'], axis=1)


        #st.write('Sample vote records:', voting_snapshots_list)

        @st.cache
        def convert_df(df):
            return df.to_csv().encode('utf-8')


        crunch_data = db.query("select " 
                                   "votes_voter "
                                   ",votes_created"
                                   ",to_timestamp(votes_created) vote_time"
                                   ",votes_choice"
                                   ",votes_vp" 
                                   ",vote_text" 
                                   ",sum(votes_vp) over (order by votes_vp desc, votes_created asc) as cumulative_vp"
                                   ",sum(votes_vp) over (order by votes_vp desc, votes_created asc rows between unbounded preceding and unbounded following) as total_vp"
                                   ",(votes_vp::decimal/sum(votes_vp::decimal) over (order by votes_vp desc, votes_created asc , votes_created asc rows between unbounded preceding and unbounded following)) as percentage_of_total_vp "
                                   ",((sum(votes_vp) over (order by votes_vp desc, votes_created asc))::decimal/sum(votes_vp::decimal) over (order by votes_vp desc rows between unbounded preceding and unbounded following)) as cum_percentage_of_total_vp "
                               ",round((sum(votes_vp) over (order by votes_vp desc, votes_created asc))::decimal/sum(votes_vp::decimal) over (order by votes_vp desc rows between unbounded preceding and unbounded following)) as cum_percentange_of_total_vp_stepped "
                                   ",row_number() over (order by votes_vp desc, votes_created asc) as proposal_voter_rank "
                                   ",count(votes_voter) over (order by votes_vp, votes_created asc rows between unbounded preceding and unbounded following) total_voters "
                                   ",(count(*) over (order by votes_vp desc, votes_created asc))::decimal/(count(*) over (order by votes_vp rows between unbounded preceding and unbounded following))::decimal percentage_voters_counted "
                                   ",round(100*(count(*) over (order by votes_vp desc, votes_created asc))::decimal/(count(*) over (order by votes_vp rows between unbounded preceding and unbounded following)))::decimal percentage_voters_counted_stepped "
                               
                               "from "
                               "    voting_snapshots_list  "
                               ""
                               "Group by "
                               "    votes_voter"
                               "    ,votes_choice"
                               "    , votes_vp "
                               "    , votes_created "  
                               "    , vote_text "
                               ""
                               "Order by "
                               "    votes_vp desc "
                               "    , votes_created asc"
                               "").df()
        crunch_data.insert(0, 'DAO', spacename)

        crunch_data.head(n=10)




        crunch_data.head(n=10)

        st.write('Sample voting records',crunch_data)


        @st.cache
        def convert_df(df):
            return df.to_csv().encode('utf-8')


        csv = convert_df(crunch_data)

        st.download_button(
            "Press to download Stats data",
            csv,
            "aggregated_data.csv",
            "text/csv",
            key='download-csv'
        )

        st.write('Sample Aggregate data')

        fig = plt.figure(figsize=(20, 8))

        plt.rc("figure", figsize=(40, 20))
        sns.set_style("whitegrid")
        plt.rc("font", size=18)
        data_means = crunch_data.groupby("percentage_voters_counted_stepped")[
            "cum_percentage_of_total_vp", "percentage_voters_counted"].agg("mean").reset_index()
        ##print(data_means)
        plot_title = spacename + ' snapshots % of vote along population'

        st.write(data_means)


        @st.cache
        def convert_df(df):
            return df.to_csv().encode('utf-8')


        csv = convert_df(data_means)

        st.download_button(
            "Press to download Aggregated data",
            csv,
            "aggregated_data.csv",
            "text/csv",
            key='download-csv'
        )

        p50 = db.query("select min(percentage_voters_counted) "
                       "from data_means  where cum_percentage_of_total_vp>=0.5 ").df()

        p50display = round(100 * (p50.iloc[0, 0]), 2)

        voters = db.query("select count(distinct votes_voter) from voting_snapshots_list").df()
        voters = voters.iloc[0, 0]

        #st.write(Voters)
        st.write('### It took ', p50display, '% out of',voters ,' voters to accumulate half of the voting power in "',choiceOG, '".')

        st.write('The chart below describes all proposals in', spacename,
                 '.The orange markers represent what percentage of the population it takes to reach a given percentage of voting power.')

        # sns.lineplot(data=crunch_data, y="cum_percentage_of_total_vp",x="percentage_voters_counted_stepped", hue="Proposal",zorder=-3).set(title=plot_title,xlabel='% of voters',ylabel='% of voting power')#, legend=False)
        ax = sns.lineplot(data=crunch_data, y="cum_percentage_of_total_vp", x="percentage_voters_counted_stepped").set(
            title=plot_title, xlabel='% of voters', ylabel='% of voting power')
        st.pyplot(fig)

        chart_data=db.query("select vote_text, sum(percentage_of_total_vp) as percentage_of_total_vp from crunch_data group by 1").df()

        st.write(chart_data)

        fig2 = plt.figure(figsize=(10, 4))

        chart = sns.barplot(data=chart_data, y ="percentage_of_total_vp", x="vote_text", hue= "vote_text"  ).set(
            title=('Results: '+choiceOG), xlabel='Choice', ylabel='% of voting power')
        st.pyplot(fig2)

        #$st.bar_chart(data=chart_data, use_container_width=True)

        #st.altair_chart(chart_data, use_container_width=False).mark_arc()

        chart_data2 = db.query(
                                    "With initdata as "
                                    "( "
                                    "select "
                                   "    votes_voter as chart_voter"
                                   "    , votes_vp  "         
                                   "   ,PERCENTILE_CONT(0.001) WITHIN GROUP (ORDER BY votes_vp)as pnt01 "                                
                                   "   ,PERCENTILE_CONT(0.025) WITHIN GROUP (ORDER BY votes_vp) as pnt05 "                             
                                   "   ,PERCENTILE_CONT(0.01) WITHIN GROUP (ORDER BY votes_vp) as pnt10 "
                                   "   ,PERCENTILE_CONT(0.025) WITHIN GROUP (ORDER BY votes_vp) as pnt15 "
                                   "   ,PERCENTILE_CONT(0.03) WITHIN GROUP (ORDER BY votes_vp) as pnt20 " 
                                   "   ,PERCENTILE_CONT(0.035) WITHIN GROUP (ORDER BY votes_vp) as pnt25 "
                                   "   ,PERCENTILE_CONT(0.04) WITHIN GROUP (ORDER BY votes_vp) as pnt30 " 
                                   "from crunch_data as chart_vp "
                                    "Group by 1,2 "
                                   "order by 2 "
                                    ") "
                                    ""
                                    "Select "
                                    "   chart_voter "
                                    "   ,votes_vp "
                                    "   ,case "
                                    "       when  votes_vp <= pnt01 then pnt01 " 
                                    "       when  votes_vp <= pnt05 then pnt05 " 
                                    "       when  votes_vp <= pnt10 then pnt10 "
                                    "       when  votes_vp <= pnt15 then pnt15 " 
                                    "       when  votes_vp <= pnt20 then pnt20 "
                                    "       when  votes_vp <= pnt25 then pnt25 " 
                                    "       else pnt30 "
                                    "       end chart_vp "
                                    "From "
                                    "   initdata "
                                    ""
                                    ).df()

        fig3 = plt.figure(figsize=(10, 4))
        #sns.displot(chart_data2, x="chart_vp", kind="kde")

        sns.distplot(chart_data2['chart_vp'], hist=True, kde=True,
                     bins=7, color='blue',
                     hist_kws={'edgecolor': 'black'})

        #sns.barplot(data=crunch_data, y="votes_vp", x="votes_voter", hue="vote_text").set(title=('voter balances'), ylabel='power distribution')
        st.pyplot(fig3)


        st.markdown(
            '<p class="bigger-font">All done. Enjoy! Feel free to enter another space name, or choose another snapshot from the drop-down menu, to pull more data.</p>',
            unsafe_allow_html=True)
        # The chart above shows what % of all possible votes has been cast (Y axis) as each incremental percent of the voting population casts their vote (X axis). Each line is a Proposal and has a unique color, so that a dot on each percent point represents what % of total voting power was accumulated by that group. The color represents which vote was cast.
        # The Orange X shows the average % of power accumulated across all elections.



```


---

```python
#Snapshot diver allows you to look at a DAO's elections on snapshot to see how decentralized they are. Bugs? Ping me on Twitter @edgecaser.

from datetime import datetime
from datetime import date
from subgrounds.subgraph import SyntheticField, FieldPath
from subgrounds.subgrounds import Subgrounds

import pandas as pd
import duckdb as db
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

st.set_page_config(layout="wide")

st.markdown("""
<style>
.bigger-font {
    font-size:18px !important;
}
.biggest-font {
    font-size:20px !important;
}

</style>
""", unsafe_allow_html=True)



st.write('# Snapshot Surfer')
st.write('## By @Edgecaser')

st.markdown('<p class="bigger-font">This tool will help you view how decentralized a DAO\'s voting power is.</p>', unsafe_allow_html=True)

st.markdown('<p class="bigger-font">DAO stands for Decentralized Autonomous Organization, a bottoms-up team or organization. These are run by votes recorded on the Blockchain.</p>', unsafe_allow_html=True)

st.markdown('<p class="bigger-font">Some DAOs voting power has a 1:1 correlation with their token holdings. Others use different schemes that distribute voting power in different ways, all the way down to one-wallet-one-vote. </p>', unsafe_allow_html=True)

st.markdown('<p class="bigger-font"> When a few people hold a lot of voting power, a small minority drives the result of any proposal on Snapshot. This is not good or bad. There\'s examples of successful organizations with all kinds of power distribution schemes.</p>', unsafe_allow_html=True)

st.markdown('<p class="bigger-font"> This tool helps illustrate how decentralized voting power is in any DAO in Snapshot It will pull down all proposals data and analyze the distribution of power. It will download the data to the folder of your choice </p>', unsafe_allow_html=True)

st.markdown('<p class="bigger-font"> If you are interested in analyzing a single election in more detail, I recommend you visit Snapshot Diver </p>', unsafe_allow_html=True)
st.markdown('[Snapshot Diver](https://edgecaser-snapshotsurfer-snapshotdiver-jilc2t.streamlitapp.com/)')



st.write('### Instructions')

st.markdown('<p class="bigger-font"> Trolls happen. Some DAOs are bombed with fake proposals that gather a handful of voters. This filter lets you ignore them in the analysis (but will be kept in the downloaded data). I find 20 is good enough for small DAOs. For larger DAOs I recommend values of 50 or more.</p>', unsafe_allow_html=True)

filter = st.slider(
    'Only choose proposals that had at least these many voters:',
    int(0), 200, 20, 10)

st.markdown(
    '<p class="bigger-font">Enter the DAO you want to study below by entering its namespace in Snapshot. For example, OlympusDAO has a url like https://snapshot.org/#/olympusdao.eth so its userspace is olympusdao.eth.</p>',
    unsafe_allow_html=True)
st.write('')


spacename = st.text_input('Where to pull from? Type your selection then press START',help='Which space, eg: curve.eth')
daysLimit = int(input('How many days in the past do you want to go?',help='The tool will look for data starting from today and back this number of days))

if st.button('START'):

    sg = Subgrounds()
    snapshot = sg.load_api('https://hub.snapshot.org/graphql')

    snapshot.Proposal.datetime = SyntheticField(
      lambda timestamp: str(datetime.fromtimestamp(timestamp)),
      SyntheticField.STRING,
      snapshot.Proposal.end,
    )

    proposals = snapshot.Query.proposals(
        orderBy='created',
        orderDirection='desc',
        first=1000,
        where=[
            snapshot.Proposal.space == spacename,  ##'fuse.eth',
            snapshot.Proposal.state == 'closed'
            ##snapshot.Proposal.title == 'OIP-18: Reward rate framework and reduction',
        ]
    )

st.write('Let\'s get started! Pulling from: ', spacename, ':sunglasses:')

    proposals_snapshots = sg.query_df([
        proposals.title,
        proposals.created,
        proposals.id,
        proposals.start,
        proposals.end,
        proposals.votes
    ])

    proposals_snapshots['createdDate'] = (pd.to_datetime(proposals_snapshots['proposals_created'], unit='s'))
    proposals_snapshots['startDate'] = (pd.to_datetime(proposals_snapshots['proposals_start'], unit='s'))
    proposals_snapshots['endDate'] = (pd.to_datetime(proposals_snapshots['proposals_end'], unit='s'))

    proposals_choices = sg.query(proposals.choices)
    proposals_choices = pd.DataFrame(proposals_choices)

    olympus_governance_view = pd.DataFrame()
    olympus_governance_view = pd.concat([proposals_snapshots, proposals_choices], axis=1)
    olympus_governance_view.drop_duplicates()

    olympus_governance_view_clean.insert(0, 'DAO', spacename)


    st.write("Sample list of Proposals")
    st.write(olympus_governance_view.head(10))

    @st.cache
    def convert_df(df):
        return df.to_csv().encode('utf-8')


    csv = convert_df(olympus_governance_view)

    st.download_button(
        "Press to download list of Proposals",
        csv,
        "olympus_governance_view.csv",
        "text/csv",
        key='download-csv'
    )

    total_proposals = len(olympus_governance_view_clean)
    #total_proposals

    proposal_id = olympus_governance_view_clean.iloc[0,2]
    #proposal_id

    #st.write("HIYA - just checking")

    vote_tracker = snapshot.Query.votes(
        orderBy='created',
        orderDirection='desc',
        first=10000,
        where=[
            snapshot.Vote.proposal == proposal_id
        ]
    )
    #st.write("HIYA2 - just checking")

    voting_snapshots_list = sg.query_df([
        vote_tracker.id,
        vote_tracker.voter,
        vote_tracker.created,
        vote_tracker.choice,
        vote_tracker.vp
    ])

    #st.write("HIYA3 - just checking")

    st.write('Pulling vote records...')
    mybar = st.progress(0)
    x=0

    voteTicker = 0
    totalProposals = len(olympus_governance_view)
    voteslist = pd.DataFrame()
    votesDb = pd.DataFrame()
    voteListLength = 1000
    datediff = 0
    now=0
    daysAgo=0
    #daysLimit = 90
    datediff=0
    epochlimit = (90*86400)
    ut = time.time()
    limitTimestamp = int(ut - epochlimit)
    limitDate = datetime.fromtimestamp(limitTimestamp)
    limitDate = limitDate.strftime('%m-%d-%Y')
    exit = False

    while int(datediff) < int(daysLimit):
        proposal_id = olympus_governance_view.iloc[voteTicker,2]
        skipValue = (voteTicker)*(1000)
        vote_tracker = snapshot.Query.votes(
            #orderBy = 'created',
            #orderDirection='asc',
            first=1000,
            where=[
              snapshot.Vote.proposal == proposal_id
              #snapshot.Vote.created > limitTimestamp
            ]
        )
        voting_snapshots = sg.query_df([
        vote_tracker.id,
        vote_tracker.voter,
        vote_tracker.created,
        vote_tracker.choice,
        vote_tracker.vp
        ])


        voting_snapshots['proposals_id']= olympus_governance_view.iloc[voteTicker,2]
        #voteDate = votesDb.iat[voteTicker,4]

        votesDb=pd.concat([voting_snapshots, votesDb])
        votesDb['createdDate']=(pd.to_datetime(votesDb['votes_created'],unit='s'))
        then = votesDb.iat[voteTicker,6]
        now = datetime.now()
        delta = now-then
        datediff = delta.days
        votesDbLength = len(votesDb)
        voteListLength = len(voting_snapshots)
        recordTimestamp1 = votesDb.iat[voteTicker,2]
        recordTimestamp = dt.datetime.fromtimestamp( recordTimestamp1 )
        now = (int(dt.datetime.utcnow().timestamp()))
        #datediff=abs(int(now) - recordTimestamp1)

        if int(datediff) > int(daysLimit):
            exit
        if voteTicker== totalProposals:
            exit

        #print('ticker', voteTicker, 'proposal',proposal_id, 'records:',voteListLength, 'DB size:',votesDbLength, '    -days ago:', datediff, '     -date', then, '    -exit?', exit )
        #print(proposal_id, voteDate, datediff)
        chartprogress = min((voteTicker/total_proposals),1)
        progress = 100*(round(voteTicker/total_proposals,4))
        mybar.progress(chartprogress)
        voteTicker = voteTicker+1



    st.write('Sample output: Vote records',voting_snapshots_list.head(10))

    @st.cache
    def convert_df(df):
        return df.to_csv().encode('utf-8')
    csv = convert_df(voting_snapshots_list)

    st.download_button(
        "Press to download vote records",
        csv,
        "voting_snapshots_list.csv",
        "text/csv",
        key='download-csv'
    )

    votesDb.rename(columns={"createdDate": "voteDate"}, inplace = True)
    votesDb.drop_duplicates(inplace=True)
    votesDb.drop_duplicates()


    governance_data  = pd.DataFrame()

    #I join these two tables to create my charts as it makes life easier. We are going to build the charts here now, so here we go
    governance_data = pd.merge(voting_snapshots_list, olympus_governance_view_clean, how='inner', left_on='Proposal', right_on='proposals_id')
    del governance_data["proposals_body"]
    st.write('sample output: governance data', governance_data.head(10))

    @st.cache
    def convert_df(df):
        return df.to_csv().encode('utf-8')

    csv = convert_df(governance_data)

    st.download_button(
        "Press to download joined governance data",
        csv,
        "governance_data.csv",
        "text/csv",
        key='download-csv'
    )

    crunch_data = db.query("select "
                           "A.proposals_id"
                           "    ,A.startDate "
                           "    ,A.proposals_title "
                           "    ,A.votes_voter "
                           "    ,A.votes_vp "
                           "    ,A.voteDate "
                           ",sum(A.votes_vp) over (Partition by proposals_id  order by votes_vp desc, voteDate asc) as cumulative_vp "
                           ",sum(A.votes_vp) over (Partition by proposals_id) as total_vp "
                           ",(votes_vp::decimal/sum(votes_vp::decimal) over (Partition by proposals_id)) as percentage_of_total_vp "
                           ",((sum(A.votes_vp) over (Partition by proposals_id  order by votes_vp desc, voteDate asc))::decimal/sum(votes_vp::decimal) over (Partition by proposals_id)) as cum_percentage_of_total_vp "
                           ",round((sum(A.votes_vp) over (Partition by proposals_id  order by votes_vp desc, voteDate asc))::decimal/sum(votes_vp::decimal) over (Partition by proposals_id)) as cum_percentage_of_total_vp_stepped "
                           ",row_number() over (Partition by proposals_id order by votes_vp desc, voteDate asc) as proposal_voter_rank "
    
                           ",(count(*) over (Partition by proposals_id))::decimal total_voters "
    
                           ",(count(*) over (Partition by proposals_id  order by votes_vp desc, voteDate asc))::decimal/(count(*) over (Partition by proposals_id))::decimal percentage_voters_counted "
    
                           ",round(100*(count(*) over (Partition by proposals_id  order by votes_vp desc, voteDate asc))::decimal/(count(*) over (Partition by proposals_id)))::decimal percentage_voters_counted_stepped "
                           "from "
                           "    governance_data  A "
                           # "where   to_timestamp((votes_Created::bigint))<'2023-01-01' "
                           ""
                           "Group by "
                           "A.proposals_id"
                           "    ,A.startDate "
                           "    ,A.proposals_title "
                           "    ,A.votes_voter "
                           "    ,A.votes_vp "
                           "    ,A.voteDate "
                           ""
                           "Order by "
                           "    A.startDate  asc "
                           "    , votes_vp desc "
                           "    , voteDate asc"
                           "").df()

    crunch_data.insert(0, 'DAO', spacename)
    crunch_data.drop_duplicates

    #leaders = crunch_data.loc[crunch_data['proposal_voter_rank'] <= 3]
    #leader_count = leaders.votes_voter.nunique()

    leader_ranks = db.query("with leader_ranks as "
                            "(Select distinct "
                            "   B.proposals_id"
                            "   ,B.votes_voter"
                            "   ,B.proposal_voter_rank "
                            "   ,(B.proposal_voter_rank +1) as leader_rank "
                            "From "
                            "   (select "
                            "proposals_id"
                            ",votes_voter "
                            ",votes_choice"
                            ",votes_vp"
                            ",votes_created  "
                            ",sum(votes_vp) over (Partition by proposals_id  order by votes_vp desc, votes_created asc) as cumulative_vp"
                            ",sum(votes_vp) over (Partition by proposals_id) as total_vp"
                            ",(votes_vp::decimal/sum(votes_vp::decimal) over (Partition by proposals_id)) as percentage_of_total_vp "
                            ",((sum(votes_vp) over (Partition by proposals_id  order by votes_vp desc, votes_created asc))::decimal/sum(votes_vp::decimal) over (Partition by proposals_id)) as cum_percentage_of_total_vp "
                            "    ,round((sum(votes_vp) over (Partition by proposals_id  order by votes_vp desc, votes_created asc))::decimal/sum(votes_vp::decimal) over (Partition by proposals_id)) as cum_percentage_of_total_vp_stepped "
                            ",row_number() over (Partition by proposals_id order by votes_vp desc, votes_created asc) as proposal_voter_rank "
                            ",count(votes_voter) over (Partition by proposals_id  order by votes_vp desc, votes_created asc) total_voters "
                            ",(count(*) over (Partition by proposals_id  order by votes_vp desc, votes_created asc))::decimal/(count(*) over (Partition by proposals_id))::decimal percentage_voters_counted "
                            ",round(100*(count(*) over (Partition by proposals_id  order by votes_vp desc, votes_created asc))::decimal/(count(*) over (Partition by proposals_id)))::decimal percentage_voters_counted_stepped "
                            "from "
                            "    governance_data  "
                            ""
                            "Group by "
                            "    proposals_id"
                            "    ,votes_voter"
                            "    ,votes_choice"
                            "    , votes_vp "
                            "    , votes_created "
                            ""
                            "Order by "
                            "    proposals_id "
                            "    ,votes_vp desc "
                            "    , votes_created asc) B "
                            "where "
                            "   B.cum_percentage_of_total_vp<=0.5) "
                            ""
                            "Select "
                            "   *"
                            "From crunch_data A"
                            "   Join leader_ranks B on A.proposal_voter_rank = B.leader_rank and A.proposals_id = B.proposals_id"
                            ""
                            ).df()
    #st.write(leader_ranks)


    dao_members = crunch_data.groupby('DAO').votes_voter.nunique()
    dao_members = dao_members.iloc[0]
    leader_count = leader_ranks.votes_voter.nunique()
    elite = round((leader_count) / (dao_members), 4)

#print(dao_members, "{0:.2%}".format(elite))

#$print(dao_members, "{0:.2%}".format(elite))

    st.write('Sample Stats data')
    st.write(crunch_data.head(10))
    ##spit out the file!


    crunch_data = crunch_data.loc[crunch_data['total_voters']>filter]

    @st.cache
    def convert_df(df):
        return df.to_csv().encode('utf-8')
    csv = convert_df(crunch_data)
    st.download_button(
        "Press to download Stats data",
        csv,
        "aggregated_data.csv",
        "text/csv",
        key='download-csv'
    )

    #crunch_data_path =final_file+'\\'+spacename+'_crunch_data_path'+str(date.today().strftime("%b-%d-%Y"))+'_'+str(len(crunch_data))+'.csv'
    #crunch_data.to_csv(crunch_data_path, index = False)
    curve_data = db.query(
        "select "
        "   percentage_voters_counted_stepped "
        "   , avg(percentage_voters_counted) avg_percentage_voters_counted "
        "   , avg(cum_percentage_of_total_vp) avg_percentage_of_total_vp "
        "   ,'Grand Average' as proposal "
        "from crunch_data "
        " group by 1 "
        "UNION ALL "
        "SELECT "
        "   percentage_voters_counted_stepped "
        "   ,percentage_voters_counted "
        "   ,cum_percentage_of_total_vp "
        "   ,proposals_id "
        "FROM crunch_data "
    ).df()

    plt.rc("figure", figsize=(40, 20))
    # sns.set_style("whitegrid")
    plt.rc("font", size=25)
    data_means = crunch_data.groupby("percentage_voters_counted_stepped")[
        "cum_percentage_of_total_vp", "percentage_voters_counted"].agg("mean").reset_index()
    ##print(data_means)
    plot_title = spacename + ' snapshots % of vote along population with Average as X'

    ax = sns.scatterplot(data=crunch_data, hue="proposals_id", y="cum_percentage_of_total_vp",
                         x="percentage_voters_counted_stepped").set(title=plot_title, xlabel='% of voters',
                                                                    ylabel='% of voting power')
    chart = sns.scatterplot(data=data_means, x="percentage_voters_counted_stepped", y="cum_percentage_of_total_vp",
                            zorder=3, s=800, marker='X', color='orange')
    plt.legend(bbox_to_anchor=(1.02, 0.99), loc='upper left', borderaxespad=0)

    st.write(data_means)

    @st.cache
    def convert_df(df):
        return df.to_csv().encode('utf-8')

    csv = convert_df(data_means)

    st.download_button(
        "Press to download Aggregated data",
        csv,
        "aggregated_data.csv",
        "text/csv",
        key='download-csv'
    )

    st.markdown(
        '<p class="bigger-font">All done. Enjoy! Feel free to enter another space name to pull more data.</p>',
        unsafe_allow_html=True)
    # The chart above shows what % of all possible votes has been cast (Y axis) as each incremental percent of the voting population casts their vote (X axis). Each line is a Proposal and has a unique color, so that a dot on each percent point represents what % of total voting power was accumulated by that group. The color represents which vote was cast.
    # The Orange X shows the average % of power accumulated across all elections.


```


---

```python
global file
file = input('Selet a folder to save output') ##enter your file path here - the file is in the repo "summary_stats.csv".
raw_file = file
```
```python
from datetime import datetime
from datetime import date
from subgrounds.subgraph import SyntheticField, FieldPath
from subgrounds.subgrounds import Subgrounds
import pandas as pd
import  os as os
import duckdb as db
import seaborn as sns
import matplotlib.pyplot as plt
import datetime as dt

```
```python
sg = Subgrounds()
snapshot = sg.load_api('https://hub.snapshot.org/graphql')

```
```python
snapshot.Proposal.datetime = SyntheticField(
  lambda timestamp: str(datetime.fromtimestamp(timestamp)),
  SyntheticField.STRING,
  snapshot.Proposal.end,
)
```
spaces = snapshot.Query.spaces(

    first=5000,

    orderby = 'name',

    orderdirection = 'asc'

)

print(spaces)

spaces_list = sg.query_df([

    spaces.name

])

spaces_list

```python
spacename = input('spacename plz?')
# based on their url, for example "curve.eth" for  https://snapshot.org/#/curve.eth
print  (spacename)
```
```python
proposals = snapshot.Query.proposals(
  orderBy='created',
  orderDirection='desc',
  first=1000,
  where=[
    snapshot.Proposal.space == spacename, ##'fuse.eth',
    snapshot.Proposal.state == 'closed'
    ##snapshot.Proposal.title == 'OIP-18: Reward rate framework and reduction',
  ]
)

```
```python
proposals_snapshots = sg.query_df([
    proposals.title,
    proposals.created,
    proposals.id,
    proposals.body,
    proposals.start,
    proposals.end,
    proposals.votes
])

proposals_snapshots.head(10)
```
```python
total_snapshots = len(proposals_snapshots)
print(total_snapshots)
```
```python
proposals_choices = sg.query(proposals.choices)
```
```python
proposals_choices = pd.DataFrame(proposals_choices, columns = ['option_1', 'option_2', 'option_3', 'option_4', 'option_5','option_6','option_7'])#,'option_8', 'option_9', 'option_10', 'option_11', 'option_12','option_13','option_14','option_15', 'option_16', 'option_17', 'option_18', 'option_19'])
```
```python
proposals_choices.head(10)
```
```python
total_choices = len(proposals_choices)
print(total_choices)
```
```python
olympus_governance_view = pd.concat([proposals_snapshots,proposals_choices], axis=1)
```
olympus_governance_view["proposal_date"] = (datetime.fromtimestamp(olympus_governance_view["proposals_created"]))

```python
##let's view the output just to make sure
olympus_governance_view.head(5)
```
```python
#let's remove duplicate rows the easy way, and add the name of the DAO to the table
olympus_governance_view_clean = olympus_governance_view.copy(deep=True)
olympus_governance_view_clean = db.query("select "
                                 "  *"
                                 "  , (to_timestamp((proposals_created::bigint)))::date proposal_date  "
                                 ""
                                 "from olympus_governance_view").df()
#make sure we know which DAO we are working with
olympus_governance_view_clean.insert(0, 'DAO', spacename)
olympus_governance_view_clean.head(10)
```
```python
total_proposals = len(olympus_governance_view_clean)
total_proposals
```
```python
max_index = len(olympus_governance_view_clean.columns)
max_index
```
```python
path =file+'/'+spacename+'_proposals_table_'+str(date.today().strftime("%b-%d-%Y"))+'_'+str(len(olympus_governance_view_clean))+'_proposals.csv'
olympus_governance_view_clean.to_csv(path, index = False)
```
```python
proposal_id = olympus_governance_view_clean.iloc[0,3]
proposal_id
```
vote_proposals = snapshot.Query.votes(

orderBy = 'created',

orderDirection='desc',

first=1000,

where=[

  snapshot.Vote.proposal == '0x058bda9a27ba8e0e154df38fdd6f41e59c640a44cd6252cacad965549d0994d7'

]

)

print(vote_proposals)

```python
vote_tracker = snapshot.Query.votes(
orderBy = 'created',
orderDirection='desc',
first=1000,
where=[
  snapshot.Vote.proposal == proposal_id
]
)
```
```python
print(vote_tracker)
```
```python
voting_snapshots_list_pre = sg.query_df([
    vote_tracker.id,
    vote_tracker.voter,
    vote_tracker.created,
    vote_tracker.choice,
    vote_tracker.vp
])
```
```python

voting_snapshots_list = db.query("select "
                                 "  *"
                                 "  , to_timestamp((votes_Created::bigint)) vote_timestamp  "
                                 ""
                                 "from voting_snapshots_list_pre order by votes_Created").df()
```
```python
voting_snapshots_list.head(65)
```
```python
    vote_tracker = snapshot.Query.votes(
        orderBy = 'created',
        orderDirection='desc',
        first=1000,
        where=[
          snapshot.Vote.proposal == proposal_id
        ]
    )
    voting_snapshots = sg.query_df([
    vote_tracker.id,
    vote_tracker.voter,
    vote_tracker.created,
    vote_tracker.choice,
    vote_tracker.vp
    ])

    #votesDb=pd.concat([vote_tracker, voteslist])
    recordTimestamp1 = votesDb.iat[voteTicker,2]
    recordTimestamp = dt.datetime.fromtimestamp( recordTimestamp1 )
    votesDbLength = len(votesDb)
    now = (int(dt.datetime.utcnow().timestamp()))
    datediff=abs(int(now) - recordTimestamp1)
    daysAgo = int(datediff/86400)
    voteListLength = len(vote_tracker)
    recordID = votesDb.iat[voteTicker,0]
    vote = silovotesDb.iat[voteTicker,3]
    print("iterations: ", voteTicker, "Lines skipped: ",skipValue, "records collected: ", silovoteListLength, " - latest recordID: ",vote, " ", recordID , " - votes DB length: ", silovotesDbLength, " - latest record from: ", recordTimestamp, daysAgo,"days ago")
    #print("iterations: ", voteTicker, "records collected: ", voteListLength, " - userdb length: ", votesDbLength)
    voteTicker = voteTicker+1
```
```python
##this captures the ENTIRE list of people who voteed OHM
voteTicker = 0
totalProposals = len(olympus_governance_view_clean)
voteslist = pd.DataFrame()
votesDb = pd.DataFrame()
voteListLength = 1000
datediff = 0
now=0
daysAgo=0
daysLimit = 90
exit = False
while exit==False:
    proposal_id = olympus_governance_view_clean.iloc[voteTicker,3]
    skipValue = (voteTicker)*(1000)
    vote_tracker = snapshot.Query.votes(
        orderBy = 'created',
        orderDirection='desc',
        first=1000,
        where=[
          snapshot.Vote.proposal == proposal_id
        ]
    )
    voting_snapshots = sg.query_df([
    vote_tracker.id,
    vote_tracker.voter,
    vote_tracker.created,
    vote_tracker.choice,
    vote_tracker.vp
    ])

    votesDb=pd.concat([voting_snapshots, votesDb])
    votesDbLength = len(votesDb)
    voteListLength = len(voting_snapshots)
    recordTimestamp1 = votesDb.iat[voteTicker,2]
    recordTimestamp = dt.datetime.fromtimestamp( recordTimestamp1 )
    now = (int(dt.datetime.utcnow().timestamp()))
    datediff=abs(int(now) - recordTimestamp1)

    if datediff> daysLimit: exit
    if voteTicker== totalProposals: exit
    print('ticker', voteTicker, 'proposal',proposal_id, 'records:',voteListLength, 'DB size:',votesDbLength, 'days ago:', datediff )
    voteTicker = voteTicker+1

votesDb.drop_duplicates
print("Done. Total Records collected: ", votesDbLength)
```
```python
voting_snapshots_list.drop
voting_snapshots_list = db.query("select "
                                 "  *"
                                 "  , to_timestamp((votes_Created::bigint)) vote_timestamp  "
                                 ""
                                 "from voting_snapshots_list_pre where to_timestamp((votes_Created::bigint))<'2022-01-01 00:00:01' order by vote_timestamp"
                                 ""
                                  ).df()

x=0
progress=0
while progress <100:
    proposal_id = olympus_governance_view_clean.iloc[x,3]
    proposal_date = olympus_governance_view_clean.iloc[x,15]
    print(x,' ',progress,' ', proposal_id, ' ', proposal_date)
    vote_tracker = snapshot.Query.votes(
    orderBy = 'created',
    orderDirection='desc',
    first=1000,
    where=[
      snapshot.Vote.proposal == proposal_id
    ]
    )
    voting_snapshots = sg.query_df([
    vote_tracker.id,
    vote_tracker.voter,
    vote_tracker.created,
    vote_tracker.choice,
    vote_tracker.vp
    ])

    voting_snapshots['Proposal'] = proposal_id
    voting_snapshots_list=pd.concat([voting_snapshots_list, voting_snapshots])

    x=x+1
    progress = 100*(round(x/total_proposals,4))


print(len(voting_snapshots_list),' records')
```
```python
#spit out the file
path =file+'/'+spacename+'_voting_snapshots_list_'+str(date.today().strftime("%b-%d-%Y"))+'_'+str(len(olympus_governance_view_clean))+'.csv'
voting_snapshots_list.to_csv(path, index = False)
```
```python
#I join these two tables to create my charts as it makes life easier. We are going to build the charts here now, so here we go
governance_data = pd.merge(voting_snapshots_list, olympus_governance_view_clean, how='inner', left_on='Proposal', right_on='proposals_id')
del governance_data["proposals_body"] #breaks the table with weird characters
#governance_data["vote_value"] = governance_data["votes_vp"]*governance_data["usd_price"]
governance_data.head(10)
```
```python
#Spit out the file, but save it in its own folder for easy access
final_file = file+'\\'+'final'
final_raw_file = final_file
os.makedirs(final_raw_file, exist_ok=True)
final_path =file+'\\'+spacename+'governance_data_'+str(date.today().strftime("%b-%d-%Y"))+'_'+str(len(governance_data))+'.csv'
governance_data.to_csv(final_path, index = False)
```
```python
crunch_data = db.query("select "
                           "Proposal"
                           ",votes_voter "
                           ",votes_choice"
                           ",votes_vp"
                           ",votes_created "
                       "    ,proposals_title "
                       "    ,proposal_date"
                    "       , to_timestamp(min(votes_Created::bigint)) proposal_date "
                           ",sum(votes_vp) over (Partition by Proposal  order by votes_vp desc, votes_created asc) as cumulative_vp "
                           ",sum(votes_vp) over (Partition by Proposal) as total_vp "
                           ",(votes_vp::decimal/sum(votes_vp::decimal) over (Partition by Proposal)) as percentage_of_total_vp "
                           ",((sum(votes_vp) over (Partition by Proposal  order by votes_vp desc, votes_created asc))::decimal/sum(votes_vp::decimal) over (Partition by Proposal)) as cum_percentage_of_total_vp "
                       ",round((sum(votes_vp) over (Partition by Proposal  order by votes_vp desc, votes_created asc))::decimal/sum(votes_vp::decimal) over (Partition by Proposal)) as cum_percentage_of_total_vp_stepped "
                           ",row_number() over (Partition by Proposal order by votes_vp desc, votes_created asc) as proposal_voter_rank "
                           ",count(votes_voter) over (Partition by Proposal  order by votes_vp desc, votes_created asc) total_voters "
                           ",(count(*) over (Partition by Proposal  order by votes_vp desc, votes_created asc))::decimal/(count(*) over (Partition by Proposal))::decimal percentage_voters_counted "
                           ",round(100*(count(*) over (Partition by Proposal  order by votes_vp desc, votes_created asc))::decimal/(count(*) over (Partition by Proposal)))::decimal percentage_voters_counted_stepped "
                       "from "
                       "    governance_data  "
                       #"where   to_timestamp((votes_Created::bigint))<'2023-01-01' "
                       ""
                       "Group by "
                       "    Proposal"
                       "    ,votes_voter"
                       "    ,votes_choice"
                       "    , votes_vp "
                       "    , votes_created "
                       "    , proposals_title "
                       "    ,proposal_date "
                       ""
                       "Order by "
                       "    7 asc, "
                       "    votes_vp desc "
                       "    , votes_created asc"
                       "").df()


crunch_data.insert(0, 'DAO', spacename)
crunch_data.head(n=10)

```
```python
#leaders = crunch_data.loc[crunch_data['proposal_voter_rank'] <=3]
#leader_count = leaders.votes_voter.nunique()
#leader_count
#DONT ASK ME WHY THIS DIDNT WORK. HAVE TO DO IT THE UGLY WAY

leader_ranks = db.query("with leader_ranks as "
                        "(Select distinct "
                        "   B.Proposal"
                        "   ,B.votes_voter"
                        "   ,B.proposal_voter_rank "
                        "   ,(B.proposal_voter_rank +1) as leader_rank "
                        "From "
                        "   (select "
                               "Proposal"
                               ",votes_voter "
                               ",votes_choice"
                               ",votes_vp"
                               ",votes_created  "
                               ",sum(votes_vp) over (Partition by Proposal  order by votes_vp desc, votes_created asc) as cumulative_vp"
                               ",sum(votes_vp) over (Partition by Proposal) as total_vp"
                               ",(votes_vp::decimal/sum(votes_vp::decimal) over (Partition by Proposal)) as percentage_of_total_vp "
                               ",((sum(votes_vp) over (Partition by Proposal  order by votes_vp desc, votes_created asc))::decimal/sum(votes_vp::decimal) over (Partition by Proposal)) as cum_percentage_of_total_vp "
                           "    ,round((sum(votes_vp) over (Partition by Proposal  order by votes_vp desc, votes_created asc))::decimal/sum(votes_vp::decimal) over (Partition by Proposal)) as cum_percentage_of_total_vp_stepped "
                               ",row_number() over (Partition by Proposal order by votes_vp desc, votes_created asc) as proposal_voter_rank "
                               ",count(votes_voter) over (Partition by Proposal  order by votes_vp desc, votes_created asc) total_voters "
                               ",(count(*) over (Partition by Proposal  order by votes_vp desc, votes_created asc))::decimal/(count(*) over (Partition by Proposal))::decimal percentage_voters_counted "
                               ",round(100*(count(*) over (Partition by Proposal  order by votes_vp desc, votes_created asc))::decimal/(count(*) over (Partition by Proposal)))::decimal percentage_voters_counted_stepped "
                           "from "
                           "    governance_data  "
                               ""
                           "Group by "
                           "    Proposal"
                           "    ,votes_voter"
                           "    ,votes_choice"
                           "    , votes_vp "
                           "    , votes_created "
                           ""
                           "Order by "
                           "    Proposal "
                           "    ,votes_vp desc "
                           "    , votes_created asc) B "
                        "where "
                        "   B.cum_percentage_of_total_vp<=0.5) "
                        ""
                        "Select "
                        "   *"
                        "From crunch_data A"
                        "   Join leader_ranks B on A.proposal_voter_rank = B.leader_rank and A.Proposal = B.Proposal"
                        ""
                    ).df()
leader_ranks



```
```python
#dao_members = db.query("Select count(distinct votes_voter) from crunch_data")
#dao_members
```
```python
dao_members = crunch_data.groupby('DAO').votes_voter.nunique()
dao_members = dao_members.iloc[0]
leader_count =leader_ranks.votes_voter.nunique()
elite = round((leader_count)/(dao_members),4)

print(dao_members, "{0:.2%}".format(elite))

```
```python
crunch_data.head(10)
```
```python
crunch_data.describe()
```
```python
##spit out the file!
crunch_data_path =final_file+'\\'+spacename+'_crunch_data_path'+str(date.today().strftime("%b-%d-%Y"))+'_'+str(len(crunch_data))+'.csv'
crunch_data.to_csv(crunch_data_path, index = False)
```
```python
leader_rank_paths =final_file+'\\'+spacename+'_leader_ranks'+str(date.today().strftime("%b-%d-%Y"))+'_'+str(len(crunch_data))+'.csv'
leader_ranks.to_csv(leader_rank_paths, index = False)
```
#calculate the p50 for each proposal

p50_index = db.query("with p50s as "

                     "  ( Select "

                     "          "

                     "      )"

                     ""

                     ""

                     "select "

                     "  A.DAO "

                     "  , A.Proposal "

                     "  , A.votes_voter "

                     "  , A.leader_rank "

                     "  , (select B.votes_voter from leader_ranks B where B.cum_percentage_of_total_vp>=0.5 and B.votes_voter=A.votes_voter order by cum_percentage_of_total_vp asc limit 1) as p50voter "

                     "  , (select B.cum_percentage_of_total_vp from leader_ranks B where B.cum_percentage_of_total_vp>=0.5 and B.votes_voter=A.votes_voter order by cum_percentage_of_total_vp asc limit 1) as p50index "

                    "from leader_ranks A ").df()

p50_index

```python
data_means = crunch_data.groupby("percentage_voters_counted_stepped")["cum_percentage_of_total_vp", "percentage_voters_counted"].agg("mean").reset_index()
data_means.insert(0, 'DAO', spacename)
data_means.head(51)
```
```python
data_means_file =final_file+'\\'+spacename+'data_means_'+str(date.today().strftime("%b-%d-%Y"))+'_'+str(len(crunch_data))+'.csv'
crunch_data.to_csv(data_means_file, index = False)
```
```python
plt.rc("figure", figsize=(40, 20))
#sns.set_style("whitegrid")
plt.rc("font", size=25)
data_means = crunch_data.groupby("percentage_voters_counted_stepped")["cum_percentage_of_total_vp","percentage_voters_counted"].agg("mean").reset_index()
##print(data_means)
plot_title = spacename + ' snapshots % of vote along population with Average as X'

ax=sns.scatterplot(data=crunch_data, y="cum_percentage_of_total_vp",x="percentage_voters_counted_stepped").set(title=plot_title,xlabel='% of voters',ylabel='% of voting power')
chart = sns.scatterplot(data=data_means,x="percentage_voters_counted_stepped",y="cum_percentage_of_total_vp",zorder=3, s=800,marker='X',color = 'orange')
#and save the chart file, too
plt.savefig(final_file+'\\'+spacename+' vote power distribution.png',transparent =False,  dpi=100)

means_data_path =final_file+'\\'+spacename+'_means_'+'.csv'
data_means.to_csv(means_data_path, index = False)

print(chart)
data_means
```
The chart above shows what % of all possible votes has been cast (Y axis) as each incremental percent of the voting population casts their vote (X axis). Each line is a Proposal and has a unique color, so that a dot on each percent point represents what % of total voting power was accumulated by that group. The color represents which vote was cast.

The Orange X shows the average % of power accumulated across all elections.

```python
voters_df = db.query("select  proposals_title, count(distinct votes_voter) total_voters,  min(proposal_date) proposal_date from crunch_data group by 1 order by 1 asc").df()

chart = sns.barplot(data=voters_df,x="proposal_date",y="total_voters", color = 'orange', ci=None)
x_dates = voters_df['proposal_date'].dt.strftime('%Y-%m-%d').sort_values().unique()
chart.set_xticklabels(labels=x_dates, rotation=45, ha='right')
#and save the chart file, too

print(chart)

#and save the chart file, too
plt.savefig(final_file+'\\'+spacename+'_proposal_participation.png',transparent =False,  dpi=100)

```
```python
voters_df = db.query("select  proposals_title, count(distinct votes_voter) total_voters,  min(proposal_date) proposal_date from crunch_data group by 1 order by 1 asc").df()

chart = sns.barplot(data=voters_df,x="proposals_title",y="total_voters", color = 'orange')
proposal_titles =  voters_df['proposals_title'].sort_values().unique()
chart.set_xticklabels(labels=proposal_titles, rotation=45, ha='right')
#and save the chart file, too

print(chart)
plt.savefig(final_file+'\\'+spacename+'_proposal_participation_title.png',transparent =False,  dpi=100)

means_data_path =final_file+'\\'+spacename+'proposal voters'+'.csv'
voters_df.to_csv(means_data_path, index = False)

```
```python
p50 = db.query("select min(percentage_voters_counted) "
               "from data_means  where cum_percentage_of_total_vp>=0.5 ").df()
p50display = round(100*(p50.iloc[0,0]),2)
print('On average, a proposal at ', spacename, 'takes ',p50display,'% of the voting population.')

print('A total of ',leader_count, 'wallets have driven the result of all proposals at',spacename,)
print('That\'s', ("{0:.2%}".format(elite)), 'of all DAO voters.')
```
```python
crunch_data.head(10)
```
```python
plt.rc("figure", figsize=(40, 20))
sns.set_style("whitegrid")
plt.rc("font", size=25)
plot_title = spacename + 'Voting power dist'

#ax=sns.scatterplot(data=crunch_data, y="cum_percentage_of_total_vp",x="percentage_voters_counted_stepped").set(title=plot_title,xlabel='% of voters',ylabel='% of voting power')
#chart = sns.distplot(crunch_data['votes_vp'], hist=True, kde=True,             bins=10,             color = 'darkblue',             hist_kws={'edgecolor':'black'},             kde_kws={'linewidth': 4})

chart =sns.histplot(
    diamonds,
    x="price", hue="cut",
    multiple="stack",
    palette="light:m_r",
    edgecolor=".3",
    linewidth=.5,
    log_scale=True,
)


#
#chart = sns.scatterplot(data=data_means,x="percentage_voters_counted_stepped",y="cum_percentage_of_total_vp",zorder=3, s=600,marker='X',color = 'orange')
#and save the chart file, too
#plt.savefig(final_file+'\\'+spacename+' vote power distribution.png', dpi=100)

#means_data_path =final_file+'\\'+spacename+'_means_'+'.csv'
#data_means.to_csv(means_data_path, index = False)

print(chart)
```


```python

```
```python

```
```python

```


---

```python
#Snapshot diver allows you to look at a DAO's elections on snapshot to see how decentralized they are. Bugs? Ping me on Twitter @edgecaser.

from datetime import datetime
import time
from subgrounds.subgraph import SyntheticField, FieldPath
from subgrounds.subgrounds import Subgrounds
import pandas as pd
import  os as os
import duckdb as db
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

st.set_page_config(layout="wide")

st.markdown("""
<style>
.bigger-font {
    font-size:18px !important;
}
.biggest-font {
    font-size:20px !important;
}

</style>
""", unsafe_allow_html=True)



st.write('# Snapshot Surfer')
st.write('## By @Edgecaser')
st.write('Version 2')

st.markdown('<p class="bigger-font">This tool will help you view how decentralized a DAO\'s voting power is.</p>', unsafe_allow_html=True)

st.markdown('<p class="bigger-font">DAO stands for Decentralized Autonomous Organization, a bottoms-up team or organization. These are run by votes recorded on the Blockchain.</p>', unsafe_allow_html=True)

st.markdown('<p class="bigger-font">Some DAOs voting power has a 1:1 correlation with their token holdings. Others use different schemes that distribute voting power in different ways, all the way down to one-wallet-one-vote. </p>', unsafe_allow_html=True)

st.markdown('<p class="bigger-font"> When a few people hold a lot of voting power, a small minority drives the result of any proposal on Snapshot. This is not good or bad. There\'s examples of successful organizations with all kinds of power distribution schemes.</p>', unsafe_allow_html=True)

st.markdown('<p class="bigger-font"> This tool helps illustrate how decentralized voting power is in any DAO in Snapshot It will pull down all proposals data and analyze the distribution of power. It will download the data to the folder of your choice </p>', unsafe_allow_html=True)

st.markdown('<p class="bigger-font"> If you are interested in analyzing a single election in more detail, I recommend you visit Snapshot Diver </p>', unsafe_allow_html=True)
st.markdown('[Snapshot Diver](https://edgecaser-snapshotsurfer-snapshotdiver-jilc2t.streamlitapp.com/)')



st.write('### Instructions')

st.markdown('<p class="bigger-font"> Trolls happen. Some DAOs are bombed with fake proposals that gather a handful of voters. This filter lets you ignore them in the analysis (but will be kept in the downloaded data). I find 20 is good enough for small DAOs. For larger DAOs I recommend values of 50 or more.</p>', unsafe_allow_html=True)

filter = st.slider(
    'Only choose proposals that had at least these many voters:',
    int(0), 200, 20, 10)

st.markdown(
    '<p class="bigger-font">Enter the DAO you want to study below by entering its namespace in Snapshot. For example, OlympusDAO has a url like https://snapshot.org/#/olympusdao.eth so its userspace is olympusdao.eth.</p>',
    unsafe_allow_html=True)
st.write('')

spacename = ''
spacename = st.text_input('Where to pull from? Type your selection then press START',help='Which space, eg: curve.eth')

daysLimitInput =''
#daysLimit = 10
daysLimitInput = ''

daysLimit = st.text_input('How many days in the past do you want to go?',help='Snapshotsurfer will pull data going this many days back')
#daysLimit = int(daysLimitInput)


if st.button('START'):

    sg = Subgrounds()
    snapshot = sg.load_api('https://hub.snapshot.org/graphql')

    snapshot.Proposal.datetime = SyntheticField(
      lambda timestamp: str(datetime.fromtimestamp(timestamp)),
      SyntheticField.STRING,
      snapshot.Proposal.end,
    )

    proposals = snapshot.Query.proposals(
        orderBy='created',
        orderDirection='desc',
        first=1000,
        where=[
            snapshot.Proposal.space == spacename,  ##'fuse.eth',
            snapshot.Proposal.state == 'closed'
            ##snapshot.Proposal.title == 'OIP-18: Reward rate framework and reduction',
        ]
    )

    st.write('Let\'s get started! Pulling from: ', spacename, ':sunglasses:')

    proposals_snapshots = sg.query_df([
        proposals.title,
        proposals.created,
        proposals.id,
        proposals.start,
        proposals.end,
        proposals.votes
    ])

    proposals_snapshots['createdDate'] = (pd.to_datetime(proposals_snapshots['proposals_created'], unit='s'))
    proposals_snapshots['startDate'] = (pd.to_datetime(proposals_snapshots['proposals_start'], unit='s'))
    proposals_snapshots['endDate'] = (pd.to_datetime(proposals_snapshots['proposals_end'], unit='s'))

    total_snapshots = len(proposals_snapshots)

    proposals_choices = sg.query(proposals.choices)

    proposals_choices = pd.DataFrame(proposals_choices)

    olympus_governance_view = pd.DataFrame()
    olympus_governance_view = pd.concat([proposals_snapshots, proposals_choices], axis=1)

    ##let's view the output just to make sure
    olympus_governance_view.head(5)

    #let's remove duplicate rows the easy way, and add the name of the DAO to the table
    olympus_governance_view.drop_duplicates()

    #olympus_governance_view.insert(0, 'DAO', spacename)


    st.write("Sample list of Proposals")
    st.write(olympus_governance_view.head(10))

    @st.cache
    def convert_df(df):
        return df.to_csv().encode('utf-8')


    csv = convert_df(olympus_governance_view)

    st.download_button(
        "Press to download list of Proposals",
        csv,
        "olympus_governance_view_clean.csv",
        "text/csv",
        key='download-csv'
    )


    st.write('Pulling vote records...')
    mybar = st.progress(0)

    voteTicker = 0
    totalProposals = len(olympus_governance_view)
    voteslist = pd.DataFrame()
    votesDb = pd.DataFrame()
    voteListLength = 1000
    datediff = 0
    now = 0
    daysAgo = 0
    # daysLimit = 90
    datediff = 0
    epochlimit = (90 * 86400)
    ut = time.time()
    limitTimestamp = int(ut - epochlimit)
    limitDate = datetime.fromtimestamp(limitTimestamp)
    limitDate = limitDate.strftime('%m-%d-%Y')
    exit = False

    while int(datediff) < int(daysLimit):
        proposal_id = olympus_governance_view.iloc[voteTicker, 2]
        skipValue = (voteTicker) * (1000)
        vote_tracker = snapshot.Query.votes(
            # orderBy = 'created',
            # orderDirection='asc',
            first=1000,
            where=[
                snapshot.Vote.proposal == proposal_id
                # snapshot.Vote.created > limitTimestamp
            ]
        )
        voting_snapshots = sg.query_df([
            vote_tracker.id,
            vote_tracker.voter,
            vote_tracker.created,
            vote_tracker.choice,
            vote_tracker.vp
        ])

        voting_snapshots['proposals_id'] = olympus_governance_view.iloc[voteTicker, 2]
        # voteDate = votesDb.iat[voteTicker,4]

        votesDb = pd.concat([voting_snapshots, votesDb])
        votesDb['createdDate'] = (pd.to_datetime(votesDb['votes_created'], unit='s'))
        then = votesDb.iat[voteTicker, 6]
        now = datetime.now()
        delta = now - then
        datediff = delta.days
        votesDbLength = len(votesDb)
        voteListLength = len(voting_snapshots)
        recordTimestamp1 = votesDb.iat[voteTicker, 2]
        recordTimestamp = datetime.fromtimestamp(recordTimestamp1)
        now = (int(datetime.utcnow().timestamp()))
        # datediff=abs(int(now) - recordTimestamp1)

        #print('ticker', voteTicker, 'proposal', proposal_id, 'records:', voteListLength, 'DB size:', votesDbLength,'    -days ago:', datediff, '     -date', then, '    -exit?', exit)
        # print(proposal_id, voteDate, datediff)

        #chartprogress = voteTicker/totalProposals
        ##clear_output(wait=True)
        #mybar.progress(chartprogress)
        voteTicker = voteTicker + 1

    #votesDb.drop_duplicates

    votesDb.rename(columns={"createdDate": "voteDate"}, inplace=True)
    votesDb.drop_duplicates(inplace=True)
    votesDb.drop_duplicates()
    votesDb.head(10000)

    st.write('Sample output: Vote records',votesDb.head(10))

    @st.cache
    def convert_df(df):
        return df.to_csv().encode('utf-8')
    csv = convert_df(votesDb)

    st.download_button(
        "Press to download vote records",
        csv,
        "voting_snapshots_list.csv",
        "text/csv",
        key='download-csv'
    )

    governance_data  = pd.DataFrame()

    #I join these two tables to create my charts as it makes life easier. We are going to build the charts here now, so here we go
    governance_data = pd.merge(votesDb, olympus_governance_view, how='inner', left_on='proposals_id',
                           right_on='proposals_id')
    st.write('sample output: governance data', governance_data.head(10))

    @st.cache
    def convert_df(df):
        return df.to_csv().encode('utf-8')

    csv = convert_df(governance_data)

    st.download_button(
        "Press to download joined governance data",
        csv,
        "governance_data.csv",
        "text/csv",
        key='download-csv'
    )
    crunch_data = db.query("select "
                           "A.proposals_id"
                           "    ,A.startDate "
                           "    ,A.proposals_title "
                           "    ,A.votes_voter "
                           "    ,A.votes_vp "
                           "    ,A.voteDate "
                           ",sum(A.votes_vp) over (Partition by proposals_id  order by votes_vp desc, voteDate asc) as cumulative_vp "
                           ",sum(A.votes_vp) over (Partition by proposals_id) as total_vp "
                           ",(votes_vp::decimal/sum(votes_vp::decimal) over (Partition by proposals_id)) as percentage_of_total_vp "
                           ",((sum(A.votes_vp) over (Partition by proposals_id  order by votes_vp desc, voteDate asc))::decimal/sum(votes_vp::decimal) over (Partition by proposals_id)) as cum_percentage_of_total_vp "
                           ",round((sum(A.votes_vp) over (Partition by proposals_id  order by votes_vp desc, voteDate asc))::decimal/sum(votes_vp::decimal) over (Partition by proposals_id)) as cum_percentage_of_total_vp_stepped "
                           ",row_number() over (Partition by proposals_id order by votes_vp desc, voteDate asc) as proposal_voter_rank "

                           ",(count(*) over (Partition by proposals_id))::decimal total_voters "

                           ",(count(*) over (Partition by proposals_id  order by votes_vp desc, voteDate asc))::decimal/(count(*) over (Partition by proposals_id))::decimal percentage_voters_counted "

                           ",round(100*(count(*) over (Partition by proposals_id  order by votes_vp desc, voteDate asc))::decimal/(count(*) over (Partition by proposals_id)))::decimal percentage_voters_counted_stepped "
                           "from "
                           "    governance_data  A "
                           # "where   to_timestamp((votes_Created::bigint))<'2023-01-01' "
                           ""
                           "Group by "
                           "A.proposals_id"
                           "    ,A.startDate "
                           "    ,A.proposals_title "
                           "    ,A.votes_voter "
                           "    ,A.votes_vp "
                           "    ,A.voteDate "
                           ""
                           "Order by "
                           "    A.startDate  asc "
                           "    , votes_vp desc "
                           "    , voteDate asc"
                           "").df()

    crunch_data.insert(0, 'DAO', spacename)




    #leaders = crunch_data.loc[crunch_data['proposal_voter_rank'] <= 3]
    #leader_count = leaders.votes_voter.nunique()

    leader_ranks = db.query("with leader_ranks as "
                        "(Select distinct "
                        "   B.proposals_id"
                        "   ,B.votes_voter"
                        "   ,B.proposal_voter_rank "
                        "   ,(B.proposal_voter_rank +1) as leader_rank "
                        "From "
                        "   (select "
                        "proposals_id"
                        ",votes_voter "
                        ",votes_choice"
                        ",votes_vp"
                        ",votes_created  "
                        ",sum(votes_vp) over (Partition by proposals_id  order by votes_vp desc, votes_created asc) as cumulative_vp"
                        ",sum(votes_vp) over (Partition by proposals_id) as total_vp"
                        ",(votes_vp::decimal/sum(votes_vp::decimal) over (Partition by proposals_id)) as percentage_of_total_vp "
                        ",((sum(votes_vp) over (Partition by proposals_id  order by votes_vp desc, votes_created asc))::decimal/sum(votes_vp::decimal) over (Partition by proposals_id)) as cum_percentage_of_total_vp "
                        "    ,round((sum(votes_vp) over (Partition by proposals_id  order by votes_vp desc, votes_created asc))::decimal/sum(votes_vp::decimal) over (Partition by proposals_id)) as cum_percentage_of_total_vp_stepped "
                        ",row_number() over (Partition by proposals_id order by votes_vp desc, votes_created asc) as proposal_voter_rank "
                        ",count(votes_voter) over (Partition by proposals_id  order by votes_vp desc, votes_created asc) total_voters "
                        ",(count(*) over (Partition by proposals_id  order by votes_vp desc, votes_created asc))::decimal/(count(*) over (Partition by proposals_id))::decimal percentage_voters_counted "
                        ",round(100*(count(*) over (Partition by proposals_id  order by votes_vp desc, votes_created asc))::decimal/(count(*) over (Partition by proposals_id)))::decimal percentage_voters_counted_stepped "
                        "from "
                        "    governance_data  "
                        ""
                        "Group by "
                        "    proposals_id"
                        "    ,votes_voter"
                        "    ,votes_choice"
                        "    , votes_vp "
                        "    , votes_created "
                        ""
                        "Order by "
                        "    proposals_id "
                        "    ,votes_vp desc "
                        "    , votes_created asc) B "
                        "where "
                        "   B.cum_percentage_of_total_vp<=0.5) "
                        ""
                        "Select "
                        "   *"
                        "From crunch_data A"
                        "   Join leader_ranks B on A.proposal_voter_rank = B.leader_rank and A.proposals_id = B.proposals_id"
                        ""
                        ).df()
    #st.write(leader_ranks)

    dao_members = crunch_data.groupby('DAO').votes_voter.nunique()
    dao_members = dao_members.iloc[0]
    leader_count =leader_ranks.votes_voter.nunique()
    elite = round((leader_count)/(dao_members),4)

    #$print(dao_members, "{0:.2%}".format(elite))

    st.write('Sample Stats data')
    st.write(crunch_data.head(10))
    ##spit out the file!


    crunch_data = crunch_data.loc[crunch_data['total_voters']>filter]

    @st.cache
    def convert_df(df):
        return df.to_csv().encode('utf-8')
    csv = convert_df(crunch_data)
    st.download_button(
        "Press to download Stats data",
        csv,
        "aggregated_data.csv",
        "text/csv",
        key='download-csv'
    )

    curve_data = db.query(
        "select "
        "   percentage_voters_counted_stepped "
        "   , avg(percentage_voters_counted) avg_percentage_voters_counted "
        "   , avg(cum_percentage_of_total_vp) avg_percentage_of_total_vp "
        "   ,'Grand Average' as proposal "
        "from crunch_data "
        " group by 1 "
        "UNION ALL "
        "SELECT "
        "   percentage_voters_counted_stepped "
        "   ,percentage_voters_counted "
        "   ,cum_percentage_of_total_vp "
        "   ,proposals_id "
        "FROM crunch_data "
         ).df()

    @st.cache
    def convert_df(df):
        return df.to_csv().encode('utf-8')
    csv = convert_df(curve_data)
    st.download_button(
        "Press to download aggregate curve data",
        csv,
        "aggregated_data.csv",
        "text/csv",
        key='download-csv'
    )

    plt.rc("figure", figsize=(40, 20))
    #sns.set_style("whitegrid")
    plt.rc("font", size=25)
    data_means = crunch_data.groupby("percentage_voters_counted_stepped")["cum_percentage_of_total_vp","percentage_voters_counted"].agg("mean").reset_index()
    ##print(data_means)
    plot_title = spacename + ' snapshots % of vote along population with Average as X'

    fig = plt.figure(figsize=(30, 15))

    #plt.rc("figure", figsize=(40, 20))
    sns.set_style("whitegrid")
    plt.rc("font", size=25)
    data_means = crunch_data.groupby("percentage_voters_counted_stepped")[
        "cum_percentage_of_total_vp", "percentage_voters_counted"].agg("mean").reset_index()
    ##print(data_means)

    p50 = db.query("select min(percentage_voters_counted) "
                   "from data_means  where cum_percentage_of_total_vp>=0.5 ").df()
    p50_val = p50.iloc[0, 0]
    p50display = round(100 * (p50.iloc[0, 0]), 2)

    st.write('### On average, a proposal at ', ("{0}".format(spacename)), 'takes ', ("{0:.2%}".format(p50_val)),
             'of the voting population to accumulate half or more of all the votes.')

    st.write('### A total of ', ("{0}".format(leader_count)), 'addresses have driven the result of all proposals at',
             spacename, '.')
    st.write('### That\'s', ("{0:.2%}".format(elite)), 'of all', ("{0}".format(dao_members)),
             'voters the DAO has had in the last',("{0}".format(daysLimit)),'days.')

    st.write('### Let\'s visualize this: The chart below describes all proposals in', spacename,
             '.The orange markers represent what percentage of the population it takes to reach a given percentage of voting power.')

    plot_title = spacename + ' snapshots\' % of vote along population with Average as X'

    ax = sns.scatterplot(data=crunch_data, hue="proposals_id", y="cum_percentage_of_total_vp",
                         x="percentage_voters_counted_stepped").set(title=plot_title, xlabel='% of voters',
                                                                    ylabel='% of voting power')
    chart = sns.scatterplot(data=data_means, x="percentage_voters_counted_stepped", y="cum_percentage_of_total_vp",
                            zorder=3, s=800, marker='X', color='orange')
    plt.legend(bbox_to_anchor=(1.02, 0.99), loc='upper left', borderaxespad=0)
    st.pyplot(fig)

    voterCounts = db.query("Select"
                           " cast(startDate as date) as startDate "
                           ",count(distinct votes_voter) as voters "
                           "From crunch_data "
                           "Group by 1").df()

    #Second chart
    fig = plt.figure(figsize=(30, 15))
    #plt.rc("figure", figsize=(40, 20))
    sns.set_style("whitegrid")
    plt.rc("font", size=25)
    plot_title = spacename + ': Voters per proposal'
    chart = sns.barplot(data=voterCounts, x="startDate", y="voters", color='orange')
    st.pyplot(fig)


    st.markdown(
        '<p class="bigger-font">All done. Enjoy! Feel free to enter another space name to pull more data.</p>',
        unsafe_allow_html=True)
    # The chart above shows what % of all possible votes has been cast (Y axis) as each incremental percent of the voting population casts their vote (X axis). Each line is a Proposal and has a unique color, so that a dot on each percent point represents what % of total voting power was accumulated by that group. The color represents which vote was cast.
    # The Orange X shows the average % of power accumulated across all elections.


```


---

