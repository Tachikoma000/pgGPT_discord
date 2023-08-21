
#  Subgrounds  #

An intuitive python library for interfacing with Subgraphs.

##  Features  #

  * **Simple** : Leverage a Pythonic API to easily build queries and transformations without the need for raw GraphQL manipulation. 

  * **Automated** : Automatically handle pagination and schema introspection for effortless data retrieval. 

  * **Powerful** : Create sophisticated queries using the ` SyntheticFields  ` transformation system. 

* * *

###  Getting Started

Start using Subgrounds in 5 minutes!

[ ](getting_started/)

###  Advanced Topics

Learn how to conjure more complex queries

[ ](advanced_topics/)

###  Examples

Checkout our curated list of community examples

[ ](examples/)

###  FAQ

Quick answers to your most burning questions

[ ](faq/)

###  Tutorials

Links to our recorded video tutorials

[ ](videos/)

###  API Reference

Auto-generated docs from our codebase

[ ](api_reference/)

* * *

###  Changelog

Keep up with Subgrounds and the latest changes

[ ](changelog/)

###  Contributing

Learn how you can help improve Subgrounds!

[ ](contributing/)

* * *

[ Next  Getting Started  ](getting_started/) [ Previous  Deployment ID
](../api/reference/proxy/deployment_id/)

Made with [ Furo ](https://github.com/pradyunsg/furo)

[ ](https://github.com/0xPlaygrounds/subgrounds) [
](https://discord.gg/v4r4zhBAh2) [ ](https://twitter.com/Playgrounds0x)



Contents  Menu  Expand  Light mode  Dark mode  Auto light/dark mode

Hide navigation sidebar

Hide table of contents sidebar

Give us a ⭐️ on [ Github ](https://github.com/0xPlaygrounds/subgrounds)

Toggle site navigation sidebar

_ _

[ Playgrounds  ](../../)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

_ _

[ ![Light Logo](../../_static/assets/pg-logotype-dark.svg) ![Dark
Logo](../../_static/assets/pg-logotype-primary.svg)
](https://playgrounds.network)

Playgrounds API

  * [ Overview ](../../api/)
  * [ Getting an API Key ](../../api/key/)
  * [ Subgraph Proxy ](../../api/subgraph-proxy/)
  * [ Subgrounds Integration ](../../api/subgrounds/)
  * [ FAQ ](../../api/faq/)

Toggle child pages in navigation

_ _

    * [ What is a Query? ](../../api/faq/query/)
  * [ API Reference ](../../api/api-reference/)

Toggle child pages in navigation

_ _

    * [ Subgraph Proxy ](../../api/reference/proxy/)

Toggle child pages in navigation

_ _

      * [ Subgraph ID ](../../api/reference/proxy/subgraph_id/)
      * [ Deployment ID ](../../api/reference/proxy/deployment_id/)

Subgrounds

  * [ Overview ](../)
  * Getting Started 

Toggle child pages in navigation

_ _

    * [ The Basics ](basics/)
    * [ Field Paths ](field_paths/)

Toggle child pages in navigation

_ _

      * [ Arguments ](field_paths/arguments/)
      * [ Filtering ](field_paths/filtering/)
      * [ Sorting ](field_paths/sorting/)
      * [ Merging ](field_paths/merging/)
    * [ Querying ](querying/)

Toggle child pages in navigation

_ _

    * [ Synthetic Fields ](synthetic_fields/)
  * [ Advanced Topics ](../advanced_topics/)

Toggle child pages in navigation

_ _

    * [ Contrib ](../advanced_topics/contrib/)

Toggle child pages in navigation

_ _

      * [ Plotly ](../advanced_topics/contrib/plotly/)
    * [ Pagination ](../advanced_topics/pagination/)

Toggle child pages in navigation

_ _

      * [ Custom Strategies ](../advanced_topics/pagination/custom/)
  * [ FAQ ](../faq/)

Toggle child pages in navigation

_ _

    * [ Exporting to Disk ](../faq/exporting/)
    * [ Getting More Data ](../faq/more_data/)
    * [ Python Setup ](../faq/setup/)

Toggle child pages in navigation

_ _

      * [ Python Versioning ](../faq/setup/version_management/)
  * [ Examples ](../examples/)

Toggle child pages in navigation

_ _

    * [ Exchanges ](../examples/exchanges/)
    * [ Bridges ](../examples/bridges/)
    * [ Liquid Staking ](../examples/liquid_staking/)
    * [ Governance ](../examples/governance/)
    * [ Advanced Research ](../examples/advanced_research/)
    * [ Vaults ](../examples/vaults/)
  * [ Videos ](../videos/)
  * [ Changelog ](../changelog/)
  * [ Contributing ](../contributing/)
  * [ API Reference ](../api_reference/)

Toggle child pages in navigation

_ _

    * [ Top Level APIs ](../api_reference/top_level/)
    * [ Internal ](../api_reference/internal/)

Toggle child pages in navigation

_ _

      * [ Client ](../api_reference/internal/client/)

Toggle child pages in navigation

_ _

        * [ Base ](../api_reference/internal/client/base/)
        * [ Sync ](../api_reference/internal/client/sync/)
        * [ Async_ ](../api_reference/internal/client/async_/)
      * [ Contrib ](../api_reference/internal/contrib/)

Toggle child pages in navigation

_ _

        * [ Plotly ](../api_reference/internal/contrib/plotly/)
        * [ Dash ](../api_reference/internal/contrib/dash/)
      * [ Pagination ](../api_reference/internal/pagination/)

Toggle child pages in navigation

_ _

        * [ Strategies ](../api_reference/internal/pagination/strategies/)
        * [ Preprocess ](../api_reference/internal/pagination/preprocess/)
        * [ Pagination ](../api_reference/internal/pagination/pagination/)
        * [ Utils ](../api_reference/internal/pagination/utils/)
      * [ Transform ](../api_reference/internal/transform/)

Toggle child pages in navigation

_ _

        * [ ABCs ](../api_reference/internal/transform/abcs/)
        * [ Apply ](../api_reference/internal/transform/apply/)
        * [ Defaults ](../api_reference/internal/transform/defaults/)
        * [ Transforms ](../api_reference/internal/transform/transforms/)
        * [ Utils ](../api_reference/internal/transform/utils/)
      * [ Subgraph ](../api_reference/internal/subgraph/)

Toggle child pages in navigation

_ _

        * [ Fieldpath ](../api_reference/internal/subgraph/fieldpath/)
        * [ Filter ](../api_reference/internal/subgraph/filter/)
        * [ Object ](../api_reference/internal/subgraph/object/)
        * [ Subgraph ](../api_reference/internal/subgraph/subgraph/)
      * [ Errors ](../api_reference/internal/errors/)
      * [ Query ](../api_reference/internal/query/)
      * [ Schema ](../api_reference/internal/schema/)
      * [ Utils ](../api_reference/internal/utils/)

Meta

  * [ Improving the Docs ](../../meta/contributing/)

Back to top

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

_ _

#  Getting Started  #

##  Installation  #

Subgrounds can be installed via ` pip  ` with the following commands:

    
    
    pip install --upgrade subgrounds
    # or
    python -m pip install --upgrade subgrounds
    

Important

Subgrounds requires ` python  >=  3.10  ` .

You can check your version of python via: ` python  --version  `

Note

We recommend creating python environments to help manage your packages. These
help in ensuring your projects have the correct versions for the packages you
care about.

If you run into problems during installation, see [ Environment Setup
](../faq/setup/) .

##  Simple example  #

The following example grabs a subgraph for the Aave v2 protocol and queries
the top 5 markets ordered by TVL (total value locked), selects their name and
their TVL (in USD) and returns the data as a pandas [ ` DataFrame  `
](http://pandas.pydata.org/pandas-
docs/dev/reference/api/pandas.DataFrame.html#pandas.DataFrame "\(in pandas
v2.1.0.dev0+1421.g5f672dc704\)") .

    
    
    >>> from subgrounds import Subgrounds
    >>> 
    >>> sg = Subgrounds()
    >>> 
    >>> # Load
    >>> aave_v2 = sg.load_subgraph(
    ...     "https://api.thegraph.com/subgraphs/name/messari/aave-v2-ethereum")
    >>> 
    >>> # Construct the query
    >>> latest = aave_v2.Query.markets(
    ...     orderBy=aave_v2.Market.totalValueLockedUSD,
    ...     orderDirection='desc',
    ...     first=5,
    ... )
    >>> 
    >>> # Return query to a dataframe
    >>> sg.query_df([
    ...     latest.name,
    ...     latest.totalValueLockedUSD,
    ... ])
                      markets_name  markets_totalValueLockedUSD
    0  Aave interest bearing STETH                 1.338931e+09
    1   Aave interest bearing WETH                 8.387106e+08
    2   Aave interest bearing WBTC                 6.082906e+08
    3   Aave interest bearing USDC                 4.085144e+08
    4   Aave interest bearing USDT                 3.370399e+08
    

[ Next  The Basics  ](basics/) [ Previous  Subgrounds  ](../)

Made with [ Furo ](https://github.com/pradyunsg/furo)

[ ](https://github.com/0xPlaygrounds/subgrounds) [
](https://discord.gg/v4r4zhBAh2) [ ](https://twitter.com/Playgrounds0x)

On this page

  * Getting Started 
    * Installation 
    * Simple example 



Contents  Menu  Expand  Light mode  Dark mode  Auto light/dark mode

Hide navigation sidebar

Hide table of contents sidebar

Give us a ⭐️ on [ Github ](https://github.com/0xPlaygrounds/subgrounds)

Toggle site navigation sidebar

_ _

[ Playgrounds  ](../../../)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

_ _

[ ![Light Logo](../../../_static/assets/pg-logotype-dark.svg) ![Dark
Logo](../../../_static/assets/pg-logotype-primary.svg)
](https://playgrounds.network)

Playgrounds API

  * [ Overview ](../../../api/)
  * [ Getting an API Key ](../../../api/key/)
  * [ Subgraph Proxy ](../../../api/subgraph-proxy/)
  * [ Subgrounds Integration ](../../../api/subgrounds/)
  * [ FAQ ](../../../api/faq/)

Toggle child pages in navigation

_ _

    * [ What is a Query? ](../../../api/faq/query/)
  * [ API Reference ](../../../api/api-reference/)

Toggle child pages in navigation

_ _

    * [ Subgraph Proxy ](../../../api/reference/proxy/)

Toggle child pages in navigation

_ _

      * [ Subgraph ID ](../../../api/reference/proxy/subgraph_id/)
      * [ Deployment ID ](../../../api/reference/proxy/deployment_id/)

Subgrounds

  * [ Overview ](../../)
  * [ Getting Started ](../)

Toggle child pages in navigation

_ _

    * The Basics 
    * [ Field Paths ](../field_paths/)

Toggle child pages in navigation

_ _

      * [ Arguments ](../field_paths/arguments/)
      * [ Filtering ](../field_paths/filtering/)
      * [ Sorting ](../field_paths/sorting/)
      * [ Merging ](../field_paths/merging/)
    * [ Querying ](../querying/)

Toggle child pages in navigation

_ _

    * [ Synthetic Fields ](../synthetic_fields/)
  * [ Advanced Topics ](../../advanced_topics/)

Toggle child pages in navigation

_ _

    * [ Contrib ](../../advanced_topics/contrib/)

Toggle child pages in navigation

_ _

      * [ Plotly ](../../advanced_topics/contrib/plotly/)
    * [ Pagination ](../../advanced_topics/pagination/)

Toggle child pages in navigation

_ _

      * [ Custom Strategies ](../../advanced_topics/pagination/custom/)
  * [ FAQ ](../../faq/)

Toggle child pages in navigation

_ _

    * [ Exporting to Disk ](../../faq/exporting/)
    * [ Getting More Data ](../../faq/more_data/)
    * [ Python Setup ](../../faq/setup/)

Toggle child pages in navigation

_ _

      * [ Python Versioning ](../../faq/setup/version_management/)
  * [ Examples ](../../examples/)

Toggle child pages in navigation

_ _

    * [ Exchanges ](../../examples/exchanges/)
    * [ Bridges ](../../examples/bridges/)
    * [ Liquid Staking ](../../examples/liquid_staking/)
    * [ Governance ](../../examples/governance/)
    * [ Advanced Research ](../../examples/advanced_research/)
    * [ Vaults ](../../examples/vaults/)
  * [ Videos ](../../videos/)
  * [ Changelog ](../../changelog/)
  * [ Contributing ](../../contributing/)
  * [ API Reference ](../../api_reference/)

Toggle child pages in navigation

_ _

    * [ Top Level APIs ](../../api_reference/top_level/)
    * [ Internal ](../../api_reference/internal/)

Toggle child pages in navigation

_ _

      * [ Client ](../../api_reference/internal/client/)

Toggle child pages in navigation

_ _

        * [ Base ](../../api_reference/internal/client/base/)
        * [ Sync ](../../api_reference/internal/client/sync/)
        * [ Async_ ](../../api_reference/internal/client/async_/)
      * [ Contrib ](../../api_reference/internal/contrib/)

Toggle child pages in navigation

_ _

        * [ Plotly ](../../api_reference/internal/contrib/plotly/)
        * [ Dash ](../../api_reference/internal/contrib/dash/)
      * [ Pagination ](../../api_reference/internal/pagination/)

Toggle child pages in navigation

_ _

        * [ Strategies ](../../api_reference/internal/pagination/strategies/)
        * [ Preprocess ](../../api_reference/internal/pagination/preprocess/)
        * [ Pagination ](../../api_reference/internal/pagination/pagination/)
        * [ Utils ](../../api_reference/internal/pagination/utils/)
      * [ Transform ](../../api_reference/internal/transform/)

Toggle child pages in navigation

_ _

        * [ ABCs ](../../api_reference/internal/transform/abcs/)
        * [ Apply ](../../api_reference/internal/transform/apply/)
        * [ Defaults ](../../api_reference/internal/transform/defaults/)
        * [ Transforms ](../../api_reference/internal/transform/transforms/)
        * [ Utils ](../../api_reference/internal/transform/utils/)
      * [ Subgraph ](../../api_reference/internal/subgraph/)

Toggle child pages in navigation

_ _

        * [ Fieldpath ](../../api_reference/internal/subgraph/fieldpath/)
        * [ Filter ](../../api_reference/internal/subgraph/filter/)
        * [ Object ](../../api_reference/internal/subgraph/object/)
        * [ Subgraph ](../../api_reference/internal/subgraph/subgraph/)
      * [ Errors ](../../api_reference/internal/errors/)
      * [ Query ](../../api_reference/internal/query/)
      * [ Schema ](../../api_reference/internal/schema/)
      * [ Utils ](../../api_reference/internal/utils/)

Meta

  * [ Improving the Docs ](../../../meta/contributing/)

Back to top

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

_ _

#  The Basics  #

Important

This documentation is ✨ interactive ✨, allowing you to easily test and
experiment with subgrounds. By clicking the "Run Code" button below, a Python
server will be launched in the background using Jupyter Notebook. This will
give you access to a Python environment where you can execute and interact
with subgrounds code in real-time.

Each code block acts like a cell within a Jupyter notebook which means they
are **connected** . So [ ` Subgrounds  `
](../../api_reference/top_level/#subgrounds.Subgrounds
"subgrounds.Subgrounds") created in an earlier cell can be reused in lower
ones.

Once you click the "Run Code" button, the code cells will visually change with
3 new buttons:

Command

|

Description  
  
---|---  
  
Run

|

This executes the current cell  
  
Restart

|

This will restart the kernel  
  
Restart & Run All

|

This will restart the kernel and run every cell from top to bottom.  
  
The _easiest_ way to interact with the docs is via the "Restart & Run All"
button as it ensures that all the python state is loaded corrected. Then you
can feel free to edit a cell and click "Run" to play around as you please.

Run code

Warning

After you click "Run Code", interactivity will begin to hydrate the page and
**This takes time** . In some cases, you might need to refresh the page and
try again.

This feature is best used on the **latest** Chrome-based browsers, feel free
to report any issues on other browsers to our [ Discord
](https://discord.gg/v4r4zhBAh2) .

##  Subgrounds  #

The [ ` Subgrounds  ` ](../../api_reference/top_level/#subgrounds.Subgrounds
"subgrounds.Subgrounds") class provides the top level API and most users will
be using this class exclusively. This class is used to load (i.e.: introspect)
GraphQL APIs (subgraph **or** vanilla GraphQL APIs) as well as execute
querying operations. Moreover, this class is meant to be used as a singleton,
i.e.: initialized once and reused throughout a project.

The code cell below demonstrates how to initialize your [ ` Subgrounds  `
](../../api_reference/top_level/#subgrounds.Subgrounds
"subgrounds.Subgrounds") object and load a GraphQL API.

Note

Both [ ` load_subgraph  `
](../../api_reference/top_level/#subgrounds.Subgrounds.load_subgraph
"subgrounds.Subgrounds.load_subgraph") and [ ` load_api  `
](../../api_reference/top_level/#subgrounds.Subgrounds.load_api
"subgrounds.Subgrounds.load_api") result in similar structures except
subgraphs provide better optics since there's more schema data to explore.

Loading Aave v2 and snapshot api sources  #

    
    
    from subgrounds import Subgrounds
    
    # Initialize Subgrounds
    sg = Subgrounds()
    
    # Load a subgraph using its API URL
    aave_v2 = sg.load_subgraph(
        "https://api.thegraph.com/subgraphs/name/messari/aave-v2-ethereum")
    
    # Load a vanilla GraphQL API using its API URL
    snapshot = sg.load_api("https://hub.snapshot.org/graphql")
    

##  Getting the Data  #

Once you load in your subgraphs (or vanilla APIs), you can start gathering
data via [ ` query()  `
](../../api_reference/top_level/#subgrounds.Subgrounds.query
"subgrounds.Subgrounds.query") .

Gathering the names of the latest markets in Aave  #

    
    
    sg.query([
        aave_v2.Query.markets.name
    ])
    

Gathering the titles and scores of the latest proposals from snapshot  #

    
    
    sg.query([
        snapshot.Query.proposals.title,
        snapshot.Query.proposals.scores_total,
    ])
    

[ Next  Field Paths  ](../field_paths/) [ Previous  Getting Started  ](../)

Made with [ Furo ](https://github.com/pradyunsg/furo)

[ ](https://github.com/0xPlaygrounds/subgrounds) [
](https://discord.gg/v4r4zhBAh2) [ ](https://twitter.com/Playgrounds0x)

On this page

  * The Basics 
    * Subgrounds 
    * Getting the Data 



Contents  Menu  Expand  Light mode  Dark mode  Auto light/dark mode

Hide navigation sidebar

Hide table of contents sidebar

Give us a ⭐️ on [ Github ](https://github.com/0xPlaygrounds/subgrounds)

Toggle site navigation sidebar

_ _

[ Playgrounds  ](../../../)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

_ _

[ ![Light Logo](../../../_static/assets/pg-logotype-dark.svg) ![Dark
Logo](../../../_static/assets/pg-logotype-primary.svg)
](https://playgrounds.network)

Playgrounds API

  * [ Overview ](../../../api/)
  * [ Getting an API Key ](../../../api/key/)
  * [ Subgraph Proxy ](../../../api/subgraph-proxy/)
  * [ Subgrounds Integration ](../../../api/subgrounds/)
  * [ FAQ ](../../../api/faq/)

Toggle child pages in navigation

_ _

    * [ What is a Query? ](../../../api/faq/query/)
  * [ API Reference ](../../../api/api-reference/)

Toggle child pages in navigation

_ _

    * [ Subgraph Proxy ](../../../api/reference/proxy/)

Toggle child pages in navigation

_ _

      * [ Subgraph ID ](../../../api/reference/proxy/subgraph_id/)
      * [ Deployment ID ](../../../api/reference/proxy/deployment_id/)

Subgrounds

  * [ Overview ](../../)
  * [ Getting Started ](../)

Toggle child pages in navigation

_ _

    * [ The Basics ](../basics/)
    * Field Paths 

Toggle child pages in navigation

_ _

      * [ Arguments ](arguments/)
      * [ Filtering ](filtering/)
      * [ Sorting ](sorting/)
      * [ Merging ](merging/)
    * [ Querying ](../querying/)

Toggle child pages in navigation

_ _

    * [ Synthetic Fields ](../synthetic_fields/)
  * [ Advanced Topics ](../../advanced_topics/)

Toggle child pages in navigation

_ _

    * [ Contrib ](../../advanced_topics/contrib/)

Toggle child pages in navigation

_ _

      * [ Plotly ](../../advanced_topics/contrib/plotly/)
    * [ Pagination ](../../advanced_topics/pagination/)

Toggle child pages in navigation

_ _

      * [ Custom Strategies ](../../advanced_topics/pagination/custom/)
  * [ FAQ ](../../faq/)

Toggle child pages in navigation

_ _

    * [ Exporting to Disk ](../../faq/exporting/)
    * [ Getting More Data ](../../faq/more_data/)
    * [ Python Setup ](../../faq/setup/)

Toggle child pages in navigation

_ _

      * [ Python Versioning ](../../faq/setup/version_management/)
  * [ Examples ](../../examples/)

Toggle child pages in navigation

_ _

    * [ Exchanges ](../../examples/exchanges/)
    * [ Bridges ](../../examples/bridges/)
    * [ Liquid Staking ](../../examples/liquid_staking/)
    * [ Governance ](../../examples/governance/)
    * [ Advanced Research ](../../examples/advanced_research/)
    * [ Vaults ](../../examples/vaults/)
  * [ Videos ](../../videos/)
  * [ Changelog ](../../changelog/)
  * [ Contributing ](../../contributing/)
  * [ API Reference ](../../api_reference/)

Toggle child pages in navigation

_ _

    * [ Top Level APIs ](../../api_reference/top_level/)
    * [ Internal ](../../api_reference/internal/)

Toggle child pages in navigation

_ _

      * [ Client ](../../api_reference/internal/client/)

Toggle child pages in navigation

_ _

        * [ Base ](../../api_reference/internal/client/base/)
        * [ Sync ](../../api_reference/internal/client/sync/)
        * [ Async_ ](../../api_reference/internal/client/async_/)
      * [ Contrib ](../../api_reference/internal/contrib/)

Toggle child pages in navigation

_ _

        * [ Plotly ](../../api_reference/internal/contrib/plotly/)
        * [ Dash ](../../api_reference/internal/contrib/dash/)
      * [ Pagination ](../../api_reference/internal/pagination/)

Toggle child pages in navigation

_ _

        * [ Strategies ](../../api_reference/internal/pagination/strategies/)
        * [ Preprocess ](../../api_reference/internal/pagination/preprocess/)
        * [ Pagination ](../../api_reference/internal/pagination/pagination/)
        * [ Utils ](../../api_reference/internal/pagination/utils/)
      * [ Transform ](../../api_reference/internal/transform/)

Toggle child pages in navigation

_ _

        * [ ABCs ](../../api_reference/internal/transform/abcs/)
        * [ Apply ](../../api_reference/internal/transform/apply/)
        * [ Defaults ](../../api_reference/internal/transform/defaults/)
        * [ Transforms ](../../api_reference/internal/transform/transforms/)
        * [ Utils ](../../api_reference/internal/transform/utils/)
      * [ Subgraph ](../../api_reference/internal/subgraph/)

Toggle child pages in navigation

_ _

        * [ Fieldpath ](../../api_reference/internal/subgraph/fieldpath/)
        * [ Filter ](../../api_reference/internal/subgraph/filter/)
        * [ Object ](../../api_reference/internal/subgraph/object/)
        * [ Subgraph ](../../api_reference/internal/subgraph/subgraph/)
      * [ Errors ](../../api_reference/internal/errors/)
      * [ Query ](../../api_reference/internal/query/)
      * [ Schema ](../../api_reference/internal/schema/)
      * [ Utils ](../../api_reference/internal/utils/)

Meta

  * [ Improving the Docs ](../../../meta/contributing/)

Back to top

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

_ _

#  Field Paths  #

[ ` FieldPaths  ` ](../../api_reference/top_level/#subgrounds.FieldPath
"subgrounds.FieldPath") are the main building blocks used to construct
Subgrounds queries. A [ ` FieldPath  `
](../../api_reference/top_level/#subgrounds.FieldPath "subgrounds.FieldPath")
represents a selection path through a GraphQL schema starting from the root `
Query  ` entity (see [ The Query and Mutation types
](https://graphql.org/learn/schema/#the-query-and-mutation-types) ) all the
way down to a scalar leaf.

[ ` FieldPath  ` ](../../api_reference/top_level/#subgrounds.FieldPath
"subgrounds.FieldPath") are created by simply selecting attributes starting
from the subgraph object returned by the [ ` load_subgraph  `
](../../api_reference/top_level/#subgrounds.Subgrounds.load_subgraph
"subgrounds.Subgrounds.load_subgraph") or [ ` load_api  `
](../../api_reference/top_level/#subgrounds.Subgrounds.load_api
"subgrounds.Subgrounds.load_api") methods:

Click for Interactive Documentation

Clicking this button will enable editing and execution of the code-blocks on
this page. Learn more [ here  ](../basics/) .

Run code

Loading a curve subgraph  #

    
    
    from subgrounds import Subgrounds
    sg = Subgrounds()
    
    curve = sg.load_subgraph(
        "https://api.thegraph.com/subgraphs/name/messari/curve-finance-ethereum")
    

Python

Analyzing curve pool data via the ` curve.Query.pools  ` [ ` FieldPath  `
](../../api_reference/top_level/#subgrounds.FieldPath "subgrounds.FieldPath")
#

    
    
    # `curve.Query.pools` is a field path
    curve_pools = curve.Query.liquidityPools
    
    # We can then query based on the routing of these objects
    sg.query_df([
        curve_pools.inputTokens.name,
        curve_pools.outputToken.name,
    ])
    

GraphQL

This is the GraphQL that subgrounds produces  #

    
    
    query {
      liquidityPools {
        inputTokens {
          name
        }
        outputToken {
          name
        }
      }
    }
    

Note

If you're having trouble understanding the naming and pathing of the [ `
FieldPath  ` ](../../api_reference/top_level/#subgrounds.FieldPath
"subgrounds.FieldPath") classes in subgrounds, we recommend:

  * **Use the[ Graph _i_ QL ](https://api.thegraph.com/subgraphs/name/messari/curve-finance-ethereum) Interface: **

    * Copy and paste the subgraph URL into your web browser to access the [ Graph _i_ QL ](https://api.thegraph.com/subgraphs/name/messari/curve-finance-ethereum) interface. 

    * This tool allows you to build a GraphQL string via the graphical query builder, which can help you understand the structure of the subgraph. 

  * **Leverage IDE Language Support:**

    * If you use an IDE with Jupyter Notebook support (i.e. VSCode), you can take advantage of the built-in language server to auto-complete the field paths as you work. 

    * To use this method, import and load the subgraph in the first notebook cell, then use it in later cells to benefit from auto-completion suggestions based on the schema. 

    * This feature is particularly easy to use in VSCode, as the included Python extension automatically enables this behavior. 

[ Next  Arguments  ](arguments/) [ Previous  The Basics  ](../basics/)

Made with [ Furo ](https://github.com/pradyunsg/furo)

[ ](https://github.com/0xPlaygrounds/subgrounds) [
](https://discord.gg/v4r4zhBAh2) [ ](https://twitter.com/Playgrounds0x)



Contents  Menu  Expand  Light mode  Dark mode  Auto light/dark mode

Hide navigation sidebar

Hide table of contents sidebar

Give us a ⭐️ on [ Github ](https://github.com/0xPlaygrounds/subgrounds)

Toggle site navigation sidebar

_ _

[ Playgrounds  ](../../../../)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

_ _

[ ![Light Logo](../../../../_static/assets/pg-logotype-dark.svg) ![Dark
Logo](../../../../_static/assets/pg-logotype-primary.svg)
](https://playgrounds.network)

Playgrounds API

  * [ Overview ](../../../../api/)
  * [ Getting an API Key ](../../../../api/key/)
  * [ Subgraph Proxy ](../../../../api/subgraph-proxy/)
  * [ Subgrounds Integration ](../../../../api/subgrounds/)
  * [ FAQ ](../../../../api/faq/)

Toggle child pages in navigation

_ _

    * [ What is a Query? ](../../../../api/faq/query/)
  * [ API Reference ](../../../../api/api-reference/)

Toggle child pages in navigation

_ _

    * [ Subgraph Proxy ](../../../../api/reference/proxy/)

Toggle child pages in navigation

_ _

      * [ Subgraph ID ](../../../../api/reference/proxy/subgraph_id/)
      * [ Deployment ID ](../../../../api/reference/proxy/deployment_id/)

Subgrounds

  * [ Overview ](../../../)
  * [ Getting Started ](../../)

Toggle child pages in navigation

_ _

    * [ The Basics ](../../basics/)
    * [ Field Paths ](../)

Toggle child pages in navigation

_ _

      * Arguments 
      * [ Filtering ](../filtering/)
      * [ Sorting ](../sorting/)
      * [ Merging ](../merging/)
    * [ Querying ](../../querying/)

Toggle child pages in navigation

_ _

    * [ Synthetic Fields ](../../synthetic_fields/)
  * [ Advanced Topics ](../../../advanced_topics/)

Toggle child pages in navigation

_ _

    * [ Contrib ](../../../advanced_topics/contrib/)

Toggle child pages in navigation

_ _

      * [ Plotly ](../../../advanced_topics/contrib/plotly/)
    * [ Pagination ](../../../advanced_topics/pagination/)

Toggle child pages in navigation

_ _

      * [ Custom Strategies ](../../../advanced_topics/pagination/custom/)
  * [ FAQ ](../../../faq/)

Toggle child pages in navigation

_ _

    * [ Exporting to Disk ](../../../faq/exporting/)
    * [ Getting More Data ](../../../faq/more_data/)
    * [ Python Setup ](../../../faq/setup/)

Toggle child pages in navigation

_ _

      * [ Python Versioning ](../../../faq/setup/version_management/)
  * [ Examples ](../../../examples/)

Toggle child pages in navigation

_ _

    * [ Exchanges ](../../../examples/exchanges/)
    * [ Bridges ](../../../examples/bridges/)
    * [ Liquid Staking ](../../../examples/liquid_staking/)
    * [ Governance ](../../../examples/governance/)
    * [ Advanced Research ](../../../examples/advanced_research/)
    * [ Vaults ](../../../examples/vaults/)
  * [ Videos ](../../../videos/)
  * [ Changelog ](../../../changelog/)
  * [ Contributing ](../../../contributing/)
  * [ API Reference ](../../../api_reference/)

Toggle child pages in navigation

_ _

    * [ Top Level APIs ](../../../api_reference/top_level/)
    * [ Internal ](../../../api_reference/internal/)

Toggle child pages in navigation

_ _

      * [ Client ](../../../api_reference/internal/client/)

Toggle child pages in navigation

_ _

        * [ Base ](../../../api_reference/internal/client/base/)
        * [ Sync ](../../../api_reference/internal/client/sync/)
        * [ Async_ ](../../../api_reference/internal/client/async_/)
      * [ Contrib ](../../../api_reference/internal/contrib/)

Toggle child pages in navigation

_ _

        * [ Plotly ](../../../api_reference/internal/contrib/plotly/)
        * [ Dash ](../../../api_reference/internal/contrib/dash/)
      * [ Pagination ](../../../api_reference/internal/pagination/)

Toggle child pages in navigation

_ _

        * [ Strategies ](../../../api_reference/internal/pagination/strategies/)
        * [ Preprocess ](../../../api_reference/internal/pagination/preprocess/)
        * [ Pagination ](../../../api_reference/internal/pagination/pagination/)
        * [ Utils ](../../../api_reference/internal/pagination/utils/)
      * [ Transform ](../../../api_reference/internal/transform/)

Toggle child pages in navigation

_ _

        * [ ABCs ](../../../api_reference/internal/transform/abcs/)
        * [ Apply ](../../../api_reference/internal/transform/apply/)
        * [ Defaults ](../../../api_reference/internal/transform/defaults/)
        * [ Transforms ](../../../api_reference/internal/transform/transforms/)
        * [ Utils ](../../../api_reference/internal/transform/utils/)
      * [ Subgraph ](../../../api_reference/internal/subgraph/)

Toggle child pages in navigation

_ _

        * [ Fieldpath ](../../../api_reference/internal/subgraph/fieldpath/)
        * [ Filter ](../../../api_reference/internal/subgraph/filter/)
        * [ Object ](../../../api_reference/internal/subgraph/object/)
        * [ Subgraph ](../../../api_reference/internal/subgraph/subgraph/)
      * [ Errors ](../../../api_reference/internal/errors/)
      * [ Query ](../../../api_reference/internal/query/)
      * [ Schema ](../../../api_reference/internal/schema/)
      * [ Utils ](../../../api_reference/internal/utils/)

Meta

  * [ Improving the Docs ](../../../../meta/contributing/)

Back to top

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

_ _

#  Arguments  #

Some [ ` FieldPaths  `
](../../../api_reference/top_level/#subgrounds.FieldPath
"subgrounds.FieldPath") can be parameterized with certain arguments such as
specific token ids, sorting by certain fields, etc. These arguments can be
configured by "calling" said function (e.g. ` aave_v2.Query.market(first=10)
` ).

Click for Interactive Documentation

Clicking this button will enable editing and execution of the code-blocks on
this page. Learn more [ here  ](../../basics/) .

Run code

Loading a curve subgraph  #

    
    
    from subgrounds import Subgrounds
    sg = Subgrounds()
    
    curve = sg.load_subgraph(
        "https://api.thegraph.com/subgraphs/name/messari/curve-finance-ethereum")
    

Python

Analyzing curve pool data via the ` curve.Query.pools  ` [ ` FieldPath  `
](../../../api_reference/top_level/#subgrounds.FieldPath
"subgrounds.FieldPath") #

    
    
    # `curve.Query.pools` is a field path
    #  we "call it to add arguments!
    curve_pools = curve.Query.liquidityPools(
        first=10,
        orderBy=curve.LiquidityPool.totalValueLockedUSD,
        orderDirection="desc",
        where=[
            curve.LiquidityPool.createdBlockNumber > 14720000
        ]
    )
    
    # We can then query based on the routing of these objects
    sg.query_df([
        curve_pools.outputToken.name,
        curve_pools.totalValueLockedUSD,
    ])
    

GraphQL

Analyzing curve pool data via the ` curve.Query.pools  ` [ ` FieldPath  `
](../../../api_reference/top_level/#subgrounds.FieldPath
"subgrounds.FieldPath") #

    
    
    query {
      liquidityPools(
        first: 10
        orderBy: totalValueLockedUSD
        orderDirection: desc
        where: {createdBlockNumber_gt: 14720000}
      ) {
        outputToken{
          name
        }
        totalValueLockedUSD
      }
    }
    

Note

Notice that the values for the ` orderBy  ` and ` where  ` arguments are [ `
FieldPath  ` ](../../../api_reference/top_level/#subgrounds.FieldPath
"subgrounds.FieldPath") themselves. This allows users to construct complex
queries in pure Python by using the [ ` Subgraph  `
](../../../api_reference/top_level/#subgrounds.Subgraph "subgrounds.Subgraph")
object returned when loading an API.

The [ ` FieldPaths  ` ](../../../api_reference/top_level/#subgrounds.FieldPath
"subgrounds.FieldPath") _here_ are used as in their relative form, i.e.: they
do not start from the root ` Query  ` entity, but rather start from an entity
type (in this case the ` Pool  ` entity).

Warning

It is important to make sure that the relative [ ` FieldPath  `
](../../../api_reference/top_level/#subgrounds.FieldPath
"subgrounds.FieldPath") used as values for the ` orderBy  ` and ` where  `
arguments match the entity type of the field on which the arguments are
applied (in our example, the ` pools  ` field is of type ` Pool  ` ). If this
is not respected, a type error exception will be thrown.

Argument values can _also_ be supplied in their "raw" form, without the use of
relative [ ` FieldPaths  `
](../../../api_reference/top_level/#subgrounds.FieldPath
"subgrounds.FieldPath") :

Raw Form

    
    
    curve_pools = curve.Query.liquidityPools(
        first=10,
        orderBy="totalValueLockedUSD",
        orderDirection="desc",
        where={
            "createdBlockNumber_gt": 14720000
        }
    )
    

Relative Form

    
    
    curve_pools = curve.Query.liquidityPools(
        first=10,
        orderBy=curve.LiquidityPool.totalValueLockedUSD,
        orderDirection="desc",
        where=[
            curve.LiquidityPool.createdBlockNumber > 14720000
        ]
    )
    

Warning

When using raw form instead of relative form, you lose out on any type
validation. This means, errors will only surface when using ` query  ` rather
than surfacing when building the [ ` FieldPaths  `
](../../../api_reference/top_level/#subgrounds.FieldPath
"subgrounds.FieldPath") .

We **highly** recommend sticking with relative form, even if it seems more
verbose!

[ Next  Filtering  ](../filtering/) [ Previous  Field Paths  ](../)

Made with [ Furo ](https://github.com/pradyunsg/furo)

[ ](https://github.com/0xPlaygrounds/subgrounds) [
](https://discord.gg/v4r4zhBAh2) [ ](https://twitter.com/Playgrounds0x)



Contents  Menu  Expand  Light mode  Dark mode  Auto light/dark mode

Hide navigation sidebar

Hide table of contents sidebar

Give us a ⭐️ on [ Github ](https://github.com/0xPlaygrounds/subgrounds)

Toggle site navigation sidebar

_ _

[ Playgrounds  ](../../../../)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

_ _

[ ![Light Logo](../../../../_static/assets/pg-logotype-dark.svg) ![Dark
Logo](../../../../_static/assets/pg-logotype-primary.svg)
](https://playgrounds.network)

Playgrounds API

  * [ Overview ](../../../../api/)
  * [ Getting an API Key ](../../../../api/key/)
  * [ Subgraph Proxy ](../../../../api/subgraph-proxy/)
  * [ Subgrounds Integration ](../../../../api/subgrounds/)
  * [ FAQ ](../../../../api/faq/)

Toggle child pages in navigation

_ _

    * [ What is a Query? ](../../../../api/faq/query/)
  * [ API Reference ](../../../../api/api-reference/)

Toggle child pages in navigation

_ _

    * [ Subgraph Proxy ](../../../../api/reference/proxy/)

Toggle child pages in navigation

_ _

      * [ Subgraph ID ](../../../../api/reference/proxy/subgraph_id/)
      * [ Deployment ID ](../../../../api/reference/proxy/deployment_id/)

Subgrounds

  * [ Overview ](../../../)
  * [ Getting Started ](../../)

Toggle child pages in navigation

_ _

    * [ The Basics ](../../basics/)
    * [ Field Paths ](../)

Toggle child pages in navigation

_ _

      * [ Arguments ](../arguments/)
      * Filtering 
      * [ Sorting ](../sorting/)
      * [ Merging ](../merging/)
    * [ Querying ](../../querying/)

Toggle child pages in navigation

_ _

    * [ Synthetic Fields ](../../synthetic_fields/)
  * [ Advanced Topics ](../../../advanced_topics/)

Toggle child pages in navigation

_ _

    * [ Contrib ](../../../advanced_topics/contrib/)

Toggle child pages in navigation

_ _

      * [ Plotly ](../../../advanced_topics/contrib/plotly/)
    * [ Pagination ](../../../advanced_topics/pagination/)

Toggle child pages in navigation

_ _

      * [ Custom Strategies ](../../../advanced_topics/pagination/custom/)
  * [ FAQ ](../../../faq/)

Toggle child pages in navigation

_ _

    * [ Exporting to Disk ](../../../faq/exporting/)
    * [ Getting More Data ](../../../faq/more_data/)
    * [ Python Setup ](../../../faq/setup/)

Toggle child pages in navigation

_ _

      * [ Python Versioning ](../../../faq/setup/version_management/)
  * [ Examples ](../../../examples/)

Toggle child pages in navigation

_ _

    * [ Exchanges ](../../../examples/exchanges/)
    * [ Bridges ](../../../examples/bridges/)
    * [ Liquid Staking ](../../../examples/liquid_staking/)
    * [ Governance ](../../../examples/governance/)
    * [ Advanced Research ](../../../examples/advanced_research/)
    * [ Vaults ](../../../examples/vaults/)
  * [ Videos ](../../../videos/)
  * [ Changelog ](../../../changelog/)
  * [ Contributing ](../../../contributing/)
  * [ API Reference ](../../../api_reference/)

Toggle child pages in navigation

_ _

    * [ Top Level APIs ](../../../api_reference/top_level/)
    * [ Internal ](../../../api_reference/internal/)

Toggle child pages in navigation

_ _

      * [ Client ](../../../api_reference/internal/client/)

Toggle child pages in navigation

_ _

        * [ Base ](../../../api_reference/internal/client/base/)
        * [ Sync ](../../../api_reference/internal/client/sync/)
        * [ Async_ ](../../../api_reference/internal/client/async_/)
      * [ Contrib ](../../../api_reference/internal/contrib/)

Toggle child pages in navigation

_ _

        * [ Plotly ](../../../api_reference/internal/contrib/plotly/)
        * [ Dash ](../../../api_reference/internal/contrib/dash/)
      * [ Pagination ](../../../api_reference/internal/pagination/)

Toggle child pages in navigation

_ _

        * [ Strategies ](../../../api_reference/internal/pagination/strategies/)
        * [ Preprocess ](../../../api_reference/internal/pagination/preprocess/)
        * [ Pagination ](../../../api_reference/internal/pagination/pagination/)
        * [ Utils ](../../../api_reference/internal/pagination/utils/)
      * [ Transform ](../../../api_reference/internal/transform/)

Toggle child pages in navigation

_ _

        * [ ABCs ](../../../api_reference/internal/transform/abcs/)
        * [ Apply ](../../../api_reference/internal/transform/apply/)
        * [ Defaults ](../../../api_reference/internal/transform/defaults/)
        * [ Transforms ](../../../api_reference/internal/transform/transforms/)
        * [ Utils ](../../../api_reference/internal/transform/utils/)
      * [ Subgraph ](../../../api_reference/internal/subgraph/)

Toggle child pages in navigation

_ _

        * [ Fieldpath ](../../../api_reference/internal/subgraph/fieldpath/)
        * [ Filter ](../../../api_reference/internal/subgraph/filter/)
        * [ Object ](../../../api_reference/internal/subgraph/object/)
        * [ Subgraph ](../../../api_reference/internal/subgraph/subgraph/)
      * [ Errors ](../../../api_reference/internal/errors/)
      * [ Query ](../../../api_reference/internal/query/)
      * [ Schema ](../../../api_reference/internal/schema/)
      * [ Utils ](../../../api_reference/internal/utils/)

Meta

  * [ Improving the Docs ](../../../../meta/contributing/)

Back to top

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

_ _

#  Filtering  #

Filtering subgraphs in ` subgrounds  ` is done via the ` where  ` argument in
[ ` FieldPath  ` ](../../../api_reference/top_level/#subgrounds.FieldPath
"subgrounds.FieldPath") . A subgraph's GraphQL provides several options to
filter based on nearly any field path.

Click for Interactive Documentation

Clicking this button will enable editing and execution of the code-blocks on
this page. Learn more [ here  ](../../basics/) .

Run code

We will be using curve as the base subgraph for the following examples  #

    
    
    from subgrounds import Subgrounds
    
    sg = Subgrounds()
    
    curve = sg.load_subgraph(
        "https://api.thegraph.com/subgraphs/name/messari/curve-finance-ethereum")
    
    pool = curve.LiquidityPool  # shorthand for examples
    

Note

In some of the following examples, multiple conditions are stacked on top of
each other. This would **not** result in any data being returned since the
multiple conditions would likely conflict with each other.

##  Matching Values  #

Using the ` ==  ` and ` =!  ` operators in Python, matching exact or negated
values on field paths is pretty straight forward:

Relative Form

    
    
    sg.query_df(
        curve.Query.liquidityPools(
            where=[
                isSingleSided == False,
                # or
                isSingleSided != True,
            ]
        )
    )
    

Raw Form

    
    
    sg.query_df(
        curve.Query.liquidityPools(
            where={
                "isSingleSided": False,
                # or
                "isSingleSided_not": False,
            }
        )
    )
    

##  Comparisons  #

Filtering can also be based on standard comparison logic on any field path,
such as "greater than", "less than", etc — generally more useful for numeric
fields.

Relative Form

    
    
    sg.query_df(
        curve.Query.liquidityPools(
            where=[
                pool.cumulativeVolumeUSD > 150000000,
                pool.cumulativeVolumeUSD >= 150000000,
                pool.cumulativeVolumeUSD < 150000000,
                pool.cumulativeVolumeUSD <= 150000000,
            ]
        )
    )
    

Raw Form

    
    
    sg.query_df(
        curve.Query.liquidityPools(
            where={
                "cumulativeVolumeUSD_gt": 150000000,
                "cumulativeVolumeUSD_gte": 150000000,
                "cumulativeVolumeUSD_lt": 150000000,
                "cumulativeVolumeUSD_lte": 150000000,
            }
        )
    )
    

##  Nested Filtering  #

Entities can have any layer of nestable objects which thereby are **also**
filterable in the ` where  ` clause:

Relative Form

    
    
    sg.query_df(
        curve.Query.liquidityPools(
            where=[
                pool.hourlySnapshots.hourlyVolumeUSD > 1000
            ]
        )
    )
    

Raw Form

    
    
    sg.query_df(
        curve.Query.liquidityPools(
            where={
                "hourlySnapshots_": {"hourlyVolumeUSD_gt": 14720000}
            }
        )
    )
    

Note

The trailing ` _  ` prefix is needed in the GraphQL form since without it,
GraphQL assumes you are matching the exact value!

[ Next  Sorting  ](../sorting/) [ Previous  Arguments  ](../arguments/)

Made with [ Furo ](https://github.com/pradyunsg/furo)

[ ](https://github.com/0xPlaygrounds/subgrounds) [
](https://discord.gg/v4r4zhBAh2) [ ](https://twitter.com/Playgrounds0x)

On this page

  * Filtering 
    * Matching Values 
    * Comparisons 
    * Nested Filtering 



Contents  Menu  Expand  Light mode  Dark mode  Auto light/dark mode

Hide navigation sidebar

Hide table of contents sidebar

Give us a ⭐️ on [ Github ](https://github.com/0xPlaygrounds/subgrounds)

Toggle site navigation sidebar

_ _

[ Playgrounds  ](../../../../)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

_ _

[ ![Light Logo](../../../../_static/assets/pg-logotype-dark.svg) ![Dark
Logo](../../../../_static/assets/pg-logotype-primary.svg)
](https://playgrounds.network)

Playgrounds API

  * [ Overview ](../../../../api/)
  * [ Getting an API Key ](../../../../api/key/)
  * [ Subgraph Proxy ](../../../../api/subgraph-proxy/)
  * [ Subgrounds Integration ](../../../../api/subgrounds/)
  * [ FAQ ](../../../../api/faq/)

Toggle child pages in navigation

_ _

    * [ What is a Query? ](../../../../api/faq/query/)
  * [ API Reference ](../../../../api/api-reference/)

Toggle child pages in navigation

_ _

    * [ Subgraph Proxy ](../../../../api/reference/proxy/)

Toggle child pages in navigation

_ _

      * [ Subgraph ID ](../../../../api/reference/proxy/subgraph_id/)
      * [ Deployment ID ](../../../../api/reference/proxy/deployment_id/)

Subgrounds

  * [ Overview ](../../../)
  * [ Getting Started ](../../)

Toggle child pages in navigation

_ _

    * [ The Basics ](../../basics/)
    * [ Field Paths ](../)

Toggle child pages in navigation

_ _

      * [ Arguments ](../arguments/)
      * [ Filtering ](../filtering/)
      * Sorting 
      * [ Merging ](../merging/)
    * [ Querying ](../../querying/)

Toggle child pages in navigation

_ _

    * [ Synthetic Fields ](../../synthetic_fields/)
  * [ Advanced Topics ](../../../advanced_topics/)

Toggle child pages in navigation

_ _

    * [ Contrib ](../../../advanced_topics/contrib/)

Toggle child pages in navigation

_ _

      * [ Plotly ](../../../advanced_topics/contrib/plotly/)
    * [ Pagination ](../../../advanced_topics/pagination/)

Toggle child pages in navigation

_ _

      * [ Custom Strategies ](../../../advanced_topics/pagination/custom/)
  * [ FAQ ](../../../faq/)

Toggle child pages in navigation

_ _

    * [ Exporting to Disk ](../../../faq/exporting/)
    * [ Getting More Data ](../../../faq/more_data/)
    * [ Python Setup ](../../../faq/setup/)

Toggle child pages in navigation

_ _

      * [ Python Versioning ](../../../faq/setup/version_management/)
  * [ Examples ](../../../examples/)

Toggle child pages in navigation

_ _

    * [ Exchanges ](../../../examples/exchanges/)
    * [ Bridges ](../../../examples/bridges/)
    * [ Liquid Staking ](../../../examples/liquid_staking/)
    * [ Governance ](../../../examples/governance/)
    * [ Advanced Research ](../../../examples/advanced_research/)
    * [ Vaults ](../../../examples/vaults/)
  * [ Videos ](../../../videos/)
  * [ Changelog ](../../../changelog/)
  * [ Contributing ](../../../contributing/)
  * [ API Reference ](../../../api_reference/)

Toggle child pages in navigation

_ _

    * [ Top Level APIs ](../../../api_reference/top_level/)
    * [ Internal ](../../../api_reference/internal/)

Toggle child pages in navigation

_ _

      * [ Client ](../../../api_reference/internal/client/)

Toggle child pages in navigation

_ _

        * [ Base ](../../../api_reference/internal/client/base/)
        * [ Sync ](../../../api_reference/internal/client/sync/)
        * [ Async_ ](../../../api_reference/internal/client/async_/)
      * [ Contrib ](../../../api_reference/internal/contrib/)

Toggle child pages in navigation

_ _

        * [ Plotly ](../../../api_reference/internal/contrib/plotly/)
        * [ Dash ](../../../api_reference/internal/contrib/dash/)
      * [ Pagination ](../../../api_reference/internal/pagination/)

Toggle child pages in navigation

_ _

        * [ Strategies ](../../../api_reference/internal/pagination/strategies/)
        * [ Preprocess ](../../../api_reference/internal/pagination/preprocess/)
        * [ Pagination ](../../../api_reference/internal/pagination/pagination/)
        * [ Utils ](../../../api_reference/internal/pagination/utils/)
      * [ Transform ](../../../api_reference/internal/transform/)

Toggle child pages in navigation

_ _

        * [ ABCs ](../../../api_reference/internal/transform/abcs/)
        * [ Apply ](../../../api_reference/internal/transform/apply/)
        * [ Defaults ](../../../api_reference/internal/transform/defaults/)
        * [ Transforms ](../../../api_reference/internal/transform/transforms/)
        * [ Utils ](../../../api_reference/internal/transform/utils/)
      * [ Subgraph ](../../../api_reference/internal/subgraph/)

Toggle child pages in navigation

_ _

        * [ Fieldpath ](../../../api_reference/internal/subgraph/fieldpath/)
        * [ Filter ](../../../api_reference/internal/subgraph/filter/)
        * [ Object ](../../../api_reference/internal/subgraph/object/)
        * [ Subgraph ](../../../api_reference/internal/subgraph/subgraph/)
      * [ Errors ](../../../api_reference/internal/errors/)
      * [ Query ](../../../api_reference/internal/query/)
      * [ Schema ](../../../api_reference/internal/schema/)
      * [ Utils ](../../../api_reference/internal/utils/)

Meta

  * [ Improving the Docs ](../../../../meta/contributing/)

Back to top

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

_ _

#  Sorting  #

Data can also be queried based on specific sort of a field path. This can be
helpful if you want get data such as the top performing pools based on
revenue, etc.

Click for Interactive Documentation

Clicking this button will enable editing and execution of the code-blocks on
this page. Learn more [ here  ](../../basics/) .

Run code

We will be using curve as the base subgraph for the following examples  #

    
    
    from subgrounds import Subgrounds
    
    sg = Subgrounds()
    
    curve = sg.load_subgraph(
        "https://api.thegraph.com/subgraphs/name/messari/curve-finance-ethereum")
    
    pool = curve.LiquidtyPool  # shorthand for examples
    snapshot = curve.DailySnapshot
    

##  The Basics  #

To sort, we define the ` orderBy  ` argument on a field path:

Sorting by performing pools by total cumulative revenue  #

    
    
    sg.query_df(
        curve.Query.liquidityPool(orderBy=pool.cumulativeTotalRevenueUSD)
    )
    

By default, the sorting method is ascending. We can change it to descending
(providing us with the highest performing pools) via ` orderDirection  ` :

Sorting by the top performing pools by total cumulative revenue  #

    
    
    sg.query_df(
        curve.Query.liquidityPool(orderBy=pool.cumulativeTotalRevenueUSD, orderDirection="desc")
    )
    

##  Layered Sorting  #

Since nested fields can also have arguments, we can layer multiple sortings on
top of each other:

Sorting the top 4 liquidity pools and the top 3 trading days  #

    
    
    top_pools = curve.Query.liquidityPool(
        first=4,
        orderBy=pool.cumulativeTotalRevenueUSD,
        orderDirection="desc",
    )
    
    sg.query_df(
        top_pools.dailySnapshots(
            first=3,
            orderBy=snapshot.dailyVolumeUSD,
            orderDirection="desc",
        )
    )
    

Warning

Adding more complexity to your query will lead to longer query times as the
indexer has to perform multiple internal database queries to construct the
data as you request. If you hit the natural timeout of 30s, you can try
running the query again as the indexer will continue to process your query in
the background, caching the value for future queries.

##  Sorting by Nested Fields  #

We aren't just limited by sorting only on the top-level fields — we can sort
_by_ nested fields. This is different than layering since we are ordering the
main list of rows based upon a nested value (usually within an object).

Danger

Nested filtering usually only works at a maximum depth of **2** and may not
work across older subgraphs.

Sorting liquidity pools based upon the output token's last traded price.  #

    
    
    sg.query_df(
        curve.Query.liquidityPool(
            orderBy=pool.outputToken.lastPriceUSD,
            orderDirection="desc",
        )
    )
    

[ Next  Merging  ](../merging/) [ Previous  Filtering  ](../filtering/)

Made with [ Furo ](https://github.com/pradyunsg/furo)

[ ](https://github.com/0xPlaygrounds/subgrounds) [
](https://discord.gg/v4r4zhBAh2) [ ](https://twitter.com/Playgrounds0x)

On this page

  * Sorting 
    * The Basics 
    * Layered Sorting 
    * Sorting by Nested Fields 



Contents  Menu  Expand  Light mode  Dark mode  Auto light/dark mode

Hide navigation sidebar

Hide table of contents sidebar

Give us a ⭐️ on [ Github ](https://github.com/0xPlaygrounds/subgrounds)

Toggle site navigation sidebar

_ _

[ Playgrounds  ](../../../../)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

_ _

[ ![Light Logo](../../../../_static/assets/pg-logotype-dark.svg) ![Dark
Logo](../../../../_static/assets/pg-logotype-primary.svg)
](https://playgrounds.network)

Playgrounds API

  * [ Overview ](../../../../api/)
  * [ Getting an API Key ](../../../../api/key/)
  * [ Subgraph Proxy ](../../../../api/subgraph-proxy/)
  * [ Subgrounds Integration ](../../../../api/subgrounds/)
  * [ FAQ ](../../../../api/faq/)

Toggle child pages in navigation

_ _

    * [ What is a Query? ](../../../../api/faq/query/)
  * [ API Reference ](../../../../api/api-reference/)

Toggle child pages in navigation

_ _

    * [ Subgraph Proxy ](../../../../api/reference/proxy/)

Toggle child pages in navigation

_ _

      * [ Subgraph ID ](../../../../api/reference/proxy/subgraph_id/)
      * [ Deployment ID ](../../../../api/reference/proxy/deployment_id/)

Subgrounds

  * [ Overview ](../../../)
  * [ Getting Started ](../../)

Toggle child pages in navigation

_ _

    * [ The Basics ](../../basics/)
    * [ Field Paths ](../)

Toggle child pages in navigation

_ _

      * [ Arguments ](../arguments/)
      * [ Filtering ](../filtering/)
      * [ Sorting ](../sorting/)
      * Merging 
    * [ Querying ](../../querying/)

Toggle child pages in navigation

_ _

    * [ Synthetic Fields ](../../synthetic_fields/)
  * [ Advanced Topics ](../../../advanced_topics/)

Toggle child pages in navigation

_ _

    * [ Contrib ](../../../advanced_topics/contrib/)

Toggle child pages in navigation

_ _

      * [ Plotly ](../../../advanced_topics/contrib/plotly/)
    * [ Pagination ](../../../advanced_topics/pagination/)

Toggle child pages in navigation

_ _

      * [ Custom Strategies ](../../../advanced_topics/pagination/custom/)
  * [ FAQ ](../../../faq/)

Toggle child pages in navigation

_ _

    * [ Exporting to Disk ](../../../faq/exporting/)
    * [ Getting More Data ](../../../faq/more_data/)
    * [ Python Setup ](../../../faq/setup/)

Toggle child pages in navigation

_ _

      * [ Python Versioning ](../../../faq/setup/version_management/)
  * [ Examples ](../../../examples/)

Toggle child pages in navigation

_ _

    * [ Exchanges ](../../../examples/exchanges/)
    * [ Bridges ](../../../examples/bridges/)
    * [ Liquid Staking ](../../../examples/liquid_staking/)
    * [ Governance ](../../../examples/governance/)
    * [ Advanced Research ](../../../examples/advanced_research/)
    * [ Vaults ](../../../examples/vaults/)
  * [ Videos ](../../../videos/)
  * [ Changelog ](../../../changelog/)
  * [ Contributing ](../../../contributing/)
  * [ API Reference ](../../../api_reference/)

Toggle child pages in navigation

_ _

    * [ Top Level APIs ](../../../api_reference/top_level/)
    * [ Internal ](../../../api_reference/internal/)

Toggle child pages in navigation

_ _

      * [ Client ](../../../api_reference/internal/client/)

Toggle child pages in navigation

_ _

        * [ Base ](../../../api_reference/internal/client/base/)
        * [ Sync ](../../../api_reference/internal/client/sync/)
        * [ Async_ ](../../../api_reference/internal/client/async_/)
      * [ Contrib ](../../../api_reference/internal/contrib/)

Toggle child pages in navigation

_ _

        * [ Plotly ](../../../api_reference/internal/contrib/plotly/)
        * [ Dash ](../../../api_reference/internal/contrib/dash/)
      * [ Pagination ](../../../api_reference/internal/pagination/)

Toggle child pages in navigation

_ _

        * [ Strategies ](../../../api_reference/internal/pagination/strategies/)
        * [ Preprocess ](../../../api_reference/internal/pagination/preprocess/)
        * [ Pagination ](../../../api_reference/internal/pagination/pagination/)
        * [ Utils ](../../../api_reference/internal/pagination/utils/)
      * [ Transform ](../../../api_reference/internal/transform/)

Toggle child pages in navigation

_ _

        * [ ABCs ](../../../api_reference/internal/transform/abcs/)
        * [ Apply ](../../../api_reference/internal/transform/apply/)
        * [ Defaults ](../../../api_reference/internal/transform/defaults/)
        * [ Transforms ](../../../api_reference/internal/transform/transforms/)
        * [ Utils ](../../../api_reference/internal/transform/utils/)
      * [ Subgraph ](../../../api_reference/internal/subgraph/)

Toggle child pages in navigation

_ _

        * [ Fieldpath ](../../../api_reference/internal/subgraph/fieldpath/)
        * [ Filter ](../../../api_reference/internal/subgraph/filter/)
        * [ Object ](../../../api_reference/internal/subgraph/object/)
        * [ Subgraph ](../../../api_reference/internal/subgraph/subgraph/)
      * [ Errors ](../../../api_reference/internal/errors/)
      * [ Query ](../../../api_reference/internal/query/)
      * [ Schema ](../../../api_reference/internal/schema/)
      * [ Utils ](../../../api_reference/internal/utils/)

Meta

  * [ Improving the Docs ](../../../../meta/contributing/)

Back to top

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

_ _

#  Merging  #

When passing a list of [ ` FieldPaths  `
](../../../api_reference/top_level/#subgrounds.FieldPath
"subgrounds.FieldPath") to any [ ` query()  `
](../../../api_reference/top_level/#subgrounds.Subgrounds.query
"subgrounds.Subgrounds.query") function, subgrounds will merge them into a
single query.

Warning

This is **only** true if the [ ` FieldPaths  `
](../../../api_reference/top_level/#subgrounds.FieldPath
"subgrounds.FieldPath") originate from the **same subgraph** .

Click for Interactive Documentation

Clicking this button will enable editing and execution of the code-blocks on
this page. Learn more [ here  ](../../basics/) .

Run code

Python

In this query, we are taking the **top 4 curve pools** by **cumulative
volume** and analyzing the **top 3 days by daily total revenue** #

    
    
    from subgrounds import Subgrounds
    sg = Subgrounds()
    
    curve = sg.load_subgraph(
        "https://api.thegraph.com/subgraphs/name/messari/curve-finance-ethereum")
    
    # Partial FieldPath selecting the top 4 most traded pools on Curve
    most_traded_pools = curve.Query.liquidityPools(
        orderBy=curve.LiquidityPool.cumulativeVolumeUSD,
        orderDirection="desc",
        first=4,
    )
    
    # Partial FieldPath selecting the top 2 pools by daily total revenue of
    #  the top 4 most traded tokens.
    # Mote that reuse of `most_traded_pools` in the partial FieldPath
    most_traded_snapshots = most_traded_pools.dailySnapshots(
        orderBy=curve.LiquidityPoolDailySnapshot.dailyTotalRevenue,
        orderDirection="desc",
        first=3,
    ) 
    
    # Querying:
    #  - the name of the top 4 most traded pools, their 2 most liquid 
    # pools' token symbols and their 2 most liquid pool's TVL in USD
    sg.query_df([
        most_traded_pools.name,
        most_traded_snapshots.dailyVolumeUSD,
        most_traded_snapshots.dailyTotalRevenueUSD,
    ])
    

GraphQL

In this query, we are taking the **top 4 curve pools** by **cumulative
volume** and analyzing the **top 3 days by daily total revenue** #

    
    
    query {
      liquidityPools(first: 4, orderBy: cumulativeVolumeUSD, orderDirection: desc) {
        name
        dailySnapshots(first: 3, orderBy: dailyTotalRevenueUSD, orderDirection: desc) {
          dailyVolumeUSD
          dailyTotalRevenueUSD
        }
      }
    }
    

Note

This becomes very helpful when chaining partial [ ` FieldPaths  `
](../../../api_reference/top_level/#subgrounds.FieldPath
"subgrounds.FieldPath") together since you can leverage normal python
constructs to help organize the data as you want to access and [ ` query()  `
](../../../api_reference/top_level/#subgrounds.Subgrounds.query
"subgrounds.Subgrounds.query") will handle the rest!

[ Next  Querying  ](../../querying/) [ Previous  Sorting  ](../sorting/)

Made with [ Furo ](https://github.com/pradyunsg/furo)

[ ](https://github.com/0xPlaygrounds/subgrounds) [
](https://discord.gg/v4r4zhBAh2) [ ](https://twitter.com/Playgrounds0x)



Contents  Menu  Expand  Light mode  Dark mode  Auto light/dark mode

Hide navigation sidebar

Hide table of contents sidebar

Give us a ⭐️ on [ Github ](https://github.com/0xPlaygrounds/subgrounds)

Toggle site navigation sidebar

_ _

[ Playgrounds  ](../../../)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

_ _

[ ![Light Logo](../../../_static/assets/pg-logotype-dark.svg) ![Dark
Logo](../../../_static/assets/pg-logotype-primary.svg)
](https://playgrounds.network)

Playgrounds API

  * [ Overview ](../../../api/)
  * [ Getting an API Key ](../../../api/key/)
  * [ Subgraph Proxy ](../../../api/subgraph-proxy/)
  * [ Subgrounds Integration ](../../../api/subgrounds/)
  * [ FAQ ](../../../api/faq/)

Toggle child pages in navigation

_ _

    * [ What is a Query? ](../../../api/faq/query/)
  * [ API Reference ](../../../api/api-reference/)

Toggle child pages in navigation

_ _

    * [ Subgraph Proxy ](../../../api/reference/proxy/)

Toggle child pages in navigation

_ _

      * [ Subgraph ID ](../../../api/reference/proxy/subgraph_id/)
      * [ Deployment ID ](../../../api/reference/proxy/deployment_id/)

Subgrounds

  * [ Overview ](../../)
  * [ Getting Started ](../)

Toggle child pages in navigation

_ _

    * [ The Basics ](../basics/)
    * [ Field Paths ](../field_paths/)

Toggle child pages in navigation

_ _

      * [ Arguments ](../field_paths/arguments/)
      * [ Filtering ](../field_paths/filtering/)
      * [ Sorting ](../field_paths/sorting/)
      * [ Merging ](../field_paths/merging/)
    * Querying 

Toggle child pages in navigation

_ _

    * [ Synthetic Fields ](../synthetic_fields/)
  * [ Advanced Topics ](../../advanced_topics/)

Toggle child pages in navigation

_ _

    * [ Contrib ](../../advanced_topics/contrib/)

Toggle child pages in navigation

_ _

      * [ Plotly ](../../advanced_topics/contrib/plotly/)
    * [ Pagination ](../../advanced_topics/pagination/)

Toggle child pages in navigation

_ _

      * [ Custom Strategies ](../../advanced_topics/pagination/custom/)
  * [ FAQ ](../../faq/)

Toggle child pages in navigation

_ _

    * [ Exporting to Disk ](../../faq/exporting/)
    * [ Getting More Data ](../../faq/more_data/)
    * [ Python Setup ](../../faq/setup/)

Toggle child pages in navigation

_ _

      * [ Python Versioning ](../../faq/setup/version_management/)
  * [ Examples ](../../examples/)

Toggle child pages in navigation

_ _

    * [ Exchanges ](../../examples/exchanges/)
    * [ Bridges ](../../examples/bridges/)
    * [ Liquid Staking ](../../examples/liquid_staking/)
    * [ Governance ](../../examples/governance/)
    * [ Advanced Research ](../../examples/advanced_research/)
    * [ Vaults ](../../examples/vaults/)
  * [ Videos ](../../videos/)
  * [ Changelog ](../../changelog/)
  * [ Contributing ](../../contributing/)
  * [ API Reference ](../../api_reference/)

Toggle child pages in navigation

_ _

    * [ Top Level APIs ](../../api_reference/top_level/)
    * [ Internal ](../../api_reference/internal/)

Toggle child pages in navigation

_ _

      * [ Client ](../../api_reference/internal/client/)

Toggle child pages in navigation

_ _

        * [ Base ](../../api_reference/internal/client/base/)
        * [ Sync ](../../api_reference/internal/client/sync/)
        * [ Async_ ](../../api_reference/internal/client/async_/)
      * [ Contrib ](../../api_reference/internal/contrib/)

Toggle child pages in navigation

_ _

        * [ Plotly ](../../api_reference/internal/contrib/plotly/)
        * [ Dash ](../../api_reference/internal/contrib/dash/)
      * [ Pagination ](../../api_reference/internal/pagination/)

Toggle child pages in navigation

_ _

        * [ Strategies ](../../api_reference/internal/pagination/strategies/)
        * [ Preprocess ](../../api_reference/internal/pagination/preprocess/)
        * [ Pagination ](../../api_reference/internal/pagination/pagination/)
        * [ Utils ](../../api_reference/internal/pagination/utils/)
      * [ Transform ](../../api_reference/internal/transform/)

Toggle child pages in navigation

_ _

        * [ ABCs ](../../api_reference/internal/transform/abcs/)
        * [ Apply ](../../api_reference/internal/transform/apply/)
        * [ Defaults ](../../api_reference/internal/transform/defaults/)
        * [ Transforms ](../../api_reference/internal/transform/transforms/)
        * [ Utils ](../../api_reference/internal/transform/utils/)
      * [ Subgraph ](../../api_reference/internal/subgraph/)

Toggle child pages in navigation

_ _

        * [ Fieldpath ](../../api_reference/internal/subgraph/fieldpath/)
        * [ Filter ](../../api_reference/internal/subgraph/filter/)
        * [ Object ](../../api_reference/internal/subgraph/object/)
        * [ Subgraph ](../../api_reference/internal/subgraph/subgraph/)
      * [ Errors ](../../api_reference/internal/errors/)
      * [ Query ](../../api_reference/internal/query/)
      * [ Schema ](../../api_reference/internal/schema/)
      * [ Utils ](../../api_reference/internal/utils/)

Meta

  * [ Improving the Docs ](../../../meta/contributing/)

Back to top

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

_ _

#  Querying  #

Subgrounds provides 3 main ways to query data, which provide different data
structures and typing:

Function

|

Return Type

|

Description  
  
---|---|---  
  
[ ` query()  ` ](../../api_reference/top_level/#subgrounds.Subgrounds.query
"subgrounds.Subgrounds.query")

|

[ ` str  ` ](https://docs.python.org/3/library/stdtypes.html#str "\(in Python
v3.11\)") | [ ` int  ` ](https://docs.python.org/3/library/functions.html#int
"\(in Python v3.11\)") | [ ` float  `
](https://docs.python.org/3/library/functions.html#float "\(in Python
v3.11\)") | [ ` bool  `
](https://docs.python.org/3/library/functions.html#bool "\(in Python v3.11\)")
| [ ` list  ` ](https://docs.python.org/3/library/stdtypes.html#list "\(in
Python v3.11\)") | [ ` tuple  `
](https://docs.python.org/3/library/stdtypes.html#tuple "\(in Python v3.11\)")
| ` None  `

|

The shape of the queried data will determine the shape of the returned data
(e.g. whether you query a single entity, list of entities)  
  
[ ` query_json()  `
](../../api_reference/top_level/#subgrounds.Subgrounds.query_json
"subgrounds.Subgrounds.query_json")

|

[ ` dict  ` ](https://docs.python.org/3/library/stdtypes.html#dict "\(in
Python v3.11\)")

|

For subgraphs, this _can_ include generated id keys for each generated sub-
query.  
  
[ ` query_df()  `
](../../api_reference/top_level/#subgrounds.Subgrounds.query_df
"subgrounds.Subgrounds.query_df")

|

[ ` DataFrame  ` ](http://pandas.pydata.org/pandas-
docs/dev/reference/api/pandas.DataFrame.html#pandas.DataFrame "\(in pandas
v2.1.0.dev0+1421.g5f672dc704\)") | [ ` list  `
](https://docs.python.org/3/library/stdtypes.html#list "\(in Python v3.11\)")
[ [ ` DataFrame  ` ](http://pandas.pydata.org/pandas-
docs/dev/reference/api/pandas.DataFrame.html#pandas.DataFrame "\(in pandas
v2.1.0.dev0+1421.g5f672dc704\)") ]

|

Flattened based on the schema of the API from [ ` query_json()  `
](../../api_reference/top_level/#subgrounds.Subgrounds.query_json
"subgrounds.Subgrounds.query_json") , mimicking an SQL ` JOIN  ` operation. If
flattening isn't possible, multiple [ ` Dataframes  `
](http://pandas.pydata.org/pandas-
docs/dev/reference/api/pandas.DataFrame.html#pandas.DataFrame "\(in pandas
v2.1.0.dev0+1421.g5f672dc704\)") will be returned (like when querying a nested
list).  
  
Tip

[ ` query_df()  `
](../../api_reference/top_level/#subgrounds.Subgrounds.query_df
"subgrounds.Subgrounds.query_df") will likely the best choice for you!

##  Quick Example  #

The following code blocks present a comparison between all methods using the `
aave-v2  ` market data:

Click for Interactive Documentation

Clicking this button will enable editing and execution of the code-blocks on
this page. Learn more [ here  ](../basics/) .

Run code

Setup for the following examples of the query methods using the Aave V2 data
from Ethereum  #

    
    
    from subgrounds import Subgrounds
    
    sg = Subgrounds()
    aave_v2 = sg.load_subgraph(
        "https://api.thegraph.com/subgraphs/name/messari/aave-v2-ethereum")
    
    aave_markets = aave_v2.Query.markets(
        first=3,
        orderBy=aave_v2.Market.totalValueLockedUSD,
        orderDirection="desc",
        where=[
            aave_v2.Market.createdBlockNumber > 14720000
        ]
    )
    

query

A list of names and a matching list TVL values gets returned  #

    
    
    sg.query([
        aave_markets.name,
        aave_markets.totalValueLockedUSD,
    ])
    

query_json

A more complex JSON data structure gets returned  #

    
    
    sg.query_json([
        aave_markets.name,
        aave_markets.totalValueLockedUSD,
    ])
    

query_df

✨ A simple [ ` DataFrame  ` ](http://pandas.pydata.org/pandas-
docs/dev/reference/api/pandas.DataFrame.html#pandas.DataFrame "\(in pandas
v2.1.0.dev0+1421.g5f672dc704\)") gets returned  #

    
    
    sg.query_df([
        aave_markets.name,
        aave_markets.totalValueLockedUSD,
    ])
    

Naming your columns

[ ` query_df()  `
](../../api_reference/top_level/#subgrounds.Subgrounds.query_df
"subgrounds.Subgrounds.query_df") can also take an optional parameter `
columns  ` , which let you name the column for each field path!

    
    
    sg.query_df(
        [aave_markets.name, aave_markets.totalValueLockedUSD],
        columns=["Name", "TVL (USD)"],
    )
    

Tip _New in version 1.7.0_

The Graph provides a default server timeout of 30s so we've chosen this as our
default for subgrounds. However, if you are using a custom or self-hosted
indexer, you might want to adjust this timeout value. You can do so via the `
timeout  ` constructor param.

    
    
    sg = Subgrounds(timeout=60)
    

[ Next  Synthetic Fields  ](../synthetic_fields/) [ Previous  Merging
](../field_paths/merging/)

Made with [ Furo ](https://github.com/pradyunsg/furo)

[ ](https://github.com/0xPlaygrounds/subgrounds) [
](https://discord.gg/v4r4zhBAh2) [ ](https://twitter.com/Playgrounds0x)

On this page

  * Querying 
    * Quick Example 



Contents  Menu  Expand  Light mode  Dark mode  Auto light/dark mode

Hide navigation sidebar

Hide table of contents sidebar

Give us a ⭐️ on [ Github ](https://github.com/0xPlaygrounds/subgrounds)

Toggle site navigation sidebar

_ _

[ Playgrounds  ](../../../)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

_ _

[ ![Light Logo](../../../_static/assets/pg-logotype-dark.svg) ![Dark
Logo](../../../_static/assets/pg-logotype-primary.svg)
](https://playgrounds.network)

Playgrounds API

  * [ Overview ](../../../api/)
  * [ Getting an API Key ](../../../api/key/)
  * [ Subgraph Proxy ](../../../api/subgraph-proxy/)
  * [ Subgrounds Integration ](../../../api/subgrounds/)
  * [ FAQ ](../../../api/faq/)

Toggle child pages in navigation

_ _

    * [ What is a Query? ](../../../api/faq/query/)
  * [ API Reference ](../../../api/api-reference/)

Toggle child pages in navigation

_ _

    * [ Subgraph Proxy ](../../../api/reference/proxy/)

Toggle child pages in navigation

_ _

      * [ Subgraph ID ](../../../api/reference/proxy/subgraph_id/)
      * [ Deployment ID ](../../../api/reference/proxy/deployment_id/)

Subgrounds

  * [ Overview ](../../)
  * [ Getting Started ](../)

Toggle child pages in navigation

_ _

    * [ The Basics ](../basics/)
    * [ Field Paths ](../field_paths/)

Toggle child pages in navigation

_ _

      * [ Arguments ](../field_paths/arguments/)
      * [ Filtering ](../field_paths/filtering/)
      * [ Sorting ](../field_paths/sorting/)
      * [ Merging ](../field_paths/merging/)
    * [ Querying ](../querying/)

Toggle child pages in navigation

_ _

    * Synthetic Fields 
  * [ Advanced Topics ](../../advanced_topics/)

Toggle child pages in navigation

_ _

    * [ Contrib ](../../advanced_topics/contrib/)

Toggle child pages in navigation

_ _

      * [ Plotly ](../../advanced_topics/contrib/plotly/)
    * [ Pagination ](../../advanced_topics/pagination/)

Toggle child pages in navigation

_ _

      * [ Custom Strategies ](../../advanced_topics/pagination/custom/)
  * [ FAQ ](../../faq/)

Toggle child pages in navigation

_ _

    * [ Exporting to Disk ](../../faq/exporting/)
    * [ Getting More Data ](../../faq/more_data/)
    * [ Python Setup ](../../faq/setup/)

Toggle child pages in navigation

_ _

      * [ Python Versioning ](../../faq/setup/version_management/)
  * [ Examples ](../../examples/)

Toggle child pages in navigation

_ _

    * [ Exchanges ](../../examples/exchanges/)
    * [ Bridges ](../../examples/bridges/)
    * [ Liquid Staking ](../../examples/liquid_staking/)
    * [ Governance ](../../examples/governance/)
    * [ Advanced Research ](../../examples/advanced_research/)
    * [ Vaults ](../../examples/vaults/)
  * [ Videos ](../../videos/)
  * [ Changelog ](../../changelog/)
  * [ Contributing ](../../contributing/)
  * [ API Reference ](../../api_reference/)

Toggle child pages in navigation

_ _

    * [ Top Level APIs ](../../api_reference/top_level/)
    * [ Internal ](../../api_reference/internal/)

Toggle child pages in navigation

_ _

      * [ Client ](../../api_reference/internal/client/)

Toggle child pages in navigation

_ _

        * [ Base ](../../api_reference/internal/client/base/)
        * [ Sync ](../../api_reference/internal/client/sync/)
        * [ Async_ ](../../api_reference/internal/client/async_/)
      * [ Contrib ](../../api_reference/internal/contrib/)

Toggle child pages in navigation

_ _

        * [ Plotly ](../../api_reference/internal/contrib/plotly/)
        * [ Dash ](../../api_reference/internal/contrib/dash/)
      * [ Pagination ](../../api_reference/internal/pagination/)

Toggle child pages in navigation

_ _

        * [ Strategies ](../../api_reference/internal/pagination/strategies/)
        * [ Preprocess ](../../api_reference/internal/pagination/preprocess/)
        * [ Pagination ](../../api_reference/internal/pagination/pagination/)
        * [ Utils ](../../api_reference/internal/pagination/utils/)
      * [ Transform ](../../api_reference/internal/transform/)

Toggle child pages in navigation

_ _

        * [ ABCs ](../../api_reference/internal/transform/abcs/)
        * [ Apply ](../../api_reference/internal/transform/apply/)
        * [ Defaults ](../../api_reference/internal/transform/defaults/)
        * [ Transforms ](../../api_reference/internal/transform/transforms/)
        * [ Utils ](../../api_reference/internal/transform/utils/)
      * [ Subgraph ](../../api_reference/internal/subgraph/)

Toggle child pages in navigation

_ _

        * [ Fieldpath ](../../api_reference/internal/subgraph/fieldpath/)
        * [ Filter ](../../api_reference/internal/subgraph/filter/)
        * [ Object ](../../api_reference/internal/subgraph/object/)
        * [ Subgraph ](../../api_reference/internal/subgraph/subgraph/)
      * [ Errors ](../../api_reference/internal/errors/)
      * [ Query ](../../api_reference/internal/query/)
      * [ Schema ](../../api_reference/internal/schema/)
      * [ Utils ](../../api_reference/internal/utils/)

Meta

  * [ Improving the Docs ](../../../meta/contributing/)

Back to top

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

_ _

#  Synthetic Fields  #

One of Subgrounds' unique features is the ability to define schema-based
(i.e.: pre-querying) transformations using [ ` SyntheticFields  `
](../../api_reference/top_level/#subgrounds.SyntheticField
"subgrounds.SyntheticField") .

[ ` SyntheticFields  `
](../../api_reference/top_level/#subgrounds.SyntheticField
"subgrounds.SyntheticField") can be created using Python arithmetic operators
on relative [ ` FieldPath  `
](../../api_reference/top_level/#subgrounds.FieldPath "subgrounds.FieldPath")
(i.e.: [ ` FieldPaths  ` ](../../api_reference/top_level/#subgrounds.FieldPath
"subgrounds.FieldPath") starting from an entity and not the root ` Query  `
object) and must be added to the entity which they enhance. Once added to an
entity, [ ` SyntheticFields  `
](../../api_reference/top_level/#subgrounds.SyntheticField
"subgrounds.SyntheticField") can be queried just like regular GraphQL fields.

The example below demonstrates how to create a simple [ ` SyntheticField  `
](../../api_reference/top_level/#subgrounds.SyntheticField
"subgrounds.SyntheticField") to calculate the swap price of ` Swap  ` events
stored on the Sushiswap subgraph:

Click for Interactive Documentation

Clicking this button will enable editing and execution of the code-blocks on
this page. Learn more [ here  ](../basics/) .

Run code

    
    
    from subgrounds import Subgrounds
    sg = Subgrounds()
    
    sushiswap = sg.load_subgraph(
        "https://api.thegraph.com/subgraphs/name/sushiswap/exchange")
    swap = sushiswap.Swap  # short hand for ease-of-use
    
    # Define a synthetic field named price1 (the swap price of token1,
    #   in terms of token0) on Swap entities
    swap.price1 = (
        abs(swap.amount0Out - swap.amount0In)
        / abs(swap.amount1Out - swap.amount1In)
    )
    
    # Build query to get the last 10 swaps of the WETH-USDC pair on Sushiswap 
    weth_usdc = sushiswap.Query.pair(id="0x397ff1542f962076d0bfe58ea045ffa2d347aca0")
    
    last_10_swaps = weth_usdc.swaps(
        orderBy=swap.timestamp,
        orderDirection="desc",
        first=10
    )
    
    # Query swap prices using the `SyntheticField` price1 as if they were regular fields
    sg.query_df([
        last_10_swaps.timestamp,
        last_10_swaps.price1     # synthetic fields get used the same!
    ])
    

[ ` SyntheticFields  `
](../../api_reference/top_level/#subgrounds.SyntheticField
"subgrounds.SyntheticField") can _also_ be created using the constructor,
allowing for much more complex transformations.

    
    
    from datetime import datetime
    from subgrounds import SyntheticField
    
    # Create a SyntheticField on the Swap entity called `datetime`, which will format 
    # the timestamp field into something more human readable
    swap.datetime = SyntheticField(
        f=lambda timestamp: str(datetime.fromtimestamp(timestamp)),
        type_=SyntheticField.STRING,
        deps=swap.timestamp,
    )
    
    last_10_swaps = sushiswap.Query.swaps(
        orderBy=swap.timestamp,
        orderDirection="desc",
        first=10,
    )
    
    sg.query_df([
        last_10_swaps.datetime,
        last_10_swaps.pair.token0.symbol,
        last_10_swaps.pair.token1.symbol,
    ])
    

##  Helpers  #

Since there are several common instances [ ` SyntheticFields  `
](../../api_reference/top_level/#subgrounds.SyntheticField
"subgrounds.SyntheticField") we see in the wild, we've added some helper
constructors for ease of use.

###  ` SyntheticField.datetime_of_timestamp  ` #

This helper constructor makes it easy to convert ` timestamps  ` into [ `
datetime  `
](https://docs.python.org/3/library/datetime.html#datetime.datetime "\(in
Python v3.11\)") objects.

Helper Method

    
    
    swap.datetime = SyntheticField.datetime_of_timestamp(swap.timestamp)
    

Translation

    
    
    swap.datetime = SyntheticField(
        f=lambda timestamp: str(datetime.fromtimestamp(timestamp)),
        type_=SyntheticField.STRING,
        deps=swap.timestamp,
    )
    

[ Next  Advanced Topics  ](../../advanced_topics/) [ Previous  Querying
](../querying/)

Made with [ Furo ](https://github.com/pradyunsg/furo)

[ ](https://github.com/0xPlaygrounds/subgrounds) [
](https://discord.gg/v4r4zhBAh2) [ ](https://twitter.com/Playgrounds0x)

On this page

  * Synthetic Fields 
    * Helpers 
      * ` SyntheticField.datetime_of_timestamp  `



Contents  Menu  Expand  Light mode  Dark mode  Auto light/dark mode

Hide navigation sidebar

Hide table of contents sidebar

Give us a ⭐️ on [ Github ](https://github.com/0xPlaygrounds/subgrounds)

Toggle site navigation sidebar

_ _

[ Playgrounds  ](../../../)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

_ _

[ ![Light Logo](../../../_static/assets/pg-logotype-dark.svg) ![Dark
Logo](../../../_static/assets/pg-logotype-primary.svg)
](https://playgrounds.network)

Playgrounds API

  * [ Overview ](../../../api/)
  * [ Getting an API Key ](../../../api/key/)
  * [ Subgraph Proxy ](../../../api/subgraph-proxy/)
  * [ Subgrounds Integration ](../../../api/subgrounds/)
  * [ FAQ ](../../../api/faq/)

Toggle child pages in navigation

_ _

    * [ What is a Query? ](../../../api/faq/query/)
  * [ API Reference ](../../../api/api-reference/)

Toggle child pages in navigation

_ _

    * [ Subgraph Proxy ](../../../api/reference/proxy/)

Toggle child pages in navigation

_ _

      * [ Subgraph ID ](../../../api/reference/proxy/subgraph_id/)
      * [ Deployment ID ](../../../api/reference/proxy/deployment_id/)

Subgrounds

  * [ Overview ](../../)
  * [ Getting Started ](../../getting_started/)

Toggle child pages in navigation

_ _

    * [ The Basics ](../../getting_started/basics/)
    * [ Field Paths ](../../getting_started/field_paths/)

Toggle child pages in navigation

_ _

      * [ Arguments ](../../getting_started/field_paths/arguments/)
      * [ Filtering ](../../getting_started/field_paths/filtering/)
      * [ Sorting ](../../getting_started/field_paths/sorting/)
      * [ Merging ](../../getting_started/field_paths/merging/)
    * [ Querying ](../../getting_started/querying/)

Toggle child pages in navigation

_ _

    * [ Synthetic Fields ](../../getting_started/synthetic_fields/)
  * [ Advanced Topics ](../)

Toggle child pages in navigation

_ _

    * [ Contrib ](../contrib/)

Toggle child pages in navigation

_ _

      * [ Plotly ](../contrib/plotly/)
    * Pagination 

Toggle child pages in navigation

_ _

      * [ Custom Strategies ](custom/)
  * [ FAQ ](../../faq/)

Toggle child pages in navigation

_ _

    * [ Exporting to Disk ](../../faq/exporting/)
    * [ Getting More Data ](../../faq/more_data/)
    * [ Python Setup ](../../faq/setup/)

Toggle child pages in navigation

_ _

      * [ Python Versioning ](../../faq/setup/version_management/)
  * [ Examples ](../../examples/)

Toggle child pages in navigation

_ _

    * [ Exchanges ](../../examples/exchanges/)
    * [ Bridges ](../../examples/bridges/)
    * [ Liquid Staking ](../../examples/liquid_staking/)
    * [ Governance ](../../examples/governance/)
    * [ Advanced Research ](../../examples/advanced_research/)
    * [ Vaults ](../../examples/vaults/)
  * [ Videos ](../../videos/)
  * [ Changelog ](../../changelog/)
  * [ Contributing ](../../contributing/)
  * [ API Reference ](../../api_reference/)

Toggle child pages in navigation

_ _

    * [ Top Level APIs ](../../api_reference/top_level/)
    * [ Internal ](../../api_reference/internal/)

Toggle child pages in navigation

_ _

      * [ Client ](../../api_reference/internal/client/)

Toggle child pages in navigation

_ _

        * [ Base ](../../api_reference/internal/client/base/)
        * [ Sync ](../../api_reference/internal/client/sync/)
        * [ Async_ ](../../api_reference/internal/client/async_/)
      * [ Contrib ](../../api_reference/internal/contrib/)

Toggle child pages in navigation

_ _

        * [ Plotly ](../../api_reference/internal/contrib/plotly/)
        * [ Dash ](../../api_reference/internal/contrib/dash/)
      * [ Pagination ](../../api_reference/internal/pagination/)

Toggle child pages in navigation

_ _

        * [ Strategies ](../../api_reference/internal/pagination/strategies/)
        * [ Preprocess ](../../api_reference/internal/pagination/preprocess/)
        * [ Pagination ](../../api_reference/internal/pagination/pagination/)
        * [ Utils ](../../api_reference/internal/pagination/utils/)
      * [ Transform ](../../api_reference/internal/transform/)

Toggle child pages in navigation

_ _

        * [ ABCs ](../../api_reference/internal/transform/abcs/)
        * [ Apply ](../../api_reference/internal/transform/apply/)
        * [ Defaults ](../../api_reference/internal/transform/defaults/)
        * [ Transforms ](../../api_reference/internal/transform/transforms/)
        * [ Utils ](../../api_reference/internal/transform/utils/)
      * [ Subgraph ](../../api_reference/internal/subgraph/)

Toggle child pages in navigation

_ _

        * [ Fieldpath ](../../api_reference/internal/subgraph/fieldpath/)
        * [ Filter ](../../api_reference/internal/subgraph/filter/)
        * [ Object ](../../api_reference/internal/subgraph/object/)
        * [ Subgraph ](../../api_reference/internal/subgraph/subgraph/)
      * [ Errors ](../../api_reference/internal/errors/)
      * [ Query ](../../api_reference/internal/query/)
      * [ Schema ](../../api_reference/internal/schema/)
      * [ Utils ](../../api_reference/internal/utils/)

Meta

  * [ Improving the Docs ](../../../meta/contributing/)

Back to top

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

_ _

#  Pagination  #

_New in version` 1.0.0  ` _

Click for Interactive Documentation

Clicking this button will enable editing and execution of the code-blocks on
this page. Learn more [ here  ](../../getting_started/basics/) .

Run code

By default, Subgrounds handles GraphQL query pagination automatically. That
is, if a query selects more than 1000 entities using the ` first  ` argument
(1000 being The Graph's limit to the ` first  ` argument), then Subgrounds
will automatically split the query into multiple queries that each query at
most 1000 entities.

Pagination is performed by Subgrounds with the use of a pagination strategy: a
class that implements the [ ` PaginationStrategy  `
](../../api_reference/internal/pagination/#subgrounds.pagination.PaginationStrategy
"subgrounds.pagination.PaginationStrategy") protocol. Subgrounds provides two
pagination strategies out of the box, however, users wishing to implement
their own strategy should create a class that implements the aforementioned
protocol (see below).

If at some point during the pagination process, an unhandled exception occurs,
Subgrounds will raise a [ ` PaginationError  `
](../../api_reference/internal/pagination/#subgrounds.pagination.PaginationError
"subgrounds.pagination.PaginationError") exception containing the initial
exception message as well as the [ ` PaginationStrategy  `
](../../api_reference/internal/pagination/#subgrounds.pagination.PaginationStrategy
"subgrounds.pagination.PaginationStrategy") object in the state it was in when
the error occured, which, in the case of iterative querying (e.g.: when using
[ ` query_df_iter()  `
](../../api_reference/top_level/#subgrounds.Subgrounds.query_df_iter
"subgrounds.Subgrounds.query_df_iter") ), could be useful to recover and start
pagination from a later stage.

##  Available Strategies  #

Subgrounds provides two pagination strategies out of the box:

  1. ` LegacyStrategy  ` : A pagination strategy that implements the pagination algorithm that was used by default prior to this update. This pagination strategy supports pagination on nested fields, but is quite slow. Below is an example of a query for which you should use this strategy: 

    
    
    query {
      liquidityPools(first: 10) {
        swaps(first: 5000) {
          id
        }
      }
    }
    

  2. ` ShallowStrategy  ` : A new pagination strategy that is faster than the ` LegacyStrategy  ` , but does not paginate on nested list fields. In other words, this strategy is best when nested list fields select fewer than 1000 entities. Below is an example of a query for which you should use this strategy: 

    
    
    query {
      liquidityPools(first: 5000) {
        swaps(first: 10) {
          id
        }
      }
    }
    

To use either pagination strategy, set the ` pagination_strategy  ` argument
of toplevel querying functions:

    
    
    from subgrounds import Subgrounds
    from subgrounds.pagination import ShallowStrategy
    
    sg = Subgrounds()
    subgraph = sg.load_subgraph(
        "https://api.thegraph.com/subgraphs/name/messari/compound-v2-ethereum")
    
    mkt_daily_snapshots = subgraph.Query.marketDailySnapshots(
        orderBy="timestamp",
        orderDirection="desc",
        first=50,
    )
    
    field_paths = [
        mkt_daily_snapshots.timestamp,
        mkt_daily_snapshots.market.inputToken.symbol,
        mkt_daily_snapshots.rates.rate,
        mkt_daily_snapshots.rates.side,
    ]
    
    sg.query_df(field_paths, pagination_strategy=ShallowStrategy) 
    

Note that pagination can be explicitly disabled by setting ` LegacyStrategy  `
to ` None  ` , in which case the query will be executed as-is:

    
    
    sg.query_df(field_paths, pagination_strategy=None) 
    

[ Next  Custom Strategies  ](custom/) [ Previous  Plotly
](../contrib/plotly/)

Made with [ Furo ](https://github.com/pradyunsg/furo)

[ ](https://github.com/0xPlaygrounds/subgrounds) [
](https://discord.gg/v4r4zhBAh2) [ ](https://twitter.com/Playgrounds0x)

On this page

  * Pagination 
    * Available Strategies 



Contents  Menu  Expand  Light mode  Dark mode  Auto light/dark mode

Hide navigation sidebar

Hide table of contents sidebar

Give us a ⭐️ on [ Github ](https://github.com/0xPlaygrounds/subgrounds)

Toggle site navigation sidebar

_ _

[ Playgrounds  ](../../../../)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

_ _

[ ![Light Logo](../../../../_static/assets/pg-logotype-dark.svg) ![Dark
Logo](../../../../_static/assets/pg-logotype-primary.svg)
](https://playgrounds.network)

Playgrounds API

  * [ Overview ](../../../../api/)
  * [ Getting an API Key ](../../../../api/key/)
  * [ Subgraph Proxy ](../../../../api/subgraph-proxy/)
  * [ Subgrounds Integration ](../../../../api/subgrounds/)
  * [ FAQ ](../../../../api/faq/)

Toggle child pages in navigation

_ _

    * [ What is a Query? ](../../../../api/faq/query/)
  * [ API Reference ](../../../../api/api-reference/)

Toggle child pages in navigation

_ _

    * [ Subgraph Proxy ](../../../../api/reference/proxy/)

Toggle child pages in navigation

_ _

      * [ Subgraph ID ](../../../../api/reference/proxy/subgraph_id/)
      * [ Deployment ID ](../../../../api/reference/proxy/deployment_id/)

Subgrounds

  * [ Overview ](../../../)
  * [ Getting Started ](../../../getting_started/)

Toggle child pages in navigation

_ _

    * [ The Basics ](../../../getting_started/basics/)
    * [ Field Paths ](../../../getting_started/field_paths/)

Toggle child pages in navigation

_ _

      * [ Arguments ](../../../getting_started/field_paths/arguments/)
      * [ Filtering ](../../../getting_started/field_paths/filtering/)
      * [ Sorting ](../../../getting_started/field_paths/sorting/)
      * [ Merging ](../../../getting_started/field_paths/merging/)
    * [ Querying ](../../../getting_started/querying/)

Toggle child pages in navigation

_ _

    * [ Synthetic Fields ](../../../getting_started/synthetic_fields/)
  * [ Advanced Topics ](../../)

Toggle child pages in navigation

_ _

    * [ Contrib ](../../contrib/)

Toggle child pages in navigation

_ _

      * [ Plotly ](../../contrib/plotly/)
    * [ Pagination ](../)

Toggle child pages in navigation

_ _

      * Custom Strategies 
  * [ FAQ ](../../../faq/)

Toggle child pages in navigation

_ _

    * [ Exporting to Disk ](../../../faq/exporting/)
    * [ Getting More Data ](../../../faq/more_data/)
    * [ Python Setup ](../../../faq/setup/)

Toggle child pages in navigation

_ _

      * [ Python Versioning ](../../../faq/setup/version_management/)
  * [ Examples ](../../../examples/)

Toggle child pages in navigation

_ _

    * [ Exchanges ](../../../examples/exchanges/)
    * [ Bridges ](../../../examples/bridges/)
    * [ Liquid Staking ](../../../examples/liquid_staking/)
    * [ Governance ](../../../examples/governance/)
    * [ Advanced Research ](../../../examples/advanced_research/)
    * [ Vaults ](../../../examples/vaults/)
  * [ Videos ](../../../videos/)
  * [ Changelog ](../../../changelog/)
  * [ Contributing ](../../../contributing/)
  * [ API Reference ](../../../api_reference/)

Toggle child pages in navigation

_ _

    * [ Top Level APIs ](../../../api_reference/top_level/)
    * [ Internal ](../../../api_reference/internal/)

Toggle child pages in navigation

_ _

      * [ Client ](../../../api_reference/internal/client/)

Toggle child pages in navigation

_ _

        * [ Base ](../../../api_reference/internal/client/base/)
        * [ Sync ](../../../api_reference/internal/client/sync/)
        * [ Async_ ](../../../api_reference/internal/client/async_/)
      * [ Contrib ](../../../api_reference/internal/contrib/)

Toggle child pages in navigation

_ _

        * [ Plotly ](../../../api_reference/internal/contrib/plotly/)
        * [ Dash ](../../../api_reference/internal/contrib/dash/)
      * [ Pagination ](../../../api_reference/internal/pagination/)

Toggle child pages in navigation

_ _

        * [ Strategies ](../../../api_reference/internal/pagination/strategies/)
        * [ Preprocess ](../../../api_reference/internal/pagination/preprocess/)
        * [ Pagination ](../../../api_reference/internal/pagination/pagination/)
        * [ Utils ](../../../api_reference/internal/pagination/utils/)
      * [ Transform ](../../../api_reference/internal/transform/)

Toggle child pages in navigation

_ _

        * [ ABCs ](../../../api_reference/internal/transform/abcs/)
        * [ Apply ](../../../api_reference/internal/transform/apply/)
        * [ Defaults ](../../../api_reference/internal/transform/defaults/)
        * [ Transforms ](../../../api_reference/internal/transform/transforms/)
        * [ Utils ](../../../api_reference/internal/transform/utils/)
      * [ Subgraph ](../../../api_reference/internal/subgraph/)

Toggle child pages in navigation

_ _

        * [ Fieldpath ](../../../api_reference/internal/subgraph/fieldpath/)
        * [ Filter ](../../../api_reference/internal/subgraph/filter/)
        * [ Object ](../../../api_reference/internal/subgraph/object/)
        * [ Subgraph ](../../../api_reference/internal/subgraph/subgraph/)
      * [ Errors ](../../../api_reference/internal/errors/)
      * [ Query ](../../../api_reference/internal/query/)
      * [ Schema ](../../../api_reference/internal/schema/)
      * [ Utils ](../../../api_reference/internal/utils/)

Meta

  * [ Improving the Docs ](../../../../meta/contributing/)

Back to top

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

_ _

#  Custom Strategies  #

_New in version` 1.0.0  ` _

Subgrounds allows developers to create their own pagination strategy by
creating a class that implements the [ ` PaginationStrategy  `
](../../../api_reference/internal/pagination/#subgrounds.pagination.PaginationStrategy
"subgrounds.pagination.PaginationStrategy") protocol:

The class's constructor should accept a [ ` SchemaMeta  `
](../../../api_reference/internal/schema/#subgrounds.schema.SchemaMeta
"subgrounds.schema.SchemaMeta") argument which represents the schema of the
subgraph API that the query is directed to and a [ ` Document  `
](../../../api_reference/internal/query/#subgrounds.query.Document
"subgrounds.query.Document") argument which represents the query to be
paginated on. If no pagination is required for the given document, then the
constructor should raise a [ ` SkipPagination  `
](../../../api_reference/internal/pagination/strategies/#subgrounds.pagination.strategies.SkipPagination
"subgrounds.pagination.strategies.SkipPagination") exception.

The class's ` step  ` method is where the main logic of the pagination
strategy is located. The method accepts a single argument, ` page_data  `
which is a dictionary containing the response data of the previous query
(i.e.: the previous page of data). The ` step  ` method should return a tuple
` (doc,  vars)  ` , where ` doc  ` is a [ ` Document  `
](../../../api_reference/internal/query/#subgrounds.query.Document
"subgrounds.query.Document") representing the query to be made to fetch the
next page of data. When pagination is over (e.g.: when all pages of data have
been fetched), the ` step  ` method should raise a [ ` StopPagination  `
](../../../api_reference/internal/pagination/strategies/#subgrounds.pagination.strategies.StopPagination
"subgrounds.pagination.strategies.StopPagination") exception.

Below is the algorithm used by [ ` Subgrounds  `
](../../../api_reference/top_level/#subgrounds.Subgrounds
"subgrounds.Subgrounds") to paginate over a query document given a pagination
strategy:

    
    
    def paginate(
        schema: SchemaMeta,
        doc: Document,
        pagination_strategy: Type[PaginationStrategy],
        headers: dict[str, Any],
    ) -> dict[str, Any]:
        """Executes the request document `doc` based on the GraphQL schema `schema` and returns
        the response as a JSON dictionary.
    
        Args:
          schema (SchemaMeta): The GraphQL schema on which the request document is based
          doc (Document): The request document
    
        Returns:
          dict[str, Any]: The response data as a JSON dictionary
        """
    
        try:
            strategy = pagination_strategy(schema, doc)
    
            data: dict[str, Any] = {}
            doc, args = strategy.step()
    
            while True:
                try:
                    page_data = client.query(
                        url=doc.url,
                        query_str=doc.graphql,
                        variables=doc.variables | args,
                        headers=headers,
                    )
                    data = merge(data, page_data)
                    doc, args = strategy.step(page_data)
                except StopPagination:
                    break
                except Exception as exn:
                    raise PaginationError(exn.args[0], strategy)
    
            return data
    
        except SkipPagination:
            return client.query(
                doc.url, doc.graphql, variables=doc.variables, headers=headers
            )
    

[ Next  FAQ  ](../../../faq/) [ Previous  Pagination  ](../)

Made with [ Furo ](https://github.com/pradyunsg/furo)

[ ](https://github.com/0xPlaygrounds/subgrounds) [
](https://discord.gg/v4r4zhBAh2) [ ](https://twitter.com/Playgrounds0x)



Contents  Menu  Expand  Light mode  Dark mode  Auto light/dark mode

Hide navigation sidebar

Hide table of contents sidebar

Give us a ⭐️ on [ Github ](https://github.com/0xPlaygrounds/subgrounds)

Toggle site navigation sidebar

_ _

[ Playgrounds  ](../../../)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

_ _

[ ![Light Logo](../../../_static/assets/pg-logotype-dark.svg) ![Dark
Logo](../../../_static/assets/pg-logotype-primary.svg)
](https://playgrounds.network)

Playgrounds API

  * [ Overview ](../../../api/)
  * [ Getting an API Key ](../../../api/key/)
  * [ Subgraph Proxy ](../../../api/subgraph-proxy/)
  * [ Subgrounds Integration ](../../../api/subgrounds/)
  * [ FAQ ](../../../api/faq/)

Toggle child pages in navigation

_ _

    * [ What is a Query? ](../../../api/faq/query/)
  * [ API Reference ](../../../api/api-reference/)

Toggle child pages in navigation

_ _

    * [ Subgraph Proxy ](../../../api/reference/proxy/)

Toggle child pages in navigation

_ _

      * [ Subgraph ID ](../../../api/reference/proxy/subgraph_id/)
      * [ Deployment ID ](../../../api/reference/proxy/deployment_id/)

Subgrounds

  * [ Overview ](../../)
  * [ Getting Started ](../../getting_started/)

Toggle child pages in navigation

_ _

    * [ The Basics ](../../getting_started/basics/)
    * [ Field Paths ](../../getting_started/field_paths/)

Toggle child pages in navigation

_ _

      * [ Arguments ](../../getting_started/field_paths/arguments/)
      * [ Filtering ](../../getting_started/field_paths/filtering/)
      * [ Sorting ](../../getting_started/field_paths/sorting/)
      * [ Merging ](../../getting_started/field_paths/merging/)
    * [ Querying ](../../getting_started/querying/)

Toggle child pages in navigation

_ _

    * [ Synthetic Fields ](../../getting_started/synthetic_fields/)
  * [ Advanced Topics ](../../advanced_topics/)

Toggle child pages in navigation

_ _

    * [ Contrib ](../../advanced_topics/contrib/)

Toggle child pages in navigation

_ _

      * [ Plotly ](../../advanced_topics/contrib/plotly/)
    * [ Pagination ](../../advanced_topics/pagination/)

Toggle child pages in navigation

_ _

      * [ Custom Strategies ](../../advanced_topics/pagination/custom/)
  * [ FAQ ](../)

Toggle child pages in navigation

_ _

    * [ Exporting to Disk ](../exporting/)
    * Getting More Data 
    * [ Python Setup ](../setup/)

Toggle child pages in navigation

_ _

      * [ Python Versioning ](../setup/version_management/)
  * [ Examples ](../../examples/)

Toggle child pages in navigation

_ _

    * [ Exchanges ](../../examples/exchanges/)
    * [ Bridges ](../../examples/bridges/)
    * [ Liquid Staking ](../../examples/liquid_staking/)
    * [ Governance ](../../examples/governance/)
    * [ Advanced Research ](../../examples/advanced_research/)
    * [ Vaults ](../../examples/vaults/)
  * [ Videos ](../../videos/)
  * [ Changelog ](../../changelog/)
  * [ Contributing ](../../contributing/)
  * [ API Reference ](../../api_reference/)

Toggle child pages in navigation

_ _

    * [ Top Level APIs ](../../api_reference/top_level/)
    * [ Internal ](../../api_reference/internal/)

Toggle child pages in navigation

_ _

      * [ Client ](../../api_reference/internal/client/)

Toggle child pages in navigation

_ _

        * [ Base ](../../api_reference/internal/client/base/)
        * [ Sync ](../../api_reference/internal/client/sync/)
        * [ Async_ ](../../api_reference/internal/client/async_/)
      * [ Contrib ](../../api_reference/internal/contrib/)

Toggle child pages in navigation

_ _

        * [ Plotly ](../../api_reference/internal/contrib/plotly/)
        * [ Dash ](../../api_reference/internal/contrib/dash/)
      * [ Pagination ](../../api_reference/internal/pagination/)

Toggle child pages in navigation

_ _

        * [ Strategies ](../../api_reference/internal/pagination/strategies/)
        * [ Preprocess ](../../api_reference/internal/pagination/preprocess/)
        * [ Pagination ](../../api_reference/internal/pagination/pagination/)
        * [ Utils ](../../api_reference/internal/pagination/utils/)
      * [ Transform ](../../api_reference/internal/transform/)

Toggle child pages in navigation

_ _

        * [ ABCs ](../../api_reference/internal/transform/abcs/)
        * [ Apply ](../../api_reference/internal/transform/apply/)
        * [ Defaults ](../../api_reference/internal/transform/defaults/)
        * [ Transforms ](../../api_reference/internal/transform/transforms/)
        * [ Utils ](../../api_reference/internal/transform/utils/)
      * [ Subgraph ](../../api_reference/internal/subgraph/)

Toggle child pages in navigation

_ _

        * [ Fieldpath ](../../api_reference/internal/subgraph/fieldpath/)
        * [ Filter ](../../api_reference/internal/subgraph/filter/)
        * [ Object ](../../api_reference/internal/subgraph/object/)
        * [ Subgraph ](../../api_reference/internal/subgraph/subgraph/)
      * [ Errors ](../../api_reference/internal/errors/)
      * [ Query ](../../api_reference/internal/query/)
      * [ Schema ](../../api_reference/internal/schema/)
      * [ Utils ](../../api_reference/internal/utils/)

Meta

  * [ Improving the Docs ](../../../meta/contributing/)

Back to top

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

_ _

#  Getting More Data  #

Click for Interactive Documentation

Clicking this button will enable editing and execution of the code-blocks on
this page. Learn more [ here  ](../../getting_started/basics/) .

Run code

By default, subgraphs will emit only 100 rows for a given entity. In order to
surface more data from an entity, you must leverage [ field arguments
](../../getting_started/field_paths/arguments/) , specifically the ` first  `
argument. This specifies how many entities you wish to retrieve from that
specific entity.

Gathering data from the curve finance subgraph  #

    
    
    from subgrounds import Subgrounds
    
    with Subgrounds() as sg:
        curve = sg.load_subgraph(
            "https://api.thegraph.com/subgraphs/name/messari/curve-finance-ethereum")
    
        sg.query_df(
            curve.Query.financialsDailySnapshots(first=2500)
        )
    

Note

It is possible to query more than a 100 rows worth of data **without**
specifying a ` first  ` argument by using nested fields. Essentially, you
would be querying multiple rows for each row as ` subgrounds  ` would
paginated the nested field and then auto-flatten said field.

##  Pagination  #

Subgraphs and GraphQL usually restrict you to a maximum ` first  ` argument of
` 1000  ` . In ` subgrounds  ` , you can specify as large as a number as you
want as ` subgrounds  ` will automatically create multiple, **paginated** ,
requests to retrieve more data. This means you'll be able to access all the
data from an entity by just setting the ` first  ` argument to a high-enough
number!

* * *

###  Field Arguments

Customizing other field path arguments

[ ](../../getting_started/field_paths/arguments/)

###  Pagination

Learn more about how ` subgrounds  ` paginates!

[ ](../../advanced_topics/pagination/)

[ Next  Python Setup  ](../setup/) [ Previous  Exporting to Disk
](../exporting/)

Made with [ Furo ](https://github.com/pradyunsg/furo)

[ ](https://github.com/0xPlaygrounds/subgrounds) [
](https://discord.gg/v4r4zhBAh2) [ ](https://twitter.com/Playgrounds0x)

On this page

  * Getting More Data 
    * Pagination 



Contents  Menu  Expand  Light mode  Dark mode  Auto light/dark mode

Hide navigation sidebar

Hide table of contents sidebar

Give us a ⭐️ on [ Github ](https://github.com/0xPlaygrounds/subgrounds)

Toggle site navigation sidebar

_ _

[ Playgrounds  ](../../../../)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

_ _

[ ![Light Logo](../../../../_static/assets/pg-logotype-dark.svg) ![Dark
Logo](../../../../_static/assets/pg-logotype-primary.svg)
](https://playgrounds.network)

Playgrounds API

  * [ Overview ](../../../../api/)
  * [ Getting an API Key ](../../../../api/key/)
  * [ Subgraph Proxy ](../../../../api/subgraph-proxy/)
  * [ Subgrounds Integration ](../../../../api/subgrounds/)
  * [ FAQ ](../../../../api/faq/)

Toggle child pages in navigation

_ _

    * [ What is a Query? ](../../../../api/faq/query/)
  * [ API Reference ](../../../../api/api-reference/)

Toggle child pages in navigation

_ _

    * [ Subgraph Proxy ](../../../../api/reference/proxy/)

Toggle child pages in navigation

_ _

      * [ Subgraph ID ](../../../../api/reference/proxy/subgraph_id/)
      * [ Deployment ID ](../../../../api/reference/proxy/deployment_id/)

Subgrounds

  * [ Overview ](../../../)
  * [ Getting Started ](../../../getting_started/)

Toggle child pages in navigation

_ _

    * [ The Basics ](../../../getting_started/basics/)
    * [ Field Paths ](../../../getting_started/field_paths/)

Toggle child pages in navigation

_ _

      * [ Arguments ](../../../getting_started/field_paths/arguments/)
      * [ Filtering ](../../../getting_started/field_paths/filtering/)
      * [ Sorting ](../../../getting_started/field_paths/sorting/)
      * [ Merging ](../../../getting_started/field_paths/merging/)
    * [ Querying ](../../../getting_started/querying/)

Toggle child pages in navigation

_ _

    * [ Synthetic Fields ](../../../getting_started/synthetic_fields/)
  * [ Advanced Topics ](../../)

Toggle child pages in navigation

_ _

    * [ Contrib ](../)

Toggle child pages in navigation

_ _

      * Plotly 
    * [ Pagination ](../../pagination/)

Toggle child pages in navigation

_ _

      * [ Custom Strategies ](../../pagination/custom/)
  * [ FAQ ](../../../faq/)

Toggle child pages in navigation

_ _

    * [ Exporting to Disk ](../../../faq/exporting/)
    * [ Getting More Data ](../../../faq/more_data/)
    * [ Python Setup ](../../../faq/setup/)

Toggle child pages in navigation

_ _

      * [ Python Versioning ](../../../faq/setup/version_management/)
  * [ Examples ](../../../examples/)

Toggle child pages in navigation

_ _

    * [ Exchanges ](../../../examples/exchanges/)
    * [ Bridges ](../../../examples/bridges/)
    * [ Liquid Staking ](../../../examples/liquid_staking/)
    * [ Governance ](../../../examples/governance/)
    * [ Advanced Research ](../../../examples/advanced_research/)
    * [ Vaults ](../../../examples/vaults/)
  * [ Videos ](../../../videos/)
  * [ Changelog ](../../../changelog/)
  * [ Contributing ](../../../contributing/)
  * [ API Reference ](../../../api_reference/)

Toggle child pages in navigation

_ _

    * [ Top Level APIs ](../../../api_reference/top_level/)
    * [ Internal ](../../../api_reference/internal/)

Toggle child pages in navigation

_ _

      * [ Client ](../../../api_reference/internal/client/)

Toggle child pages in navigation

_ _

        * [ Base ](../../../api_reference/internal/client/base/)
        * [ Sync ](../../../api_reference/internal/client/sync/)
        * [ Async_ ](../../../api_reference/internal/client/async_/)
      * [ Contrib ](../../../api_reference/internal/contrib/)

Toggle child pages in navigation

_ _

        * [ Plotly ](../../../api_reference/internal/contrib/plotly/)
        * [ Dash ](../../../api_reference/internal/contrib/dash/)
      * [ Pagination ](../../../api_reference/internal/pagination/)

Toggle child pages in navigation

_ _

        * [ Strategies ](../../../api_reference/internal/pagination/strategies/)
        * [ Preprocess ](../../../api_reference/internal/pagination/preprocess/)
        * [ Pagination ](../../../api_reference/internal/pagination/pagination/)
        * [ Utils ](../../../api_reference/internal/pagination/utils/)
      * [ Transform ](../../../api_reference/internal/transform/)

Toggle child pages in navigation

_ _

        * [ ABCs ](../../../api_reference/internal/transform/abcs/)
        * [ Apply ](../../../api_reference/internal/transform/apply/)
        * [ Defaults ](../../../api_reference/internal/transform/defaults/)
        * [ Transforms ](../../../api_reference/internal/transform/transforms/)
        * [ Utils ](../../../api_reference/internal/transform/utils/)
      * [ Subgraph ](../../../api_reference/internal/subgraph/)

Toggle child pages in navigation

_ _

        * [ Fieldpath ](../../../api_reference/internal/subgraph/fieldpath/)
        * [ Filter ](../../../api_reference/internal/subgraph/filter/)
        * [ Object ](../../../api_reference/internal/subgraph/object/)
        * [ Subgraph ](../../../api_reference/internal/subgraph/subgraph/)
      * [ Errors ](../../../api_reference/internal/errors/)
      * [ Query ](../../../api_reference/internal/query/)
      * [ Schema ](../../../api_reference/internal/schema/)
      * [ Utils ](../../../api_reference/internal/utils/)

Meta

  * [ Improving the Docs ](../../../../meta/contributing/)

Back to top

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

_ _

#  Plotly  #

_New in version` 1.4.0  ` _

The Subgrounds Plotly Wrapper is an extension of the Plotly components to
understand and work seamlessly with the Subgrounds library. It provides a
convenient way to visualize data fetched from subgraphs using Plotly, by
wrapping Plotly's trace components with additional functionality.

**Resources**

  * [ Plotly Docs ](https://plotly.com/python/)

Run code

##  Getting Started  #

To start using the Subgrounds Plotly Wrapper, you'll need to import the
required components:

    
    
    from subgrounds import Subgrounds
    from subgrounds.contrib.plotly import Figure, Indicator
    

Next, load your subgraph using the Subgrounds library:

    
    
    sg = Subgrounds()
    aave_v2 = sg.load_subgraph("https://api.thegraph.com/subgraphs/name/messari/aave-v2-ethereum")
    

Now, you can create a Figure instance with the appropriate traces:

    
    
    Figure(
        subgrounds=sg,
        traces=[
            Indicator(value=pair.token0Price),
        ],
    )
    

##  Examples  #

Here are some code examples demonstrating how to use the Subgrounds Plotly
Wrapper:

###  Simple Indcator  #

An indicator for the price of a token  #

    
    
    from subgrounds import Subgrounds
    from subgrounds.contrib.plotly import Figure, Indicator
    
    sg = Subgrounds()
    aave_v2 = sg.load_subgraph("https://api.thegraph.com/subgraphs/name/messari/aave-v2-ethereum")
    
    Figure(
        subgrounds=sg,
        traces=[
            Indicator(value=pair.token0Price),
        ],
    )
    

###  Scatter and Bar Plots  #

Scatter and bar plots across a months worth of data  #

    
    
    from datetime import datetime
    
    import pandas as pd
    
    from subgrounds import FieldPath, Subgrounds, SyntheticField
    from subgrounds.contrib.plotly import Figure, Scatter, Bar
    
    sg = Subgrounds()
    
    lido_activity = sg.load_subgraph(
        "https://api.thegraph.com/subgraphs/name/messari/lido-ethereum"
    )
    
    usage_daily_snapshot_30days = lido_activity.Query.usageMetricsDailySnapshots(
        orderBy=lido_activity.UsageMetricsDailySnapshot.timestamp,
        orderDirection="desc",
        first=30,
    )
    
    daily_snapshot = lido_activity.UsageMetricsDailySnapshot
    
    daily_snapshot.datetime = SyntheticField.datetime_of_timestamp(
        daily_snapshot.timestamp
    )
    
    # Create the Scatter trace with appropriate field paths
    trace = Scatter(
        x=usage_daily_snapshot_30days.datetime,
        y=usage_daily_snapshot_30days.dailyActiveUsers,
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
    
    # Create the Bar trace with appropriate field paths:
    trace2 = Bar(
        x=usage_daily_snapshot_30days.datetime,
        y=usage_daily_snapshot_30days.dailyTransactionCount,
    )
    
    # Create the Figure instance with the trace and display it:
    fig2 = Figure(
        subgrounds=sg,
        traces=trace2,
        layout=dict(
            title="Daily Transaction Count",
            xaxis=dict(title="Datetime"),
            yaxis=dict(title="Daily Transaction Count")
        ),
    )
    

Show figure 1  #

    
    
    fig.figure.show()
    

Show figure 2  #

    
    
    fig2.figure.show()
    

In this example, we first load a subgraph and fetch data for the past 30 days.
We then create a synthetic field to convert the timestamp into a datetime
object. Next, we create a Scatter trace and a Bar trace with the appropriate
field paths. Finally, we create two Figure instances and display them.

With the Subgrounds Plotly Wrapper, you can easily extend the provided classes
to support more Plotly trace types and create custom visualizations for your
subgraph data.

[ Next  Pagination  ](../../pagination/) [ Previous  Contrib  ](../)

Made with [ Furo ](https://github.com/pradyunsg/furo)

[ ](https://github.com/0xPlaygrounds/subgrounds) [
](https://discord.gg/v4r4zhBAh2) [ ](https://twitter.com/Playgrounds0x)

On this page

  * Plotly 
    * Getting Started 
    * Examples 
      * Simple Indcator 
      * Scatter and Bar Plots 



Contents  Menu  Expand  Light mode  Dark mode  Auto light/dark mode

Hide navigation sidebar

Hide table of contents sidebar

Give us a ⭐️ on [ Github ](https://github.com/0xPlaygrounds/subgrounds)

Toggle site navigation sidebar

_ _

[ Playgrounds  ](../../../)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

_ _

[ ![Light Logo](../../../_static/assets/pg-logotype-dark.svg) ![Dark
Logo](../../../_static/assets/pg-logotype-primary.svg)
](https://playgrounds.network)

Playgrounds API

  * [ Overview ](../../../api/)
  * [ Getting an API Key ](../../../api/key/)
  * [ Subgraph Proxy ](../../../api/subgraph-proxy/)
  * [ Subgrounds Integration ](../../../api/subgrounds/)
  * [ FAQ ](../../../api/faq/)

Toggle child pages in navigation

_ _

    * [ What is a Query? ](../../../api/faq/query/)
  * [ API Reference ](../../../api/api-reference/)

Toggle child pages in navigation

_ _

    * [ Subgraph Proxy ](../../../api/reference/proxy/)

Toggle child pages in navigation

_ _

      * [ Subgraph ID ](../../../api/reference/proxy/subgraph_id/)
      * [ Deployment ID ](../../../api/reference/proxy/deployment_id/)

Subgrounds

  * [ Overview ](../../)
  * [ Getting Started ](../../getting_started/)

Toggle child pages in navigation

_ _

    * [ The Basics ](../../getting_started/basics/)
    * [ Field Paths ](../../getting_started/field_paths/)

Toggle child pages in navigation

_ _

      * [ Arguments ](../../getting_started/field_paths/arguments/)
      * [ Filtering ](../../getting_started/field_paths/filtering/)
      * [ Sorting ](../../getting_started/field_paths/sorting/)
      * [ Merging ](../../getting_started/field_paths/merging/)
    * [ Querying ](../../getting_started/querying/)

Toggle child pages in navigation

_ _

    * [ Synthetic Fields ](../../getting_started/synthetic_fields/)
  * [ Advanced Topics ](../../advanced_topics/)

Toggle child pages in navigation

_ _

    * [ Contrib ](../../advanced_topics/contrib/)

Toggle child pages in navigation

_ _

      * [ Plotly ](../../advanced_topics/contrib/plotly/)
    * [ Pagination ](../../advanced_topics/pagination/)

Toggle child pages in navigation

_ _

      * [ Custom Strategies ](../../advanced_topics/pagination/custom/)
  * [ FAQ ](../../faq/)

Toggle child pages in navigation

_ _

    * [ Exporting to Disk ](../../faq/exporting/)
    * [ Getting More Data ](../../faq/more_data/)
    * [ Python Setup ](../../faq/setup/)

Toggle child pages in navigation

_ _

      * [ Python Versioning ](../../faq/setup/version_management/)
  * [ Examples ](../../examples/)

Toggle child pages in navigation

_ _

    * [ Exchanges ](../../examples/exchanges/)
    * [ Bridges ](../../examples/bridges/)
    * [ Liquid Staking ](../../examples/liquid_staking/)
    * [ Governance ](../../examples/governance/)
    * [ Advanced Research ](../../examples/advanced_research/)
    * [ Vaults ](../../examples/vaults/)
  * [ Videos ](../../videos/)
  * [ Changelog ](../../changelog/)
  * [ Contributing ](../../contributing/)
  * [ API Reference ](../)

Toggle child pages in navigation

_ _

    * Top Level APIs 
    * [ Internal ](../internal/)

Toggle child pages in navigation

_ _

      * [ Client ](../internal/client/)

Toggle child pages in navigation

_ _

        * [ Base ](../internal/client/base/)
        * [ Sync ](../internal/client/sync/)
        * [ Async_ ](../internal/client/async_/)
      * [ Contrib ](../internal/contrib/)

Toggle child pages in navigation

_ _

        * [ Plotly ](../internal/contrib/plotly/)
        * [ Dash ](../internal/contrib/dash/)
      * [ Pagination ](../internal/pagination/)

Toggle child pages in navigation

_ _

        * [ Strategies ](../internal/pagination/strategies/)
        * [ Preprocess ](../internal/pagination/preprocess/)
        * [ Pagination ](../internal/pagination/pagination/)
        * [ Utils ](../internal/pagination/utils/)
      * [ Transform ](../internal/transform/)

Toggle child pages in navigation

_ _

        * [ ABCs ](../internal/transform/abcs/)
        * [ Apply ](../internal/transform/apply/)
        * [ Defaults ](../internal/transform/defaults/)
        * [ Transforms ](../internal/transform/transforms/)
        * [ Utils ](../internal/transform/utils/)
      * [ Subgraph ](../internal/subgraph/)

Toggle child pages in navigation

_ _

        * [ Fieldpath ](../internal/subgraph/fieldpath/)
        * [ Filter ](../internal/subgraph/filter/)
        * [ Object ](../internal/subgraph/object/)
        * [ Subgraph ](../internal/subgraph/subgraph/)
      * [ Errors ](../internal/errors/)
      * [ Query ](../internal/query/)
      * [ Schema ](../internal/schema/)
      * [ Utils ](../internal/utils/)

Meta

  * [ Improving the Docs ](../../../meta/contributing/)

Back to top

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

_ _

#  Top Level APIs  #

This page outlines the api-reference describing all of the APIs that are
exported at the top-level of ` subgrounds  ` — aka, APIs for the majority of
users.

##  Clients  #

This is your main entrypoint for using ` Subgrounds  ` as all aspects of the
subgrounds logic is integrated through these clients.

_ class  _ subgrounds.  Subgrounds  (  _ headers:  dict[str  _ , _ typing.Any]
=  <factory> _ , _ global_transforms:
list[subgrounds.transform.RequestTransform]  =  <factory> _ , _ subgraphs:
dict[str  _ , _ subgrounds.subgraph.subgraph.Subgraph]  =  <factory> _ )  #

    

Bases: [ ` object  ` ](https://docs.python.org/3/library/functions.html#object
"\(in Python v3.11\)")

load_subgraph  (  _ url  _ , _ save_schema  =  False  _ , _ cache_dir  =
'schemas/'  _ )  #

    

Performs introspection on the provided GraphQL API ` url  ` to get the schema,
stores the schema if ` save_schema  ` is ` True  ` and returns a generated
class representing the subgraph with all its entities.

Parameters  :

    

  * **url** ( [ _str_ ](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.11\)") ) -- The url of the API 

  * **save_schema** ( [ _bool_ ](https://docs.python.org/3/library/functions.html#bool "\(in Python v3.11\)") _,_ _optional_ ) -- Flag indicating whether or not the schema should be cached to disk. Defaults to False. 

  * **cache_dir** ( [ _str_ ](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.11\)") _,_ _optional_ ) -- If ` save_schema  ==  True  ` , then subgraph schemas will be stored under ` cache_dir  ` . Defaults to ` schemas/  `

Returns  :

    

A generated class representing the subgraph and its entities

Return type  :

    

Subgraph

load_api  (  _ url  _ , _ save_schema  =  False  _ , _ cache_dir  =
'schemas/'  _ )  #

    

Performs introspection on the provided GraphQL API ` url  ` to get the schema,
stores the schema if ` save_schema  ` is ` True  ` and returns a generated
class representing the GraphQL endpoint with all its entities.

Parameters  :

    

  * **url** ( [ _str_ ](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.11\)") ) -- The url of the API 

  * **save_schema** ( [ _bool_ ](https://docs.python.org/3/library/functions.html#bool "\(in Python v3.11\)") _,_ _optional_ ) -- Flag indicating whether or not the schema should be saved to disk. Defaults to False. 

Returns  :

    

A generated class representing the subgraph and its entities

Return type  :

    

Subgraph

mk_request  (  _ fpaths  _ )  #

    

Creates a ` DataRequest  ` object by combining one or more  ` FieldPath  `
objects.

Parameters  :

    

**fpaths** (  _FieldPath_ _|_ [ _list_
](https://docs.python.org/3/library/stdtypes.html#list "\(in Python v3.11\)")
_[_ _FieldPath_ _]_ ) -- One or more  ` FieldPath  ` objects that should be
included in the request

Returns  :

    

A new ` DataRequest  ` object

Return type  :

    

[ DataRequest ](../internal/query/#subgrounds.query.DataRequest
"subgrounds.query.DataRequest")

execute  (  _ req  _ , _ pagination_strategy  =  LegacyStrategy  _ )  #

    

Executes a ` DataRequest  ` object, sending the underlying query(ies) to the
server and returning a data blob (list of Python dictionaries, one per actual
query).

Parameters  :

    

  * **req** ( [ _DataRequest_ ](../internal/query/#subgrounds.query.DataRequest "subgrounds.query.DataRequest") ) -- The ` DataRequest  ` object to be executed 

  * **pagination_strategy** ( _Optional_ _[_ _Type_ _[_ [ _PaginationStrategy_ ](../internal/pagination/#subgrounds.pagination.PaginationStrategy "subgrounds.pagination.PaginationStrategy") _]_ _]_ _,_ _optional_ ) -- A Class implementing the ` PaginationStrategy  ` ` Protocol  ` . If ` None  ` , then automatic pagination is disabled. Defaults to ` LegacyStrategy  ` . 

Returns  :

    

The reponse data

Return type  :

    

[ list ](https://docs.python.org/3/library/stdtypes.html#list "\(in Python
v3.11\)") [ [ dict ](https://docs.python.org/3/library/stdtypes.html#dict
"\(in Python v3.11\)") ]

execute_iter  (  _ req  _ , _ pagination_strategy  =  LegacyStrategy  _ )  #

    

Same as  execute  , except that an iterator is returned which will iterate the
data pages.

Parameters  :

    

  * **req** ( [ _DataRequest_ ](../internal/query/#subgrounds.query.DataRequest "subgrounds.query.DataRequest") ) -- The ` DataRequest  ` object to be executed 

  * **pagination_strategy** ( _Optional_ _[_ _Type_ _[_ [ _PaginationStrategy_ ](../internal/pagination/#subgrounds.pagination.PaginationStrategy "subgrounds.pagination.PaginationStrategy") _]_ _]_ _,_ _optional_ ) -- A Class implementing the ` PaginationStrategy  ` ` Protocol  ` . If ` None  ` , then automatic pagination is disabled. Defaults to ` LegacyStrategy  ` . 

Returns  :

    

An iterator over the reponse data pages

Return type  :

    

Iterator[ [ dict ](https://docs.python.org/3/library/stdtypes.html#dict "\(in
Python v3.11\)") ]

query_json  (  _ fpaths  _ , _ pagination_strategy  =  LegacyStrategy  _ )  #

    

Equivalent to ` Subgrounds.execute(Subgrounds.mk_request(fpaths),
pagination_strategy)  ` .

Parameters  :

    

  * **fpaths** (  _FieldPath_ _|_ [ _list_ ](https://docs.python.org/3/library/stdtypes.html#list "\(in Python v3.11\)") _[_ _FieldPath_ _]_ ) -- One or more  ` FieldPath  ` objects that should be included in the request. 

  * **pagination_strategy** ( _Optional_ _[_ _Type_ _[_ [ _PaginationStrategy_ ](../internal/pagination/#subgrounds.pagination.PaginationStrategy "subgrounds.pagination.PaginationStrategy") _]_ _]_ _,_ _optional_ ) -- A Class implementing the ` PaginationStrategy  ` ` Protocol  ` . If ` None  ` , then automatic pagination is disabled. Defaults to ` LegacyStrategy  ` . 

Returns  :

    

The reponse data

Return type  :

    

[ list ](https://docs.python.org/3/library/stdtypes.html#list "\(in Python
v3.11\)") [ [ dict ](https://docs.python.org/3/library/stdtypes.html#dict
"\(in Python v3.11\)") [ [ str
](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.11\)") ,
Any]]

query_json_iter  (  _ fpaths  _ , _ pagination_strategy  =  LegacyStrategy  _
)  #

    

Same as  query_json  except an iterator over the response data pages is
returned.

Parameters  :

    

  * **fpaths** (  _FieldPath_ _|_ [ _list_ ](https://docs.python.org/3/library/stdtypes.html#list "\(in Python v3.11\)") _[_ _FieldPath_ _]_ ) -- One or more  ` FieldPath  ` objects that should be included in the request. 

  * **pagination_strategy** ( _Optional_ _[_ _Type_ _[_ [ _PaginationStrategy_ ](../internal/pagination/#subgrounds.pagination.PaginationStrategy "subgrounds.pagination.PaginationStrategy") _]_ _]_ _,_ _optional_ ) -- A Class implementing the ` PaginationStrategy  ` ` Protocol  ` . If ` None  ` , then automatic pagination is disabled. Defaults to ` LegacyStrategy  ` . 

Returns  :

    

The reponse data

Return type  :

    

[ list ](https://docs.python.org/3/library/stdtypes.html#list "\(in Python
v3.11\)") [ [ dict ](https://docs.python.org/3/library/stdtypes.html#dict
"\(in Python v3.11\)") [ [ str
](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.11\)") ,
Any]]

query_df  (  _ fpaths  _ , _ columns  =  None  _ , _ concat  =  False  _ , _
pagination_strategy  =  LegacyStrategy  _ )  #

    

Same as  ` Subgrounds.query()  ` but formats the response data into a Pandas
DataFrame. If the response data cannot be flattened to a single query (e.g.:
when querying multiple list fields that return different entities), then
multiple dataframes are returned

` fpaths  ` is a list of  ` FieldPath  ` objects that indicate which data must
be queried.

` columns  ` is an optional argument used to rename the dataframes(s) columns.
The length of ` columns  ` must be the same as the number of columns of _all_
returned dataframes.

` concat  ` indicates whether or not the resulting dataframes should be
concatenated together. The dataframes must have the same number of columns, as
well as the same column names and types (the names can be set using the `
columns  ` argument).

Parameters  :

    

  * **fpaths** (  _FieldPath_ _|_ [ _list_ ](https://docs.python.org/3/library/stdtypes.html#list "\(in Python v3.11\)") _[_ _FieldPath_ _]_ ) -- One or more  FieldPath  objects that should be included in the request. 

  * **columns** ( _Optional_ _[_ [ _list_ ](https://docs.python.org/3/library/stdtypes.html#list "\(in Python v3.11\)") _[_ [ _str_ ](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.11\)") _]_ _]_ _,_ _optional_ ) -- The column labels. Defaults to None. 

  * **merge** ( [ _bool_ ](https://docs.python.org/3/library/functions.html#bool "\(in Python v3.11\)") _,_ _optional_ ) -- Whether or not to merge resulting dataframes. 

  * **pagination_strategy** ( _Optional_ _[_ _Type_ _[_ [ _PaginationStrategy_ ](../internal/pagination/#subgrounds.pagination.PaginationStrategy "subgrounds.pagination.PaginationStrategy") _]_ _]_ _,_ _optional_ ) -- A Class implementing the ` PaginationStrategy  ` ` Protocol  ` . If ` None  ` , then automatic pagination is disabled. Defaults to ` LegacyStrategy  ` . 

Returns  :

    

A DataFrame containing the reponse data

Return type  :

    

pd.DataFrame | [ list ](https://docs.python.org/3/library/stdtypes.html#list
"\(in Python v3.11\)") [pd.DataFrame]

Example:

    
    
    >>> from subgrounds import Subgrounds
    >>> sg = Subgrounds()
    >>> univ3 = sg.load_subgraph('https://api.thegraph.com/subgraphs/name/uniswap/uniswap-v3')
    
    # Define price SyntheticField
    >>> univ3.Swap.price = abs(univ3.Swap.amount0) / abs(univ3.Swap.amount1)
    
    # Query last 10 swaps from the ETH/USDC pool
    >>> eth_usdc = univ3.Query.swaps(
    ...     orderBy=univ3.Swap.timestamp,
    ...     orderDirection='desc',
    ...     first=10,
    ...     where=[
    ...         univ3.Swap.pool == '0x8ad599c3a0ff1de082011efddc58f1908eb6e6d8'
    ...     ]
    ... )
    >>> sg.query_df([
    ...     eth_usdc.timestamp,
    ...     eth_usdc.price
    ... ])
      swaps_timestamp  swaps_price
    0       1643213811  2618.886394
    1       1643213792  2618.814281
    2       1643213792  2617.500494
    3       1643213763  2615.458495
    4       1643213763  2615.876574
    5       1643213739  2615.352390
    6       1643213678  2615.205713
    7       1643213370  2614.115746
    8       1643213210  2613.077301
    9       1643213196  2610.686563
    

query_df_iter  (  _ fpaths  _ , _ pagination_strategy  =  LegacyStrategy  _ )
#

    

Same as  query_df  except an iterator over the response data pages is returned
:param fpaths: One or more  FieldPath  objects that

> should be included in the request

Parameters  :

    

  * **columns** ( _Optional_ _[_ [ _list_ ](https://docs.python.org/3/library/stdtypes.html#list "\(in Python v3.11\)") _[_ [ _str_ ](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.11\)") _]_ _]_ _,_ _optional_ ) -- The column labels. Defaults to None. 

  * **merge** ( [ _bool_ ](https://docs.python.org/3/library/functions.html#bool "\(in Python v3.11\)") _,_ _optional_ ) -- Whether or not to merge resulting dataframes. 

  * **pagination_strategy** ( _Optional_ _[_ _Type_ _[_ [ _PaginationStrategy_ ](../internal/pagination/#subgrounds.pagination.PaginationStrategy "subgrounds.pagination.PaginationStrategy") _]_ _]_ _,_ _optional_ ) -- A Class implementing the ` PaginationStrategy  ` ` Protocol  ` . If ` None  ` , then automatic pagination is disabled. Defaults to ` LegacyStrategy  ` . 

Returns  :

    

An iterator over the response data pages, each as a DataFrame

Return type  :

    

Iterator[pd.DataFrame]

query  (  _ fpaths  _ , _ unwrap  =  True  _ , _ pagination_strategy  =
LegacyStrategy  _ )  #

    

Executes one or multiple ` FieldPath  ` objects immediately and return the
data (as a tuple if multiple ` FieldPath  ` objects are provided).

Parameters  :

    

  * **fpaths** (  _FieldPath_ _|_ [ _list_ ](https://docs.python.org/3/library/stdtypes.html#list "\(in Python v3.11\)") _[_ _FieldPath_ _]_ ) -- One or more ` FieldPath  ` object(s) to query. 

  * **unwrap** ( [ _bool_ ](https://docs.python.org/3/library/functions.html#bool "\(in Python v3.11\)") _,_ _optional_ ) -- Flag indicating whether or not, in the case where the returned data is a list of one element, the element itself should be returned instead of the list. Defaults to ` True  ` . 

  * **pagination_strategy** ( _Optional_ _[_ _Type_ _[_ [ _PaginationStrategy_ ](../internal/pagination/#subgrounds.pagination.PaginationStrategy "subgrounds.pagination.PaginationStrategy") _]_ _]_ _,_ _optional_ ) -- A Class implementing the ` PaginationStrategy  ` ` Protocol  ` . If ` None  ` , then automatic pagination is disabled. Defaults to ` LegacyStrategy  ` . 

Returns  :

    

The ` FieldPath  ` object(s) data

Return type  :

    

[ [ type ](https://docs.python.org/3/library/functions.html#type "\(in Python
v3.11\)") ]

Example:

    
    
    >>> from subgrounds import Subgrounds
    >>> sg = Subgrounds()
    >>> univ3 = sg.load_subgraph('https://api.thegraph.com/subgraphs/name/uniswap/uniswap-v3')
    
    # Define price SyntheticField
    >>> univ3.Swap.price = abs(univ3.Swap.amount0) / abs(univ3.Swap.amount1)
    
    # Construct FieldPath to get price of last swap on ETH/USDC pool
    >>> eth_usdc_last = univ3.Query.swaps(
    ...     orderBy=univ3.Swap.timestamp,
    ...     orderDirection='desc',
    ...     first=1,
    ...     where=[
    ...         univ3.Swap.pool == '0x8ad599c3a0ff1de082011efddc58f1908eb6e6d8'
    ...     ]
    ... ).price
    
    # Query last price FieldPath
    >>> sg.query(eth_usdc_last)
    2628.975030015892
    

query_iter  (  _ fpaths  _ , _ unwrap  =  True  _ , _ pagination_strategy  =
LegacyStrategy  _ )  #

    

Same as  query  except an iterator over the resonse data pages is returned.

Parameters  :

    

  * **fpath** (  _FieldPath_ _|_ [ _list_ ](https://docs.python.org/3/library/stdtypes.html#list "\(in Python v3.11\)") _[_ _FieldPath_ _]_ ) -- One or more ` FieldPath  ` object(s) to query. 

  * **unwrap** ( [ _bool_ ](https://docs.python.org/3/library/functions.html#bool "\(in Python v3.11\)") _,_ _optional_ ) -- Flag indicating whether or not, in the case where the returned data is a list of one element, the element itself should be returned instead of the list. Defaults to ` True  ` . 

  * **pagination_strategy** ( _Optional_ _[_ _Type_ _[_ [ _PaginationStrategy_ ](../internal/pagination/#subgrounds.pagination.PaginationStrategy "subgrounds.pagination.PaginationStrategy") _]_ _]_ _,_ _optional_ ) -- A Class implementing the ` PaginationStrategy  ` ` Protocol  ` . If ` None  ` , then automatic pagination is disabled. Defaults to ` LegacyStrategy  ` . 

Returns  :

    

An iterator over the ` FieldPath  ` object(s)' data pages

Return type  :

    

Iterator[ [ type ](https://docs.python.org/3/library/functions.html#type "\(in
Python v3.11\)") ]

##  Subgraph Utilities  #

_ class  _ subgrounds.  Subgraph  (  _ url:  'str',  schema:  'SchemaMeta',
transforms:  'list[DocumentTransform]'  =
[<subgrounds.transform.TypeTransform  object  at  0x7fba98ae0580>,
<subgrounds.transform.TypeTransform  object  at  0x7fba98ae0640>],
is_subgraph:  'bool'  =  True  _ )  #

    

_ class  _ subgrounds.  FieldPath  (  _ subgraph  :  'Subgraph'  _ , _
root_type  :  'TypeRef.T'  _ , _ type_  :  'TypeRef.T'  _ , _ path  :
'list[Tuple[Optional[dict[str,  Any]],  TypeMeta.FieldMeta]]'  _ )  #

    

_ class  _ subgrounds.  SyntheticField  (  _ f  :  'Callable'  _ , _ type_  :
'TypeRef.T'  _ , _ deps  :  'list[FieldPath  |  SyntheticField]  |  FieldPath
|  SyntheticField'  _ , _ default  :  'Any'  =  None  _ )  #

    

_ static  _ constant  (  _ value  _ )  #

    

Returns a constant ` SyntheticField  ` with value ` value  ` . Useful for
injecting additional static data to a schema or merging entities.

Parameters  :

    

**value** ( [ _str_ ](https://docs.python.org/3/library/stdtypes.html#str
"\(in Python v3.11\)") _|_ [ _int_
](https://docs.python.org/3/library/functions.html#int "\(in Python v3.11\)")
_|_ [ _float_ ](https://docs.python.org/3/library/functions.html#float "\(in
Python v3.11\)") _|_ [ _bool_
](https://docs.python.org/3/library/functions.html#bool "\(in Python v3.11\)")
) -- The constant field's value

Returns  :

    

The constant ` SyntheticField  `

Return type  :

    

SyntheticField

Example:

    
    
    >>> from subgrounds.subgrounds import Subgrounds
    >>> from subgrounds.subgraph import SyntheticField
    >>> sg = Subgrounds()
    >>> univ3 = sg.load_subgraph(
    ...     'https://api.thegraph.com/subgraphs/name/uniswap/uniswap-v3'
    ... )
    
    # Create constant SyntheticFields
    >>> univ3.Mint.tx_type = SyntheticField.constant('MINT')
    >>> univ3.Burn.tx_type = SyntheticField.constant('BURN')
    
    # Last 10 mints and burns
    >>> mints = univ3.Query.mints(
    ...     first=10,
    ...     orderBy=univ3.Mint.timestamp,
    ...     orderDirection='desc'
    ... )
    >>> burns = univ3.Query.burns(
    ...     first=10,
    ...     orderBy=univ3.Burn.timestamp,
    ...     orderDirection='desc'
    ... )
    
    # Query mints and burns. Notice that we merge the two entity tables by
    # setting `concat=True` and overwriting the column names (columns must
    # match the `FieldPaths`)
    >>> df = sg.query_df([
    ...     mints.transaction.id,
    ...     mints.timestamp,
    ...     mints.tx_type,
    ...     mints.origin,
    ...     mints.amountUSD,
    ...     burns.transaction.id,
    ...     burns.timestamp,
    ...     burns.tx_type,
    ...     burns.origin,
    ...     burns.amountUSD,
    ... ], columns=['tx_hash', 'timestamp', 'tx_type', 'origin', 'amount_USD'], concat=True)
    
    # Sort the DataFrame
    >>> df.sort_values(by=['timestamp'], ascending=False)
                                                  tx_hash   timestamp tx_type                                      origin    amount_USD
    0   0xcbe1bacacc1e64fe613ae5eef2063563bd0057d1e3df...  1656016553    MINT  0x3435e7946d40b1a83c0cf154326fc6b3ca908952  7.879784e+03
    1   0xdddaaddf59e5a3abff4feadef83b3ceb023a74424ea7...  1656016284    MINT  0xc747962e7e416e2a582813b1d7ad59eb83077fa6  5.110840e+04
    10  0xa7671452c34a3b083083ef81e364489c2c9ee801a3b8...  1656016284    BURN  0xd40db77990bbb30514276b5ac17c3ce5cc9c951f  2.804573e+05
    2   0xc132e73975e77c2c2c91fcf332018dfb01aac0ca9471...  1656015853    MINT  0xc747962e7e416e2a582813b1d7ad59eb83077fa6  5.122569e+04
    3   0x1444744f4021a2046787c1b7b88cd9ac21f071c65acc...  1656015773    MINT  0xd11aa2e3a000275ed12b87515c9ac0d67b32e7b9  8.897983e+03
    4   0x3315617d426fc2b0db5d8dbccd549efaa8f1ae2969ca...  1656015693    MINT  0xb7dd4d134b1794ee848e1af1a62b85d7b2ea9301  0.000000e+00
    11  0xcc713daa2dc58cd1f2218c8f438e7fcf04d2e9c7c83d...  1656015278    BURN  0xa7c43e2057d89b6946b8865efc8bee3a4ea7d28d  1.254942e+06
    5   0x7bbfae86f0c3c983651bd0671557cd851fc301317c06...  1656015111    MINT  0xac56cee8ccd00d0c1d72ce3415140874552e80f4  3.432075e+04
    12  0xea21c3a68a8f0c6a2721a3072e0c8b2edc77f4d2f0d9...  1656014785    BURN  0x0709b103d46d71458a71e5d81230dd688809a53d  2.059106e+04
    6   0x3bd369bf45c55cab40c62db81bb3e0684fd85fe2b662...  1656014120    MINT  0x509984bfc0fb24e2d1377cfec224d3afec4c341e  2.517578e+03
    13  0x1ea59da77c442479af8fb51501a931260d473e249de7...  1656014018    BURN  0x509984bfc0fb24e2d1377cfec224d3afec4c341e  0.000000e+00
    7   0xb9d31ef78b8bf786b422d948dd1fba246710078abff8...  1656013998    MINT  0x22dfec183294d257f80c15d3c9cd47495bdc728c  8.365750e+04
    14  0xc5e3ec84a2860e3c3a055ccdced435a67b4aff4dd3be...  1656013946    BURN  0xac56cee8ccd00d0c1d72ce3415140874552e80f4  3.363809e+04
    8   0x7c736255d9a4ebf4781069a1b2a929ad89100f1af980...  1656013913    MINT  0x4ce6aea89f059915ae5efbf34a2a8adc544ae09e  4.837287e+04
    15  0x95cf56b9eb69aa45048a9b7b3e472df5bc3bfad591cd...  1656013728    BURN  0x4ce6aea89f059915ae5efbf34a2a8adc544ae09e  5.110010e+04
    9   0x76dd2bbf43485c224471dd823c2992178f031f27194b...  1656013599    MINT  0x234a644868c419ce0dcdd9fd539762eba47f3759  5.363896e+03
    16  0x47e595b02fdcb51ff42a5008e53be7ee3bdf8063b580...  1656013580    BURN  0xaf0fdd39e5d92499b0ed9f68693da99c0ec1e92e  0.000000e+00
    17  0xe20ec9702f455d74b3cc1f54fe2f3450604ca5037a72...  1656013455    BURN  0xaf0fdd39e5d92499b0ed9f68693da99c0ec1e92e  0.000000e+00
    18  0xac3e95666be3a45fdfbbfa513a114136ea6ecffb9de2...  1656013237    BURN  0x665d2d2444f2384fb3d96aaa0ea3536b92984dce  2.254100e+05
    19  0x01c3424a48c36104ea388482723347f15c0bc1bb1a80...  1656013034    BURN  0x0084ee6c8893c01e252198b56ec127443dc27464  0.000000e+00
    

_ static  _ datetime_of_timestamp  (  _ timestamp  _ )  #

    

Returns a ` SyntheticField  ` that will transform the ` FieldPath  ` `
timestamp  ` into a human-readable ISO8601 string.

Parameters  :

    

**timestamp** (  _FieldPath_ _|_ _SyntheticField_ ) -- A ` FieldPath  `
representing a Unix timestamp field.

Returns  :

    

An ISO8601 datetime string ` SyntheticField  ` .

Return type  :

    

SyntheticField

Example:

    
    
    >>> from subgrounds.subgrounds import Subgrounds
    >>> from subgrounds.subgraph import SyntheticField
    >>> sg = Subgrounds()
    >>> univ3 = sg.load_subgraph(
    ...     'https://api.thegraph.com/subgraphs/name/uniswap/uniswap-v3'
    ... )
    
    # Create datetime SyntheticField
    >>> univ3.Swap.datetime = SyntheticField.datetime_of_timestamp(univ3.Swap.timestamp)
    
    # Query 100 swaps
    >>> sg.query_df([
    ...     univ3.Query.swaps.timestamp,
    ...     univ3.Query.swaps.datetime,
    ... ])
        swaps_timestamp       swaps_datetime
    0        1625105710  2021-06-30 22:15:10
    1        1629253724  2021-08-17 22:28:44
    2        1647333277  2022-03-15 04:34:37
    3        1630801974  2021-09-04 20:32:54
    4        1653240241  2022-05-22 13:24:01
    ..              ...                  ...
    95       1646128326  2022-03-01 04:52:06
    96       1646128326  2022-03-01 04:52:06
    97       1626416555  2021-07-16 02:22:35
    98       1626416555  2021-07-16 02:22:35
    99       1625837291  2021-07-09 09:28:11
    

_ static  _ map  (  _ dict  _ , _ type_  _ , _ fpath  _ , _ default  =  None
_ )  #

    

Returns a SyntheticField that will map the values of ` fpath  ` using the key
value pairs in ` dict  ` . If a value is not in the dictionary, then ` default
` will be used instead.

Parameters  :

    

  * **dict** ( [ _dict_ ](https://docs.python.org/3/library/stdtypes.html#dict "\(in Python v3.11\)") _[_ _Any_ _,_ _Any_ _]_ ) -- The dictionary containing the key value pairs used to map ` fpath  ` 's values 

  * **type** ( _TypeRef.T_ ) -- The type of the resulting field 

  * **fpath** (  _FieldPath_ _|_ _SyntheticField_ ) -- The FieldPath whose values will be mapped using the dictionary 

  * **default** ( _Optional_ _[_ _Any_ _]_ ) -- Default value used when a value is not in the provided dictionary 

Returns  :

    

A map SyntheticField

Return type  :

    

SyntheticField

Example:

    
    
    >>> from subgrounds.subgrounds import Subgrounds
    >>> from subgrounds.subgraph import SyntheticField
    >>> sg = Subgrounds()
    >>> univ3 = sg.load_subgraph(
    ...     'https://api.thegraph.com/subgraphs/name/uniswap/uniswap-v3'
    ... )
    
    # Hand-crafted mapping of pool addresses to symbol
    >>> pooladdr_symbol_map = {
    ...     '0x5777d92f208679db4b9778590fa3cab3ac9e2168': 'DAI/USDC-001',
    ...     '0x6c6bc977e13df9b0de53b251522280bb72383700': 'DAI/USDC-005',
    ...     '0x8ad599c3a0ff1de082011efddc58f1908eb6e6d8': 'USDC/ETH-030',
    ...     '0x88e6a0c2ddd26feeb64f039a2c41296fcb3f5640': 'USDC/ETH-005',
    ... }
    
    # Create map SyntheticField using our dictionary with 'UNKNOWN' as the
    # default value
    >>> univ3.Pool.symbol = SyntheticField.map(
    ...     pooladdr_symbol_map,
    ...     SyntheticField.STRING,
    ...     univ3.Pool.id,
    ...     'UNKNOWN'
    ... )
    
    # Query top 10 pools by TVL
    >>> pools = univ3.Query.pools(
    ...     first=10,
    ...     orderBy=univ3.Pool.totalValueLockedUSD,
    ...     orderDirection='desc'
    ... )
    >>> sg.query_df([
    ...     pools.id,
    ...     pools.symbol
    ... ])
                                         pools_id  pools_symbol
    0  0xa850478adaace4c08fc61de44d8cf3b64f359bec       UNKNOWN
    1  0x5777d92f208679db4b9778590fa3cab3ac9e2168  DAI/USDC-001
    2  0x6c6bc977e13df9b0de53b251522280bb72383700  DAI/USDC-005
    3  0x8ad599c3a0ff1de082011efddc58f1908eb6e6d8  USDC/ETH-030
    4  0x88e6a0c2ddd26feeb64f039a2c41296fcb3f5640  USDC/ETH-005
    5  0x3416cf6c708da44db2624d63ea0aaef7113527c6       UNKNOWN
    6  0xcbcdf9626bc03e24f779434178a73a0b4bad62ed       UNKNOWN
    7  0xc63b0708e2f7e69cb8a1df0e1389a98c35a76d52       UNKNOWN
    8  0x4585fe77225b41b697c938b018e2ac67ac5a20c0       UNKNOWN
    9  0x4e68ccd3e89f51c3074ca5072bbac773960dfa36       UNKNOWN
    

[ Next  Internal  ](../internal/) [ Previous  API Reference  ](../)

Made with [ Furo ](https://github.com/pradyunsg/furo)

[ ](https://github.com/0xPlaygrounds/subgrounds) [
](https://discord.gg/v4r4zhBAh2) [ ](https://twitter.com/Playgrounds0x)

On this page

  * Top Level APIs 
    * Clients 
      * ` Subgrounds  `
        * ` Subgrounds.load_subgraph()  `
        * ` Subgrounds.load_api()  `
        * ` Subgrounds.mk_request()  `
        * ` Subgrounds.execute()  `
        * ` Subgrounds.execute_iter()  `
        * ` Subgrounds.query_json()  `
        * ` Subgrounds.query_json_iter()  `
        * ` Subgrounds.query_df()  `
        * ` Subgrounds.query_df_iter()  `
        * ` Subgrounds.query()  `
        * ` Subgrounds.query_iter()  `
    * Subgraph Utilities 
      * ` Subgraph  `
      * ` FieldPath  `
      * ` SyntheticField  `
        * ` SyntheticField.constant()  `
        * ` SyntheticField.datetime_of_timestamp()  `
        * ` SyntheticField.map()  `



Contents  Menu  Expand  Light mode  Dark mode  Auto light/dark mode

Hide navigation sidebar

Hide table of contents sidebar

Give us a ⭐️ on [ Github ](https://github.com/0xPlaygrounds/subgrounds)

Toggle site navigation sidebar

_ _

[ Playgrounds  ](../../../)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

_ _

[ ![Light Logo](../../../_static/assets/pg-logotype-dark.svg) ![Dark
Logo](../../../_static/assets/pg-logotype-primary.svg)
](https://playgrounds.network)

Playgrounds API

  * [ Overview ](../../../api/)
  * [ Getting an API Key ](../../../api/key/)
  * [ Subgraph Proxy ](../../../api/subgraph-proxy/)
  * [ Subgrounds Integration ](../../../api/subgrounds/)
  * [ FAQ ](../../../api/faq/)

Toggle child pages in navigation

_ _

    * [ What is a Query? ](../../../api/faq/query/)
  * [ API Reference ](../../../api/api-reference/)

Toggle child pages in navigation

_ _

    * [ Subgraph Proxy ](../../../api/reference/proxy/)

Toggle child pages in navigation

_ _

      * [ Subgraph ID ](../../../api/reference/proxy/subgraph_id/)
      * [ Deployment ID ](../../../api/reference/proxy/deployment_id/)

Subgrounds

  * [ Overview ](../../)
  * [ Getting Started ](../../getting_started/)

Toggle child pages in navigation

_ _

    * [ The Basics ](../../getting_started/basics/)
    * [ Field Paths ](../../getting_started/field_paths/)

Toggle child pages in navigation

_ _

      * [ Arguments ](../../getting_started/field_paths/arguments/)
      * [ Filtering ](../../getting_started/field_paths/filtering/)
      * [ Sorting ](../../getting_started/field_paths/sorting/)
      * [ Merging ](../../getting_started/field_paths/merging/)
    * [ Querying ](../../getting_started/querying/)

Toggle child pages in navigation

_ _

    * [ Synthetic Fields ](../../getting_started/synthetic_fields/)
  * [ Advanced Topics ](../../advanced_topics/)

Toggle child pages in navigation

_ _

    * [ Contrib ](../../advanced_topics/contrib/)

Toggle child pages in navigation

_ _

      * [ Plotly ](../../advanced_topics/contrib/plotly/)
    * [ Pagination ](../../advanced_topics/pagination/)

Toggle child pages in navigation

_ _

      * [ Custom Strategies ](../../advanced_topics/pagination/custom/)
  * [ FAQ ](../../faq/)

Toggle child pages in navigation

_ _

    * [ Exporting to Disk ](../../faq/exporting/)
    * [ Getting More Data ](../../faq/more_data/)
    * [ Python Setup ](../../faq/setup/)

Toggle child pages in navigation

_ _

      * [ Python Versioning ](../../faq/setup/version_management/)
  * [ Examples ](../../examples/)

Toggle child pages in navigation

_ _

    * [ Exchanges ](../../examples/exchanges/)
    * [ Bridges ](../../examples/bridges/)
    * [ Liquid Staking ](../../examples/liquid_staking/)
    * [ Governance ](../../examples/governance/)
    * [ Advanced Research ](../../examples/advanced_research/)
    * [ Vaults ](../../examples/vaults/)
  * [ Videos ](../../videos/)
  * [ Changelog ](../../changelog/)
  * [ Contributing ](../../contributing/)
  * [ API Reference ](../)

Toggle child pages in navigation

_ _

    * [ Top Level APIs ](../top_level/)
    * Internal 

Toggle child pages in navigation

_ _

      * [ Client ](client/)

Toggle child pages in navigation

_ _

        * [ Base ](client/base/)
        * [ Sync ](client/sync/)
        * [ Async_ ](client/async_/)
      * [ Contrib ](contrib/)

Toggle child pages in navigation

_ _

        * [ Plotly ](contrib/plotly/)
        * [ Dash ](contrib/dash/)
      * [ Pagination ](pagination/)

Toggle child pages in navigation

_ _

        * [ Strategies ](pagination/strategies/)
        * [ Preprocess ](pagination/preprocess/)
        * [ Pagination ](pagination/pagination/)
        * [ Utils ](pagination/utils/)
      * [ Transform ](transform/)

Toggle child pages in navigation

_ _

        * [ ABCs ](transform/abcs/)
        * [ Apply ](transform/apply/)
        * [ Defaults ](transform/defaults/)
        * [ Transforms ](transform/transforms/)
        * [ Utils ](transform/utils/)
      * [ Subgraph ](subgraph/)

Toggle child pages in navigation

_ _

        * [ Fieldpath ](subgraph/fieldpath/)
        * [ Filter ](subgraph/filter/)
        * [ Object ](subgraph/object/)
        * [ Subgraph ](subgraph/subgraph/)
      * [ Errors ](errors/)
      * [ Query ](query/)
      * [ Schema ](schema/)
      * [ Utils ](utils/)

Meta

  * [ Improving the Docs ](../../../meta/contributing/)

Back to top

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

_ _

#  Internal  #

  * [ Client ](client/)
    * [ Base ](client/base/)
    * [ Sync ](client/sync/)
    * [ Async_ ](client/async_/)
    * [ ` get_schema()  ` ](client/#subgrounds.client.get_schema)
    * [ ` query()  ` ](client/#subgrounds.client.query)
  * [ Contrib ](contrib/)
    * [ Plotly ](contrib/plotly/)
      * [ ` TraceWrapper  ` ](contrib/plotly/#subgrounds.contrib.plotly.TraceWrapper)
      * [ ` Scatter  ` ](contrib/plotly/#subgrounds.contrib.plotly.Scatter)
        * [ ` Scatter.graph_object  ` ](contrib/plotly/#subgrounds.contrib.plotly.Scatter.graph_object)
      * [ ` Pie  ` ](contrib/plotly/#subgrounds.contrib.plotly.Pie)
        * [ ` Pie.graph_object  ` ](contrib/plotly/#subgrounds.contrib.plotly.Pie.graph_object)
      * [ ` Bar  ` ](contrib/plotly/#subgrounds.contrib.plotly.Bar)
        * [ ` Bar.graph_object  ` ](contrib/plotly/#subgrounds.contrib.plotly.Bar.graph_object)
      * [ ` Heatmap  ` ](contrib/plotly/#subgrounds.contrib.plotly.Heatmap)
        * [ ` Heatmap.graph_object  ` ](contrib/plotly/#subgrounds.contrib.plotly.Heatmap.graph_object)
      * [ ` Contour  ` ](contrib/plotly/#subgrounds.contrib.plotly.Contour)
        * [ ` Contour.graph_object  ` ](contrib/plotly/#subgrounds.contrib.plotly.Contour.graph_object)
      * [ ` Table  ` ](contrib/plotly/#subgrounds.contrib.plotly.Table)
        * [ ` Table.graph_object  ` ](contrib/plotly/#subgrounds.contrib.plotly.Table.graph_object)
      * [ ` Box  ` ](contrib/plotly/#subgrounds.contrib.plotly.Box)
        * [ ` Box.graph_object  ` ](contrib/plotly/#subgrounds.contrib.plotly.Box.graph_object)
      * [ ` Violin  ` ](contrib/plotly/#subgrounds.contrib.plotly.Violin)
        * [ ` Violin.graph_object  ` ](contrib/plotly/#subgrounds.contrib.plotly.Violin.graph_object)
      * [ ` Histogram  ` ](contrib/plotly/#subgrounds.contrib.plotly.Histogram)
        * [ ` Histogram.graph_object  ` ](contrib/plotly/#subgrounds.contrib.plotly.Histogram.graph_object)
      * [ ` Histogram2d  ` ](contrib/plotly/#subgrounds.contrib.plotly.Histogram2d)
        * [ ` Histogram2d.graph_object  ` ](contrib/plotly/#subgrounds.contrib.plotly.Histogram2d.graph_object)
      * [ ` Histogram2dContour  ` ](contrib/plotly/#subgrounds.contrib.plotly.Histogram2dContour)
        * [ ` Histogram2dContour.graph_object  ` ](contrib/plotly/#subgrounds.contrib.plotly.Histogram2dContour.graph_object)
      * [ ` Ohlc  ` ](contrib/plotly/#subgrounds.contrib.plotly.Ohlc)
        * [ ` Ohlc.graph_object  ` ](contrib/plotly/#subgrounds.contrib.plotly.Ohlc.graph_object)
      * [ ` Candlestick  ` ](contrib/plotly/#subgrounds.contrib.plotly.Candlestick)
        * [ ` Candlestick.graph_object  ` ](contrib/plotly/#subgrounds.contrib.plotly.Candlestick.graph_object)
      * [ ` Waterfall  ` ](contrib/plotly/#subgrounds.contrib.plotly.Waterfall)
        * [ ` Waterfall.graph_object  ` ](contrib/plotly/#subgrounds.contrib.plotly.Waterfall.graph_object)
      * [ ` Funnel  ` ](contrib/plotly/#subgrounds.contrib.plotly.Funnel)
        * [ ` Funnel.graph_object  ` ](contrib/plotly/#subgrounds.contrib.plotly.Funnel.graph_object)
      * [ ` Indicator  ` ](contrib/plotly/#subgrounds.contrib.plotly.Indicator)
        * [ ` Indicator.graph_object  ` ](contrib/plotly/#subgrounds.contrib.plotly.Indicator.graph_object)
      * [ ` Scatter3d  ` ](contrib/plotly/#subgrounds.contrib.plotly.Scatter3d)
        * [ ` Scatter3d.graph_object  ` ](contrib/plotly/#subgrounds.contrib.plotly.Scatter3d.graph_object)
      * [ ` Surface  ` ](contrib/plotly/#subgrounds.contrib.plotly.Surface)
        * [ ` Surface.graph_object  ` ](contrib/plotly/#subgrounds.contrib.plotly.Surface.graph_object)
      * [ ` Scattergeo  ` ](contrib/plotly/#subgrounds.contrib.plotly.Scattergeo)
        * [ ` Scattergeo.graph_object  ` ](contrib/plotly/#subgrounds.contrib.plotly.Scattergeo.graph_object)
      * [ ` Choropleth  ` ](contrib/plotly/#subgrounds.contrib.plotly.Choropleth)
        * [ ` Choropleth.graph_object  ` ](contrib/plotly/#subgrounds.contrib.plotly.Choropleth.graph_object)
      * [ ` Scattermapbox  ` ](contrib/plotly/#subgrounds.contrib.plotly.Scattermapbox)
        * [ ` Scattermapbox.graph_object  ` ](contrib/plotly/#subgrounds.contrib.plotly.Scattermapbox.graph_object)
      * [ ` Choroplethmapbox  ` ](contrib/plotly/#subgrounds.contrib.plotly.Choroplethmapbox)
        * [ ` Choroplethmapbox.graph_object  ` ](contrib/plotly/#subgrounds.contrib.plotly.Choroplethmapbox.graph_object)
      * [ ` Densitymapbox  ` ](contrib/plotly/#subgrounds.contrib.plotly.Densitymapbox)
        * [ ` Densitymapbox.graph_object  ` ](contrib/plotly/#subgrounds.contrib.plotly.Densitymapbox.graph_object)
      * [ ` Scatterpolar  ` ](contrib/plotly/#subgrounds.contrib.plotly.Scatterpolar)
        * [ ` Scatterpolar.graph_object  ` ](contrib/plotly/#subgrounds.contrib.plotly.Scatterpolar.graph_object)
      * [ ` Barpolar  ` ](contrib/plotly/#subgrounds.contrib.plotly.Barpolar)
        * [ ` Barpolar.graph_object  ` ](contrib/plotly/#subgrounds.contrib.plotly.Barpolar.graph_object)
      * [ ` Sunburst  ` ](contrib/plotly/#subgrounds.contrib.plotly.Sunburst)
        * [ ` Sunburst.graph_object  ` ](contrib/plotly/#subgrounds.contrib.plotly.Sunburst.graph_object)
      * [ ` Treemap  ` ](contrib/plotly/#subgrounds.contrib.plotly.Treemap)
        * [ ` Treemap.graph_object  ` ](contrib/plotly/#subgrounds.contrib.plotly.Treemap.graph_object)
      * [ ` Icicle  ` ](contrib/plotly/#subgrounds.contrib.plotly.Icicle)
        * [ ` Icicle.graph_object  ` ](contrib/plotly/#subgrounds.contrib.plotly.Icicle.graph_object)
      * [ ` Sankey  ` ](contrib/plotly/#subgrounds.contrib.plotly.Sankey)
        * [ ` Sankey.graph_object  ` ](contrib/plotly/#subgrounds.contrib.plotly.Sankey.graph_object)
      * [ ` Parcoords  ` ](contrib/plotly/#subgrounds.contrib.plotly.Parcoords)
        * [ ` Parcoords.graph_object  ` ](contrib/plotly/#subgrounds.contrib.plotly.Parcoords.graph_object)
      * [ ` Parcats  ` ](contrib/plotly/#subgrounds.contrib.plotly.Parcats)
        * [ ` Parcats.graph_object  ` ](contrib/plotly/#subgrounds.contrib.plotly.Parcats.graph_object)
      * [ ` Carpet  ` ](contrib/plotly/#subgrounds.contrib.plotly.Carpet)
        * [ ` Carpet.graph_object  ` ](contrib/plotly/#subgrounds.contrib.plotly.Carpet.graph_object)
      * [ ` Scattercarpet  ` ](contrib/plotly/#subgrounds.contrib.plotly.Scattercarpet)
        * [ ` Scattercarpet.graph_object  ` ](contrib/plotly/#subgrounds.contrib.plotly.Scattercarpet.graph_object)
      * [ ` Contourcarpet  ` ](contrib/plotly/#subgrounds.contrib.plotly.Contourcarpet)
        * [ ` Contourcarpet.graph_object  ` ](contrib/plotly/#subgrounds.contrib.plotly.Contourcarpet.graph_object)
    * [ Dash ](contrib/dash/)
      * [ ` Refreshable  ` ](contrib/dash/#subgrounds.contrib.dash.Refreshable)
      * [ ` Graph  ` ](contrib/dash/#subgrounds.contrib.dash.Graph)
      * [ ` DataTable  ` ](contrib/dash/#subgrounds.contrib.dash.DataTable)
      * [ ` AutoUpdate  ` ](contrib/dash/#subgrounds.contrib.dash.AutoUpdate)
  * [ Pagination ](pagination/)
    * [ Strategies ](pagination/strategies/)
      * [ ` StopPagination  ` ](pagination/strategies/#subgrounds.pagination.strategies.StopPagination)
      * [ ` SkipPagination  ` ](pagination/strategies/#subgrounds.pagination.strategies.SkipPagination)
      * [ ` LegacyStrategyArgGenerator  ` ](pagination/strategies/#subgrounds.pagination.strategies.LegacyStrategyArgGenerator)
        * [ ` LegacyStrategyArgGenerator.Cursor  ` ](pagination/strategies/#subgrounds.pagination.strategies.LegacyStrategyArgGenerator.Cursor)
      * [ ` ShallowStrategyArgGenerator  ` ](pagination/strategies/#subgrounds.pagination.strategies.ShallowStrategyArgGenerator)
        * [ ` ShallowStrategyArgGenerator.Cursor  ` ](pagination/strategies/#subgrounds.pagination.strategies.ShallowStrategyArgGenerator.Cursor)
    * [ Preprocess ](pagination/preprocess/)
      * [ ` PaginationNode  ` ](pagination/preprocess/#subgrounds.pagination.preprocess.PaginationNode)
        * [ ` PaginationNode.node_idx  ` ](pagination/preprocess/#subgrounds.pagination.preprocess.PaginationNode.node_idx)
        * [ ` PaginationNode.filter_field  ` ](pagination/preprocess/#subgrounds.pagination.preprocess.PaginationNode.filter_field)
        * [ ` PaginationNode.first_value  ` ](pagination/preprocess/#subgrounds.pagination.preprocess.PaginationNode.first_value)
        * [ ` PaginationNode.skip_value  ` ](pagination/preprocess/#subgrounds.pagination.preprocess.PaginationNode.skip_value)
        * [ ` PaginationNode.filter_value  ` ](pagination/preprocess/#subgrounds.pagination.preprocess.PaginationNode.filter_value)
        * [ ` PaginationNode.filter_value_type  ` ](pagination/preprocess/#subgrounds.pagination.preprocess.PaginationNode.filter_value_type)
        * [ ` PaginationNode.key_path  ` ](pagination/preprocess/#subgrounds.pagination.preprocess.PaginationNode.key_path)
        * [ ` PaginationNode.inner  ` ](pagination/preprocess/#subgrounds.pagination.preprocess.PaginationNode.inner)
        * [ ` PaginationNode.get_vardefs()  ` ](pagination/preprocess/#subgrounds.pagination.preprocess.PaginationNode.get_vardefs)
      * [ ` normalize()  ` ](pagination/preprocess/#subgrounds.pagination.preprocess.normalize)
    * [ Pagination ](pagination/pagination/)
      * [ ` PaginationError  ` ](pagination/pagination/#subgrounds.pagination.pagination.PaginationError)
      * [ ` PaginationStrategy  ` ](pagination/pagination/#subgrounds.pagination.pagination.PaginationStrategy)
        * [ ` PaginationStrategy.step()  ` ](pagination/pagination/#subgrounds.pagination.pagination.PaginationStrategy.step)
      * [ ` paginate()  ` ](pagination/pagination/#subgrounds.pagination.pagination.paginate)
      * [ ` paginate_iter()  ` ](pagination/pagination/#subgrounds.pagination.pagination.paginate_iter)
    * [ Utils ](pagination/utils/)
      * [ ` merge()  ` ](pagination/utils/#subgrounds.pagination.utils.merge)
      * [ ` merge_input_value_object_metas()  ` ](pagination/utils/#subgrounds.pagination.utils.merge_input_value_object_metas)
    * [ ` normalize()  ` ](pagination/#subgrounds.pagination.normalize)
    * [ ` paginate_iter()  ` ](pagination/#subgrounds.pagination.paginate_iter)
    * [ ` paginate()  ` ](pagination/#subgrounds.pagination.paginate)
    * [ ` PaginationError  ` ](pagination/#subgrounds.pagination.PaginationError)
    * [ ` PaginationNode  ` ](pagination/#subgrounds.pagination.PaginationNode)
      * [ ` PaginationNode.node_idx  ` ](pagination/#subgrounds.pagination.PaginationNode.node_idx)
      * [ ` PaginationNode.filter_field  ` ](pagination/#subgrounds.pagination.PaginationNode.filter_field)
      * [ ` PaginationNode.first_value  ` ](pagination/#subgrounds.pagination.PaginationNode.first_value)
      * [ ` PaginationNode.skip_value  ` ](pagination/#subgrounds.pagination.PaginationNode.skip_value)
      * [ ` PaginationNode.filter_value  ` ](pagination/#subgrounds.pagination.PaginationNode.filter_value)
      * [ ` PaginationNode.filter_value_type  ` ](pagination/#subgrounds.pagination.PaginationNode.filter_value_type)
      * [ ` PaginationNode.key_path  ` ](pagination/#subgrounds.pagination.PaginationNode.key_path)
      * [ ` PaginationNode.inner  ` ](pagination/#subgrounds.pagination.PaginationNode.inner)
      * [ ` PaginationNode.get_vardefs()  ` ](pagination/#subgrounds.pagination.PaginationNode.get_vardefs)
    * [ ` PaginationStrategy  ` ](pagination/#subgrounds.pagination.PaginationStrategy)
      * [ ` PaginationStrategy.step()  ` ](pagination/#subgrounds.pagination.PaginationStrategy.step)
  * [ Transform ](transform/)
    * [ ABCs ](transform/abcs/)
    * [ Apply ](transform/apply/)
    * [ Defaults ](transform/defaults/)
    * [ Transforms ](transform/transforms/)
    * [ Utils ](transform/utils/)
    * [ ` RequestTransform  ` ](transform/#subgrounds.transform.RequestTransform)
      * [ ` RequestTransform.transform_request()  ` ](transform/#subgrounds.transform.RequestTransform.transform_request)
      * [ ` RequestTransform.transform_response()  ` ](transform/#subgrounds.transform.RequestTransform.transform_response)
    * [ ` DocumentTransform  ` ](transform/#subgrounds.transform.DocumentTransform)
      * [ ` DocumentTransform.transform_document()  ` ](transform/#subgrounds.transform.DocumentTransform.transform_document)
      * [ ` DocumentTransform.transform_response()  ` ](transform/#subgrounds.transform.DocumentTransform.transform_response)
    * [ ` TypeTransform  ` ](transform/#subgrounds.transform.TypeTransform)
      * [ ` TypeTransform.type_  ` ](transform/#subgrounds.transform.TypeTransform.type_)
      * [ ` TypeTransform.f  ` ](transform/#subgrounds.transform.TypeTransform.f)
      * [ ` TypeTransform.transform_document()  ` ](transform/#subgrounds.transform.TypeTransform.transform_document)
      * [ ` TypeTransform.transform_response()  ` ](transform/#subgrounds.transform.TypeTransform.transform_response)
    * [ ` LocalSyntheticField  ` ](transform/#subgrounds.transform.LocalSyntheticField)
      * [ ` LocalSyntheticField.subgraph  ` ](transform/#subgrounds.transform.LocalSyntheticField.subgraph)
      * [ ` LocalSyntheticField.fmeta  ` ](transform/#subgrounds.transform.LocalSyntheticField.fmeta)
      * [ ` LocalSyntheticField.type_  ` ](transform/#subgrounds.transform.LocalSyntheticField.type_)
      * [ ` LocalSyntheticField.f  ` ](transform/#subgrounds.transform.LocalSyntheticField.f)
      * [ ` LocalSyntheticField.default  ` ](transform/#subgrounds.transform.LocalSyntheticField.default)
      * [ ` LocalSyntheticField.args  ` ](transform/#subgrounds.transform.LocalSyntheticField.args)
      * [ ` LocalSyntheticField.transform_document()  ` ](transform/#subgrounds.transform.LocalSyntheticField.transform_document)
      * [ ` LocalSyntheticField.transform_response()  ` ](transform/#subgrounds.transform.LocalSyntheticField.transform_response)
    * [ ` SplitTransform  ` ](transform/#subgrounds.transform.SplitTransform)
      * [ ` SplitTransform.transform_request()  ` ](transform/#subgrounds.transform.SplitTransform.transform_request)
      * [ ` SplitTransform.transform_response()  ` ](transform/#subgrounds.transform.SplitTransform.transform_response)
  * [ Subgraph ](subgraph/)
    * [ Fieldpath ](subgraph/fieldpath/)
      * [ ` fieldpaths_of_object()  ` ](subgraph/fieldpath/#subgrounds.subgraph.fieldpath.fieldpaths_of_object)
      * [ ` FieldPath  ` ](subgraph/fieldpath/#subgrounds.subgraph.fieldpath.FieldPath)
        * [ ` FieldPath._root  ` ](subgraph/fieldpath/#subgrounds.subgraph.fieldpath.FieldPath._root)
        * [ ` FieldPath._leaf  ` ](subgraph/fieldpath/#subgrounds.subgraph.fieldpath.FieldPath._leaf)
        * [ ` FieldPath._merge()  ` ](subgraph/fieldpath/#subgrounds.subgraph.fieldpath.FieldPath._merge)
        * [ ` FieldPath._name_path()  ` ](subgraph/fieldpath/#subgrounds.subgraph.fieldpath.FieldPath._name_path)
        * [ ` FieldPath._name()  ` ](subgraph/fieldpath/#subgrounds.subgraph.fieldpath.FieldPath._name)
        * [ ` FieldPath._extract_data()  ` ](subgraph/fieldpath/#subgrounds.subgraph.fieldpath.FieldPath._extract_data)
        * [ ` FieldPath._selection()  ` ](subgraph/fieldpath/#subgrounds.subgraph.fieldpath.FieldPath._selection)
        * [ ` FieldPath._set_arguments()  ` ](subgraph/fieldpath/#subgrounds.subgraph.fieldpath.FieldPath._set_arguments)
        * [ ` FieldPath._select()  ` ](subgraph/fieldpath/#subgrounds.subgraph.fieldpath.FieldPath._select)
        * [ ` FieldPath._extend()  ` ](subgraph/fieldpath/#subgrounds.subgraph.fieldpath.FieldPath._extend)
      * [ ` SyntheticField  ` ](subgraph/fieldpath/#subgrounds.subgraph.fieldpath.SyntheticField)
        * [ ` SyntheticField.constant()  ` ](subgraph/fieldpath/#subgrounds.subgraph.fieldpath.SyntheticField.constant)
        * [ ` SyntheticField.datetime_of_timestamp()  ` ](subgraph/fieldpath/#subgrounds.subgraph.fieldpath.SyntheticField.datetime_of_timestamp)
        * [ ` SyntheticField.map()  ` ](subgraph/fieldpath/#subgrounds.subgraph.fieldpath.SyntheticField.map)
    * [ Filter ](subgraph/filter/)
      * [ ` Filter  ` ](subgraph/filter/#subgrounds.subgraph.filter.Filter)
        * [ ` Filter.Operator  ` ](subgraph/filter/#subgrounds.subgraph.filter.Filter.Operator)
    * [ Object ](subgraph/object/)
      * [ ` Object  ` ](subgraph/object/#subgrounds.subgraph.object.Object)
        * [ ` Object._select()  ` ](subgraph/object/#subgrounds.subgraph.object.Object._select)
    * [ Subgraph ](subgraph/subgraph/)
      * [ ` Subgraph  ` ](subgraph/subgraph/#subgrounds.subgraph.subgraph.Subgraph)
    * [ ` FieldPath  ` ](subgraph/#subgrounds.subgraph.FieldPath)
    * [ ` Filter  ` ](subgraph/#subgrounds.subgraph.Filter)
      * [ ` Filter.Operator  ` ](subgraph/#subgrounds.subgraph.Filter.Operator)
    * [ ` Object  ` ](subgraph/#subgrounds.subgraph.Object)
    * [ ` Subgraph  ` ](subgraph/#subgrounds.subgraph.Subgraph)
    * [ ` SyntheticField  ` ](subgraph/#subgrounds.subgraph.SyntheticField)
      * [ ` SyntheticField.constant()  ` ](subgraph/#subgrounds.subgraph.SyntheticField.constant)
      * [ ` SyntheticField.datetime_of_timestamp()  ` ](subgraph/#subgrounds.subgraph.SyntheticField.datetime_of_timestamp)
      * [ ` SyntheticField.map()  ` ](subgraph/#subgrounds.subgraph.SyntheticField.map)
  * [ Errors ](errors/)
    * [ ` SubgroundsError  ` ](errors/#subgrounds.errors.SubgroundsError)
    * [ ` SchemaError  ` ](errors/#subgrounds.errors.SchemaError)
    * [ ` TransformError  ` ](errors/#subgrounds.errors.TransformError)
    * [ ` ServerError  ` ](errors/#subgrounds.errors.ServerError)
    * [ ` GraphQLError  ` ](errors/#subgrounds.errors.GraphQLError)
  * [ Query ](query/)
    * [ ` VariableDefinition  ` ](query/#subgrounds.query.VariableDefinition)
      * [ ` VariableDefinition.name  ` ](query/#subgrounds.query.VariableDefinition.name)
      * [ ` VariableDefinition.type_  ` ](query/#subgrounds.query.VariableDefinition.type_)
      * [ ` VariableDefinition.default  ` ](query/#subgrounds.query.VariableDefinition.default)
      * [ ` VariableDefinition.graphql  ` ](query/#subgrounds.query.VariableDefinition.graphql)
    * [ ` Argument  ` ](query/#subgrounds.query.Argument)
    * [ ` Selection  ` ](query/#subgrounds.query.Selection)
      * [ ` Selection.fmeta  ` ](query/#subgrounds.query.Selection.fmeta)
      * [ ` Selection.alias  ` ](query/#subgrounds.query.Selection.alias)
      * [ ` Selection.arguments  ` ](query/#subgrounds.query.Selection.arguments)
      * [ ` Selection.selection  ` ](query/#subgrounds.query.Selection.selection)
      * [ ` Selection.iter()  ` ](query/#subgrounds.query.Selection.iter)
      * [ ` Selection.iter_args()  ` ](query/#subgrounds.query.Selection.iter_args)
      * [ ` Selection.filter()  ` ](query/#subgrounds.query.Selection.filter)
      * [ ` Selection.filter_args()  ` ](query/#subgrounds.query.Selection.filter_args)
      * [ ` Selection.map()  ` ](query/#subgrounds.query.Selection.map)
      * [ ` Selection.map_args()  ` ](query/#subgrounds.query.Selection.map_args)
      * [ ` Selection.contains_list()  ` ](query/#subgrounds.query.Selection.contains_list)
      * [ ` Selection.split()  ` ](query/#subgrounds.query.Selection.split)
      * [ ` Selection.add()  ` ](query/#subgrounds.query.Selection.add)
      * [ ` Selection.remove()  ` ](query/#subgrounds.query.Selection.remove)
      * [ ` Selection.variable_args()  ` ](query/#subgrounds.query.Selection.variable_args)
      * [ ` Selection.merge()  ` ](query/#subgrounds.query.Selection.merge)
      * [ ` Selection.contains()  ` ](query/#subgrounds.query.Selection.contains)
      * [ ` Selection.contains_argument()  ` ](query/#subgrounds.query.Selection.contains_argument)
      * [ ` Selection.get_argument()  ` ](query/#subgrounds.query.Selection.get_argument)
      * [ ` Selection.get_argument_by_variable()  ` ](query/#subgrounds.query.Selection.get_argument_by_variable)
      * [ ` Selection.substitute_arg()  ` ](query/#subgrounds.query.Selection.substitute_arg)
      * [ ` Selection.prune_undefined()  ` ](query/#subgrounds.query.Selection.prune_undefined)
    * [ ` Query  ` ](query/#subgrounds.query.Query)
      * [ ` Query.graphql  ` ](query/#subgrounds.query.Query.graphql)
      * [ ` Query.iter()  ` ](query/#subgrounds.query.Query.iter)
      * [ ` Query.iter_args()  ` ](query/#subgrounds.query.Query.iter_args)
      * [ ` Query.iter_vardefs()  ` ](query/#subgrounds.query.Query.iter_vardefs)
      * [ ` Query.filter()  ` ](query/#subgrounds.query.Query.filter)
      * [ ` Query.filter_args()  ` ](query/#subgrounds.query.Query.filter_args)
      * [ ` Query.map()  ` ](query/#subgrounds.query.Query.map)
      * [ ` Query.map_args()  ` ](query/#subgrounds.query.Query.map_args)
      * [ ` Query.add()  ` ](query/#subgrounds.query.Query.add)
      * [ ` Query.remove()  ` ](query/#subgrounds.query.Query.remove)
      * [ ` Query.contains_selection()  ` ](query/#subgrounds.query.Query.contains_selection)
      * [ ` Query.contains()  ` ](query/#subgrounds.query.Query.contains)
      * [ ` Query.select()  ` ](query/#subgrounds.query.Query.select)
    * [ ` Fragment  ` ](query/#subgrounds.query.Fragment)
    * [ ` Document  ` ](query/#subgrounds.query.Document)
      * [ ` Document.map()  ` ](query/#subgrounds.query.Document.map)
      * [ ` Document.map_args()  ` ](query/#subgrounds.query.Document.map_args)
      * [ ` Document.prune_undefined()  ` ](query/#subgrounds.query.Document.prune_undefined)
    * [ ` DataRequest  ` ](query/#subgrounds.query.DataRequest)
    * [ ` selections_of_object()  ` ](query/#subgrounds.query.selections_of_object)
  * [ Schema ](schema/)
    * [ ` SchemaMeta  ` ](schema/#subgrounds.schema.SchemaMeta)
      * [ ` SchemaMeta.type_of_typeref()  ` ](schema/#subgrounds.schema.SchemaMeta.type_of_typeref)
      * [ ` SchemaMeta.type_of()  ` ](schema/#subgrounds.schema.SchemaMeta.type_of)
      * [ ` SchemaMeta.type_of_input_object_meta()  ` ](schema/#subgrounds.schema.SchemaMeta.type_of_input_object_meta)
  * [ Utils ](utils/)
    * [ ` flatten_dict()  ` ](utils/#subgrounds.utils.flatten_dict)
    * [ ` contains_list()  ` ](utils/#subgrounds.utils.contains_list)
    * [ ` default_header()  ` ](utils/#subgrounds.utils.default_header)
    * [ ` user_agent()  ` ](utils/#subgrounds.utils.user_agent)
    * [ ` DataFrameColumns  ` ](utils/#subgrounds.dataframe_utils.DataFrameColumns)
      * [ ` DataFrameColumns.combine()  ` ](utils/#subgrounds.dataframe_utils.DataFrameColumns.combine)
      * [ ` DataFrameColumns.mk_df()  ` ](utils/#subgrounds.dataframe_utils.DataFrameColumns.mk_df)
    * [ ` columns_of_selections()  ` ](utils/#subgrounds.dataframe_utils.columns_of_selections)
    * [ ` df_of_json()  ` ](utils/#subgrounds.dataframe_utils.df_of_json)

##  Module contents  #

_ class  _ subgrounds.  FieldPath  (  _ subgraph  :  'Subgraph'  _ , _
root_type  :  'TypeRef.T'  _ , _ type_  :  'TypeRef.T'  _ , _ path  :
'list[Tuple[Optional[dict[str,  Any]],  TypeMeta.FieldMeta]]'  _ )  #

    

Bases: ` FieldOperatorMixin  `

_ class  _ subgrounds.  Subgraph  (  _ url:  'str',  schema:  'SchemaMeta',
transforms:  'list[DocumentTransform]'  =
[<subgrounds.transform.TypeTransform  object  at  0x7fba98ae0580>,
<subgrounds.transform.TypeTransform  object  at  0x7fba98ae0640>],
is_subgraph:  'bool'  =  True  _ )  #

    

Bases: [ ` object  ` ](https://docs.python.org/3/library/functions.html#object
"\(in Python v3.11\)")

_ class  _ subgrounds.  Subgrounds  (  _ headers:  dict[str  _ , _ typing.Any]
=  <factory> _ , _ global_transforms:
list[subgrounds.transform.RequestTransform]  =  <factory> _ , _ subgraphs:
dict[str  _ , _ subgrounds.subgraph.subgraph.Subgraph]  =  <factory> _ )  #

    

Bases: [ ` object  ` ](https://docs.python.org/3/library/functions.html#object
"\(in Python v3.11\)")

headers  _ :  [ dict  ](https://docs.python.org/3/library/stdtypes.html#dict
"\(in Python v3.11\)") [  [ str
](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.11\)") ,
[ Any  ](https://docs.python.org/3/library/typing.html#typing.Any "\(in Python
v3.11\)") ]  _ #

    

global_transforms  _ :  [ list
](https://docs.python.org/3/library/stdtypes.html#list "\(in Python v3.11\)")
[  [ subgrounds.transform.RequestTransform
](transform/#subgrounds.transform.RequestTransform
"subgrounds.transform.RequestTransform") ]  _ #

    

subgraphs  _ :  [ dict  ](https://docs.python.org/3/library/stdtypes.html#dict
"\(in Python v3.11\)") [  [ str
](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.11\)") ,
[ subgrounds.subgraph.subgraph.Subgraph
](subgraph/subgraph/#subgrounds.subgraph.subgraph.Subgraph
"subgrounds.subgraph.subgraph.Subgraph") ]  _ #

    

_ classmethod  _ from_pg_key  (  _ key  _ )  #

    

load  (  _ url  _ , _ save_schema  =  False  _ , _ cache_dir  =  'schemas/'  _
, _ is_subgraph  =  True  _ )  #

    

load_subgraph  (  _ url  _ , _ save_schema  =  False  _ , _ cache_dir  =
'schemas/'  _ )  #

    

Performs introspection on the provided GraphQL API ` url  ` to get the schema,
stores the schema if ` save_schema  ` is ` True  ` and returns a generated
class representing the subgraph with all its entities.

Parameters  :

    

  * **url** ( [ _str_ ](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.11\)") ) -- The url of the API 

  * **save_schema** ( [ _bool_ ](https://docs.python.org/3/library/functions.html#bool "\(in Python v3.11\)") _,_ _optional_ ) -- Flag indicating whether or not the schema should be cached to disk. Defaults to False. 

  * **cache_dir** ( [ _str_ ](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.11\)") _,_ _optional_ ) -- If ` save_schema  ==  True  ` , then subgraph schemas will be stored under ` cache_dir  ` . Defaults to ` schemas/  `

Returns  :

    

A generated class representing the subgraph and its entities

Return type  :

    

[ Subgraph ](../top_level/#subgrounds.Subgraph "subgrounds.Subgraph")

load_api  (  _ url  _ , _ save_schema  =  False  _ , _ cache_dir  =
'schemas/'  _ )  #

    

Performs introspection on the provided GraphQL API ` url  ` to get the schema,
stores the schema if ` save_schema  ` is ` True  ` and returns a generated
class representing the GraphQL endpoint with all its entities.

Parameters  :

    

  * **url** ( [ _str_ ](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.11\)") ) -- The url of the API 

  * **save_schema** ( [ _bool_ ](https://docs.python.org/3/library/functions.html#bool "\(in Python v3.11\)") _,_ _optional_ ) -- Flag indicating whether or not the schema should be saved to disk. Defaults to False. 

Returns  :

    

A generated class representing the subgraph and its entities

Return type  :

    

[ Subgraph ](../top_level/#subgrounds.Subgraph "subgrounds.Subgraph")

mk_request  (  _ fpaths  _ )  #

    

Creates a ` DataRequest  ` object by combining one or more [ ` FieldPath  `
](../top_level/#subgrounds.FieldPath "subgrounds.FieldPath") objects.

Parameters  :

    

**fpaths** ( [ _FieldPath_ ](../top_level/#subgrounds.FieldPath
"subgrounds.FieldPath") _|_ [ _list_
](https://docs.python.org/3/library/stdtypes.html#list "\(in Python v3.11\)")
_[_ [ _FieldPath_ ](../top_level/#subgrounds.FieldPath "subgrounds.FieldPath")
_]_ ) -- One or more [ ` FieldPath  ` ](../top_level/#subgrounds.FieldPath
"subgrounds.FieldPath") objects that should be included in the request

Returns  :

    

A new ` DataRequest  ` object

Return type  :

    

[ DataRequest ](query/#subgrounds.query.DataRequest
"subgrounds.query.DataRequest")

execute  (  _ req  _ , _ pagination_strategy  =  LegacyStrategy  _ )  #

    

Executes a ` DataRequest  ` object, sending the underlying query(ies) to the
server and returning a data blob (list of Python dictionaries, one per actual
query).

Parameters  :

    

  * **req** ( [ _DataRequest_ ](query/#subgrounds.query.DataRequest "subgrounds.query.DataRequest") ) -- The ` DataRequest  ` object to be executed 

  * **pagination_strategy** ( _Optional_ _[_ _Type_ _[_ [ _PaginationStrategy_ ](pagination/#subgrounds.pagination.PaginationStrategy "subgrounds.pagination.PaginationStrategy") _]_ _]_ _,_ _optional_ ) -- A Class implementing the ` PaginationStrategy  ` ` Protocol  ` . If ` None  ` , then automatic pagination is disabled. Defaults to ` LegacyStrategy  ` . 

Returns  :

    

The reponse data

Return type  :

    

[ list ](https://docs.python.org/3/library/stdtypes.html#list "\(in Python
v3.11\)") [ [ dict ](https://docs.python.org/3/library/stdtypes.html#dict
"\(in Python v3.11\)") ]

execute_iter  (  _ req  _ , _ pagination_strategy  =  LegacyStrategy  _ )  #

    

Same as  execute  , except that an iterator is returned which will iterate the
data pages.

Parameters  :

    

  * **req** ( [ _DataRequest_ ](query/#subgrounds.query.DataRequest "subgrounds.query.DataRequest") ) -- The ` DataRequest  ` object to be executed 

  * **pagination_strategy** ( _Optional_ _[_ _Type_ _[_ [ _PaginationStrategy_ ](pagination/#subgrounds.pagination.PaginationStrategy "subgrounds.pagination.PaginationStrategy") _]_ _]_ _,_ _optional_ ) -- A Class implementing the ` PaginationStrategy  ` ` Protocol  ` . If ` None  ` , then automatic pagination is disabled. Defaults to ` LegacyStrategy  ` . 

Returns  :

    

An iterator over the reponse data pages

Return type  :

    

Iterator[ [ dict ](https://docs.python.org/3/library/stdtypes.html#dict "\(in
Python v3.11\)") ]

query_json  (  _ fpaths  _ , _ pagination_strategy  =  LegacyStrategy  _ )  #

    

Equivalent to ` Subgrounds.execute(Subgrounds.mk_request(fpaths),
pagination_strategy)  ` .

Parameters  :

    

  * **fpaths** ( [ _FieldPath_ ](../top_level/#subgrounds.FieldPath "subgrounds.FieldPath") _|_ [ _list_ ](https://docs.python.org/3/library/stdtypes.html#list "\(in Python v3.11\)") _[_ [ _FieldPath_ ](../top_level/#subgrounds.FieldPath "subgrounds.FieldPath") _]_ ) -- One or more [ ` FieldPath  ` ](../top_level/#subgrounds.FieldPath "subgrounds.FieldPath") objects that should be included in the request. 

  * **pagination_strategy** ( _Optional_ _[_ _Type_ _[_ [ _PaginationStrategy_ ](pagination/#subgrounds.pagination.PaginationStrategy "subgrounds.pagination.PaginationStrategy") _]_ _]_ _,_ _optional_ ) -- A Class implementing the ` PaginationStrategy  ` ` Protocol  ` . If ` None  ` , then automatic pagination is disabled. Defaults to ` LegacyStrategy  ` . 

Returns  :

    

The reponse data

Return type  :

    

[ list ](https://docs.python.org/3/library/stdtypes.html#list "\(in Python
v3.11\)") [ [ dict ](https://docs.python.org/3/library/stdtypes.html#dict
"\(in Python v3.11\)") [ [ str
](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.11\)") ,
Any]]

query_json_iter  (  _ fpaths  _ , _ pagination_strategy  =  LegacyStrategy  _
)  #

    

Same as  query_json  except an iterator over the response data pages is
returned.

Parameters  :

    

  * **fpaths** ( [ _FieldPath_ ](../top_level/#subgrounds.FieldPath "subgrounds.FieldPath") _|_ [ _list_ ](https://docs.python.org/3/library/stdtypes.html#list "\(in Python v3.11\)") _[_ [ _FieldPath_ ](../top_level/#subgrounds.FieldPath "subgrounds.FieldPath") _]_ ) -- One or more [ ` FieldPath  ` ](../top_level/#subgrounds.FieldPath "subgrounds.FieldPath") objects that should be included in the request. 

  * **pagination_strategy** ( _Optional_ _[_ _Type_ _[_ [ _PaginationStrategy_ ](pagination/#subgrounds.pagination.PaginationStrategy "subgrounds.pagination.PaginationStrategy") _]_ _]_ _,_ _optional_ ) -- A Class implementing the ` PaginationStrategy  ` ` Protocol  ` . If ` None  ` , then automatic pagination is disabled. Defaults to ` LegacyStrategy  ` . 

Returns  :

    

The reponse data

Return type  :

    

[ list ](https://docs.python.org/3/library/stdtypes.html#list "\(in Python
v3.11\)") [ [ dict ](https://docs.python.org/3/library/stdtypes.html#dict
"\(in Python v3.11\)") [ [ str
](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.11\)") ,
Any]]

query_df  (  _ fpaths  _ , _ columns  =  None  _ , _ concat  =  False  _ , _
pagination_strategy  =  LegacyStrategy  _ )  #

    

Same as [ ` Subgrounds.query()  ` ](../top_level/#subgrounds.Subgrounds.query
"subgrounds.Subgrounds.query") but formats the response data into a Pandas
DataFrame. If the response data cannot be flattened to a single query (e.g.:
when querying multiple list fields that return different entities), then
multiple dataframes are returned

` fpaths  ` is a list of [ ` FieldPath  ` ](../top_level/#subgrounds.FieldPath
"subgrounds.FieldPath") objects that indicate which data must be queried.

` columns  ` is an optional argument used to rename the dataframes(s) columns.
The length of ` columns  ` must be the same as the number of columns of _all_
returned dataframes.

` concat  ` indicates whether or not the resulting dataframes should be
concatenated together. The dataframes must have the same number of columns, as
well as the same column names and types (the names can be set using the `
columns  ` argument).

Parameters  :

    

  * **fpaths** ( [ _FieldPath_ ](../top_level/#subgrounds.FieldPath "subgrounds.FieldPath") _|_ [ _list_ ](https://docs.python.org/3/library/stdtypes.html#list "\(in Python v3.11\)") _[_ [ _FieldPath_ ](../top_level/#subgrounds.FieldPath "subgrounds.FieldPath") _]_ ) -- One or more  FieldPath  objects that should be included in the request. 

  * **columns** ( _Optional_ _[_ [ _list_ ](https://docs.python.org/3/library/stdtypes.html#list "\(in Python v3.11\)") _[_ [ _str_ ](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.11\)") _]_ _]_ _,_ _optional_ ) -- The column labels. Defaults to None. 

  * **merge** ( [ _bool_ ](https://docs.python.org/3/library/functions.html#bool "\(in Python v3.11\)") _,_ _optional_ ) -- Whether or not to merge resulting dataframes. 

  * **pagination_strategy** ( _Optional_ _[_ _Type_ _[_ [ _PaginationStrategy_ ](pagination/#subgrounds.pagination.PaginationStrategy "subgrounds.pagination.PaginationStrategy") _]_ _]_ _,_ _optional_ ) -- A Class implementing the ` PaginationStrategy  ` ` Protocol  ` . If ` None  ` , then automatic pagination is disabled. Defaults to ` LegacyStrategy  ` . 

Returns  :

    

A DataFrame containing the reponse data

Return type  :

    

pd.DataFrame | [ list ](https://docs.python.org/3/library/stdtypes.html#list
"\(in Python v3.11\)") [pd.DataFrame]

Example:

    
    
    >>> from subgrounds import Subgrounds
    >>> sg = Subgrounds()
    >>> univ3 = sg.load_subgraph('https://api.thegraph.com/subgraphs/name/uniswap/uniswap-v3')
    
    # Define price SyntheticField
    >>> univ3.Swap.price = abs(univ3.Swap.amount0) / abs(univ3.Swap.amount1)
    
    # Query last 10 swaps from the ETH/USDC pool
    >>> eth_usdc = univ3.Query.swaps(
    ...     orderBy=univ3.Swap.timestamp,
    ...     orderDirection='desc',
    ...     first=10,
    ...     where=[
    ...         univ3.Swap.pool == '0x8ad599c3a0ff1de082011efddc58f1908eb6e6d8'
    ...     ]
    ... )
    >>> sg.query_df([
    ...     eth_usdc.timestamp,
    ...     eth_usdc.price
    ... ])
      swaps_timestamp  swaps_price
    0       1643213811  2618.886394
    1       1643213792  2618.814281
    2       1643213792  2617.500494
    3       1643213763  2615.458495
    4       1643213763  2615.876574
    5       1643213739  2615.352390
    6       1643213678  2615.205713
    7       1643213370  2614.115746
    8       1643213210  2613.077301
    9       1643213196  2610.686563
    

query_df_iter  (  _ fpaths  _ , _ pagination_strategy  =  LegacyStrategy  _ )
#

    

Same as  query_df  except an iterator over the response data pages is returned
:param fpaths: One or more  FieldPath  objects that

> should be included in the request

Parameters  :

    

  * **columns** ( _Optional_ _[_ [ _list_ ](https://docs.python.org/3/library/stdtypes.html#list "\(in Python v3.11\)") _[_ [ _str_ ](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.11\)") _]_ _]_ _,_ _optional_ ) -- The column labels. Defaults to None. 

  * **merge** ( [ _bool_ ](https://docs.python.org/3/library/functions.html#bool "\(in Python v3.11\)") _,_ _optional_ ) -- Whether or not to merge resulting dataframes. 

  * **pagination_strategy** ( _Optional_ _[_ _Type_ _[_ [ _PaginationStrategy_ ](pagination/#subgrounds.pagination.PaginationStrategy "subgrounds.pagination.PaginationStrategy") _]_ _]_ _,_ _optional_ ) -- A Class implementing the ` PaginationStrategy  ` ` Protocol  ` . If ` None  ` , then automatic pagination is disabled. Defaults to ` LegacyStrategy  ` . 

Returns  :

    

An iterator over the response data pages, each as a DataFrame

Return type  :

    

Iterator[pd.DataFrame]

query  (  _ fpaths  _ , _ unwrap  =  True  _ , _ pagination_strategy  =
LegacyStrategy  _ )  #

    

Executes one or multiple ` FieldPath  ` objects immediately and return the
data (as a tuple if multiple ` FieldPath  ` objects are provided).

Parameters  :

    

  * **fpaths** ( [ _FieldPath_ ](../top_level/#subgrounds.FieldPath "subgrounds.FieldPath") _|_ [ _list_ ](https://docs.python.org/3/library/stdtypes.html#list "\(in Python v3.11\)") _[_ [ _FieldPath_ ](../top_level/#subgrounds.FieldPath "subgrounds.FieldPath") _]_ ) -- One or more ` FieldPath  ` object(s) to query. 

  * **unwrap** ( [ _bool_ ](https://docs.python.org/3/library/functions.html#bool "\(in Python v3.11\)") _,_ _optional_ ) -- Flag indicating whether or not, in the case where the returned data is a list of one element, the element itself should be returned instead of the list. Defaults to ` True  ` . 

  * **pagination_strategy** ( _Optional_ _[_ _Type_ _[_ [ _PaginationStrategy_ ](pagination/#subgrounds.pagination.PaginationStrategy "subgrounds.pagination.PaginationStrategy") _]_ _]_ _,_ _optional_ ) -- A Class implementing the ` PaginationStrategy  ` ` Protocol  ` . If ` None  ` , then automatic pagination is disabled. Defaults to ` LegacyStrategy  ` . 

Returns  :

    

The ` FieldPath  ` object(s) data

Return type  :

    

[ [ type ](https://docs.python.org/3/library/functions.html#type "\(in Python
v3.11\)") ]

Example:

    
    
    >>> from subgrounds import Subgrounds
    >>> sg = Subgrounds()
    >>> univ3 = sg.load_subgraph('https://api.thegraph.com/subgraphs/name/uniswap/uniswap-v3')
    
    # Define price SyntheticField
    >>> univ3.Swap.price = abs(univ3.Swap.amount0) / abs(univ3.Swap.amount1)
    
    # Construct FieldPath to get price of last swap on ETH/USDC pool
    >>> eth_usdc_last = univ3.Query.swaps(
    ...     orderBy=univ3.Swap.timestamp,
    ...     orderDirection='desc',
    ...     first=1,
    ...     where=[
    ...         univ3.Swap.pool == '0x8ad599c3a0ff1de082011efddc58f1908eb6e6d8'
    ...     ]
    ... ).price
    
    # Query last price FieldPath
    >>> sg.query(eth_usdc_last)
    2628.975030015892
    

query_iter  (  _ fpaths  _ , _ unwrap  =  True  _ , _ pagination_strategy  =
LegacyStrategy  _ )  #

    

Same as  query  except an iterator over the resonse data pages is returned.

Parameters  :

    

  * **fpath** ( [ _FieldPath_ ](../top_level/#subgrounds.FieldPath "subgrounds.FieldPath") _|_ [ _list_ ](https://docs.python.org/3/library/stdtypes.html#list "\(in Python v3.11\)") _[_ [ _FieldPath_ ](../top_level/#subgrounds.FieldPath "subgrounds.FieldPath") _]_ ) -- One or more ` FieldPath  ` object(s) to query. 

  * **unwrap** ( [ _bool_ ](https://docs.python.org/3/library/functions.html#bool "\(in Python v3.11\)") _,_ _optional_ ) -- Flag indicating whether or not, in the case where the returned data is a list of one element, the element itself should be returned instead of the list. Defaults to ` True  ` . 

  * **pagination_strategy** ( _Optional_ _[_ _Type_ _[_ [ _PaginationStrategy_ ](pagination/#subgrounds.pagination.PaginationStrategy "subgrounds.pagination.PaginationStrategy") _]_ _]_ _,_ _optional_ ) -- A Class implementing the ` PaginationStrategy  ` ` Protocol  ` . If ` None  ` , then automatic pagination is disabled. Defaults to ` LegacyStrategy  ` . 

Returns  :

    

An iterator over the ` FieldPath  ` object(s)' data pages

Return type  :

    

Iterator[ [ type ](https://docs.python.org/3/library/functions.html#type "\(in
Python v3.11\)") ]

_ class  _ subgrounds.  SyntheticField  (  _ f  :  'Callable'  _ , _ type_  :
'TypeRef.T'  _ , _ deps  :  'list[FieldPath  |  SyntheticField]  |  FieldPath
|  SyntheticField'  _ , _ default  :  'Any'  =  None  _ )  #

    

Bases: ` FieldOperatorMixin  `

STRING  _ :  ClassVar  [  TypeRef.Named  ]  _ _ =  Named(name_='String',
kind='SCALAR')  _ #

    

INT  _ :  ClassVar  [  TypeRef.Named  ]  _ _ =  Named(name_='Int',
kind='SCALAR')  _ #

    

FLOAT  _ :  ClassVar  [  TypeRef.Named  ]  _ _ =  Named(name_='Float',
kind='SCALAR')  _ #

    

BOOL  _ :  ClassVar  [  TypeRef.Named  ]  _ _ =  Named(name_='Boolean',
kind='SCALAR')  _ #

    

_ static  _ default_of_type  (  _ type_  _ )  #

    

_ static  _ constant  (  _ value  _ )  #

    

Returns a constant ` SyntheticField  ` with value ` value  ` . Useful for
injecting additional static data to a schema or merging entities.

Parameters  :

    

**value** ( [ _str_ ](https://docs.python.org/3/library/stdtypes.html#str
"\(in Python v3.11\)") _|_ [ _int_
](https://docs.python.org/3/library/functions.html#int "\(in Python v3.11\)")
_|_ [ _float_ ](https://docs.python.org/3/library/functions.html#float "\(in
Python v3.11\)") _|_ [ _bool_
](https://docs.python.org/3/library/functions.html#bool "\(in Python v3.11\)")
) -- The constant field's value

Returns  :

    

The constant ` SyntheticField  `

Return type  :

    

[ SyntheticField ](../top_level/#subgrounds.SyntheticField
"subgrounds.SyntheticField")

Example:

    
    
    >>> from subgrounds.subgrounds import Subgrounds
    >>> from subgrounds.subgraph import SyntheticField
    >>> sg = Subgrounds()
    >>> univ3 = sg.load_subgraph(
    ...     'https://api.thegraph.com/subgraphs/name/uniswap/uniswap-v3'
    ... )
    
    # Create constant SyntheticFields
    >>> univ3.Mint.tx_type = SyntheticField.constant('MINT')
    >>> univ3.Burn.tx_type = SyntheticField.constant('BURN')
    
    # Last 10 mints and burns
    >>> mints = univ3.Query.mints(
    ...     first=10,
    ...     orderBy=univ3.Mint.timestamp,
    ...     orderDirection='desc'
    ... )
    >>> burns = univ3.Query.burns(
    ...     first=10,
    ...     orderBy=univ3.Burn.timestamp,
    ...     orderDirection='desc'
    ... )
    
    # Query mints and burns. Notice that we merge the two entity tables by
    # setting `concat=True` and overwriting the column names (columns must
    # match the `FieldPaths`)
    >>> df = sg.query_df([
    ...     mints.transaction.id,
    ...     mints.timestamp,
    ...     mints.tx_type,
    ...     mints.origin,
    ...     mints.amountUSD,
    ...     burns.transaction.id,
    ...     burns.timestamp,
    ...     burns.tx_type,
    ...     burns.origin,
    ...     burns.amountUSD,
    ... ], columns=['tx_hash', 'timestamp', 'tx_type', 'origin', 'amount_USD'], concat=True)
    
    # Sort the DataFrame
    >>> df.sort_values(by=['timestamp'], ascending=False)
                                                  tx_hash   timestamp tx_type                                      origin    amount_USD
    0   0xcbe1bacacc1e64fe613ae5eef2063563bd0057d1e3df...  1656016553    MINT  0x3435e7946d40b1a83c0cf154326fc6b3ca908952  7.879784e+03
    1   0xdddaaddf59e5a3abff4feadef83b3ceb023a74424ea7...  1656016284    MINT  0xc747962e7e416e2a582813b1d7ad59eb83077fa6  5.110840e+04
    10  0xa7671452c34a3b083083ef81e364489c2c9ee801a3b8...  1656016284    BURN  0xd40db77990bbb30514276b5ac17c3ce5cc9c951f  2.804573e+05
    2   0xc132e73975e77c2c2c91fcf332018dfb01aac0ca9471...  1656015853    MINT  0xc747962e7e416e2a582813b1d7ad59eb83077fa6  5.122569e+04
    3   0x1444744f4021a2046787c1b7b88cd9ac21f071c65acc...  1656015773    MINT  0xd11aa2e3a000275ed12b87515c9ac0d67b32e7b9  8.897983e+03
    4   0x3315617d426fc2b0db5d8dbccd549efaa8f1ae2969ca...  1656015693    MINT  0xb7dd4d134b1794ee848e1af1a62b85d7b2ea9301  0.000000e+00
    11  0xcc713daa2dc58cd1f2218c8f438e7fcf04d2e9c7c83d...  1656015278    BURN  0xa7c43e2057d89b6946b8865efc8bee3a4ea7d28d  1.254942e+06
    5   0x7bbfae86f0c3c983651bd0671557cd851fc301317c06...  1656015111    MINT  0xac56cee8ccd00d0c1d72ce3415140874552e80f4  3.432075e+04
    12  0xea21c3a68a8f0c6a2721a3072e0c8b2edc77f4d2f0d9...  1656014785    BURN  0x0709b103d46d71458a71e5d81230dd688809a53d  2.059106e+04
    6   0x3bd369bf45c55cab40c62db81bb3e0684fd85fe2b662...  1656014120    MINT  0x509984bfc0fb24e2d1377cfec224d3afec4c341e  2.517578e+03
    13  0x1ea59da77c442479af8fb51501a931260d473e249de7...  1656014018    BURN  0x509984bfc0fb24e2d1377cfec224d3afec4c341e  0.000000e+00
    7   0xb9d31ef78b8bf786b422d948dd1fba246710078abff8...  1656013998    MINT  0x22dfec183294d257f80c15d3c9cd47495bdc728c  8.365750e+04
    14  0xc5e3ec84a2860e3c3a055ccdced435a67b4aff4dd3be...  1656013946    BURN  0xac56cee8ccd00d0c1d72ce3415140874552e80f4  3.363809e+04
    8   0x7c736255d9a4ebf4781069a1b2a929ad89100f1af980...  1656013913    MINT  0x4ce6aea89f059915ae5efbf34a2a8adc544ae09e  4.837287e+04
    15  0x95cf56b9eb69aa45048a9b7b3e472df5bc3bfad591cd...  1656013728    BURN  0x4ce6aea89f059915ae5efbf34a2a8adc544ae09e  5.110010e+04
    9   0x76dd2bbf43485c224471dd823c2992178f031f27194b...  1656013599    MINT  0x234a644868c419ce0dcdd9fd539762eba47f3759  5.363896e+03
    16  0x47e595b02fdcb51ff42a5008e53be7ee3bdf8063b580...  1656013580    BURN  0xaf0fdd39e5d92499b0ed9f68693da99c0ec1e92e  0.000000e+00
    17  0xe20ec9702f455d74b3cc1f54fe2f3450604ca5037a72...  1656013455    BURN  0xaf0fdd39e5d92499b0ed9f68693da99c0ec1e92e  0.000000e+00
    18  0xac3e95666be3a45fdfbbfa513a114136ea6ecffb9de2...  1656013237    BURN  0x665d2d2444f2384fb3d96aaa0ea3536b92984dce  2.254100e+05
    19  0x01c3424a48c36104ea388482723347f15c0bc1bb1a80...  1656013034    BURN  0x0084ee6c8893c01e252198b56ec127443dc27464  0.000000e+00
    

_ static  _ datetime_of_timestamp  (  _ timestamp  _ )  #

    

Returns a ` SyntheticField  ` that will transform the ` FieldPath  ` `
timestamp  ` into a human-readable ISO8601 string.

Parameters  :

    

**timestamp** ( [ _FieldPath_ ](../top_level/#subgrounds.FieldPath
"subgrounds.FieldPath") _|_ [ _SyntheticField_
](../top_level/#subgrounds.SyntheticField "subgrounds.SyntheticField") ) -- A
` FieldPath  ` representing a Unix timestamp field.

Returns  :

    

An ISO8601 datetime string ` SyntheticField  ` .

Return type  :

    

[ SyntheticField ](../top_level/#subgrounds.SyntheticField
"subgrounds.SyntheticField")

Example:

    
    
    >>> from subgrounds.subgrounds import Subgrounds
    >>> from subgrounds.subgraph import SyntheticField
    >>> sg = Subgrounds()
    >>> univ3 = sg.load_subgraph(
    ...     'https://api.thegraph.com/subgraphs/name/uniswap/uniswap-v3'
    ... )
    
    # Create datetime SyntheticField
    >>> univ3.Swap.datetime = SyntheticField.datetime_of_timestamp(univ3.Swap.timestamp)
    
    # Query 100 swaps
    >>> sg.query_df([
    ...     univ3.Query.swaps.timestamp,
    ...     univ3.Query.swaps.datetime,
    ... ])
        swaps_timestamp       swaps_datetime
    0        1625105710  2021-06-30 22:15:10
    1        1629253724  2021-08-17 22:28:44
    2        1647333277  2022-03-15 04:34:37
    3        1630801974  2021-09-04 20:32:54
    4        1653240241  2022-05-22 13:24:01
    ..              ...                  ...
    95       1646128326  2022-03-01 04:52:06
    96       1646128326  2022-03-01 04:52:06
    97       1626416555  2021-07-16 02:22:35
    98       1626416555  2021-07-16 02:22:35
    99       1625837291  2021-07-09 09:28:11
    

_ static  _ map  (  _ dict  _ , _ type_  _ , _ fpath  _ , _ default  =  None
_ )  #

    

Returns a SyntheticField that will map the values of ` fpath  ` using the key
value pairs in ` dict  ` . If a value is not in the dictionary, then ` default
` will be used instead.

Parameters  :

    

  * **dict** ( [ _dict_ ](https://docs.python.org/3/library/stdtypes.html#dict "\(in Python v3.11\)") _[_ _Any_ _,_ _Any_ _]_ ) -- The dictionary containing the key value pairs used to map ` fpath  ` 's values 

  * **type** ( _TypeRef.T_ ) -- The type of the resulting field 

  * **fpath** ( [ _FieldPath_ ](../top_level/#subgrounds.FieldPath "subgrounds.FieldPath") _|_ [ _SyntheticField_ ](../top_level/#subgrounds.SyntheticField "subgrounds.SyntheticField") ) -- The FieldPath whose values will be mapped using the dictionary 

  * **default** ( _Optional_ _[_ _Any_ _]_ ) -- Default value used when a value is not in the provided dictionary 

Returns  :

    

A map SyntheticField

Return type  :

    

[ SyntheticField ](../top_level/#subgrounds.SyntheticField
"subgrounds.SyntheticField")

Example:

    
    
    >>> from subgrounds.subgrounds import Subgrounds
    >>> from subgrounds.subgraph import SyntheticField
    >>> sg = Subgrounds()
    >>> univ3 = sg.load_subgraph(
    ...     'https://api.thegraph.com/subgraphs/name/uniswap/uniswap-v3'
    ... )
    
    # Hand-crafted mapping of pool addresses to symbol
    >>> pooladdr_symbol_map = {
    ...     '0x5777d92f208679db4b9778590fa3cab3ac9e2168': 'DAI/USDC-001',
    ...     '0x6c6bc977e13df9b0de53b251522280bb72383700': 'DAI/USDC-005',
    ...     '0x8ad599c3a0ff1de082011efddc58f1908eb6e6d8': 'USDC/ETH-030',
    ...     '0x88e6a0c2ddd26feeb64f039a2c41296fcb3f5640': 'USDC/ETH-005',
    ... }
    
    # Create map SyntheticField using our dictionary with 'UNKNOWN' as the
    # default value
    >>> univ3.Pool.symbol = SyntheticField.map(
    ...     pooladdr_symbol_map,
    ...     SyntheticField.STRING,
    ...     univ3.Pool.id,
    ...     'UNKNOWN'
    ... )
    
    # Query top 10 pools by TVL
    >>> pools = univ3.Query.pools(
    ...     first=10,
    ...     orderBy=univ3.Pool.totalValueLockedUSD,
    ...     orderDirection='desc'
    ... )
    >>> sg.query_df([
    ...     pools.id,
    ...     pools.symbol
    ... ])
                                         pools_id  pools_symbol
    0  0xa850478adaace4c08fc61de44d8cf3b64f359bec       UNKNOWN
    1  0x5777d92f208679db4b9778590fa3cab3ac9e2168  DAI/USDC-001
    2  0x6c6bc977e13df9b0de53b251522280bb72383700  DAI/USDC-005
    3  0x8ad599c3a0ff1de082011efddc58f1908eb6e6d8  USDC/ETH-030
    4  0x88e6a0c2ddd26feeb64f039a2c41296fcb3f5640  USDC/ETH-005
    5  0x3416cf6c708da44db2624d63ea0aaef7113527c6       UNKNOWN
    6  0xcbcdf9626bc03e24f779434178a73a0b4bad62ed       UNKNOWN
    7  0xc63b0708e2f7e69cb8a1df0e1389a98c35a76d52       UNKNOWN
    8  0x4585fe77225b41b697c938b018e2ac67ac5a20c0       UNKNOWN
    9  0x4e68ccd3e89f51c3074ca5072bbac773960dfa36       UNKNOWN
    

[ Next  Client  ](client/) [ Previous  Top Level APIs  ](../top_level/)

Made with [ Furo ](https://github.com/pradyunsg/furo)

[ ](https://github.com/0xPlaygrounds/subgrounds) [
](https://discord.gg/v4r4zhBAh2) [ ](https://twitter.com/Playgrounds0x)

On this page

  * Internal 
    * Module contents 
      * ` FieldPath  `
      * ` Subgraph  `
      * ` Subgrounds  `
        * ` Subgrounds.headers  `
        * ` Subgrounds.global_transforms  `
        * ` Subgrounds.subgraphs  `
        * ` Subgrounds.from_pg_key()  `
        * ` Subgrounds.load()  `
        * ` Subgrounds.load_subgraph()  `
        * ` Subgrounds.load_api()  `
        * ` Subgrounds.mk_request()  `
        * ` Subgrounds.execute()  `
        * ` Subgrounds.execute_iter()  `
        * ` Subgrounds.query_json()  `
        * ` Subgrounds.query_json_iter()  `
        * ` Subgrounds.query_df()  `
        * ` Subgrounds.query_df_iter()  `
        * ` Subgrounds.query()  `
        * ` Subgrounds.query_iter()  `
      * ` SyntheticField  `
        * ` SyntheticField.STRING  `
        * ` SyntheticField.INT  `
        * ` SyntheticField.FLOAT  `
        * ` SyntheticField.BOOL  `
        * ` SyntheticField.default_of_type()  `
        * ` SyntheticField.constant()  `
        * ` SyntheticField.datetime_of_timestamp()  `
        * ` SyntheticField.map()  `



Contents  Menu  Expand  Light mode  Dark mode  Auto light/dark mode

Hide navigation sidebar

Hide table of contents sidebar

Give us a ⭐️ on [ Github ](https://github.com/0xPlaygrounds/subgrounds)

Toggle site navigation sidebar

_ _

[ Playgrounds  ](../../../../)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

_ _

[ ![Light Logo](../../../../_static/assets/pg-logotype-dark.svg) ![Dark
Logo](../../../../_static/assets/pg-logotype-primary.svg)
](https://playgrounds.network)

Playgrounds API

  * [ Overview ](../../../../api/)
  * [ Getting an API Key ](../../../../api/key/)
  * [ Subgraph Proxy ](../../../../api/subgraph-proxy/)
  * [ Subgrounds Integration ](../../../../api/subgrounds/)
  * [ FAQ ](../../../../api/faq/)

Toggle child pages in navigation

_ _

    * [ What is a Query? ](../../../../api/faq/query/)
  * [ API Reference ](../../../../api/api-reference/)

Toggle child pages in navigation

_ _

    * [ Subgraph Proxy ](../../../../api/reference/proxy/)

Toggle child pages in navigation

_ _

      * [ Subgraph ID ](../../../../api/reference/proxy/subgraph_id/)
      * [ Deployment ID ](../../../../api/reference/proxy/deployment_id/)

Subgrounds

  * [ Overview ](../../../)
  * [ Getting Started ](../../../getting_started/)

Toggle child pages in navigation

_ _

    * [ The Basics ](../../../getting_started/basics/)
    * [ Field Paths ](../../../getting_started/field_paths/)

Toggle child pages in navigation

_ _

      * [ Arguments ](../../../getting_started/field_paths/arguments/)
      * [ Filtering ](../../../getting_started/field_paths/filtering/)
      * [ Sorting ](../../../getting_started/field_paths/sorting/)
      * [ Merging ](../../../getting_started/field_paths/merging/)
    * [ Querying ](../../../getting_started/querying/)

Toggle child pages in navigation

_ _

    * [ Synthetic Fields ](../../../getting_started/synthetic_fields/)
  * [ Advanced Topics ](../../../advanced_topics/)

Toggle child pages in navigation

_ _

    * [ Contrib ](../../../advanced_topics/contrib/)

Toggle child pages in navigation

_ _

      * [ Plotly ](../../../advanced_topics/contrib/plotly/)
    * [ Pagination ](../../../advanced_topics/pagination/)

Toggle child pages in navigation

_ _

      * [ Custom Strategies ](../../../advanced_topics/pagination/custom/)
  * [ FAQ ](../../../faq/)

Toggle child pages in navigation

_ _

    * [ Exporting to Disk ](../../../faq/exporting/)
    * [ Getting More Data ](../../../faq/more_data/)
    * [ Python Setup ](../../../faq/setup/)

Toggle child pages in navigation

_ _

      * [ Python Versioning ](../../../faq/setup/version_management/)
  * [ Examples ](../../../examples/)

Toggle child pages in navigation

_ _

    * [ Exchanges ](../../../examples/exchanges/)
    * [ Bridges ](../../../examples/bridges/)
    * [ Liquid Staking ](../../../examples/liquid_staking/)
    * [ Governance ](../../../examples/governance/)
    * [ Advanced Research ](../../../examples/advanced_research/)
    * [ Vaults ](../../../examples/vaults/)
  * [ Videos ](../../../videos/)
  * [ Changelog ](../../../changelog/)
  * [ Contributing ](../../../contributing/)
  * [ API Reference ](../../)

Toggle child pages in navigation

_ _

    * [ Top Level APIs ](../../top_level/)
    * [ Internal ](../)

Toggle child pages in navigation

_ _

      * Client 

Toggle child pages in navigation

_ _

        * [ Base ](base/)
        * [ Sync ](sync/)
        * [ Async_ ](async_/)
      * [ Contrib ](../contrib/)

Toggle child pages in navigation

_ _

        * [ Plotly ](../contrib/plotly/)
        * [ Dash ](../contrib/dash/)
      * [ Pagination ](../pagination/)

Toggle child pages in navigation

_ _

        * [ Strategies ](../pagination/strategies/)
        * [ Preprocess ](../pagination/preprocess/)
        * [ Pagination ](../pagination/pagination/)
        * [ Utils ](../pagination/utils/)
      * [ Transform ](../transform/)

Toggle child pages in navigation

_ _

        * [ ABCs ](../transform/abcs/)
        * [ Apply ](../transform/apply/)
        * [ Defaults ](../transform/defaults/)
        * [ Transforms ](../transform/transforms/)
        * [ Utils ](../transform/utils/)
      * [ Subgraph ](../subgraph/)

Toggle child pages in navigation

_ _

        * [ Fieldpath ](../subgraph/fieldpath/)
        * [ Filter ](../subgraph/filter/)
        * [ Object ](../subgraph/object/)
        * [ Subgraph ](../subgraph/subgraph/)
      * [ Errors ](../errors/)
      * [ Query ](../query/)
      * [ Schema ](../schema/)
      * [ Utils ](../utils/)

Meta

  * [ Improving the Docs ](../../../../meta/contributing/)

Back to top

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

_ _

#  Client  #

  * [ Base ](base/)
  * [ Sync ](sync/)
  * [ Async_ ](async_/)

Small module containing low level functions related to sending GraphQL http
requests.

subgrounds.client.  get_schema  (  _ url  _ , _ headers  _ )  #

    

Runs the introspection query on the GraphQL API served localed at ` url  ` and
returns the result. In case of errors, an exception containing the error
message is thrown.

Parameters  :

    

**url** ( [ _str_ ](https://docs.python.org/3/library/stdtypes.html#str "\(in
Python v3.11\)") ) -- The url of the GraphQL API

Raises  :

    

  * **HttpError** \-- If the request response resulted in an error 

  * [ **ServerError** ](../errors/#subgrounds.errors.ServerError "subgrounds.errors.ServerError") \-- If server responds back non-json content 

  * [ **GraphQLError** ](../errors/#subgrounds.errors.GraphQLError "subgrounds.errors.GraphQLError") \-- If the GraphQL query failed or other grapql server errors 

Returns  :

    

The GraphQL API's schema in JSON

Return type  :

    

[ dict ](https://docs.python.org/3/library/stdtypes.html#dict "\(in Python
v3.11\)") [ [ str ](https://docs.python.org/3/library/stdtypes.html#str "\(in
Python v3.11\)") , Any]

subgrounds.client.  query  (  _ url  _ , _ query_str  _ , _ variables  =  {}
_ , _ headers  =  {}  _ )  #

    

Executes the GraphQL query ` query_str  ` with variables ` variables  `
against the API served at ` url  ` and returns the response data. In case of
errors, an exception containing the error message is thrown.

Parameters  :

    

  * **url** ( [ _str_ ](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.11\)") ) -- The URL of the GraphQL API 

  * **query_str** ( [ _str_ ](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.11\)") ) -- The GraphQL query string 

  * **variables** ( [ _dict_ ](https://docs.python.org/3/library/stdtypes.html#dict "\(in Python v3.11\)") _[_ [ _str_ ](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.11\)") _,_ _Any_ _]_ _,_ _optional_ ) -- Variables for the GraphQL query. Defaults to {}. 

Raises  :

    

  * **HttpError** \-- If the request response resulted in an error 

  * [ **ServerError** ](../errors/#subgrounds.errors.ServerError "subgrounds.errors.ServerError") \-- If server responds back non-json content 

  * [ **GraphQLError** ](../errors/#subgrounds.errors.GraphQLError "subgrounds.errors.GraphQLError") \-- If the GraphQL query failed or other grapql server errors 

Returns  :

    

Response data

Return type  :

    

[ dict ](https://docs.python.org/3/library/stdtypes.html#dict "\(in Python
v3.11\)") [ [ str ](https://docs.python.org/3/library/stdtypes.html#str "\(in
Python v3.11\)") , Any]

[ Next  Base  ](base/) [ Previous  Internal  ](../)

Made with [ Furo ](https://github.com/pradyunsg/furo)

[ ](https://github.com/0xPlaygrounds/subgrounds) [
](https://discord.gg/v4r4zhBAh2) [ ](https://twitter.com/Playgrounds0x)

On this page

  * Client 
    * ` get_schema()  `
    * ` query()  `



Contents  Menu  Expand  Light mode  Dark mode  Auto light/dark mode

Hide navigation sidebar

Hide table of contents sidebar

Give us a ⭐️ on [ Github ](https://github.com/0xPlaygrounds/subgrounds)

Toggle site navigation sidebar

_ _

[ Playgrounds  ](../../../../../)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

_ _

[ ![Light Logo](../../../../../_static/assets/pg-logotype-dark.svg) ![Dark
Logo](../../../../../_static/assets/pg-logotype-primary.svg)
](https://playgrounds.network)

Playgrounds API

  * [ Overview ](../../../../../api/)
  * [ Getting an API Key ](../../../../../api/key/)
  * [ Subgraph Proxy ](../../../../../api/subgraph-proxy/)
  * [ Subgrounds Integration ](../../../../../api/subgrounds/)
  * [ FAQ ](../../../../../api/faq/)

Toggle child pages in navigation

_ _

    * [ What is a Query? ](../../../../../api/faq/query/)
  * [ API Reference ](../../../../../api/api-reference/)

Toggle child pages in navigation

_ _

    * [ Subgraph Proxy ](../../../../../api/reference/proxy/)

Toggle child pages in navigation

_ _

      * [ Subgraph ID ](../../../../../api/reference/proxy/subgraph_id/)
      * [ Deployment ID ](../../../../../api/reference/proxy/deployment_id/)

Subgrounds

  * [ Overview ](../../../../)
  * [ Getting Started ](../../../../getting_started/)

Toggle child pages in navigation

_ _

    * [ The Basics ](../../../../getting_started/basics/)
    * [ Field Paths ](../../../../getting_started/field_paths/)

Toggle child pages in navigation

_ _

      * [ Arguments ](../../../../getting_started/field_paths/arguments/)
      * [ Filtering ](../../../../getting_started/field_paths/filtering/)
      * [ Sorting ](../../../../getting_started/field_paths/sorting/)
      * [ Merging ](../../../../getting_started/field_paths/merging/)
    * [ Querying ](../../../../getting_started/querying/)

Toggle child pages in navigation

_ _

    * [ Synthetic Fields ](../../../../getting_started/synthetic_fields/)
  * [ Advanced Topics ](../../../../advanced_topics/)

Toggle child pages in navigation

_ _

    * [ Contrib ](../../../../advanced_topics/contrib/)

Toggle child pages in navigation

_ _

      * [ Plotly ](../../../../advanced_topics/contrib/plotly/)
    * [ Pagination ](../../../../advanced_topics/pagination/)

Toggle child pages in navigation

_ _

      * [ Custom Strategies ](../../../../advanced_topics/pagination/custom/)
  * [ FAQ ](../../../../faq/)

Toggle child pages in navigation

_ _

    * [ Exporting to Disk ](../../../../faq/exporting/)
    * [ Getting More Data ](../../../../faq/more_data/)
    * [ Python Setup ](../../../../faq/setup/)

Toggle child pages in navigation

_ _

      * [ Python Versioning ](../../../../faq/setup/version_management/)
  * [ Examples ](../../../../examples/)

Toggle child pages in navigation

_ _

    * [ Exchanges ](../../../../examples/exchanges/)
    * [ Bridges ](../../../../examples/bridges/)
    * [ Liquid Staking ](../../../../examples/liquid_staking/)
    * [ Governance ](../../../../examples/governance/)
    * [ Advanced Research ](../../../../examples/advanced_research/)
    * [ Vaults ](../../../../examples/vaults/)
  * [ Videos ](../../../../videos/)
  * [ Changelog ](../../../../changelog/)
  * [ Contributing ](../../../../contributing/)
  * [ API Reference ](../../../)

Toggle child pages in navigation

_ _

    * [ Top Level APIs ](../../../top_level/)
    * [ Internal ](../../)

Toggle child pages in navigation

_ _

      * [ Client ](../../client/)

Toggle child pages in navigation

_ _

        * [ Base ](../../client/base/)
        * [ Sync ](../../client/sync/)
        * [ Async_ ](../../client/async_/)
      * [ Contrib ](../)

Toggle child pages in navigation

_ _

        * Plotly 
        * [ Dash ](../dash/)
      * [ Pagination ](../../pagination/)

Toggle child pages in navigation

_ _

        * [ Strategies ](../../pagination/strategies/)
        * [ Preprocess ](../../pagination/preprocess/)
        * [ Pagination ](../../pagination/pagination/)
        * [ Utils ](../../pagination/utils/)
      * [ Transform ](../../transform/)

Toggle child pages in navigation

_ _

        * [ ABCs ](../../transform/abcs/)
        * [ Apply ](../../transform/apply/)
        * [ Defaults ](../../transform/defaults/)
        * [ Transforms ](../../transform/transforms/)
        * [ Utils ](../../transform/utils/)
      * [ Subgraph ](../../subgraph/)

Toggle child pages in navigation

_ _

        * [ Fieldpath ](../../subgraph/fieldpath/)
        * [ Filter ](../../subgraph/filter/)
        * [ Object ](../../subgraph/object/)
        * [ Subgraph ](../../subgraph/subgraph/)
      * [ Errors ](../../errors/)
      * [ Query ](../../query/)
      * [ Schema ](../../schema/)
      * [ Utils ](../../utils/)

Meta

  * [ Improving the Docs ](../../../../../meta/contributing/)

Back to top

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

_ _

#  Plotly  #

Subgrounds Plotly Components

Extending plotly components to be able to understand subgrounds logic.

_ class  _ subgrounds.contrib.plotly.  TraceWrapper  (  _ **  kwargs  _ )  #

    

_ class  _ subgrounds.contrib.plotly.  Scatter  (  _ **  kwargs  _ )  #

    

See [ https://plotly.com/python/line-and-scatter/
](https://plotly.com/python/line-and-scatter/)

graph_object  #

    

alias of ` Scatter  `

_ class  _ subgrounds.contrib.plotly.  Pie  (  _ **  kwargs  _ )  #

    

See [ https://plotly.com/python/pie-charts/ ](https://plotly.com/python/pie-
charts/)

graph_object  #

    

alias of ` Pie  `

_ class  _ subgrounds.contrib.plotly.  Bar  (  _ **  kwargs  _ )  #

    

See [ https://plotly.com/python/bar-charts/ ](https://plotly.com/python/bar-
charts/)

graph_object  #

    

alias of ` Bar  `

_ class  _ subgrounds.contrib.plotly.  Heatmap  (  _ **  kwargs  _ )  #

    

See [ https://plotly.com/python/heatmaps/
](https://plotly.com/python/heatmaps/)

graph_object  #

    

alias of ` Heatmap  `

_ class  _ subgrounds.contrib.plotly.  Contour  (  _ **  kwargs  _ )  #

    

See [ https://plotly.com/python/contour-plots/
](https://plotly.com/python/contour-plots/)

graph_object  #

    

alias of ` Contour  `

_ class  _ subgrounds.contrib.plotly.  Table  (  _ **  kwargs  _ )  #

    

See [ https://plotly.com/python/contour-plots/
](https://plotly.com/python/contour-plots/)

graph_object  #

    

alias of ` Table  `

_ class  _ subgrounds.contrib.plotly.  Box  (  _ **  kwargs  _ )  #

    

See [ https://plotly.com/python/box-plots/ ](https://plotly.com/python/box-
plots/)

graph_object  #

    

alias of ` Box  `

_ class  _ subgrounds.contrib.plotly.  Violin  (  _ **  kwargs  _ )  #

    

See [ https://plotly.com/python/violin/ ](https://plotly.com/python/violin/)

graph_object  #

    

alias of ` Violin  `

_ class  _ subgrounds.contrib.plotly.  Histogram  (  _ **  kwargs  _ )  #

    

See [ https://plotly.com/python/histograms/
](https://plotly.com/python/histograms/)

graph_object  #

    

alias of ` Histogram  `

_ class  _ subgrounds.contrib.plotly.  Histogram2d  (  _ **  kwargs  _ )  #

    

See [ https://plotly.com/python/2D-Histogram/
](https://plotly.com/python/2D-Histogram/)

graph_object  #

    

alias of ` Histogram2d  `

_ class  _ subgrounds.contrib.plotly.  Histogram2dContour  (  _ **  kwargs  _
)  #

    

See [ https://plotly.com/python/2d-histogram-contour/
](https://plotly.com/python/2d-histogram-contour/)

graph_object  #

    

alias of ` Histogram2dContour  `

_ class  _ subgrounds.contrib.plotly.  Ohlc  (  _ **  kwargs  _ )  #

    

See [ https://plotly.com/python/ohlc-charts/ ](https://plotly.com/python/ohlc-
charts/)

graph_object  #

    

alias of ` Ohlc  `

_ class  _ subgrounds.contrib.plotly.  Candlestick  (  _ **  kwargs  _ )  #

    

See [ https://plotly.com/python/candlestick-charts/
](https://plotly.com/python/candlestick-charts/)

graph_object  #

    

alias of ` Candlestick  `

_ class  _ subgrounds.contrib.plotly.  Waterfall  (  _ **  kwargs  _ )  #

    

See [ https://plotly.com/python/waterfall-charts/
](https://plotly.com/python/waterfall-charts/)

graph_object  #

    

alias of ` Waterfall  `

_ class  _ subgrounds.contrib.plotly.  Funnel  (  _ **  kwargs  _ )  #

    

See [ https://plotly.com/python/funnel-charts/
](https://plotly.com/python/funnel-charts/)

graph_object  #

    

alias of ` Funnel  `

_ class  _ subgrounds.contrib.plotly.  Indicator  (  _ **  kwargs  _ )  #

    

See [ https://plotly.com/python/indicator/
](https://plotly.com/python/indicator/)

graph_object  #

    

alias of ` Indicator  `

_ class  _ subgrounds.contrib.plotly.  Scatter3d  (  _ **  kwargs  _ )  #

    

See [ https://plotly.com/python/3d-scatter-plots/
](https://plotly.com/python/3d-scatter-plots/)

graph_object  #

    

alias of ` Scatter3d  `

_ class  _ subgrounds.contrib.plotly.  Surface  (  _ **  kwargs  _ )  #

    

See [ https://plotly.com/python/3d-surface-plots/
](https://plotly.com/python/3d-surface-plots/)

graph_object  #

    

alias of ` Surface  `

_ class  _ subgrounds.contrib.plotly.  Scattergeo  (  _ **  kwargs  _ )  #

    

See [ https://plotly.com/python/scatter-plots-on-maps/
](https://plotly.com/python/scatter-plots-on-maps/)

graph_object  #

    

alias of ` Scattergeo  `

_ class  _ subgrounds.contrib.plotly.  Choropleth  (  _ **  kwargs  _ )  #

    

See [ https://plotly.com/python/choropleth-maps/
](https://plotly.com/python/choropleth-maps/)

graph_object  #

    

alias of ` Choropleth  `

_ class  _ subgrounds.contrib.plotly.  Scattermapbox  (  _ **  kwargs  _ )  #

    

See [ https://plotly.com/python/scattermapbox/
](https://plotly.com/python/scattermapbox/)

graph_object  #

    

alias of ` Scattermapbox  `

_ class  _ subgrounds.contrib.plotly.  Choroplethmapbox  (  _ **  kwargs  _ )
#

    

See [ https://plotly.com/python/mapbox-county-choropleth/
](https://plotly.com/python/mapbox-county-choropleth/)

graph_object  #

    

alias of ` Choroplethmapbox  `

_ class  _ subgrounds.contrib.plotly.  Densitymapbox  (  _ **  kwargs  _ )  #

    

See [ https://plotly.com/python/mapbox-density-heatmaps/
](https://plotly.com/python/mapbox-density-heatmaps/)

graph_object  #

    

alias of ` Densitymapbox  `

_ class  _ subgrounds.contrib.plotly.  Scatterpolar  (  _ **  kwargs  _ )  #

    

See [ https://plotly.com/python/polar-chart/
](https://plotly.com/python/polar-chart/)

graph_object  #

    

alias of ` Scatterpolar  `

_ class  _ subgrounds.contrib.plotly.  Barpolar  (  _ **  kwargs  _ )  #

    

See [ https://plotly.com/python/wind-rose-charts/
](https://plotly.com/python/wind-rose-charts/)

graph_object  #

    

alias of ` Barpolar  `

_ class  _ subgrounds.contrib.plotly.  Sunburst  (  _ **  kwargs  _ )  #

    

See [ https://plotly.com/python/sunburst-charts/
](https://plotly.com/python/sunburst-charts/)

graph_object  #

    

alias of ` Sunburst  `

_ class  _ subgrounds.contrib.plotly.  Treemap  (  _ **  kwargs  _ )  #

    

See [ https://plotly.com/python/treemaps/
](https://plotly.com/python/treemaps/)

graph_object  #

    

alias of ` Treemap  `

_ class  _ subgrounds.contrib.plotly.  Icicle  (  _ **  kwargs  _ )  #

    

See [ https://plotly.com/python/icicle-charts/
](https://plotly.com/python/icicle-charts/)

graph_object  #

    

alias of ` Icicle  `

_ class  _ subgrounds.contrib.plotly.  Sankey  (  _ **  kwargs  _ )  #

    

See [ https://plotly.com/python/sankey-diagram/
](https://plotly.com/python/sankey-diagram/)

graph_object  #

    

alias of ` Sankey  `

_ class  _ subgrounds.contrib.plotly.  Parcoords  (  _ **  kwargs  _ )  #

    

See [ https://plotly.com/python/parallel-coordinates-plot/
](https://plotly.com/python/parallel-coordinates-plot/)

graph_object  #

    

alias of ` Parcoords  `

_ class  _ subgrounds.contrib.plotly.  Parcats  (  _ **  kwargs  _ )  #

    

See [ https://plotly.com/python/parallel-categories-diagram/
](https://plotly.com/python/parallel-categories-diagram/)

graph_object  #

    

alias of ` Parcats  `

_ class  _ subgrounds.contrib.plotly.  Carpet  (  _ **  kwargs  _ )  #

    

See [ https://plotly.com/python/carpet-plot/
](https://plotly.com/python/carpet-plot/)

graph_object  #

    

alias of ` Carpet  `

_ class  _ subgrounds.contrib.plotly.  Scattercarpet  (  _ **  kwargs  _ )  #

    

See [ https://plotly.com/python/carpet-scatter/
](https://plotly.com/python/carpet-scatter/)

graph_object  #

    

alias of ` Scattercarpet  `

_ class  _ subgrounds.contrib.plotly.  Contourcarpet  (  _ **  kwargs  _ )  #

    

See [ https://plotly.com/python/carpet-contour/
](https://plotly.com/python/carpet-contour/)

graph_object  #

    

alias of ` Contourcarpet  `

[ Next  Dash  ](../dash/) [ Previous  Contrib  ](../)

Made with [ Furo ](https://github.com/pradyunsg/furo)

[ ](https://github.com/0xPlaygrounds/subgrounds) [
](https://discord.gg/v4r4zhBAh2) [ ](https://twitter.com/Playgrounds0x)

On this page

  * Plotly 
    * ` TraceWrapper  `
    * ` Scatter  `
      * ` Scatter.graph_object  `
    * ` Pie  `
      * ` Pie.graph_object  `
    * ` Bar  `
      * ` Bar.graph_object  `
    * ` Heatmap  `
      * ` Heatmap.graph_object  `
    * ` Contour  `
      * ` Contour.graph_object  `
    * ` Table  `
      * ` Table.graph_object  `
    * ` Box  `
      * ` Box.graph_object  `
    * ` Violin  `
      * ` Violin.graph_object  `
    * ` Histogram  `
      * ` Histogram.graph_object  `
    * ` Histogram2d  `
      * ` Histogram2d.graph_object  `
    * ` Histogram2dContour  `
      * ` Histogram2dContour.graph_object  `
    * ` Ohlc  `
      * ` Ohlc.graph_object  `
    * ` Candlestick  `
      * ` Candlestick.graph_object  `
    * ` Waterfall  `
      * ` Waterfall.graph_object  `
    * ` Funnel  `
      * ` Funnel.graph_object  `
    * ` Indicator  `
      * ` Indicator.graph_object  `
    * ` Scatter3d  `
      * ` Scatter3d.graph_object  `
    * ` Surface  `
      * ` Surface.graph_object  `
    * ` Scattergeo  `
      * ` Scattergeo.graph_object  `
    * ` Choropleth  `
      * ` Choropleth.graph_object  `
    * ` Scattermapbox  `
      * ` Scattermapbox.graph_object  `
    * ` Choroplethmapbox  `
      * ` Choroplethmapbox.graph_object  `
    * ` Densitymapbox  `
      * ` Densitymapbox.graph_object  `
    * ` Scatterpolar  `
      * ` Scatterpolar.graph_object  `
    * ` Barpolar  `
      * ` Barpolar.graph_object  `
    * ` Sunburst  `
      * ` Sunburst.graph_object  `
    * ` Treemap  `
      * ` Treemap.graph_object  `
    * ` Icicle  `
      * ` Icicle.graph_object  `
    * ` Sankey  `
      * ` Sankey.graph_object  `
    * ` Parcoords  `
      * ` Parcoords.graph_object  `
    * ` Parcats  `
      * ` Parcats.graph_object  `
    * ` Carpet  `
      * ` Carpet.graph_object  `
    * ` Scattercarpet  `
      * ` Scattercarpet.graph_object  `
    * ` Contourcarpet  `
      * ` Contourcarpet.graph_object  `



Contents  Menu  Expand  Light mode  Dark mode  Auto light/dark mode

Hide navigation sidebar

Hide table of contents sidebar

Give us a ⭐️ on [ Github ](https://github.com/0xPlaygrounds/subgrounds)

Toggle site navigation sidebar

_ _

[ Playgrounds  ](../../../../../)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

_ _

[ ![Light Logo](../../../../../_static/assets/pg-logotype-dark.svg) ![Dark
Logo](../../../../../_static/assets/pg-logotype-primary.svg)
](https://playgrounds.network)

Playgrounds API

  * [ Overview ](../../../../../api/)
  * [ Getting an API Key ](../../../../../api/key/)
  * [ Subgraph Proxy ](../../../../../api/subgraph-proxy/)
  * [ Subgrounds Integration ](../../../../../api/subgrounds/)
  * [ FAQ ](../../../../../api/faq/)

Toggle child pages in navigation

_ _

    * [ What is a Query? ](../../../../../api/faq/query/)
  * [ API Reference ](../../../../../api/api-reference/)

Toggle child pages in navigation

_ _

    * [ Subgraph Proxy ](../../../../../api/reference/proxy/)

Toggle child pages in navigation

_ _

      * [ Subgraph ID ](../../../../../api/reference/proxy/subgraph_id/)
      * [ Deployment ID ](../../../../../api/reference/proxy/deployment_id/)

Subgrounds

  * [ Overview ](../../../../)
  * [ Getting Started ](../../../../getting_started/)

Toggle child pages in navigation

_ _

    * [ The Basics ](../../../../getting_started/basics/)
    * [ Field Paths ](../../../../getting_started/field_paths/)

Toggle child pages in navigation

_ _

      * [ Arguments ](../../../../getting_started/field_paths/arguments/)
      * [ Filtering ](../../../../getting_started/field_paths/filtering/)
      * [ Sorting ](../../../../getting_started/field_paths/sorting/)
      * [ Merging ](../../../../getting_started/field_paths/merging/)
    * [ Querying ](../../../../getting_started/querying/)

Toggle child pages in navigation

_ _

    * [ Synthetic Fields ](../../../../getting_started/synthetic_fields/)
  * [ Advanced Topics ](../../../../advanced_topics/)

Toggle child pages in navigation

_ _

    * [ Contrib ](../../../../advanced_topics/contrib/)

Toggle child pages in navigation

_ _

      * [ Plotly ](../../../../advanced_topics/contrib/plotly/)
    * [ Pagination ](../../../../advanced_topics/pagination/)

Toggle child pages in navigation

_ _

      * [ Custom Strategies ](../../../../advanced_topics/pagination/custom/)
  * [ FAQ ](../../../../faq/)

Toggle child pages in navigation

_ _

    * [ Exporting to Disk ](../../../../faq/exporting/)
    * [ Getting More Data ](../../../../faq/more_data/)
    * [ Python Setup ](../../../../faq/setup/)

Toggle child pages in navigation

_ _

      * [ Python Versioning ](../../../../faq/setup/version_management/)
  * [ Examples ](../../../../examples/)

Toggle child pages in navigation

_ _

    * [ Exchanges ](../../../../examples/exchanges/)
    * [ Bridges ](../../../../examples/bridges/)
    * [ Liquid Staking ](../../../../examples/liquid_staking/)
    * [ Governance ](../../../../examples/governance/)
    * [ Advanced Research ](../../../../examples/advanced_research/)
    * [ Vaults ](../../../../examples/vaults/)
  * [ Videos ](../../../../videos/)
  * [ Changelog ](../../../../changelog/)
  * [ Contributing ](../../../../contributing/)
  * [ API Reference ](../../../)

Toggle child pages in navigation

_ _

    * [ Top Level APIs ](../../../top_level/)
    * [ Internal ](../../)

Toggle child pages in navigation

_ _

      * [ Client ](../../client/)

Toggle child pages in navigation

_ _

        * [ Base ](../../client/base/)
        * [ Sync ](../../client/sync/)
        * [ Async_ ](../../client/async_/)
      * [ Contrib ](../)

Toggle child pages in navigation

_ _

        * [ Plotly ](../plotly/)
        * Dash 
      * [ Pagination ](../../pagination/)

Toggle child pages in navigation

_ _

        * [ Strategies ](../../pagination/strategies/)
        * [ Preprocess ](../../pagination/preprocess/)
        * [ Pagination ](../../pagination/pagination/)
        * [ Utils ](../../pagination/utils/)
      * [ Transform ](../../transform/)

Toggle child pages in navigation

_ _

        * [ ABCs ](../../transform/abcs/)
        * [ Apply ](../../transform/apply/)
        * [ Defaults ](../../transform/defaults/)
        * [ Transforms ](../../transform/transforms/)
        * [ Utils ](../../transform/utils/)
      * [ Subgraph ](../../subgraph/)

Toggle child pages in navigation

_ _

        * [ Fieldpath ](../../subgraph/fieldpath/)
        * [ Filter ](../../subgraph/filter/)
        * [ Object ](../../subgraph/object/)
        * [ Subgraph ](../../subgraph/subgraph/)
      * [ Errors ](../../errors/)
      * [ Query ](../../query/)
      * [ Schema ](../../schema/)
      * [ Utils ](../../utils/)

Meta

  * [ Improving the Docs ](../../../../../meta/contributing/)

Back to top

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

_ _

#  Dash  #

Subgrounds Dash Components

Extending dash components to be able to understand subgrounds logic. This
includes other

    

extended components of other libraries such as  plotly  .

_ class  _ subgrounds.contrib.dash.  Refreshable  #

    

_ class  _ subgrounds.contrib.dash.  Graph  (  _ fig  _ , _ **  kwargs  _ )  #

    

_ class  _ subgrounds.contrib.dash.  DataTable  (  _ subgrounds  _ , _ data  _
, _ columns  =  None  _ , _ concat  =  False  _ , _ append  =  False  _ , _ **
kwargs  _ )  #

    

_ class  _ subgrounds.contrib.dash.  AutoUpdate  (  _ app  _ , _ sec_interval
=  1  _ , _ children  =  []  _ , _ **  kwargs  _ )  #

    

[ Next  Pagination  ](../../pagination/) [ Previous  Plotly  ](../plotly/)

Made with [ Furo ](https://github.com/pradyunsg/furo)

[ ](https://github.com/0xPlaygrounds/subgrounds) [
](https://discord.gg/v4r4zhBAh2) [ ](https://twitter.com/Playgrounds0x)

On this page

  * Dash 
    * ` Refreshable  `
    * ` Graph  `
    * ` DataTable  `
    * ` AutoUpdate  `



Contents  Menu  Expand  Light mode  Dark mode  Auto light/dark mode

Hide navigation sidebar

Hide table of contents sidebar

Give us a ⭐️ on [ Github ](https://github.com/0xPlaygrounds/subgrounds)

Toggle site navigation sidebar

_ _

[ Playgrounds  ](../../../../)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

_ _

[ ![Light Logo](../../../../_static/assets/pg-logotype-dark.svg) ![Dark
Logo](../../../../_static/assets/pg-logotype-primary.svg)
](https://playgrounds.network)

Playgrounds API

  * [ Overview ](../../../../api/)
  * [ Getting an API Key ](../../../../api/key/)
  * [ Subgraph Proxy ](../../../../api/subgraph-proxy/)
  * [ Subgrounds Integration ](../../../../api/subgrounds/)
  * [ FAQ ](../../../../api/faq/)

Toggle child pages in navigation

_ _

    * [ What is a Query? ](../../../../api/faq/query/)
  * [ API Reference ](../../../../api/api-reference/)

Toggle child pages in navigation

_ _

    * [ Subgraph Proxy ](../../../../api/reference/proxy/)

Toggle child pages in navigation

_ _

      * [ Subgraph ID ](../../../../api/reference/proxy/subgraph_id/)
      * [ Deployment ID ](../../../../api/reference/proxy/deployment_id/)

Subgrounds

  * [ Overview ](../../../)
  * [ Getting Started ](../../../getting_started/)

Toggle child pages in navigation

_ _

    * [ The Basics ](../../../getting_started/basics/)
    * [ Field Paths ](../../../getting_started/field_paths/)

Toggle child pages in navigation

_ _

      * [ Arguments ](../../../getting_started/field_paths/arguments/)
      * [ Filtering ](../../../getting_started/field_paths/filtering/)
      * [ Sorting ](../../../getting_started/field_paths/sorting/)
      * [ Merging ](../../../getting_started/field_paths/merging/)
    * [ Querying ](../../../getting_started/querying/)

Toggle child pages in navigation

_ _

    * [ Synthetic Fields ](../../../getting_started/synthetic_fields/)
  * [ Advanced Topics ](../../../advanced_topics/)

Toggle child pages in navigation

_ _

    * [ Contrib ](../../../advanced_topics/contrib/)

Toggle child pages in navigation

_ _

      * [ Plotly ](../../../advanced_topics/contrib/plotly/)
    * [ Pagination ](../../../advanced_topics/pagination/)

Toggle child pages in navigation

_ _

      * [ Custom Strategies ](../../../advanced_topics/pagination/custom/)
  * [ FAQ ](../../../faq/)

Toggle child pages in navigation

_ _

    * [ Exporting to Disk ](../../../faq/exporting/)
    * [ Getting More Data ](../../../faq/more_data/)
    * [ Python Setup ](../../../faq/setup/)

Toggle child pages in navigation

_ _

      * [ Python Versioning ](../../../faq/setup/version_management/)
  * [ Examples ](../../../examples/)

Toggle child pages in navigation

_ _

    * [ Exchanges ](../../../examples/exchanges/)
    * [ Bridges ](../../../examples/bridges/)
    * [ Liquid Staking ](../../../examples/liquid_staking/)
    * [ Governance ](../../../examples/governance/)
    * [ Advanced Research ](../../../examples/advanced_research/)
    * [ Vaults ](../../../examples/vaults/)
  * [ Videos ](../../../videos/)
  * [ Changelog ](../../../changelog/)
  * [ Contributing ](../../../contributing/)
  * [ API Reference ](../../)

Toggle child pages in navigation

_ _

    * [ Top Level APIs ](../../top_level/)
    * [ Internal ](../)

Toggle child pages in navigation

_ _

      * [ Client ](../client/)

Toggle child pages in navigation

_ _

        * [ Base ](../client/base/)
        * [ Sync ](../client/sync/)
        * [ Async_ ](../client/async_/)
      * [ Contrib ](../contrib/)

Toggle child pages in navigation

_ _

        * [ Plotly ](../contrib/plotly/)
        * [ Dash ](../contrib/dash/)
      * Pagination 

Toggle child pages in navigation

_ _

        * [ Strategies ](strategies/)
        * [ Preprocess ](preprocess/)
        * [ Pagination ](pagination/)
        * [ Utils ](utils/)
      * [ Transform ](../transform/)

Toggle child pages in navigation

_ _

        * [ ABCs ](../transform/abcs/)
        * [ Apply ](../transform/apply/)
        * [ Defaults ](../transform/defaults/)
        * [ Transforms ](../transform/transforms/)
        * [ Utils ](../transform/utils/)
      * [ Subgraph ](../subgraph/)

Toggle child pages in navigation

_ _

        * [ Fieldpath ](../subgraph/fieldpath/)
        * [ Filter ](../subgraph/filter/)
        * [ Object ](../subgraph/object/)
        * [ Subgraph ](../subgraph/subgraph/)
      * [ Errors ](../errors/)
      * [ Query ](../query/)
      * [ Schema ](../schema/)
      * [ Utils ](../utils/)

Meta

  * [ Improving the Docs ](../../../../meta/contributing/)

Back to top

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

_ _

#  Pagination  #

  * [ Strategies ](strategies/)
    * [ ` StopPagination  ` ](strategies/#subgrounds.pagination.strategies.StopPagination)
    * [ ` SkipPagination  ` ](strategies/#subgrounds.pagination.strategies.SkipPagination)
    * [ ` LegacyStrategyArgGenerator  ` ](strategies/#subgrounds.pagination.strategies.LegacyStrategyArgGenerator)
      * [ ` LegacyStrategyArgGenerator.Cursor  ` ](strategies/#subgrounds.pagination.strategies.LegacyStrategyArgGenerator.Cursor)
        * [ ` LegacyStrategyArgGenerator.Cursor.update()  ` ](strategies/#subgrounds.pagination.strategies.LegacyStrategyArgGenerator.Cursor.update)
        * [ ` LegacyStrategyArgGenerator.Cursor.step()  ` ](strategies/#subgrounds.pagination.strategies.LegacyStrategyArgGenerator.Cursor.step)
        * [ ` LegacyStrategyArgGenerator.Cursor.args()  ` ](strategies/#subgrounds.pagination.strategies.LegacyStrategyArgGenerator.Cursor.args)
        * [ ` LegacyStrategyArgGenerator.Cursor.reset()  ` ](strategies/#subgrounds.pagination.strategies.LegacyStrategyArgGenerator.Cursor.reset)
    * [ ` ShallowStrategyArgGenerator  ` ](strategies/#subgrounds.pagination.strategies.ShallowStrategyArgGenerator)
      * [ ` ShallowStrategyArgGenerator.Cursor  ` ](strategies/#subgrounds.pagination.strategies.ShallowStrategyArgGenerator.Cursor)
        * [ ` ShallowStrategyArgGenerator.Cursor.page_node  ` ](strategies/#subgrounds.pagination.strategies.ShallowStrategyArgGenerator.Cursor.page_node)
        * [ ` ShallowStrategyArgGenerator.Cursor.inner  ` ](strategies/#subgrounds.pagination.strategies.ShallowStrategyArgGenerator.Cursor.inner)
        * [ ` ShallowStrategyArgGenerator.Cursor.inner_idx  ` ](strategies/#subgrounds.pagination.strategies.ShallowStrategyArgGenerator.Cursor.inner_idx)
        * [ ` ShallowStrategyArgGenerator.Cursor.filter_value  ` ](strategies/#subgrounds.pagination.strategies.ShallowStrategyArgGenerator.Cursor.filter_value)
        * [ ` ShallowStrategyArgGenerator.Cursor.queried_entities  ` ](strategies/#subgrounds.pagination.strategies.ShallowStrategyArgGenerator.Cursor.queried_entities)
        * [ ` ShallowStrategyArgGenerator.Cursor.stop  ` ](strategies/#subgrounds.pagination.strategies.ShallowStrategyArgGenerator.Cursor.stop)
        * [ ` ShallowStrategyArgGenerator.Cursor.page_count  ` ](strategies/#subgrounds.pagination.strategies.ShallowStrategyArgGenerator.Cursor.page_count)
        * [ ` ShallowStrategyArgGenerator.Cursor.keys  ` ](strategies/#subgrounds.pagination.strategies.ShallowStrategyArgGenerator.Cursor.keys)
  * [ Preprocess ](preprocess/)
    * [ ` PaginationNode  ` ](preprocess/#subgrounds.pagination.preprocess.PaginationNode)
      * [ ` PaginationNode.node_idx  ` ](preprocess/#subgrounds.pagination.preprocess.PaginationNode.node_idx)
      * [ ` PaginationNode.filter_field  ` ](preprocess/#subgrounds.pagination.preprocess.PaginationNode.filter_field)
      * [ ` PaginationNode.first_value  ` ](preprocess/#subgrounds.pagination.preprocess.PaginationNode.first_value)
      * [ ` PaginationNode.skip_value  ` ](preprocess/#subgrounds.pagination.preprocess.PaginationNode.skip_value)
      * [ ` PaginationNode.filter_value  ` ](preprocess/#subgrounds.pagination.preprocess.PaginationNode.filter_value)
      * [ ` PaginationNode.filter_value_type  ` ](preprocess/#subgrounds.pagination.preprocess.PaginationNode.filter_value_type)
      * [ ` PaginationNode.key_path  ` ](preprocess/#subgrounds.pagination.preprocess.PaginationNode.key_path)
      * [ ` PaginationNode.inner  ` ](preprocess/#subgrounds.pagination.preprocess.PaginationNode.inner)
      * [ ` PaginationNode.get_vardefs()  ` ](preprocess/#subgrounds.pagination.preprocess.PaginationNode.get_vardefs)
    * [ ` normalize()  ` ](preprocess/#subgrounds.pagination.preprocess.normalize)
  * [ Pagination ](pagination/)
    * [ ` PaginationError  ` ](pagination/#subgrounds.pagination.pagination.PaginationError)
    * [ ` PaginationStrategy  ` ](pagination/#subgrounds.pagination.pagination.PaginationStrategy)
      * [ ` PaginationStrategy.step()  ` ](pagination/#subgrounds.pagination.pagination.PaginationStrategy.step)
    * [ ` paginate()  ` ](pagination/#subgrounds.pagination.pagination.paginate)
    * [ ` paginate_iter()  ` ](pagination/#subgrounds.pagination.pagination.paginate_iter)
  * [ Utils ](utils/)
    * [ ` merge()  ` ](utils/#subgrounds.pagination.utils.merge)
    * [ ` merge_input_value_object_metas()  ` ](utils/#subgrounds.pagination.utils.merge_input_value_object_metas)

This module contains all code related to automatic pagination.

The ` pagination  ` module contains the pagination algorithms (both regular
and iterative) that make use of ` PaginationStrategies  ` .

The ` preprocess  ` and ` strategties  ` modules implement the currently
supported ` PaginationStrategies  ` : ` LegacyStrategy  ` and `
ShallowStrategy  ` .

The ` utils  ` module contains some generic functions that are useful in the
context of pagination.

subgrounds.pagination.  normalize  (  _ schema  _ , _ document  _ , _
pagination_nodes  _ )  #

    

Inject various graphql components to "normalize" the query for pagination.

When we paginate a query, we inject custom filtering based on the order by
values. We also add GraphQL variables so that  PaginationStrategy  only need
to change those

> to perform pagination.

The main process for normalization begins by recursively adjusting  Selection
nodes

    

within the Query tree. We only apply the following steps if the node needs to
be paginated.

> Note, these steps always check the current selection and will merge new
> values
    

and selections onto whats currently there.

  1. Ensure  id  is on the  Selection 

  2. Replace  first  argument value by  $firstX 

  3. Replace  skip  argument value by  $skipX 

  4. With the  orderBy  (default being  id  ), generate where filtering arguments 

>   1. These are used to filter out values when paginating
>
>

  5. Set  where  filtering values (deep union / merge) 

subgrounds.pagination.  paginate_iter  (  _ schema  _ , _ doc  _ , _
pagination_strategy  _ , _ headers  _ )  #

    

Executes the request document  doc  based on the GraphQL schema  schema  and
returns the response as a JSON dictionary.

Parameters  :

    

  * **schema** ( [ _SchemaMeta_ ](../schema/#subgrounds.schema.SchemaMeta "subgrounds.schema.SchemaMeta") ) -- The GraphQL schema on which the request document is based 

  * **doc** ( [ _Document_ ](../query/#subgrounds.query.Document "subgrounds.query.Document") ) -- The request document 

Returns  :

    

The response data as a JSON dictionary

Return type  :

    

[ dict ](https://docs.python.org/3/library/stdtypes.html#dict "\(in Python
v3.11\)") [ [ str ](https://docs.python.org/3/library/stdtypes.html#str "\(in
Python v3.11\)") , Any]

subgrounds.pagination.  paginate  (  _ schema  _ , _ doc  _ , _
pagination_strategy  _ , _ headers  _ )  #

    

Executes the request document  doc  based on the GraphQL schema  schema  and
returns the response as a JSON dictionary.

Parameters  :

    

  * **schema** ( [ _SchemaMeta_ ](../schema/#subgrounds.schema.SchemaMeta "subgrounds.schema.SchemaMeta") ) -- The GraphQL schema on which the request document is based 

  * **doc** ( [ _Document_ ](../query/#subgrounds.query.Document "subgrounds.query.Document") ) -- The request document 

Returns  :

    

The response data as a JSON dictionary

Return type  :

    

[ dict ](https://docs.python.org/3/library/stdtypes.html#dict "\(in Python
v3.11\)") [ [ str ](https://docs.python.org/3/library/stdtypes.html#str "\(in
Python v3.11\)") , Any]

_ exception  _ subgrounds.pagination.  PaginationError  (  _ message  _ , _
strategy  _ )  #

    

_ class  _ subgrounds.pagination.  PaginationNode  (  _ node_idx  _ , _
filter_field  _ , _ first_value  _ , _ skip_value  _ , _ filter_value  _ , _
filter_value_type  _ , _ key_path  _ , _ inner=<factory> _ )  #

    

Class representing the pagination config for a single GraphQL list field.

node_idx  #

    

Index of PaginationNode, used to label pagination arguments for this node.

Type  :

    

[ int ](https://docs.python.org/3/library/functions.html#int "\(in Python
v3.11\)")

filter_field  #

    

Name of the node's filter field, e.g.: if ` filter_name  ` is ` timestamp_gt
` , then  ` filter_field  ` is ` timestamp  `

Type  :

    

[ str ](https://docs.python.org/3/library/stdtypes.html#str "\(in Python
v3.11\)")

first_value  #

    

Initial value of the ` first  ` argument

Type  :

    

[ int ](https://docs.python.org/3/library/functions.html#int "\(in Python
v3.11\)")

skip_value  #

    

Initial value of the ` skip  ` argument

Type  :

    

[ int ](https://docs.python.org/3/library/functions.html#int "\(in Python
v3.11\)")

filter_value  #

    

Initial value of the filter argument (i.e.: ` where:  {filter:  FILTER_VALUE}
` )

Type  :

    

Any

filter_value_type  #

    

Type of the filter value

Type  :

    

TypeRef.T

key_path  #

    

Location in the list field to which this pagination node refers to in the
initial query

Type  :

    

[ list ](https://docs.python.org/3/library/stdtypes.html#list "\(in Python
v3.11\)") [ [ str ](https://docs.python.org/3/library/stdtypes.html#str "\(in
Python v3.11\)") ]

inner  #

    

Nested pagination nodes (if any).

Type  :

    

[ list ](https://docs.python.org/3/library/stdtypes.html#list "\(in Python
v3.11\)") [  PaginationNode  ]

get_vardefs  (  )  #

    

Returns a list of variable definitions corresponding to this pagination node's
pagination arguments as well as the variable definitions related to any nested
pagination nodes.

Parameters  :

    

**self** (  _PaginationNode_ ) -- The current PaginationNode

Returns  :

    

_description_

Return type  :

    

[ list ](https://docs.python.org/3/library/stdtypes.html#list "\(in Python
v3.11\)") [ [ VariableDefinition
](../query/#subgrounds.query.VariableDefinition
"subgrounds.query.VariableDefinition") ]

_ class  _ subgrounds.pagination.  PaginationStrategy  (  _ *  args  _ , _ **
kwargs  _ )  #

    

step  (  _ page_data  =  None  _ )  #

    

Returns the new query document and its variables which will be executed to get
the next page of data. If this is the first query made as part of the
pagination strategy, then ` page_data  ` will be ` None  ` .

If pagination should be interupted (e.g.: if enough entities have been
queried), then this method should raise a ` StopPagination  ` exception.

Parameters  :

    

  * **page_data** ( _Optional_ _[_ [ _dict_ ](https://docs.python.org/3/library/stdtypes.html#dict "\(in Python v3.11\)") _[_ [ _str_ ](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.11\)") _,_ _Any_ _]_ _]_ _,_ _optional_ ) -- The previous query's response data. 

  * **(** **i.e.** ( _If this is the first query_ ) -- the first page of data), then it will be None. 

  * **None.** ( _Defaults to_ ) -- 

Returns  :

    

A tuple  (doc, vars)  where  doc  is the query document that will be executed
to fetch the next page of data and  vars  are the variables for that document.

Return type  :

    

Tuple[ [ Document ](../query/#subgrounds.query.Document
"subgrounds.query.Document") , [ dict
](https://docs.python.org/3/library/stdtypes.html#dict "\(in Python v3.11\)")
[ [ str ](https://docs.python.org/3/library/stdtypes.html#str "\(in Python
v3.11\)") , Any]]

[ Next  Strategies  ](strategies/) [ Previous  Dash  ](../contrib/dash/)

Made with [ Furo ](https://github.com/pradyunsg/furo)

[ ](https://github.com/0xPlaygrounds/subgrounds) [
](https://discord.gg/v4r4zhBAh2) [ ](https://twitter.com/Playgrounds0x)

On this page

  * Pagination 
    * ` normalize()  `
    * ` paginate_iter()  `
    * ` paginate()  `
    * ` PaginationError  `
    * ` PaginationNode  `
      * ` PaginationNode.node_idx  `
      * ` PaginationNode.filter_field  `
      * ` PaginationNode.first_value  `
      * ` PaginationNode.skip_value  `
      * ` PaginationNode.filter_value  `
      * ` PaginationNode.filter_value_type  `
      * ` PaginationNode.key_path  `
      * ` PaginationNode.inner  `
      * ` PaginationNode.get_vardefs()  `
    * ` PaginationStrategy  `
      * ` PaginationStrategy.step()  `



Contents  Menu  Expand  Light mode  Dark mode  Auto light/dark mode

Hide navigation sidebar

Hide table of contents sidebar

Give us a ⭐️ on [ Github ](https://github.com/0xPlaygrounds/subgrounds)

Toggle site navigation sidebar

_ _

[ Playgrounds  ](../../../../../)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

_ _

[ ![Light Logo](../../../../../_static/assets/pg-logotype-dark.svg) ![Dark
Logo](../../../../../_static/assets/pg-logotype-primary.svg)
](https://playgrounds.network)

Playgrounds API

  * [ Overview ](../../../../../api/)
  * [ Getting an API Key ](../../../../../api/key/)
  * [ Subgraph Proxy ](../../../../../api/subgraph-proxy/)
  * [ Subgrounds Integration ](../../../../../api/subgrounds/)
  * [ FAQ ](../../../../../api/faq/)

Toggle child pages in navigation

_ _

    * [ What is a Query? ](../../../../../api/faq/query/)
  * [ API Reference ](../../../../../api/api-reference/)

Toggle child pages in navigation

_ _

    * [ Subgraph Proxy ](../../../../../api/reference/proxy/)

Toggle child pages in navigation

_ _

      * [ Subgraph ID ](../../../../../api/reference/proxy/subgraph_id/)
      * [ Deployment ID ](../../../../../api/reference/proxy/deployment_id/)

Subgrounds

  * [ Overview ](../../../../)
  * [ Getting Started ](../../../../getting_started/)

Toggle child pages in navigation

_ _

    * [ The Basics ](../../../../getting_started/basics/)
    * [ Field Paths ](../../../../getting_started/field_paths/)

Toggle child pages in navigation

_ _

      * [ Arguments ](../../../../getting_started/field_paths/arguments/)
      * [ Filtering ](../../../../getting_started/field_paths/filtering/)
      * [ Sorting ](../../../../getting_started/field_paths/sorting/)
      * [ Merging ](../../../../getting_started/field_paths/merging/)
    * [ Querying ](../../../../getting_started/querying/)

Toggle child pages in navigation

_ _

    * [ Synthetic Fields ](../../../../getting_started/synthetic_fields/)
  * [ Advanced Topics ](../../../../advanced_topics/)

Toggle child pages in navigation

_ _

    * [ Contrib ](../../../../advanced_topics/contrib/)

Toggle child pages in navigation

_ _

      * [ Plotly ](../../../../advanced_topics/contrib/plotly/)
    * [ Pagination ](../../../../advanced_topics/pagination/)

Toggle child pages in navigation

_ _

      * [ Custom Strategies ](../../../../advanced_topics/pagination/custom/)
  * [ FAQ ](../../../../faq/)

Toggle child pages in navigation

_ _

    * [ Exporting to Disk ](../../../../faq/exporting/)
    * [ Getting More Data ](../../../../faq/more_data/)
    * [ Python Setup ](../../../../faq/setup/)

Toggle child pages in navigation

_ _

      * [ Python Versioning ](../../../../faq/setup/version_management/)
  * [ Examples ](../../../../examples/)

Toggle child pages in navigation

_ _

    * [ Exchanges ](../../../../examples/exchanges/)
    * [ Bridges ](../../../../examples/bridges/)
    * [ Liquid Staking ](../../../../examples/liquid_staking/)
    * [ Governance ](../../../../examples/governance/)
    * [ Advanced Research ](../../../../examples/advanced_research/)
    * [ Vaults ](../../../../examples/vaults/)
  * [ Videos ](../../../../videos/)
  * [ Changelog ](../../../../changelog/)
  * [ Contributing ](../../../../contributing/)
  * [ API Reference ](../../../)

Toggle child pages in navigation

_ _

    * [ Top Level APIs ](../../../top_level/)
    * [ Internal ](../../)

Toggle child pages in navigation

_ _

      * [ Client ](../../client/)

Toggle child pages in navigation

_ _

        * [ Base ](../../client/base/)
        * [ Sync ](../../client/sync/)
        * [ Async_ ](../../client/async_/)
      * [ Contrib ](../../contrib/)

Toggle child pages in navigation

_ _

        * [ Plotly ](../../contrib/plotly/)
        * [ Dash ](../../contrib/dash/)
      * [ Pagination ](../)

Toggle child pages in navigation

_ _

        * Strategies 
        * [ Preprocess ](../preprocess/)
        * [ Pagination ](../pagination/)
        * [ Utils ](../utils/)
      * [ Transform ](../../transform/)

Toggle child pages in navigation

_ _

        * [ ABCs ](../../transform/abcs/)
        * [ Apply ](../../transform/apply/)
        * [ Defaults ](../../transform/defaults/)
        * [ Transforms ](../../transform/transforms/)
        * [ Utils ](../../transform/utils/)
      * [ Subgraph ](../../subgraph/)

Toggle child pages in navigation

_ _

        * [ Fieldpath ](../../subgraph/fieldpath/)
        * [ Filter ](../../subgraph/filter/)
        * [ Object ](../../subgraph/object/)
        * [ Subgraph ](../../subgraph/subgraph/)
      * [ Errors ](../../errors/)
      * [ Query ](../../query/)
      * [ Schema ](../../schema/)
      * [ Utils ](../../utils/)

Meta

  * [ Improving the Docs ](../../../../../meta/contributing/)

Back to top

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

_ _

#  Strategies  #

Subgrounds pagination strategies

This module implements functions and data structures used to implement the two
` PaginationStrategies  ` that Subgrounds offers.

For both strategies, pagination is done in four steps:

  1. Generate one or many ` PaginationNode  ` objects per query document. These are tree-like data structures that extract all information about pagination fields (i.e.: fields that return lists of entities) while maintaining the nestedness relationship between each pagination field (i.e.: which is nested in which). 

  2. The query document is normalized such that every pagination field in the query has: 

>     1. An ordering (i.e.: ` orderBy  ` and ` orderDirection  ` are
> specified)
>
>     2. A ` first  ` argument set to the ` firstN  ` variable
>
>     3. A ` skip  ` argument set to the ` skipN  ` variable
>
>     4. A ` where  ` filter with the filter name derived from the ordering
> and the value being a variable named ` lastOrderingValueN  `

In other words, the query will be transformed in a form which allows
Subgrounds to paginate automatically by simply setting the set of pagination
variables (i.e.: ` firstN  ` , ` skipN  ` and ` lastOrderingValueN  ` ) to
different values. Each field that requires pagination (i.e.: each field that
yields a list) will have its own set of variables, hence the ` N  ` post-fix.

Example: The initial query

    
        query {
      items(
        orderBy: timestamp,
        orderDirection: desc,
        first: 10000
      ) {
        foo
      }
    }
    

will be transformed to

    
        query($first0: Int, $skip0: Int, $lastOrderingValue0: BigInt) {
      items(
        orderBy: timestamp,
        orderDirection: desc,
        first: $first0,
        skip: $skip0,
        where: {
          timestamp_lt: $lastOrderingValue0
        }
      ) {
        foo
      }
    }
    

  3. For each data page, generate the values for the pagination variables (i.e.: ` firstN  ` , ` skipN  ` and ` `lastOrderingValueN`  ` ) 

  4. If some variables are undefined (i.e.: they are present in the query document, but not given a value as part of step 3), then the document is pruned and all selections (and sub-selections) containing undefined variables are removed. 

Depending on the strategy, the variable values computed at step 3 will change.

_ exception  _ subgrounds.pagination.strategies.  StopPagination  (  _ *  args
_ )  #

    

_ exception  _ subgrounds.pagination.strategies.  SkipPagination  (  _ *  args
_ )  #

    

_ class  _ subgrounds.pagination.strategies.  LegacyStrategyArgGenerator  (  _
pagination_nodes  :  'list[PaginationNode]'  _ )  #

    

_ class  _ Cursor  (  _ page_node  :  'PaginationNode'  _ )  #

    

update  (  _ data  _ )  #

    

Moves ` self  ` cursor forward according to previous response data ` data  `
:param data: Previous response data :type data: dict

Raises  :

    

[ **StopIteration**
](https://docs.python.org/3/library/exceptions.html#StopIteration "\(in Python
v3.11\)") \-- _description_

step  (  _ data  _ )  #

    

Updates either ` self  ` cursor or inner state machine depending on whether
the inner state machine has reached its limit :param data: _description_ :type
data: dict

args  (  )  #

    

Returns the pagination arguments for the current state of the state machine
:returns: _description_ :rtype: dict

reset  (  )  #

    

Reset state machine

_ class  _ subgrounds.pagination.strategies.  ShallowStrategyArgGenerator  (
_ pagination_nodes  :  'list[PaginationNode]'  _ )  #

    

_ class  _ Cursor  (  _ page_node  _ , _ inner  _ , _ inner_idx  =  0  _ , _
filter_value  =  None  _ , _ queried_entities  =  0  _ , _ page_count  =  0  _
)  #

    

Class used to generate the pagination variables for a given tree of `
PaginationNode  ` objects.

page_node  #

    

The ` PaginationNode  ` object which this cursor is iterating through.

Type  :

    

[ subgrounds.pagination.preprocess.PaginationNode
](../preprocess/#subgrounds.pagination.preprocess.PaginationNode
"subgrounds.pagination.preprocess.PaginationNode")

inner  #

    

The cursors for nested ` PaginationNodes  ` , if any.

Type  :

    

[ list ](https://docs.python.org/3/library/stdtypes.html#list "\(in Python
v3.11\)") [
subgrounds.pagination.strategies.ShallowStrategyArgGenerator.Cursor  ]

inner_idx  #

    

The index of the inner ` PaginationNode  ` through which this cursor
iterating.

Type  :

    

[ int ](https://docs.python.org/3/library/functions.html#int "\(in Python
v3.11\)")

filter_value  #

    

The previous page's index value used to query the next data page. Depends on `
page_node.filter_field  ` , e.g.: if ` page_node.filter_field  ` is `
timestamp_gt  ` , then ` filter_value  ` will be the highest timestamp the
entities returned in the previous data page.

Type  :

    

Any

queried_entities  #

    

Counter keeping track of the total number of queried entities.

Type  :

    

[ int ](https://docs.python.org/3/library/functions.html#int "\(in Python
v3.11\)")

stop  #

    

Flag indicating whether or not to stop the cursor.

page_count  #

    

Counter keeping track of the total number data pages queried.

Type  :

    

[ int ](https://docs.python.org/3/library/functions.html#int "\(in Python
v3.11\)")

keys  #

    

Set keeping track of the keys of all queried entities to avoid duplicates.

[ Next  Preprocess  ](../preprocess/) [ Previous  Pagination  ](../)

Made with [ Furo ](https://github.com/pradyunsg/furo)

[ ](https://github.com/0xPlaygrounds/subgrounds) [
](https://discord.gg/v4r4zhBAh2) [ ](https://twitter.com/Playgrounds0x)

On this page

  * Strategies 
    * ` StopPagination  `
    * ` SkipPagination  `
    * ` LegacyStrategyArgGenerator  `
      * ` LegacyStrategyArgGenerator.Cursor  `
        * ` LegacyStrategyArgGenerator.Cursor.update()  `
        * ` LegacyStrategyArgGenerator.Cursor.step()  `
        * ` LegacyStrategyArgGenerator.Cursor.args()  `
        * ` LegacyStrategyArgGenerator.Cursor.reset()  `
    * ` ShallowStrategyArgGenerator  `
      * ` ShallowStrategyArgGenerator.Cursor  `
        * ` ShallowStrategyArgGenerator.Cursor.page_node  `
        * ` ShallowStrategyArgGenerator.Cursor.inner  `
        * ` ShallowStrategyArgGenerator.Cursor.inner_idx  `
        * ` ShallowStrategyArgGenerator.Cursor.filter_value  `
        * ` ShallowStrategyArgGenerator.Cursor.queried_entities  `
        * ` ShallowStrategyArgGenerator.Cursor.stop  `
        * ` ShallowStrategyArgGenerator.Cursor.page_count  `
        * ` ShallowStrategyArgGenerator.Cursor.keys  `



Contents  Menu  Expand  Light mode  Dark mode  Auto light/dark mode

Hide navigation sidebar

Hide table of contents sidebar

Give us a ⭐️ on [ Github ](https://github.com/0xPlaygrounds/subgrounds)

Toggle site navigation sidebar

_ _

[ Playgrounds  ](../../../../../)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

_ _

[ ![Light Logo](../../../../../_static/assets/pg-logotype-dark.svg) ![Dark
Logo](../../../../../_static/assets/pg-logotype-primary.svg)
](https://playgrounds.network)

Playgrounds API

  * [ Overview ](../../../../../api/)
  * [ Getting an API Key ](../../../../../api/key/)
  * [ Subgraph Proxy ](../../../../../api/subgraph-proxy/)
  * [ Subgrounds Integration ](../../../../../api/subgrounds/)
  * [ FAQ ](../../../../../api/faq/)

Toggle child pages in navigation

_ _

    * [ What is a Query? ](../../../../../api/faq/query/)
  * [ API Reference ](../../../../../api/api-reference/)

Toggle child pages in navigation

_ _

    * [ Subgraph Proxy ](../../../../../api/reference/proxy/)

Toggle child pages in navigation

_ _

      * [ Subgraph ID ](../../../../../api/reference/proxy/subgraph_id/)
      * [ Deployment ID ](../../../../../api/reference/proxy/deployment_id/)

Subgrounds

  * [ Overview ](../../../../)
  * [ Getting Started ](../../../../getting_started/)

Toggle child pages in navigation

_ _

    * [ The Basics ](../../../../getting_started/basics/)
    * [ Field Paths ](../../../../getting_started/field_paths/)

Toggle child pages in navigation

_ _

      * [ Arguments ](../../../../getting_started/field_paths/arguments/)
      * [ Filtering ](../../../../getting_started/field_paths/filtering/)
      * [ Sorting ](../../../../getting_started/field_paths/sorting/)
      * [ Merging ](../../../../getting_started/field_paths/merging/)
    * [ Querying ](../../../../getting_started/querying/)

Toggle child pages in navigation

_ _

    * [ Synthetic Fields ](../../../../getting_started/synthetic_fields/)
  * [ Advanced Topics ](../../../../advanced_topics/)

Toggle child pages in navigation

_ _

    * [ Contrib ](../../../../advanced_topics/contrib/)

Toggle child pages in navigation

_ _

      * [ Plotly ](../../../../advanced_topics/contrib/plotly/)
    * [ Pagination ](../../../../advanced_topics/pagination/)

Toggle child pages in navigation

_ _

      * [ Custom Strategies ](../../../../advanced_topics/pagination/custom/)
  * [ FAQ ](../../../../faq/)

Toggle child pages in navigation

_ _

    * [ Exporting to Disk ](../../../../faq/exporting/)
    * [ Getting More Data ](../../../../faq/more_data/)
    * [ Python Setup ](../../../../faq/setup/)

Toggle child pages in navigation

_ _

      * [ Python Versioning ](../../../../faq/setup/version_management/)
  * [ Examples ](../../../../examples/)

Toggle child pages in navigation

_ _

    * [ Exchanges ](../../../../examples/exchanges/)
    * [ Bridges ](../../../../examples/bridges/)
    * [ Liquid Staking ](../../../../examples/liquid_staking/)
    * [ Governance ](../../../../examples/governance/)
    * [ Advanced Research ](../../../../examples/advanced_research/)
    * [ Vaults ](../../../../examples/vaults/)
  * [ Videos ](../../../../videos/)
  * [ Changelog ](../../../../changelog/)
  * [ Contributing ](../../../../contributing/)
  * [ API Reference ](../../../)

Toggle child pages in navigation

_ _

    * [ Top Level APIs ](../../../top_level/)
    * [ Internal ](../../)

Toggle child pages in navigation

_ _

      * [ Client ](../../client/)

Toggle child pages in navigation

_ _

        * [ Base ](../../client/base/)
        * [ Sync ](../../client/sync/)
        * [ Async_ ](../../client/async_/)
      * [ Contrib ](../../contrib/)

Toggle child pages in navigation

_ _

        * [ Plotly ](../../contrib/plotly/)
        * [ Dash ](../../contrib/dash/)
      * [ Pagination ](../)

Toggle child pages in navigation

_ _

        * [ Strategies ](../strategies/)
        * Preprocess 
        * [ Pagination ](../pagination/)
        * [ Utils ](../utils/)
      * [ Transform ](../../transform/)

Toggle child pages in navigation

_ _

        * [ ABCs ](../../transform/abcs/)
        * [ Apply ](../../transform/apply/)
        * [ Defaults ](../../transform/defaults/)
        * [ Transforms ](../../transform/transforms/)
        * [ Utils ](../../transform/utils/)
      * [ Subgraph ](../../subgraph/)

Toggle child pages in navigation

_ _

        * [ Fieldpath ](../../subgraph/fieldpath/)
        * [ Filter ](../../subgraph/filter/)
        * [ Object ](../../subgraph/object/)
        * [ Subgraph ](../../subgraph/subgraph/)
      * [ Errors ](../../errors/)
      * [ Query ](../../query/)
      * [ Schema ](../../schema/)
      * [ Utils ](../../utils/)

Meta

  * [ Improving the Docs ](../../../../../meta/contributing/)

Back to top

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

_ _

#  Preprocess  #

Helper functions and classes used by Subgrounds' own pagination strategies.

_ class  _ subgrounds.pagination.preprocess.  PaginationNode  (  _ node_idx  _
, _ filter_field  _ , _ first_value  _ , _ skip_value  _ , _ filter_value  _ ,
_ filter_value_type  _ , _ key_path  _ , _ inner=<factory> _ )  #

    

Class representing the pagination config for a single GraphQL list field.

node_idx  #

    

Index of PaginationNode, used to label pagination arguments for this node.

Type  :

    

[ int ](https://docs.python.org/3/library/functions.html#int "\(in Python
v3.11\)")

filter_field  #

    

Name of the node's filter field, e.g.: if ` filter_name  ` is ` timestamp_gt
` , then  ` filter_field  ` is ` timestamp  `

Type  :

    

[ str ](https://docs.python.org/3/library/stdtypes.html#str "\(in Python
v3.11\)")

first_value  #

    

Initial value of the ` first  ` argument

Type  :

    

[ int ](https://docs.python.org/3/library/functions.html#int "\(in Python
v3.11\)")

skip_value  #

    

Initial value of the ` skip  ` argument

Type  :

    

[ int ](https://docs.python.org/3/library/functions.html#int "\(in Python
v3.11\)")

filter_value  #

    

Initial value of the filter argument (i.e.: ` where:  {filter:  FILTER_VALUE}
` )

Type  :

    

Any

filter_value_type  #

    

Type of the filter value

Type  :

    

TypeRef.T

key_path  #

    

Location in the list field to which this pagination node refers to in the
initial query

Type  :

    

[ list ](https://docs.python.org/3/library/stdtypes.html#list "\(in Python
v3.11\)") [ [ str ](https://docs.python.org/3/library/stdtypes.html#str "\(in
Python v3.11\)") ]

inner  #

    

Nested pagination nodes (if any).

Type  :

    

[ list ](https://docs.python.org/3/library/stdtypes.html#list "\(in Python
v3.11\)") [  PaginationNode  ]

get_vardefs  (  )  #

    

Returns a list of variable definitions corresponding to this pagination node's
pagination arguments as well as the variable definitions related to any nested
pagination nodes.

Parameters  :

    

**self** (  _PaginationNode_ ) -- The current PaginationNode

Returns  :

    

_description_

Return type  :

    

[ list ](https://docs.python.org/3/library/stdtypes.html#list "\(in Python
v3.11\)") [ [ VariableDefinition
](../../query/#subgrounds.query.VariableDefinition
"subgrounds.query.VariableDefinition") ]

subgrounds.pagination.preprocess.  normalize  (  _ schema  _ , _ document  _ ,
_ pagination_nodes  _ )  #

    

Inject various graphql components to "normalize" the query for pagination.

When we paginate a query, we inject custom filtering based on the order by
values. We also add GraphQL variables so that  PaginationStrategy  only need
to change those

> to perform pagination.

The main process for normalization begins by recursively adjusting  Selection
nodes

    

within the Query tree. We only apply the following steps if the node needs to
be paginated.

> Note, these steps always check the current selection and will merge new
> values
    

and selections onto whats currently there.

  1. Ensure  id  is on the  Selection 

  2. Replace  first  argument value by  $firstX 

  3. Replace  skip  argument value by  $skipX 

  4. With the  orderBy  (default being  id  ), generate where filtering arguments 

>   1. These are used to filter out values when paginating
>
>

  5. Set  where  filtering values (deep union / merge) 

[ Next  Pagination  ](../pagination/) [ Previous  Strategies
](../strategies/)

Made with [ Furo ](https://github.com/pradyunsg/furo)

[ ](https://github.com/0xPlaygrounds/subgrounds) [
](https://discord.gg/v4r4zhBAh2) [ ](https://twitter.com/Playgrounds0x)

On this page

  * Preprocess 
    * ` PaginationNode  `
      * ` PaginationNode.node_idx  `
      * ` PaginationNode.filter_field  `
      * ` PaginationNode.first_value  `
      * ` PaginationNode.skip_value  `
      * ` PaginationNode.filter_value  `
      * ` PaginationNode.filter_value_type  `
      * ` PaginationNode.key_path  `
      * ` PaginationNode.inner  `
      * ` PaginationNode.get_vardefs()  `
    * ` normalize()  `



Contents  Menu  Expand  Light mode  Dark mode  Auto light/dark mode

Hide navigation sidebar

Hide table of contents sidebar

Give us a ⭐️ on [ Github ](https://github.com/0xPlaygrounds/subgrounds)

Toggle site navigation sidebar

_ _

[ Playgrounds  ](../../../../../)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

_ _

[ ![Light Logo](../../../../../_static/assets/pg-logotype-dark.svg) ![Dark
Logo](../../../../../_static/assets/pg-logotype-primary.svg)
](https://playgrounds.network)

Playgrounds API

  * [ Overview ](../../../../../api/)
  * [ Getting an API Key ](../../../../../api/key/)
  * [ Subgraph Proxy ](../../../../../api/subgraph-proxy/)
  * [ Subgrounds Integration ](../../../../../api/subgrounds/)
  * [ FAQ ](../../../../../api/faq/)

Toggle child pages in navigation

_ _

    * [ What is a Query? ](../../../../../api/faq/query/)
  * [ API Reference ](../../../../../api/api-reference/)

Toggle child pages in navigation

_ _

    * [ Subgraph Proxy ](../../../../../api/reference/proxy/)

Toggle child pages in navigation

_ _

      * [ Subgraph ID ](../../../../../api/reference/proxy/subgraph_id/)
      * [ Deployment ID ](../../../../../api/reference/proxy/deployment_id/)

Subgrounds

  * [ Overview ](../../../../)
  * [ Getting Started ](../../../../getting_started/)

Toggle child pages in navigation

_ _

    * [ The Basics ](../../../../getting_started/basics/)
    * [ Field Paths ](../../../../getting_started/field_paths/)

Toggle child pages in navigation

_ _

      * [ Arguments ](../../../../getting_started/field_paths/arguments/)
      * [ Filtering ](../../../../getting_started/field_paths/filtering/)
      * [ Sorting ](../../../../getting_started/field_paths/sorting/)
      * [ Merging ](../../../../getting_started/field_paths/merging/)
    * [ Querying ](../../../../getting_started/querying/)

Toggle child pages in navigation

_ _

    * [ Synthetic Fields ](../../../../getting_started/synthetic_fields/)
  * [ Advanced Topics ](../../../../advanced_topics/)

Toggle child pages in navigation

_ _

    * [ Contrib ](../../../../advanced_topics/contrib/)

Toggle child pages in navigation

_ _

      * [ Plotly ](../../../../advanced_topics/contrib/plotly/)
    * [ Pagination ](../../../../advanced_topics/pagination/)

Toggle child pages in navigation

_ _

      * [ Custom Strategies ](../../../../advanced_topics/pagination/custom/)
  * [ FAQ ](../../../../faq/)

Toggle child pages in navigation

_ _

    * [ Exporting to Disk ](../../../../faq/exporting/)
    * [ Getting More Data ](../../../../faq/more_data/)
    * [ Python Setup ](../../../../faq/setup/)

Toggle child pages in navigation

_ _

      * [ Python Versioning ](../../../../faq/setup/version_management/)
  * [ Examples ](../../../../examples/)

Toggle child pages in navigation

_ _

    * [ Exchanges ](../../../../examples/exchanges/)
    * [ Bridges ](../../../../examples/bridges/)
    * [ Liquid Staking ](../../../../examples/liquid_staking/)
    * [ Governance ](../../../../examples/governance/)
    * [ Advanced Research ](../../../../examples/advanced_research/)
    * [ Vaults ](../../../../examples/vaults/)
  * [ Videos ](../../../../videos/)
  * [ Changelog ](../../../../changelog/)
  * [ Contributing ](../../../../contributing/)
  * [ API Reference ](../../../)

Toggle child pages in navigation

_ _

    * [ Top Level APIs ](../../../top_level/)
    * [ Internal ](../../)

Toggle child pages in navigation

_ _

      * [ Client ](../../client/)

Toggle child pages in navigation

_ _

        * [ Base ](../../client/base/)
        * [ Sync ](../../client/sync/)
        * [ Async_ ](../../client/async_/)
      * [ Contrib ](../../contrib/)

Toggle child pages in navigation

_ _

        * [ Plotly ](../../contrib/plotly/)
        * [ Dash ](../../contrib/dash/)
      * [ Pagination ](../)

Toggle child pages in navigation

_ _

        * [ Strategies ](../strategies/)
        * [ Preprocess ](../preprocess/)
        * Pagination 
        * [ Utils ](../utils/)
      * [ Transform ](../../transform/)

Toggle child pages in navigation

_ _

        * [ ABCs ](../../transform/abcs/)
        * [ Apply ](../../transform/apply/)
        * [ Defaults ](../../transform/defaults/)
        * [ Transforms ](../../transform/transforms/)
        * [ Utils ](../../transform/utils/)
      * [ Subgraph ](../../subgraph/)

Toggle child pages in navigation

_ _

        * [ Fieldpath ](../../subgraph/fieldpath/)
        * [ Filter ](../../subgraph/filter/)
        * [ Object ](../../subgraph/object/)
        * [ Subgraph ](../../subgraph/subgraph/)
      * [ Errors ](../../errors/)
      * [ Query ](../../query/)
      * [ Schema ](../../schema/)
      * [ Utils ](../../utils/)

Meta

  * [ Improving the Docs ](../../../../../meta/contributing/)

Back to top

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

_ _

#  Pagination  #

This module contains the pagination algorithms (both regular and iterative)
that make use of pagination strategies.

_ exception  _ subgrounds.pagination.pagination.  PaginationError  (  _
message  _ , _ strategy  _ )  #

    

_ class  _ subgrounds.pagination.pagination.  PaginationStrategy  (  _ *  args
_ , _ **  kwargs  _ )  #

    

step  (  _ page_data  =  None  _ )  #

    

Returns the new query document and its variables which will be executed to get
the next page of data. If this is the first query made as part of the
pagination strategy, then ` page_data  ` will be ` None  ` .

If pagination should be interupted (e.g.: if enough entities have been
queried), then this method should raise a ` StopPagination  ` exception.

Parameters  :

    

  * **page_data** ( _Optional_ _[_ [ _dict_ ](https://docs.python.org/3/library/stdtypes.html#dict "\(in Python v3.11\)") _[_ [ _str_ ](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.11\)") _,_ _Any_ _]_ _]_ _,_ _optional_ ) -- The previous query's response data. 

  * **(** **i.e.** ( _If this is the first query_ ) -- the first page of data), then it will be None. 

  * **None.** ( _Defaults to_ ) -- 

Returns  :

    

A tuple  (doc, vars)  where  doc  is the query document that will be executed
to fetch the next page of data and  vars  are the variables for that document.

Return type  :

    

Tuple[ [ Document ](../../query/#subgrounds.query.Document
"subgrounds.query.Document") , [ dict
](https://docs.python.org/3/library/stdtypes.html#dict "\(in Python v3.11\)")
[ [ str ](https://docs.python.org/3/library/stdtypes.html#str "\(in Python
v3.11\)") , Any]]

subgrounds.pagination.pagination.  paginate  (  _ schema  _ , _ doc  _ , _
pagination_strategy  _ , _ headers  _ )  #

    

Executes the request document  doc  based on the GraphQL schema  schema  and
returns the response as a JSON dictionary.

Parameters  :

    

  * **schema** ( [ _SchemaMeta_ ](../../schema/#subgrounds.schema.SchemaMeta "subgrounds.schema.SchemaMeta") ) -- The GraphQL schema on which the request document is based 

  * **doc** ( [ _Document_ ](../../query/#subgrounds.query.Document "subgrounds.query.Document") ) -- The request document 

Returns  :

    

The response data as a JSON dictionary

Return type  :

    

[ dict ](https://docs.python.org/3/library/stdtypes.html#dict "\(in Python
v3.11\)") [ [ str ](https://docs.python.org/3/library/stdtypes.html#str "\(in
Python v3.11\)") , Any]

subgrounds.pagination.pagination.  paginate_iter  (  _ schema  _ , _ doc  _ ,
_ pagination_strategy  _ , _ headers  _ )  #

    

Executes the request document  doc  based on the GraphQL schema  schema  and
returns the response as a JSON dictionary.

Parameters  :

    

  * **schema** ( [ _SchemaMeta_ ](../../schema/#subgrounds.schema.SchemaMeta "subgrounds.schema.SchemaMeta") ) -- The GraphQL schema on which the request document is based 

  * **doc** ( [ _Document_ ](../../query/#subgrounds.query.Document "subgrounds.query.Document") ) -- The request document 

Returns  :

    

The response data as a JSON dictionary

Return type  :

    

[ dict ](https://docs.python.org/3/library/stdtypes.html#dict "\(in Python
v3.11\)") [ [ str ](https://docs.python.org/3/library/stdtypes.html#str "\(in
Python v3.11\)") , Any]

[ Next  Utils  ](../utils/) [ Previous  Preprocess  ](../preprocess/)

Made with [ Furo ](https://github.com/pradyunsg/furo)

[ ](https://github.com/0xPlaygrounds/subgrounds) [
](https://discord.gg/v4r4zhBAh2) [ ](https://twitter.com/Playgrounds0x)

On this page

  * Pagination 
    * ` PaginationError  `
    * ` PaginationStrategy  `
      * ` PaginationStrategy.step()  `
    * ` paginate()  `
    * ` paginate_iter()  `



Contents  Menu  Expand  Light mode  Dark mode  Auto light/dark mode

Hide navigation sidebar

Hide table of contents sidebar

Give us a ⭐️ on [ Github ](https://github.com/0xPlaygrounds/subgrounds)

Toggle site navigation sidebar

_ _

[ Playgrounds  ](../../../../../)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

_ _

[ ![Light Logo](../../../../../_static/assets/pg-logotype-dark.svg) ![Dark
Logo](../../../../../_static/assets/pg-logotype-primary.svg)
](https://playgrounds.network)

Playgrounds API

  * [ Overview ](../../../../../api/)
  * [ Getting an API Key ](../../../../../api/key/)
  * [ Subgraph Proxy ](../../../../../api/subgraph-proxy/)
  * [ Subgrounds Integration ](../../../../../api/subgrounds/)
  * [ FAQ ](../../../../../api/faq/)

Toggle child pages in navigation

_ _

    * [ What is a Query? ](../../../../../api/faq/query/)
  * [ API Reference ](../../../../../api/api-reference/)

Toggle child pages in navigation

_ _

    * [ Subgraph Proxy ](../../../../../api/reference/proxy/)

Toggle child pages in navigation

_ _

      * [ Subgraph ID ](../../../../../api/reference/proxy/subgraph_id/)
      * [ Deployment ID ](../../../../../api/reference/proxy/deployment_id/)

Subgrounds

  * [ Overview ](../../../../)
  * [ Getting Started ](../../../../getting_started/)

Toggle child pages in navigation

_ _

    * [ The Basics ](../../../../getting_started/basics/)
    * [ Field Paths ](../../../../getting_started/field_paths/)

Toggle child pages in navigation

_ _

      * [ Arguments ](../../../../getting_started/field_paths/arguments/)
      * [ Filtering ](../../../../getting_started/field_paths/filtering/)
      * [ Sorting ](../../../../getting_started/field_paths/sorting/)
      * [ Merging ](../../../../getting_started/field_paths/merging/)
    * [ Querying ](../../../../getting_started/querying/)

Toggle child pages in navigation

_ _

    * [ Synthetic Fields ](../../../../getting_started/synthetic_fields/)
  * [ Advanced Topics ](../../../../advanced_topics/)

Toggle child pages in navigation

_ _

    * [ Contrib ](../../../../advanced_topics/contrib/)

Toggle child pages in navigation

_ _

      * [ Plotly ](../../../../advanced_topics/contrib/plotly/)
    * [ Pagination ](../../../../advanced_topics/pagination/)

Toggle child pages in navigation

_ _

      * [ Custom Strategies ](../../../../advanced_topics/pagination/custom/)
  * [ FAQ ](../../../../faq/)

Toggle child pages in navigation

_ _

    * [ Exporting to Disk ](../../../../faq/exporting/)
    * [ Getting More Data ](../../../../faq/more_data/)
    * [ Python Setup ](../../../../faq/setup/)

Toggle child pages in navigation

_ _

      * [ Python Versioning ](../../../../faq/setup/version_management/)
  * [ Examples ](../../../../examples/)

Toggle child pages in navigation

_ _

    * [ Exchanges ](../../../../examples/exchanges/)
    * [ Bridges ](../../../../examples/bridges/)
    * [ Liquid Staking ](../../../../examples/liquid_staking/)
    * [ Governance ](../../../../examples/governance/)
    * [ Advanced Research ](../../../../examples/advanced_research/)
    * [ Vaults ](../../../../examples/vaults/)
  * [ Videos ](../../../../videos/)
  * [ Changelog ](../../../../changelog/)
  * [ Contributing ](../../../../contributing/)
  * [ API Reference ](../../../)

Toggle child pages in navigation

_ _

    * [ Top Level APIs ](../../../top_level/)
    * [ Internal ](../../)

Toggle child pages in navigation

_ _

      * [ Client ](../../client/)

Toggle child pages in navigation

_ _

        * [ Base ](../../client/base/)
        * [ Sync ](../../client/sync/)
        * [ Async_ ](../../client/async_/)
      * [ Contrib ](../../contrib/)

Toggle child pages in navigation

_ _

        * [ Plotly ](../../contrib/plotly/)
        * [ Dash ](../../contrib/dash/)
      * [ Pagination ](../)

Toggle child pages in navigation

_ _

        * [ Strategies ](../strategies/)
        * [ Preprocess ](../preprocess/)
        * [ Pagination ](../pagination/)
        * Utils 
      * [ Transform ](../../transform/)

Toggle child pages in navigation

_ _

        * [ ABCs ](../../transform/abcs/)
        * [ Apply ](../../transform/apply/)
        * [ Defaults ](../../transform/defaults/)
        * [ Transforms ](../../transform/transforms/)
        * [ Utils ](../../transform/utils/)
      * [ Subgraph ](../../subgraph/)

Toggle child pages in navigation

_ _

        * [ Fieldpath ](../../subgraph/fieldpath/)
        * [ Filter ](../../subgraph/filter/)
        * [ Object ](../../subgraph/object/)
        * [ Subgraph ](../../subgraph/subgraph/)
      * [ Errors ](../../errors/)
      * [ Query ](../../query/)
      * [ Schema ](../../schema/)
      * [ Utils ](../../utils/)

Meta

  * [ Improving the Docs ](../../../../../meta/contributing/)

Back to top

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

_ _

#  Utils  #

subgrounds.pagination.utils.  merge  (  _ data1  _ , _ data2  _ )  #

    

Merges ` data1  ` and ` data2  ` and returns the combined result.

` data1  ` and ` data2  ` must be of the same type. Either both are ` dict  `
, ` list  ` or anything else.

Parameters  :

    

  * **data1** ( [ _list_ ](https://docs.python.org/3/library/stdtypes.html#list "\(in Python v3.11\)") _[_ _Any_ _]_ _|_ [ _dict_ ](https://docs.python.org/3/library/stdtypes.html#dict "\(in Python v3.11\)") _[_ [ _str_ ](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.11\)") _,_ _Any_ _]_ _|_ _Any_ ) -- First data blob 

  * **data2** ( [ _list_ ](https://docs.python.org/3/library/stdtypes.html#list "\(in Python v3.11\)") _[_ _Any_ _]_ _|_ [ _dict_ ](https://docs.python.org/3/library/stdtypes.html#dict "\(in Python v3.11\)") _[_ [ _str_ ](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.11\)") _,_ _Any_ _]_ _|_ _Any_ ) -- Second data blob 

Returns  :

    

Combined data blob

Return type  :

    

[ list ](https://docs.python.org/3/library/stdtypes.html#list "\(in Python
v3.11\)") [Any] | [ dict
](https://docs.python.org/3/library/stdtypes.html#dict "\(in Python v3.11\)")
[ [ str ](https://docs.python.org/3/library/stdtypes.html#str "\(in Python
v3.11\)") , Any] | Any

subgrounds.pagination.utils.  merge_input_value_object_metas  (  _ data1  :
Object  _ , _ data2  :  Object  _ )  →  Object  #

subgrounds.pagination.utils.  merge_input_value_object_metas  (  _ data1  :  [
dict  ](https://docs.python.org/3/library/stdtypes.html#dict "\(in Python
v3.11\)") [  [ str  ](https://docs.python.org/3/library/stdtypes.html#str
"\(in Python v3.11\)") ,  subgrounds.query.InputValue.Object  ]  _ , _ data2
:  [ dict  ](https://docs.python.org/3/library/stdtypes.html#dict "\(in Python
v3.11\)") [  [ str  ](https://docs.python.org/3/library/stdtypes.html#str
"\(in Python v3.11\)") ,  subgrounds.query.InputValue.Object  ]  _ )  →  [
dict  ](https://docs.python.org/3/library/stdtypes.html#dict "\(in Python
v3.11\)") [  [ str  ](https://docs.python.org/3/library/stdtypes.html#str
"\(in Python v3.11\)") ,  subgrounds.query.InputValue.Object  ]

    

Merges ` data1  ` and ` data2  ` and returns the combined result.

` data1  ` and ` data2  ` must be of the same type. Either both are ` dict  `
, ` InputValue.Object  `

[ Next  Transform  ](../../transform/) [ Previous  Pagination
](../pagination/)

Made with [ Furo ](https://github.com/pradyunsg/furo)

[ ](https://github.com/0xPlaygrounds/subgrounds) [
](https://discord.gg/v4r4zhBAh2) [ ](https://twitter.com/Playgrounds0x)

On this page

  * Utils 
    * ` merge()  `
    * ` merge_input_value_object_metas()  `



Contents  Menu  Expand  Light mode  Dark mode  Auto light/dark mode

Hide navigation sidebar

Hide table of contents sidebar

Give us a ⭐️ on [ Github ](https://github.com/0xPlaygrounds/subgrounds)

Toggle site navigation sidebar

_ _

[ Playgrounds  ](../../../../)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

_ _

[ ![Light Logo](../../../../_static/assets/pg-logotype-dark.svg) ![Dark
Logo](../../../../_static/assets/pg-logotype-primary.svg)
](https://playgrounds.network)

Playgrounds API

  * [ Overview ](../../../../api/)
  * [ Getting an API Key ](../../../../api/key/)
  * [ Subgraph Proxy ](../../../../api/subgraph-proxy/)
  * [ Subgrounds Integration ](../../../../api/subgrounds/)
  * [ FAQ ](../../../../api/faq/)

Toggle child pages in navigation

_ _

    * [ What is a Query? ](../../../../api/faq/query/)
  * [ API Reference ](../../../../api/api-reference/)

Toggle child pages in navigation

_ _

    * [ Subgraph Proxy ](../../../../api/reference/proxy/)

Toggle child pages in navigation

_ _

      * [ Subgraph ID ](../../../../api/reference/proxy/subgraph_id/)
      * [ Deployment ID ](../../../../api/reference/proxy/deployment_id/)

Subgrounds

  * [ Overview ](../../../)
  * [ Getting Started ](../../../getting_started/)

Toggle child pages in navigation

_ _

    * [ The Basics ](../../../getting_started/basics/)
    * [ Field Paths ](../../../getting_started/field_paths/)

Toggle child pages in navigation

_ _

      * [ Arguments ](../../../getting_started/field_paths/arguments/)
      * [ Filtering ](../../../getting_started/field_paths/filtering/)
      * [ Sorting ](../../../getting_started/field_paths/sorting/)
      * [ Merging ](../../../getting_started/field_paths/merging/)
    * [ Querying ](../../../getting_started/querying/)

Toggle child pages in navigation

_ _

    * [ Synthetic Fields ](../../../getting_started/synthetic_fields/)
  * [ Advanced Topics ](../../../advanced_topics/)

Toggle child pages in navigation

_ _

    * [ Contrib ](../../../advanced_topics/contrib/)

Toggle child pages in navigation

_ _

      * [ Plotly ](../../../advanced_topics/contrib/plotly/)
    * [ Pagination ](../../../advanced_topics/pagination/)

Toggle child pages in navigation

_ _

      * [ Custom Strategies ](../../../advanced_topics/pagination/custom/)
  * [ FAQ ](../../../faq/)

Toggle child pages in navigation

_ _

    * [ Exporting to Disk ](../../../faq/exporting/)
    * [ Getting More Data ](../../../faq/more_data/)
    * [ Python Setup ](../../../faq/setup/)

Toggle child pages in navigation

_ _

      * [ Python Versioning ](../../../faq/setup/version_management/)
  * [ Examples ](../../../examples/)

Toggle child pages in navigation

_ _

    * [ Exchanges ](../../../examples/exchanges/)
    * [ Bridges ](../../../examples/bridges/)
    * [ Liquid Staking ](../../../examples/liquid_staking/)
    * [ Governance ](../../../examples/governance/)
    * [ Advanced Research ](../../../examples/advanced_research/)
    * [ Vaults ](../../../examples/vaults/)
  * [ Videos ](../../../videos/)
  * [ Changelog ](../../../changelog/)
  * [ Contributing ](../../../contributing/)
  * [ API Reference ](../../)

Toggle child pages in navigation

_ _

    * [ Top Level APIs ](../../top_level/)
    * [ Internal ](../)

Toggle child pages in navigation

_ _

      * [ Client ](../client/)

Toggle child pages in navigation

_ _

        * [ Base ](../client/base/)
        * [ Sync ](../client/sync/)
        * [ Async_ ](../client/async_/)
      * [ Contrib ](../contrib/)

Toggle child pages in navigation

_ _

        * [ Plotly ](../contrib/plotly/)
        * [ Dash ](../contrib/dash/)
      * [ Pagination ](../pagination/)

Toggle child pages in navigation

_ _

        * [ Strategies ](../pagination/strategies/)
        * [ Preprocess ](../pagination/preprocess/)
        * [ Pagination ](../pagination/pagination/)
        * [ Utils ](../pagination/utils/)
      * Transform 

Toggle child pages in navigation

_ _

        * [ ABCs ](abcs/)
        * [ Apply ](apply/)
        * [ Defaults ](defaults/)
        * [ Transforms ](transforms/)
        * [ Utils ](utils/)
      * [ Subgraph ](../subgraph/)

Toggle child pages in navigation

_ _

        * [ Fieldpath ](../subgraph/fieldpath/)
        * [ Filter ](../subgraph/filter/)
        * [ Object ](../subgraph/object/)
        * [ Subgraph ](../subgraph/subgraph/)
      * [ Errors ](../errors/)
      * [ Query ](../query/)
      * [ Schema ](../schema/)
      * [ Utils ](../utils/)

Meta

  * [ Improving the Docs ](../../../../meta/contributing/)

Back to top

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

_ _

#  Transform  #

  * [ ABCs ](abcs/)
  * [ Apply ](apply/)
  * [ Defaults ](defaults/)
  * [ Transforms ](transforms/)
  * [ Utils ](utils/)

Subgrounds request/response transformation layers module

This module defines interfaces (abstract classes) for transformation layers.
Transformation layers, or transforms, can be applied to entire requests (see
` RequestTransform  ` ) or on a per-document basis (see  ` DocumentTransform
` ). Classes that implement either type of transforms can be used to perform
modifications to queries and their response data.

For example, the  ` TypeTransform  ` class is used to tranform the response
data of ` BigInt  ` and ` BigDecimal  ` fields (which are represented as
strings in the response JSON data) to python ` int  ` and ` float  `
respectively (see the actual transforms in ` DEFAULT_SUBGRAPH_TRANSFORMS  ` ).

Transforms are also used to apply ` SyntheticField  ` to queries and the
response data (see  ` LocalSyntheticField  ` transform class). Each `
SyntheticField  ` defined on a subgraph creates a new transformation layer by
instantiating a new  ` LocalSyntheticField  ` object.

_ class  _ subgrounds.transform.  RequestTransform  #

    

Abstract class representing a transformation layer to be applied to entire `
DataRequest  ` objects.

_ abstract  _ transform_request  (  _ req  _ )  #

    

Method that will be applied to all ` DataRequest  ` objects that pass through
the transformation layer.

Parameters  :

    

**req** ( [ _DataRequest_ ](../query/#subgrounds.query.DataRequest
"subgrounds.query.DataRequest") ) -- The initial request object

Returns  :

    

The transformed request object

Return type  :

    

[ DataRequest ](../query/#subgrounds.query.DataRequest
"subgrounds.query.DataRequest")

_ abstract  _ transform_response  (  _ req  _ , _ data  _ )  #

    

Method to be applied to all response data ` data  ` of requests that pass
through the transformation layer.

` req  ` is the initial ` DataRequest  ` object that yielded the resulting
JSON data ` data  ` .

Parameters  :

    

  * **req** ( [ _DataRequest_ ](../query/#subgrounds.query.DataRequest "subgrounds.query.DataRequest") ) -- Initial data request object 

  * **data** ( [ _list_ ](https://docs.python.org/3/library/stdtypes.html#list "\(in Python v3.11\)") _[_ [ _dict_ ](https://docs.python.org/3/library/stdtypes.html#dict "\(in Python v3.11\)") _[_ [ _str_ ](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.11\)") _,_ _Any_ _]_ _]_ ) -- JSON data blob resulting from the execution of the transformed data request. 

Returns  :

    

The transformed response data

Return type  :

    

[ list ](https://docs.python.org/3/library/stdtypes.html#list "\(in Python
v3.11\)") [ [ dict ](https://docs.python.org/3/library/stdtypes.html#dict
"\(in Python v3.11\)") [ [ str
](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.11\)") ,
Any]]

_ class  _ subgrounds.transform.  DocumentTransform  #

    

Abstract class representing a transformation layer to be applied to ` Document
` objects.

_ abstract  _ transform_document  (  _ doc  _ )  #

    

Method that will be applied to all ` Document  ` objects that pass through the
transformation layer.

Parameters  :

    

**doc** ( [ _Document_ ](../query/#subgrounds.query.Document
"subgrounds.query.Document") ) -- The initial document

Returns  :

    

The transformed document

Return type  :

    

[ Document ](../query/#subgrounds.query.Document "subgrounds.query.Document")

_ abstract  _ transform_response  (  _ req  _ , _ data  _ )  #

    

Method to be applied to all response data ` data  ` of requests that pass
through the transformation layer.

` doc  ` is the initial ` Document  ` object that yielded the resulting JSON
data ` data  ` .

Parameters  :

    

  * **doc** ( [ _Document_ ](../query/#subgrounds.query.Document "subgrounds.query.Document") ) -- Initial document 

  * **data** ( [ _dict_ ](https://docs.python.org/3/library/stdtypes.html#dict "\(in Python v3.11\)") _[_ [ _str_ ](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.11\)") _,_ _Any_ _]_ ) -- JSON data blob resulting from the execution of the transformed document. 

Returns  :

    

The transformed response data

Return type  :

    

[ dict ](https://docs.python.org/3/library/stdtypes.html#dict "\(in Python
v3.11\)") [ [ str ](https://docs.python.org/3/library/stdtypes.html#str "\(in
Python v3.11\)") , Any]

_ class  _ subgrounds.transform.  TypeTransform  (  _ type_  _ , _ f  _ )  #

    

Transform to be applied to scalar fields on a per-type basis.

type_  #

    

Type indicating which scalar values (i.e.: values of that type) should be
transformed using the function ` f  `

Type  :

    

TypeRef.T

f  #

    

Function to be applied to scalar values of type ` type_  ` in the response
data.

Type  :

    

Callable[[Any], Any]

transform_document  (  _ doc  _ )  #

    

Method that will be applied to all ` Document  ` objects that pass through the
transformation layer.

Parameters  :

    

**doc** ( [ _Document_ ](../query/#subgrounds.query.Document
"subgrounds.query.Document") ) -- The initial document

Returns  :

    

The transformed document

Return type  :

    

[ Document ](../query/#subgrounds.query.Document "subgrounds.query.Document")

transform_response  (  _ doc  _ , _ data  _ )  #

    

Method to be applied to all response data ` data  ` of requests that pass
through the transformation layer.

` doc  ` is the initial ` Document  ` object that yielded the resulting JSON
data ` data  ` .

Parameters  :

    

  * **doc** ( [ _Document_ ](../query/#subgrounds.query.Document "subgrounds.query.Document") ) -- Initial document 

  * **data** ( [ _dict_ ](https://docs.python.org/3/library/stdtypes.html#dict "\(in Python v3.11\)") _[_ [ _str_ ](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.11\)") _,_ _Any_ _]_ ) -- JSON data blob resulting from the execution of the transformed document. 

Returns  :

    

The transformed response data

Return type  :

    

[ dict ](https://docs.python.org/3/library/stdtypes.html#dict "\(in Python
v3.11\)") [ [ str ](https://docs.python.org/3/library/stdtypes.html#str "\(in
Python v3.11\)") , Any]

_ class  _ subgrounds.transform.  LocalSyntheticField  (  _ subgraph  _ , _
fmeta  _ , _ type_  _ , _ f  _ , _ default  _ , _ args  _ )  #

    

Transform used to implement synthetic fields on GraphQL objects that only
depend on values accessible from that object.

` transform_document()  ` replaces the field  ` fmeta  ` by the argument
fields selections  ` args  ` if the synthetic field  ` fmeta  ` is present in
the document.

` transform_response()  ` applied  ` f  ` to the fields corresponding to the
argument selections  ` args  ` and places the result in the response.

subgraph  #

    

The subgraph to which the synthetic field's object belongs.

Type  :

    

[ Subgraph ](../../top_level/#subgrounds.Subgraph "subgrounds.Subgraph")

fmeta  #

    

The synthetic field

Type  :

    

TypeMeta.FieldMeta

type_  #

    

The object for which the synthetic field is defined

Type  :

    

TypeMeta.ObjectMeta | TypeMeta.InterfaceMeta

f  #

    

The function to be applied to the argument fields

Type  :

    

Callable

default  #

    

The default value of the synthetic field used in case of exceptions (e.g.:
division by zero)

Type  :

    

Any

args  #

    

The selections of the fields used as arguments to compute the synthetic field

Type  :

    

[ list ](https://docs.python.org/3/library/stdtypes.html#list "\(in Python
v3.11\)") [ [ Selection ](../query/#subgrounds.query.Selection
"subgrounds.query.Selection") ]

transform_document  (  _ doc  _ )  #

    

Method that will be applied to all ` Document  ` objects that pass through the
transformation layer.

Parameters  :

    

**doc** ( [ _Document_ ](../query/#subgrounds.query.Document
"subgrounds.query.Document") ) -- The initial document

Returns  :

    

The transformed document

Return type  :

    

[ Document ](../query/#subgrounds.query.Document "subgrounds.query.Document")

transform_response  (  _ doc  _ , _ data  _ )  #

    

Method to be applied to all response data ` data  ` of requests that pass
through the transformation layer.

` doc  ` is the initial ` Document  ` object that yielded the resulting JSON
data ` data  ` .

Parameters  :

    

  * **doc** ( [ _Document_ ](../query/#subgrounds.query.Document "subgrounds.query.Document") ) -- Initial document 

  * **data** ( [ _dict_ ](https://docs.python.org/3/library/stdtypes.html#dict "\(in Python v3.11\)") _[_ [ _str_ ](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.11\)") _,_ _Any_ _]_ ) -- JSON data blob resulting from the execution of the transformed document. 

Returns  :

    

The transformed response data

Return type  :

    

[ dict ](https://docs.python.org/3/library/stdtypes.html#dict "\(in Python
v3.11\)") [ [ str ](https://docs.python.org/3/library/stdtypes.html#str "\(in
Python v3.11\)") , Any]

_ class  _ subgrounds.transform.  SplitTransform  (  _ query  _ )  #

    

transform_request  (  _ req  _ )  #

    

Method that will be applied to all ` DataRequest  ` objects that pass through
the transformation layer.

Parameters  :

    

**req** ( [ _DataRequest_ ](../query/#subgrounds.query.DataRequest
"subgrounds.query.DataRequest") ) -- The initial request object

Returns  :

    

The transformed request object

Return type  :

    

[ DataRequest ](../query/#subgrounds.query.DataRequest
"subgrounds.query.DataRequest")

transform_response  (  _ req  _ , _ data  _ )  #

    

Method to be applied to all response data ` data  ` of requests that pass
through the transformation layer.

` req  ` is the initial ` DataRequest  ` object that yielded the resulting
JSON data ` data  ` .

Parameters  :

    

  * **req** ( [ _DataRequest_ ](../query/#subgrounds.query.DataRequest "subgrounds.query.DataRequest") ) -- Initial data request object 

  * **data** ( [ _list_ ](https://docs.python.org/3/library/stdtypes.html#list "\(in Python v3.11\)") _[_ [ _dict_ ](https://docs.python.org/3/library/stdtypes.html#dict "\(in Python v3.11\)") _[_ [ _str_ ](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.11\)") _,_ _Any_ _]_ _]_ ) -- JSON data blob resulting from the execution of the transformed data request. 

Returns  :

    

The transformed response data

Return type  :

    

[ list ](https://docs.python.org/3/library/stdtypes.html#list "\(in Python
v3.11\)") [ [ dict ](https://docs.python.org/3/library/stdtypes.html#dict
"\(in Python v3.11\)") [ [ str
](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.11\)") ,
Any]]

[ Next  ABCs  ](abcs/) [ Previous  Utils  ](../pagination/utils/)

Made with [ Furo ](https://github.com/pradyunsg/furo)

[ ](https://github.com/0xPlaygrounds/subgrounds) [
](https://discord.gg/v4r4zhBAh2) [ ](https://twitter.com/Playgrounds0x)

On this page

  * Transform 
    * ` RequestTransform  `
      * ` RequestTransform.transform_request()  `
      * ` RequestTransform.transform_response()  `
    * ` DocumentTransform  `
      * ` DocumentTransform.transform_document()  `
      * ` DocumentTransform.transform_response()  `
    * ` TypeTransform  `
      * ` TypeTransform.type_  `
      * ` TypeTransform.f  `
      * ` TypeTransform.transform_document()  `
      * ` TypeTransform.transform_response()  `
    * ` LocalSyntheticField  `
      * ` LocalSyntheticField.subgraph  `
      * ` LocalSyntheticField.fmeta  `
      * ` LocalSyntheticField.type_  `
      * ` LocalSyntheticField.f  `
      * ` LocalSyntheticField.default  `
      * ` LocalSyntheticField.args  `
      * ` LocalSyntheticField.transform_document()  `
      * ` LocalSyntheticField.transform_response()  `
    * ` SplitTransform  `
      * ` SplitTransform.transform_request()  `
      * ` SplitTransform.transform_response()  `



Contents  Menu  Expand  Light mode  Dark mode  Auto light/dark mode

Hide navigation sidebar

Hide table of contents sidebar

Give us a ⭐️ on [ Github ](https://github.com/0xPlaygrounds/subgrounds)

Toggle site navigation sidebar

_ _

[ Playgrounds  ](../../../../)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

_ _

[ ![Light Logo](../../../../_static/assets/pg-logotype-dark.svg) ![Dark
Logo](../../../../_static/assets/pg-logotype-primary.svg)
](https://playgrounds.network)

Playgrounds API

  * [ Overview ](../../../../api/)
  * [ Getting an API Key ](../../../../api/key/)
  * [ Subgraph Proxy ](../../../../api/subgraph-proxy/)
  * [ Subgrounds Integration ](../../../../api/subgrounds/)
  * [ FAQ ](../../../../api/faq/)

Toggle child pages in navigation

_ _

    * [ What is a Query? ](../../../../api/faq/query/)
  * [ API Reference ](../../../../api/api-reference/)

Toggle child pages in navigation

_ _

    * [ Subgraph Proxy ](../../../../api/reference/proxy/)

Toggle child pages in navigation

_ _

      * [ Subgraph ID ](../../../../api/reference/proxy/subgraph_id/)
      * [ Deployment ID ](../../../../api/reference/proxy/deployment_id/)

Subgrounds

  * [ Overview ](../../../)
  * [ Getting Started ](../../../getting_started/)

Toggle child pages in navigation

_ _

    * [ The Basics ](../../../getting_started/basics/)
    * [ Field Paths ](../../../getting_started/field_paths/)

Toggle child pages in navigation

_ _

      * [ Arguments ](../../../getting_started/field_paths/arguments/)
      * [ Filtering ](../../../getting_started/field_paths/filtering/)
      * [ Sorting ](../../../getting_started/field_paths/sorting/)
      * [ Merging ](../../../getting_started/field_paths/merging/)
    * [ Querying ](../../../getting_started/querying/)

Toggle child pages in navigation

_ _

    * [ Synthetic Fields ](../../../getting_started/synthetic_fields/)
  * [ Advanced Topics ](../../../advanced_topics/)

Toggle child pages in navigation

_ _

    * [ Contrib ](../../../advanced_topics/contrib/)

Toggle child pages in navigation

_ _

      * [ Plotly ](../../../advanced_topics/contrib/plotly/)
    * [ Pagination ](../../../advanced_topics/pagination/)

Toggle child pages in navigation

_ _

      * [ Custom Strategies ](../../../advanced_topics/pagination/custom/)
  * [ FAQ ](../../../faq/)

Toggle child pages in navigation

_ _

    * [ Exporting to Disk ](../../../faq/exporting/)
    * [ Getting More Data ](../../../faq/more_data/)
    * [ Python Setup ](../../../faq/setup/)

Toggle child pages in navigation

_ _

      * [ Python Versioning ](../../../faq/setup/version_management/)
  * [ Examples ](../../../examples/)

Toggle child pages in navigation

_ _

    * [ Exchanges ](../../../examples/exchanges/)
    * [ Bridges ](../../../examples/bridges/)
    * [ Liquid Staking ](../../../examples/liquid_staking/)
    * [ Governance ](../../../examples/governance/)
    * [ Advanced Research ](../../../examples/advanced_research/)
    * [ Vaults ](../../../examples/vaults/)
  * [ Videos ](../../../videos/)
  * [ Changelog ](../../../changelog/)
  * [ Contributing ](../../../contributing/)
  * [ API Reference ](../../)

Toggle child pages in navigation

_ _

    * [ Top Level APIs ](../../top_level/)
    * [ Internal ](../)

Toggle child pages in navigation

_ _

      * [ Client ](../client/)

Toggle child pages in navigation

_ _

        * [ Base ](../client/base/)
        * [ Sync ](../client/sync/)
        * [ Async_ ](../client/async_/)
      * [ Contrib ](../contrib/)

Toggle child pages in navigation

_ _

        * [ Plotly ](../contrib/plotly/)
        * [ Dash ](../contrib/dash/)
      * [ Pagination ](../pagination/)

Toggle child pages in navigation

_ _

        * [ Strategies ](../pagination/strategies/)
        * [ Preprocess ](../pagination/preprocess/)
        * [ Pagination ](../pagination/pagination/)
        * [ Utils ](../pagination/utils/)
      * [ Transform ](../transform/)

Toggle child pages in navigation

_ _

        * [ ABCs ](../transform/abcs/)
        * [ Apply ](../transform/apply/)
        * [ Defaults ](../transform/defaults/)
        * [ Transforms ](../transform/transforms/)
        * [ Utils ](../transform/utils/)
      * Subgraph 

Toggle child pages in navigation

_ _

        * [ Fieldpath ](fieldpath/)
        * [ Filter ](filter/)
        * [ Object ](object/)
        * [ Subgraph ](subgraph/)
      * [ Errors ](../errors/)
      * [ Query ](../query/)
      * [ Schema ](../schema/)
      * [ Utils ](../utils/)

Meta

  * [ Improving the Docs ](../../../../meta/contributing/)

Back to top

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

_ _

#  Subgraph  #

  * [ Fieldpath ](fieldpath/)
    * [ ` fieldpaths_of_object()  ` ](fieldpath/#subgrounds.subgraph.fieldpath.fieldpaths_of_object)
    * [ ` FieldPath  ` ](fieldpath/#subgrounds.subgraph.fieldpath.FieldPath)
      * [ ` FieldPath._root  ` ](fieldpath/#subgrounds.subgraph.fieldpath.FieldPath._root)
      * [ ` FieldPath._leaf  ` ](fieldpath/#subgrounds.subgraph.fieldpath.FieldPath._leaf)
      * [ ` FieldPath._merge()  ` ](fieldpath/#subgrounds.subgraph.fieldpath.FieldPath._merge)
      * [ ` FieldPath._name_path()  ` ](fieldpath/#subgrounds.subgraph.fieldpath.FieldPath._name_path)
      * [ ` FieldPath._name()  ` ](fieldpath/#subgrounds.subgraph.fieldpath.FieldPath._name)
      * [ ` FieldPath._extract_data()  ` ](fieldpath/#subgrounds.subgraph.fieldpath.FieldPath._extract_data)
      * [ ` FieldPath._selection()  ` ](fieldpath/#subgrounds.subgraph.fieldpath.FieldPath._selection)
      * [ ` FieldPath._set_arguments()  ` ](fieldpath/#subgrounds.subgraph.fieldpath.FieldPath._set_arguments)
      * [ ` FieldPath._select()  ` ](fieldpath/#subgrounds.subgraph.fieldpath.FieldPath._select)
      * [ ` FieldPath._extend()  ` ](fieldpath/#subgrounds.subgraph.fieldpath.FieldPath._extend)
    * [ ` SyntheticField  ` ](fieldpath/#subgrounds.subgraph.fieldpath.SyntheticField)
      * [ ` SyntheticField.constant()  ` ](fieldpath/#subgrounds.subgraph.fieldpath.SyntheticField.constant)
      * [ ` SyntheticField.datetime_of_timestamp()  ` ](fieldpath/#subgrounds.subgraph.fieldpath.SyntheticField.datetime_of_timestamp)
      * [ ` SyntheticField.map()  ` ](fieldpath/#subgrounds.subgraph.fieldpath.SyntheticField.map)
  * [ Filter ](filter/)
    * [ ` Filter  ` ](filter/#subgrounds.subgraph.filter.Filter)
      * [ ` Filter.Operator  ` ](filter/#subgrounds.subgraph.filter.Filter.Operator)
  * [ Object ](object/)
    * [ ` Object  ` ](object/#subgrounds.subgraph.object.Object)
      * [ ` Object._select()  ` ](object/#subgrounds.subgraph.object.Object._select)
  * [ Subgraph ](subgraph/)
    * [ ` Subgraph  ` ](subgraph/#subgrounds.subgraph.subgraph.Subgraph)

_ class  _ subgrounds.subgraph.  FieldPath  (  _ subgraph  :  'Subgraph'  _ ,
_ root_type  :  'TypeRef.T'  _ , _ type_  :  'TypeRef.T'  _ , _ path  :
'list[Tuple[Optional[dict[str,  Any]],  TypeMeta.FieldMeta]]'  _ )  #

    

_ class  _ subgrounds.subgraph.  Filter  (  _ field  :  'TypeMeta.FieldMeta'
_ , _ op  :  'Filter.Operator'  _ , _ value  :  'Any'  _ )  #

    

_ class  _ Operator  (  _ value  _ )  #

    

An enumeration.

_ class  _ subgrounds.subgraph.  Object  (  _ subgraph  :  'Subgraph'  _ , _
object  :  'TypeMeta.ObjectMeta  |  TypeMeta.InterfaceMeta'  _ )  #

    

_ class  _ subgrounds.subgraph.  Subgraph  (  _ url:  'str',  schema:
'SchemaMeta',  transforms:  'list[DocumentTransform]'  =
[<subgrounds.transform.TypeTransform  object  at  0x7fba98ae0580>,
<subgrounds.transform.TypeTransform  object  at  0x7fba98ae0640>],
is_subgraph:  'bool'  =  True  _ )  #

    

_ class  _ subgrounds.subgraph.  SyntheticField  (  _ f  :  'Callable'  _ , _
type_  :  'TypeRef.T'  _ , _ deps  :  'list[FieldPath  |  SyntheticField]  |
FieldPath  |  SyntheticField'  _ , _ default  :  'Any'  =  None  _ )  #

    

_ static  _ constant  (  _ value  _ )  #

    

Returns a constant ` SyntheticField  ` with value ` value  ` . Useful for
injecting additional static data to a schema or merging entities.

Parameters  :

    

**value** ( [ _str_ ](https://docs.python.org/3/library/stdtypes.html#str
"\(in Python v3.11\)") _|_ [ _int_
](https://docs.python.org/3/library/functions.html#int "\(in Python v3.11\)")
_|_ [ _float_ ](https://docs.python.org/3/library/functions.html#float "\(in
Python v3.11\)") _|_ [ _bool_
](https://docs.python.org/3/library/functions.html#bool "\(in Python v3.11\)")
) -- The constant field's value

Returns  :

    

The constant ` SyntheticField  `

Return type  :

    

SyntheticField

Example:

    
    
    >>> from subgrounds.subgrounds import Subgrounds
    >>> from subgrounds.subgraph import SyntheticField
    >>> sg = Subgrounds()
    >>> univ3 = sg.load_subgraph(
    ...     'https://api.thegraph.com/subgraphs/name/uniswap/uniswap-v3'
    ... )
    
    # Create constant SyntheticFields
    >>> univ3.Mint.tx_type = SyntheticField.constant('MINT')
    >>> univ3.Burn.tx_type = SyntheticField.constant('BURN')
    
    # Last 10 mints and burns
    >>> mints = univ3.Query.mints(
    ...     first=10,
    ...     orderBy=univ3.Mint.timestamp,
    ...     orderDirection='desc'
    ... )
    >>> burns = univ3.Query.burns(
    ...     first=10,
    ...     orderBy=univ3.Burn.timestamp,
    ...     orderDirection='desc'
    ... )
    
    # Query mints and burns. Notice that we merge the two entity tables by
    # setting `concat=True` and overwriting the column names (columns must
    # match the `FieldPaths`)
    >>> df = sg.query_df([
    ...     mints.transaction.id,
    ...     mints.timestamp,
    ...     mints.tx_type,
    ...     mints.origin,
    ...     mints.amountUSD,
    ...     burns.transaction.id,
    ...     burns.timestamp,
    ...     burns.tx_type,
    ...     burns.origin,
    ...     burns.amountUSD,
    ... ], columns=['tx_hash', 'timestamp', 'tx_type', 'origin', 'amount_USD'], concat=True)
    
    # Sort the DataFrame
    >>> df.sort_values(by=['timestamp'], ascending=False)
                                                  tx_hash   timestamp tx_type                                      origin    amount_USD
    0   0xcbe1bacacc1e64fe613ae5eef2063563bd0057d1e3df...  1656016553    MINT  0x3435e7946d40b1a83c0cf154326fc6b3ca908952  7.879784e+03
    1   0xdddaaddf59e5a3abff4feadef83b3ceb023a74424ea7...  1656016284    MINT  0xc747962e7e416e2a582813b1d7ad59eb83077fa6  5.110840e+04
    10  0xa7671452c34a3b083083ef81e364489c2c9ee801a3b8...  1656016284    BURN  0xd40db77990bbb30514276b5ac17c3ce5cc9c951f  2.804573e+05
    2   0xc132e73975e77c2c2c91fcf332018dfb01aac0ca9471...  1656015853    MINT  0xc747962e7e416e2a582813b1d7ad59eb83077fa6  5.122569e+04
    3   0x1444744f4021a2046787c1b7b88cd9ac21f071c65acc...  1656015773    MINT  0xd11aa2e3a000275ed12b87515c9ac0d67b32e7b9  8.897983e+03
    4   0x3315617d426fc2b0db5d8dbccd549efaa8f1ae2969ca...  1656015693    MINT  0xb7dd4d134b1794ee848e1af1a62b85d7b2ea9301  0.000000e+00
    11  0xcc713daa2dc58cd1f2218c8f438e7fcf04d2e9c7c83d...  1656015278    BURN  0xa7c43e2057d89b6946b8865efc8bee3a4ea7d28d  1.254942e+06
    5   0x7bbfae86f0c3c983651bd0671557cd851fc301317c06...  1656015111    MINT  0xac56cee8ccd00d0c1d72ce3415140874552e80f4  3.432075e+04
    12  0xea21c3a68a8f0c6a2721a3072e0c8b2edc77f4d2f0d9...  1656014785    BURN  0x0709b103d46d71458a71e5d81230dd688809a53d  2.059106e+04
    6   0x3bd369bf45c55cab40c62db81bb3e0684fd85fe2b662...  1656014120    MINT  0x509984bfc0fb24e2d1377cfec224d3afec4c341e  2.517578e+03
    13  0x1ea59da77c442479af8fb51501a931260d473e249de7...  1656014018    BURN  0x509984bfc0fb24e2d1377cfec224d3afec4c341e  0.000000e+00
    7   0xb9d31ef78b8bf786b422d948dd1fba246710078abff8...  1656013998    MINT  0x22dfec183294d257f80c15d3c9cd47495bdc728c  8.365750e+04
    14  0xc5e3ec84a2860e3c3a055ccdced435a67b4aff4dd3be...  1656013946    BURN  0xac56cee8ccd00d0c1d72ce3415140874552e80f4  3.363809e+04
    8   0x7c736255d9a4ebf4781069a1b2a929ad89100f1af980...  1656013913    MINT  0x4ce6aea89f059915ae5efbf34a2a8adc544ae09e  4.837287e+04
    15  0x95cf56b9eb69aa45048a9b7b3e472df5bc3bfad591cd...  1656013728    BURN  0x4ce6aea89f059915ae5efbf34a2a8adc544ae09e  5.110010e+04
    9   0x76dd2bbf43485c224471dd823c2992178f031f27194b...  1656013599    MINT  0x234a644868c419ce0dcdd9fd539762eba47f3759  5.363896e+03
    16  0x47e595b02fdcb51ff42a5008e53be7ee3bdf8063b580...  1656013580    BURN  0xaf0fdd39e5d92499b0ed9f68693da99c0ec1e92e  0.000000e+00
    17  0xe20ec9702f455d74b3cc1f54fe2f3450604ca5037a72...  1656013455    BURN  0xaf0fdd39e5d92499b0ed9f68693da99c0ec1e92e  0.000000e+00
    18  0xac3e95666be3a45fdfbbfa513a114136ea6ecffb9de2...  1656013237    BURN  0x665d2d2444f2384fb3d96aaa0ea3536b92984dce  2.254100e+05
    19  0x01c3424a48c36104ea388482723347f15c0bc1bb1a80...  1656013034    BURN  0x0084ee6c8893c01e252198b56ec127443dc27464  0.000000e+00
    

_ static  _ datetime_of_timestamp  (  _ timestamp  _ )  #

    

Returns a ` SyntheticField  ` that will transform the ` FieldPath  ` `
timestamp  ` into a human-readable ISO8601 string.

Parameters  :

    

**timestamp** (  _FieldPath_ _|_ _SyntheticField_ ) -- A ` FieldPath  `
representing a Unix timestamp field.

Returns  :

    

An ISO8601 datetime string ` SyntheticField  ` .

Return type  :

    

SyntheticField

Example:

    
    
    >>> from subgrounds.subgrounds import Subgrounds
    >>> from subgrounds.subgraph import SyntheticField
    >>> sg = Subgrounds()
    >>> univ3 = sg.load_subgraph(
    ...     'https://api.thegraph.com/subgraphs/name/uniswap/uniswap-v3'
    ... )
    
    # Create datetime SyntheticField
    >>> univ3.Swap.datetime = SyntheticField.datetime_of_timestamp(univ3.Swap.timestamp)
    
    # Query 100 swaps
    >>> sg.query_df([
    ...     univ3.Query.swaps.timestamp,
    ...     univ3.Query.swaps.datetime,
    ... ])
        swaps_timestamp       swaps_datetime
    0        1625105710  2021-06-30 22:15:10
    1        1629253724  2021-08-17 22:28:44
    2        1647333277  2022-03-15 04:34:37
    3        1630801974  2021-09-04 20:32:54
    4        1653240241  2022-05-22 13:24:01
    ..              ...                  ...
    95       1646128326  2022-03-01 04:52:06
    96       1646128326  2022-03-01 04:52:06
    97       1626416555  2021-07-16 02:22:35
    98       1626416555  2021-07-16 02:22:35
    99       1625837291  2021-07-09 09:28:11
    

_ static  _ map  (  _ dict  _ , _ type_  _ , _ fpath  _ , _ default  =  None
_ )  #

    

Returns a SyntheticField that will map the values of ` fpath  ` using the key
value pairs in ` dict  ` . If a value is not in the dictionary, then ` default
` will be used instead.

Parameters  :

    

  * **dict** ( [ _dict_ ](https://docs.python.org/3/library/stdtypes.html#dict "\(in Python v3.11\)") _[_ _Any_ _,_ _Any_ _]_ ) -- The dictionary containing the key value pairs used to map ` fpath  ` 's values 

  * **type** ( _TypeRef.T_ ) -- The type of the resulting field 

  * **fpath** (  _FieldPath_ _|_ _SyntheticField_ ) -- The FieldPath whose values will be mapped using the dictionary 

  * **default** ( _Optional_ _[_ _Any_ _]_ ) -- Default value used when a value is not in the provided dictionary 

Returns  :

    

A map SyntheticField

Return type  :

    

SyntheticField

Example:

    
    
    >>> from subgrounds.subgrounds import Subgrounds
    >>> from subgrounds.subgraph import SyntheticField
    >>> sg = Subgrounds()
    >>> univ3 = sg.load_subgraph(
    ...     'https://api.thegraph.com/subgraphs/name/uniswap/uniswap-v3'
    ... )
    
    # Hand-crafted mapping of pool addresses to symbol
    >>> pooladdr_symbol_map = {
    ...     '0x5777d92f208679db4b9778590fa3cab3ac9e2168': 'DAI/USDC-001',
    ...     '0x6c6bc977e13df9b0de53b251522280bb72383700': 'DAI/USDC-005',
    ...     '0x8ad599c3a0ff1de082011efddc58f1908eb6e6d8': 'USDC/ETH-030',
    ...     '0x88e6a0c2ddd26feeb64f039a2c41296fcb3f5640': 'USDC/ETH-005',
    ... }
    
    # Create map SyntheticField using our dictionary with 'UNKNOWN' as the
    # default value
    >>> univ3.Pool.symbol = SyntheticField.map(
    ...     pooladdr_symbol_map,
    ...     SyntheticField.STRING,
    ...     univ3.Pool.id,
    ...     'UNKNOWN'
    ... )
    
    # Query top 10 pools by TVL
    >>> pools = univ3.Query.pools(
    ...     first=10,
    ...     orderBy=univ3.Pool.totalValueLockedUSD,
    ...     orderDirection='desc'
    ... )
    >>> sg.query_df([
    ...     pools.id,
    ...     pools.symbol
    ... ])
                                         pools_id  pools_symbol
    0  0xa850478adaace4c08fc61de44d8cf3b64f359bec       UNKNOWN
    1  0x5777d92f208679db4b9778590fa3cab3ac9e2168  DAI/USDC-001
    2  0x6c6bc977e13df9b0de53b251522280bb72383700  DAI/USDC-005
    3  0x8ad599c3a0ff1de082011efddc58f1908eb6e6d8  USDC/ETH-030
    4  0x88e6a0c2ddd26feeb64f039a2c41296fcb3f5640  USDC/ETH-005
    5  0x3416cf6c708da44db2624d63ea0aaef7113527c6       UNKNOWN
    6  0xcbcdf9626bc03e24f779434178a73a0b4bad62ed       UNKNOWN
    7  0xc63b0708e2f7e69cb8a1df0e1389a98c35a76d52       UNKNOWN
    8  0x4585fe77225b41b697c938b018e2ac67ac5a20c0       UNKNOWN
    9  0x4e68ccd3e89f51c3074ca5072bbac773960dfa36       UNKNOWN
    

[ Next  Fieldpath  ](fieldpath/) [ Previous  Utils  ](../transform/utils/)

Made with [ Furo ](https://github.com/pradyunsg/furo)

[ ](https://github.com/0xPlaygrounds/subgrounds) [
](https://discord.gg/v4r4zhBAh2) [ ](https://twitter.com/Playgrounds0x)

On this page

  * Subgraph 
    * ` FieldPath  `
    * ` Filter  `
      * ` Filter.Operator  `
    * ` Object  `
    * ` Subgraph  `
    * ` SyntheticField  `
      * ` SyntheticField.constant()  `
      * ` SyntheticField.datetime_of_timestamp()  `
      * ` SyntheticField.map()  `



Contents  Menu  Expand  Light mode  Dark mode  Auto light/dark mode

Hide navigation sidebar

Hide table of contents sidebar

Give us a ⭐️ on [ Github ](https://github.com/0xPlaygrounds/subgrounds)

Toggle site navigation sidebar

_ _

[ Playgrounds  ](../../../../../)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

_ _

[ ![Light Logo](../../../../../_static/assets/pg-logotype-dark.svg) ![Dark
Logo](../../../../../_static/assets/pg-logotype-primary.svg)
](https://playgrounds.network)

Playgrounds API

  * [ Overview ](../../../../../api/)
  * [ Getting an API Key ](../../../../../api/key/)
  * [ Subgraph Proxy ](../../../../../api/subgraph-proxy/)
  * [ Subgrounds Integration ](../../../../../api/subgrounds/)
  * [ FAQ ](../../../../../api/faq/)

Toggle child pages in navigation

_ _

    * [ What is a Query? ](../../../../../api/faq/query/)
  * [ API Reference ](../../../../../api/api-reference/)

Toggle child pages in navigation

_ _

    * [ Subgraph Proxy ](../../../../../api/reference/proxy/)

Toggle child pages in navigation

_ _

      * [ Subgraph ID ](../../../../../api/reference/proxy/subgraph_id/)
      * [ Deployment ID ](../../../../../api/reference/proxy/deployment_id/)

Subgrounds

  * [ Overview ](../../../../)
  * [ Getting Started ](../../../../getting_started/)

Toggle child pages in navigation

_ _

    * [ The Basics ](../../../../getting_started/basics/)
    * [ Field Paths ](../../../../getting_started/field_paths/)

Toggle child pages in navigation

_ _

      * [ Arguments ](../../../../getting_started/field_paths/arguments/)
      * [ Filtering ](../../../../getting_started/field_paths/filtering/)
      * [ Sorting ](../../../../getting_started/field_paths/sorting/)
      * [ Merging ](../../../../getting_started/field_paths/merging/)
    * [ Querying ](../../../../getting_started/querying/)

Toggle child pages in navigation

_ _

    * [ Synthetic Fields ](../../../../getting_started/synthetic_fields/)
  * [ Advanced Topics ](../../../../advanced_topics/)

Toggle child pages in navigation

_ _

    * [ Contrib ](../../../../advanced_topics/contrib/)

Toggle child pages in navigation

_ _

      * [ Plotly ](../../../../advanced_topics/contrib/plotly/)
    * [ Pagination ](../../../../advanced_topics/pagination/)

Toggle child pages in navigation

_ _

      * [ Custom Strategies ](../../../../advanced_topics/pagination/custom/)
  * [ FAQ ](../../../../faq/)

Toggle child pages in navigation

_ _

    * [ Exporting to Disk ](../../../../faq/exporting/)
    * [ Getting More Data ](../../../../faq/more_data/)
    * [ Python Setup ](../../../../faq/setup/)

Toggle child pages in navigation

_ _

      * [ Python Versioning ](../../../../faq/setup/version_management/)
  * [ Examples ](../../../../examples/)

Toggle child pages in navigation

_ _

    * [ Exchanges ](../../../../examples/exchanges/)
    * [ Bridges ](../../../../examples/bridges/)
    * [ Liquid Staking ](../../../../examples/liquid_staking/)
    * [ Governance ](../../../../examples/governance/)
    * [ Advanced Research ](../../../../examples/advanced_research/)
    * [ Vaults ](../../../../examples/vaults/)
  * [ Videos ](../../../../videos/)
  * [ Changelog ](../../../../changelog/)
  * [ Contributing ](../../../../contributing/)
  * [ API Reference ](../../../)

Toggle child pages in navigation

_ _

    * [ Top Level APIs ](../../../top_level/)
    * [ Internal ](../../)

Toggle child pages in navigation

_ _

      * [ Client ](../../client/)

Toggle child pages in navigation

_ _

        * [ Base ](../../client/base/)
        * [ Sync ](../../client/sync/)
        * [ Async_ ](../../client/async_/)
      * [ Contrib ](../../contrib/)

Toggle child pages in navigation

_ _

        * [ Plotly ](../../contrib/plotly/)
        * [ Dash ](../../contrib/dash/)
      * [ Pagination ](../../pagination/)

Toggle child pages in navigation

_ _

        * [ Strategies ](../../pagination/strategies/)
        * [ Preprocess ](../../pagination/preprocess/)
        * [ Pagination ](../../pagination/pagination/)
        * [ Utils ](../../pagination/utils/)
      * [ Transform ](../../transform/)

Toggle child pages in navigation

_ _

        * [ ABCs ](../../transform/abcs/)
        * [ Apply ](../../transform/apply/)
        * [ Defaults ](../../transform/defaults/)
        * [ Transforms ](../../transform/transforms/)
        * [ Utils ](../../transform/utils/)
      * [ Subgraph ](../)

Toggle child pages in navigation

_ _

        * Fieldpath 
        * [ Filter ](../filter/)
        * [ Object ](../object/)
        * [ Subgraph ](../subgraph/)
      * [ Errors ](../../errors/)
      * [ Query ](../../query/)
      * [ Schema ](../../schema/)
      * [ Utils ](../../utils/)

Meta

  * [ Improving the Docs ](../../../../../meta/contributing/)

Back to top

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

_ _

#  Fieldpath  #

subgrounds.subgraph.fieldpath.  fieldpaths_of_object  (  _ subgraph  _ , _
object_  _ )  #

    

Returns generator of FieldPath objects that selects all non-list fields of
GraphQL Object of Interface ` object_  ` .

Parameters  :

    

  * **schema** ( [ _SchemaMeta_ ](../../schema/#subgrounds.schema.SchemaMeta "subgrounds.schema.SchemaMeta") ) -- _description_ 

  * **object** ( _TypeMeta.ObjectMeta_ _|_ _TypeMeta.InterfaceMeta_ ) -- _description_ 

Yields  :

    

__type__ \-- _description_

_ class  _ subgrounds.subgraph.fieldpath.  FieldPath  (  _ subgraph  :
'Subgraph'  _ , _ root_type  :  'TypeRef.T'  _ , _ type_  :  'TypeRef.T'  _ ,
_ path  :  'list[Tuple[Optional[dict[str,  Any]],  TypeMeta.FieldMeta]]'  _ )
#

    

_ property  _ _root  _ :  FieldMeta  _ #

    

Returns the type information of the root field of the current  ` FieldPath  `

Returns  :

    

Type information of the root field of the current  ` FieldPath  `

Return type  :

    

TypeMeta.FieldMeta

_ property  _ _leaf  _ :  FieldMeta  _ #

    

Returns the type information of the leaf field of the current  ` FieldPath  `

Returns  :

    

Type information of the leaf field of the current  ` FieldPath  `

Return type  :

    

TypeMeta.FieldMeta

_ static  _ _merge  (  _ fpaths  _ )  #

    

Returns a Selection tree containing all selection paths in  fpaths  . This
function assumes that all fieldpaths in  fpaths  belong to the same subgraph

Parameters  :

    

**fpaths** ( [ _list_ ](https://docs.python.org/3/library/stdtypes.html#list
"\(in Python v3.11\)") _[_ _FieldPath_ _]_ ) -- _description_

Returns  :

    

_description_

Return type  :

    

[ list ](https://docs.python.org/3/library/stdtypes.html#list "\(in Python
v3.11\)") [ [ Selection ](../../query/#subgrounds.query.Selection
"subgrounds.query.Selection") ]

_name_path  (  _ use_aliases  =  False  _ )  #

    

Returns a list of strings correspoding to the names of all fields selected in
the current  ` FieldPath  ` . If ` use_aliases  ` is True, then if a field has
an automatically generated alias, the alias will be returned.

Parameters  :

    

  * **use_aliases** ( [ _bool_ ](https://docs.python.org/3/library/functions.html#bool "\(in Python v3.11\)") _,_ _optional_ ) -- Flag indicating wether of not to use the 

  * **alias** ( _fields' automatically generated_ ) -- 

Returns  :

    

List of field names selected in the current  ` FieldPath  `

Return type  :

    

[ list ](https://docs.python.org/3/library/stdtypes.html#list "\(in Python
v3.11\)") [ [ str ](https://docs.python.org/3/library/stdtypes.html#str "\(in
Python v3.11\)") ]

_name  (  _ use_aliases  =  False  _ )  #

    

Generates the name of the current  ` FieldPath  ` using the names of the
fields it selects. If ` use_aliases  ` is True, then if a field has an
automatically generated alias, the alias will be used.

Parameters  :

    

  * **use_aliases** ( [ _bool_ ](https://docs.python.org/3/library/functions.html#bool "\(in Python v3.11\)") _,_ _optional_ ) -- Flag indicating wether of not to use the 

  * **alias** ( _fields' automatically generated_ ) -- 

Returns  :

    

The generated name of the current  ` FieldPath  ` .

Return type  :

    

[ str ](https://docs.python.org/3/library/stdtypes.html#str "\(in Python
v3.11\)")

_extract_data  (  _ data  _ )  #

    

Extract the data corresponding to the current  ` FieldPath  ` from the
dictionary ` data  ` .

Parameters  :

    

**data** ( [ _dict_ ](https://docs.python.org/3/library/stdtypes.html#dict
"\(in Python v3.11\)") _|_ [ _list_
](https://docs.python.org/3/library/stdtypes.html#list "\(in Python v3.11\)")
_[_ [ _dict_ ](https://docs.python.org/3/library/stdtypes.html#dict "\(in
Python v3.11\)") _]_ ) -- Data dictionary that contains the data

:param corresponding to the current  ` FieldPath  ` .:

Returns  :

    

Data corresponding to the current  ` FieldPath  ` .

Return type  :

    

[ list ](https://docs.python.org/3/library/stdtypes.html#list "\(in Python
v3.11\)") [Any] | Any

_selection  (  )  #

    

Returns a selection or list of selections corresponding to the current  `
FieldPath  ` .

Returns  :

    

_description_

Return type  :

    

[ Selection ](../../query/#subgrounds.query.Selection
"subgrounds.query.Selection") | [ list
](https://docs.python.org/3/library/stdtypes.html#list "\(in Python v3.11\)")
[ [ Selection ](../../query/#subgrounds.query.Selection
"subgrounds.query.Selection") ]

_set_arguments  (  _ args  _ , _ selection  =  []  _ )  #

    

Set the arguments to the leaf of the current  ` FieldPath  ` . The method
returns the ` self  ` .

Parameters  :

    

  * **args** ( [ _dict_ ](https://docs.python.org/3/library/stdtypes.html#dict "\(in Python v3.11\)") _[_ [ _str_ ](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.11\)") _,_ _Any_ _]_ ) -- _description_ 

  * **selection** ( [ _list_ ](https://docs.python.org/3/library/stdtypes.html#list "\(in Python v3.11\)") _[_ _FieldPath_ _]_ _,_ _optional_ ) -- _description_. Defaults to []. 

Returns  :

    

_description_

Return type  :

    

FieldPath

_select  (  _ name  _ )  #

    

Returns a new FieldPath corresponding to the FieldPath  self  extended with an
additional selection on the field named  name  . :param name: The name of the
field to expand on the leaf of  fpath  :type name: str

Raises  :

    

  * [ **TypeError** ](https://docs.python.org/3/library/exceptions.html#TypeError "\(in Python v3.11\)") \-- [description] 

  * [ **TypeError** ](https://docs.python.org/3/library/exceptions.html#TypeError "\(in Python v3.11\)") \-- [description] 

  * [ **TypeError** ](https://docs.python.org/3/library/exceptions.html#TypeError "\(in Python v3.11\)") \-- [description] 

Returns  :

    

A new FieldPath containing  fpath  extended with the field named  name

Return type  :

    

FieldPath

_extend  (  _ ext  _ )  #

    

Extends the current  ` FieldPath  ` with the  ` FieldPath  ` ` ext  ` . ` ext
` must start where the current  ` FieldPath  ` ends.

Parameters  :

    

**ext** (  _FieldPath_ ) -- The  ` FieldPath  ` representing the extension

Raises  :

    

  * [ **TypeError** ](https://docs.python.org/3/library/exceptions.html#TypeError "\(in Python v3.11\)") \-- [description] 

  * [ **TypeError** ](https://docs.python.org/3/library/exceptions.html#TypeError "\(in Python v3.11\)") \-- [description] 

  * [ **TypeError** ](https://docs.python.org/3/library/exceptions.html#TypeError "\(in Python v3.11\)") \-- [description] 

Returns  :

    

A new  ` FieldPath  ` containing the initial current  ` FieldPath  ` extended
with ` ext  `

Return type  :

    

FieldPath

_ class  _ subgrounds.subgraph.fieldpath.  SyntheticField  (  _ f  :
'Callable'  _ , _ type_  :  'TypeRef.T'  _ , _ deps  :  'list[FieldPath  |
SyntheticField]  |  FieldPath  |  SyntheticField'  _ , _ default  :  'Any'  =
None  _ )  #

    

_ static  _ constant  (  _ value  _ )  #

    

Returns a constant ` SyntheticField  ` with value ` value  ` . Useful for
injecting additional static data to a schema or merging entities.

Parameters  :

    

**value** ( [ _str_ ](https://docs.python.org/3/library/stdtypes.html#str
"\(in Python v3.11\)") _|_ [ _int_
](https://docs.python.org/3/library/functions.html#int "\(in Python v3.11\)")
_|_ [ _float_ ](https://docs.python.org/3/library/functions.html#float "\(in
Python v3.11\)") _|_ [ _bool_
](https://docs.python.org/3/library/functions.html#bool "\(in Python v3.11\)")
) -- The constant field's value

Returns  :

    

The constant ` SyntheticField  `

Return type  :

    

SyntheticField

Example:

    
    
    >>> from subgrounds.subgrounds import Subgrounds
    >>> from subgrounds.subgraph import SyntheticField
    >>> sg = Subgrounds()
    >>> univ3 = sg.load_subgraph(
    ...     'https://api.thegraph.com/subgraphs/name/uniswap/uniswap-v3'
    ... )
    
    # Create constant SyntheticFields
    >>> univ3.Mint.tx_type = SyntheticField.constant('MINT')
    >>> univ3.Burn.tx_type = SyntheticField.constant('BURN')
    
    # Last 10 mints and burns
    >>> mints = univ3.Query.mints(
    ...     first=10,
    ...     orderBy=univ3.Mint.timestamp,
    ...     orderDirection='desc'
    ... )
    >>> burns = univ3.Query.burns(
    ...     first=10,
    ...     orderBy=univ3.Burn.timestamp,
    ...     orderDirection='desc'
    ... )
    
    # Query mints and burns. Notice that we merge the two entity tables by
    # setting `concat=True` and overwriting the column names (columns must
    # match the `FieldPaths`)
    >>> df = sg.query_df([
    ...     mints.transaction.id,
    ...     mints.timestamp,
    ...     mints.tx_type,
    ...     mints.origin,
    ...     mints.amountUSD,
    ...     burns.transaction.id,
    ...     burns.timestamp,
    ...     burns.tx_type,
    ...     burns.origin,
    ...     burns.amountUSD,
    ... ], columns=['tx_hash', 'timestamp', 'tx_type', 'origin', 'amount_USD'], concat=True)
    
    # Sort the DataFrame
    >>> df.sort_values(by=['timestamp'], ascending=False)
                                                  tx_hash   timestamp tx_type                                      origin    amount_USD
    0   0xcbe1bacacc1e64fe613ae5eef2063563bd0057d1e3df...  1656016553    MINT  0x3435e7946d40b1a83c0cf154326fc6b3ca908952  7.879784e+03
    1   0xdddaaddf59e5a3abff4feadef83b3ceb023a74424ea7...  1656016284    MINT  0xc747962e7e416e2a582813b1d7ad59eb83077fa6  5.110840e+04
    10  0xa7671452c34a3b083083ef81e364489c2c9ee801a3b8...  1656016284    BURN  0xd40db77990bbb30514276b5ac17c3ce5cc9c951f  2.804573e+05
    2   0xc132e73975e77c2c2c91fcf332018dfb01aac0ca9471...  1656015853    MINT  0xc747962e7e416e2a582813b1d7ad59eb83077fa6  5.122569e+04
    3   0x1444744f4021a2046787c1b7b88cd9ac21f071c65acc...  1656015773    MINT  0xd11aa2e3a000275ed12b87515c9ac0d67b32e7b9  8.897983e+03
    4   0x3315617d426fc2b0db5d8dbccd549efaa8f1ae2969ca...  1656015693    MINT  0xb7dd4d134b1794ee848e1af1a62b85d7b2ea9301  0.000000e+00
    11  0xcc713daa2dc58cd1f2218c8f438e7fcf04d2e9c7c83d...  1656015278    BURN  0xa7c43e2057d89b6946b8865efc8bee3a4ea7d28d  1.254942e+06
    5   0x7bbfae86f0c3c983651bd0671557cd851fc301317c06...  1656015111    MINT  0xac56cee8ccd00d0c1d72ce3415140874552e80f4  3.432075e+04
    12  0xea21c3a68a8f0c6a2721a3072e0c8b2edc77f4d2f0d9...  1656014785    BURN  0x0709b103d46d71458a71e5d81230dd688809a53d  2.059106e+04
    6   0x3bd369bf45c55cab40c62db81bb3e0684fd85fe2b662...  1656014120    MINT  0x509984bfc0fb24e2d1377cfec224d3afec4c341e  2.517578e+03
    13  0x1ea59da77c442479af8fb51501a931260d473e249de7...  1656014018    BURN  0x509984bfc0fb24e2d1377cfec224d3afec4c341e  0.000000e+00
    7   0xb9d31ef78b8bf786b422d948dd1fba246710078abff8...  1656013998    MINT  0x22dfec183294d257f80c15d3c9cd47495bdc728c  8.365750e+04
    14  0xc5e3ec84a2860e3c3a055ccdced435a67b4aff4dd3be...  1656013946    BURN  0xac56cee8ccd00d0c1d72ce3415140874552e80f4  3.363809e+04
    8   0x7c736255d9a4ebf4781069a1b2a929ad89100f1af980...  1656013913    MINT  0x4ce6aea89f059915ae5efbf34a2a8adc544ae09e  4.837287e+04
    15  0x95cf56b9eb69aa45048a9b7b3e472df5bc3bfad591cd...  1656013728    BURN  0x4ce6aea89f059915ae5efbf34a2a8adc544ae09e  5.110010e+04
    9   0x76dd2bbf43485c224471dd823c2992178f031f27194b...  1656013599    MINT  0x234a644868c419ce0dcdd9fd539762eba47f3759  5.363896e+03
    16  0x47e595b02fdcb51ff42a5008e53be7ee3bdf8063b580...  1656013580    BURN  0xaf0fdd39e5d92499b0ed9f68693da99c0ec1e92e  0.000000e+00
    17  0xe20ec9702f455d74b3cc1f54fe2f3450604ca5037a72...  1656013455    BURN  0xaf0fdd39e5d92499b0ed9f68693da99c0ec1e92e  0.000000e+00
    18  0xac3e95666be3a45fdfbbfa513a114136ea6ecffb9de2...  1656013237    BURN  0x665d2d2444f2384fb3d96aaa0ea3536b92984dce  2.254100e+05
    19  0x01c3424a48c36104ea388482723347f15c0bc1bb1a80...  1656013034    BURN  0x0084ee6c8893c01e252198b56ec127443dc27464  0.000000e+00
    

_ static  _ datetime_of_timestamp  (  _ timestamp  _ )  #

    

Returns a ` SyntheticField  ` that will transform the ` FieldPath  ` `
timestamp  ` into a human-readable ISO8601 string.

Parameters  :

    

**timestamp** (  _FieldPath_ _|_ _SyntheticField_ ) -- A ` FieldPath  `
representing a Unix timestamp field.

Returns  :

    

An ISO8601 datetime string ` SyntheticField  ` .

Return type  :

    

SyntheticField

Example:

    
    
    >>> from subgrounds.subgrounds import Subgrounds
    >>> from subgrounds.subgraph import SyntheticField
    >>> sg = Subgrounds()
    >>> univ3 = sg.load_subgraph(
    ...     'https://api.thegraph.com/subgraphs/name/uniswap/uniswap-v3'
    ... )
    
    # Create datetime SyntheticField
    >>> univ3.Swap.datetime = SyntheticField.datetime_of_timestamp(univ3.Swap.timestamp)
    
    # Query 100 swaps
    >>> sg.query_df([
    ...     univ3.Query.swaps.timestamp,
    ...     univ3.Query.swaps.datetime,
    ... ])
        swaps_timestamp       swaps_datetime
    0        1625105710  2021-06-30 22:15:10
    1        1629253724  2021-08-17 22:28:44
    2        1647333277  2022-03-15 04:34:37
    3        1630801974  2021-09-04 20:32:54
    4        1653240241  2022-05-22 13:24:01
    ..              ...                  ...
    95       1646128326  2022-03-01 04:52:06
    96       1646128326  2022-03-01 04:52:06
    97       1626416555  2021-07-16 02:22:35
    98       1626416555  2021-07-16 02:22:35
    99       1625837291  2021-07-09 09:28:11
    

_ static  _ map  (  _ dict  _ , _ type_  _ , _ fpath  _ , _ default  =  None
_ )  #

    

Returns a SyntheticField that will map the values of ` fpath  ` using the key
value pairs in ` dict  ` . If a value is not in the dictionary, then ` default
` will be used instead.

Parameters  :

    

  * **dict** ( [ _dict_ ](https://docs.python.org/3/library/stdtypes.html#dict "\(in Python v3.11\)") _[_ _Any_ _,_ _Any_ _]_ ) -- The dictionary containing the key value pairs used to map ` fpath  ` 's values 

  * **type** ( _TypeRef.T_ ) -- The type of the resulting field 

  * **fpath** (  _FieldPath_ _|_ _SyntheticField_ ) -- The FieldPath whose values will be mapped using the dictionary 

  * **default** ( _Optional_ _[_ _Any_ _]_ ) -- Default value used when a value is not in the provided dictionary 

Returns  :

    

A map SyntheticField

Return type  :

    

SyntheticField

Example:

    
    
    >>> from subgrounds.subgrounds import Subgrounds
    >>> from subgrounds.subgraph import SyntheticField
    >>> sg = Subgrounds()
    >>> univ3 = sg.load_subgraph(
    ...     'https://api.thegraph.com/subgraphs/name/uniswap/uniswap-v3'
    ... )
    
    # Hand-crafted mapping of pool addresses to symbol
    >>> pooladdr_symbol_map = {
    ...     '0x5777d92f208679db4b9778590fa3cab3ac9e2168': 'DAI/USDC-001',
    ...     '0x6c6bc977e13df9b0de53b251522280bb72383700': 'DAI/USDC-005',
    ...     '0x8ad599c3a0ff1de082011efddc58f1908eb6e6d8': 'USDC/ETH-030',
    ...     '0x88e6a0c2ddd26feeb64f039a2c41296fcb3f5640': 'USDC/ETH-005',
    ... }
    
    # Create map SyntheticField using our dictionary with 'UNKNOWN' as the
    # default value
    >>> univ3.Pool.symbol = SyntheticField.map(
    ...     pooladdr_symbol_map,
    ...     SyntheticField.STRING,
    ...     univ3.Pool.id,
    ...     'UNKNOWN'
    ... )
    
    # Query top 10 pools by TVL
    >>> pools = univ3.Query.pools(
    ...     first=10,
    ...     orderBy=univ3.Pool.totalValueLockedUSD,
    ...     orderDirection='desc'
    ... )
    >>> sg.query_df([
    ...     pools.id,
    ...     pools.symbol
    ... ])
                                         pools_id  pools_symbol
    0  0xa850478adaace4c08fc61de44d8cf3b64f359bec       UNKNOWN
    1  0x5777d92f208679db4b9778590fa3cab3ac9e2168  DAI/USDC-001
    2  0x6c6bc977e13df9b0de53b251522280bb72383700  DAI/USDC-005
    3  0x8ad599c3a0ff1de082011efddc58f1908eb6e6d8  USDC/ETH-030
    4  0x88e6a0c2ddd26feeb64f039a2c41296fcb3f5640  USDC/ETH-005
    5  0x3416cf6c708da44db2624d63ea0aaef7113527c6       UNKNOWN
    6  0xcbcdf9626bc03e24f779434178a73a0b4bad62ed       UNKNOWN
    7  0xc63b0708e2f7e69cb8a1df0e1389a98c35a76d52       UNKNOWN
    8  0x4585fe77225b41b697c938b018e2ac67ac5a20c0       UNKNOWN
    9  0x4e68ccd3e89f51c3074ca5072bbac773960dfa36       UNKNOWN
    

[ Next  Filter  ](../filter/) [ Previous  Subgraph  ](../)

Made with [ Furo ](https://github.com/pradyunsg/furo)

[ ](https://github.com/0xPlaygrounds/subgrounds) [
](https://discord.gg/v4r4zhBAh2) [ ](https://twitter.com/Playgrounds0x)

On this page

  * Fieldpath 
    * ` fieldpaths_of_object()  `
    * ` FieldPath  `
      * ` FieldPath._root  `
      * ` FieldPath._leaf  `
      * ` FieldPath._merge()  `
      * ` FieldPath._name_path()  `
      * ` FieldPath._name()  `
      * ` FieldPath._extract_data()  `
      * ` FieldPath._selection()  `
      * ` FieldPath._set_arguments()  `
      * ` FieldPath._select()  `
      * ` FieldPath._extend()  `
    * ` SyntheticField  `
      * ` SyntheticField.constant()  `
      * ` SyntheticField.datetime_of_timestamp()  `
      * ` SyntheticField.map()  `



Contents  Menu  Expand  Light mode  Dark mode  Auto light/dark mode

Hide navigation sidebar

Hide table of contents sidebar

Give us a ⭐️ on [ Github ](https://github.com/0xPlaygrounds/subgrounds)

Toggle site navigation sidebar

_ _

[ Playgrounds  ](../../../../)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

_ _

[ ![Light Logo](../../../../_static/assets/pg-logotype-dark.svg) ![Dark
Logo](../../../../_static/assets/pg-logotype-primary.svg)
](https://playgrounds.network)

Playgrounds API

  * [ Overview ](../../../../api/)
  * [ Getting an API Key ](../../../../api/key/)
  * [ Subgraph Proxy ](../../../../api/subgraph-proxy/)
  * [ Subgrounds Integration ](../../../../api/subgrounds/)
  * [ FAQ ](../../../../api/faq/)

Toggle child pages in navigation

_ _

    * [ What is a Query? ](../../../../api/faq/query/)
  * [ API Reference ](../../../../api/api-reference/)

Toggle child pages in navigation

_ _

    * [ Subgraph Proxy ](../../../../api/reference/proxy/)

Toggle child pages in navigation

_ _

      * [ Subgraph ID ](../../../../api/reference/proxy/subgraph_id/)
      * [ Deployment ID ](../../../../api/reference/proxy/deployment_id/)

Subgrounds

  * [ Overview ](../../../)
  * [ Getting Started ](../../../getting_started/)

Toggle child pages in navigation

_ _

    * [ The Basics ](../../../getting_started/basics/)
    * [ Field Paths ](../../../getting_started/field_paths/)

Toggle child pages in navigation

_ _

      * [ Arguments ](../../../getting_started/field_paths/arguments/)
      * [ Filtering ](../../../getting_started/field_paths/filtering/)
      * [ Sorting ](../../../getting_started/field_paths/sorting/)
      * [ Merging ](../../../getting_started/field_paths/merging/)
    * [ Querying ](../../../getting_started/querying/)

Toggle child pages in navigation

_ _

    * [ Synthetic Fields ](../../../getting_started/synthetic_fields/)
  * [ Advanced Topics ](../../../advanced_topics/)

Toggle child pages in navigation

_ _

    * [ Contrib ](../../../advanced_topics/contrib/)

Toggle child pages in navigation

_ _

      * [ Plotly ](../../../advanced_topics/contrib/plotly/)
    * [ Pagination ](../../../advanced_topics/pagination/)

Toggle child pages in navigation

_ _

      * [ Custom Strategies ](../../../advanced_topics/pagination/custom/)
  * [ FAQ ](../../../faq/)

Toggle child pages in navigation

_ _

    * [ Exporting to Disk ](../../../faq/exporting/)
    * [ Getting More Data ](../../../faq/more_data/)
    * [ Python Setup ](../../../faq/setup/)

Toggle child pages in navigation

_ _

      * [ Python Versioning ](../../../faq/setup/version_management/)
  * [ Examples ](../../../examples/)

Toggle child pages in navigation

_ _

    * [ Exchanges ](../../../examples/exchanges/)
    * [ Bridges ](../../../examples/bridges/)
    * [ Liquid Staking ](../../../examples/liquid_staking/)
    * [ Governance ](../../../examples/governance/)
    * [ Advanced Research ](../../../examples/advanced_research/)
    * [ Vaults ](../../../examples/vaults/)
  * [ Videos ](../../../videos/)
  * [ Changelog ](../../../changelog/)
  * [ Contributing ](../../../contributing/)
  * [ API Reference ](../../)

Toggle child pages in navigation

_ _

    * [ Top Level APIs ](../../top_level/)
    * [ Internal ](../)

Toggle child pages in navigation

_ _

      * [ Client ](../client/)

Toggle child pages in navigation

_ _

        * [ Base ](../client/base/)
        * [ Sync ](../client/sync/)
        * [ Async_ ](../client/async_/)
      * [ Contrib ](../contrib/)

Toggle child pages in navigation

_ _

        * [ Plotly ](../contrib/plotly/)
        * [ Dash ](../contrib/dash/)
      * [ Pagination ](../pagination/)

Toggle child pages in navigation

_ _

        * [ Strategies ](../pagination/strategies/)
        * [ Preprocess ](../pagination/preprocess/)
        * [ Pagination ](../pagination/pagination/)
        * [ Utils ](../pagination/utils/)
      * [ Transform ](../transform/)

Toggle child pages in navigation

_ _

        * [ ABCs ](../transform/abcs/)
        * [ Apply ](../transform/apply/)
        * [ Defaults ](../transform/defaults/)
        * [ Transforms ](../transform/transforms/)
        * [ Utils ](../transform/utils/)
      * [ Subgraph ](../subgraph/)

Toggle child pages in navigation

_ _

        * [ Fieldpath ](../subgraph/fieldpath/)
        * [ Filter ](../subgraph/filter/)
        * [ Object ](../subgraph/object/)
        * [ Subgraph ](../subgraph/subgraph/)
      * [ Errors ](../errors/)
      * Query 
      * [ Schema ](../schema/)
      * [ Utils ](../utils/)

Meta

  * [ Improving the Docs ](../../../../meta/contributing/)

Back to top

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

_ _

#  Query  #

Caution

This module will be broken into a subpackage in the future. As always,
internal APIs are **not** subject to the semver policy this repo holds.

Query data structure module

This module contains various data structures in the form of dataclasses that
are used to represent GraphQL queries in Subgrounds using an AST-like
approach. To the extent possible, these dataclasses are immutable (i.e.: `
frozen=True  ` ) to enforce a functional programming style and reduce side-
effects.

A typical Subgrounds request will have the following dataclass hierarchy:

    
    
    DataRequest
    └── Document
        └── Query
            ├── VariableDefinition
            │   └── InputValue
            └── Selection
                ├── Argument
                │   └── InputValue
                └── Selection
    

_ class  _ subgrounds.query.  VariableDefinition  (  _ name  _ , _ type_  _ ,
_ default  =  None  _ )  #

    

Representation of a GraphQL variable definition

name  #

    

Name of the argument

Type  :

    

[ str ](https://docs.python.org/3/library/stdtypes.html#str "\(in Python
v3.11\)")

type_  #

    

GraphQL type of the argument

Type  :

    

TypeRef.T

default  #

    

Default value of the variable. Defaults to None.

Type  :

    

InputValue.T, optional

_ property  _ graphql  _ :  [ str
](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.11\)") _
#

    

Returns the GraphQL string representation of the variable definition

Example:

    
    
    >>> vardef = VariableDefinition(
    ...   name='foo',
    ...   type_=TypeRef.NonNull(TypeRef.Named(name="Int", kind="SCALAR")),
    ...   default=InputValue.Int(100)
    ... )
    >>> print(vardef.graphql)
    $foo: Int! = 100
    

Returns  :

    

The GraphQL string representation of the variable definition

Return type  :

    

[ str ](https://docs.python.org/3/library/stdtypes.html#str "\(in Python
v3.11\)")

_ class  _ subgrounds.query.  Argument  (  _ name  :  'str'  _ , _ value  :
'InputValue.T'  _ )  #

    

_ class  _ subgrounds.query.  Selection  (  _ fmeta  _ , _ alias=None  _ , _
arguments=<factory> _ , _ selection=<factory> _ )  #

    

Represents a GraphQL field selection.

fmeta  #

    

The type definition of the field being selected.

Type  :

    

TypeMeta.FieldMeta

alias  #

    

The alias of the field selection. Defaults to None.

Type  :

    

[ str ](https://docs.python.org/3/library/stdtypes.html#str "\(in Python
v3.11\)") , optional

arguments  #

    

The arguments, if any, of the field selection. Defaults to [].

Type  :

    

[ list ](https://docs.python.org/3/library/stdtypes.html#list "\(in Python
v3.11\)") [  Argument  ]

selection  #

    

The inner field selections, if any. Defaults to [].

Type  :

    

[ list ](https://docs.python.org/3/library/stdtypes.html#list "\(in Python
v3.11\)") [  Selection  ]

iter  (  )  #

    

Returns an iterator over all ` Selections  ` of the current selection tree.

iter_args  (  _ recurse  =  True  _ )  #

    

Returns an iterator over all ` Arguments  ` of the current ` Selection  ` .

If ` recurse  ==  True  ` , then the iterator also includes ` Arguments  ` of
inner ` Selections  ` .

filter  (  _ predicate  _ )  #

    

Returns a new ` Selection  ` object containing all attributes of the current `
Selection  ` if ` predicate(self)  ==  True  ` and ` None  ` otherwise. The
function if also applied recursively to inner ` Selections  ` .

Parameters  :

    

**predicate** ( _Callable_ _[_ _[_ _Selection_ _]_ _,_ [ _bool_
](https://docs.python.org/3/library/functions.html#bool "\(in Python v3.11\)")
_]_ ) -- _description_

Returns  :

    

_description_

Return type  :

    

Optional[  Selection  ]

filter_args  (  _ predicate  _ , _ recurse  =  True  _ )  #

    

Returns a new ` Selection  ` object which contains all attributes of the
current ` Selection  ` except for ` Arguments  ` for which ` predicate(arg)
==  True  ` .

If ` recurse  ==  True  ` , then the function is applied recursively to inner
` Selections  `

Parameters  :

    

  * **predicate** ( _Callable_ _[_ _[_ _Argument_ _]_ _,_ [ _bool_ ](https://docs.python.org/3/library/functions.html#bool "\(in Python v3.11\)") _]_ ) -- _description_ 

  * **recurse** ( [ _bool_ ](https://docs.python.org/3/library/functions.html#bool "\(in Python v3.11\)") _,_ _optional_ ) -- _description_. Defaults to True. 

Returns  :

    

_description_

Return type  :

    

Selection

map  (  _ map_f  _ , _ priority  =  'self'  _ )  #

    

Returns a new ` Selection  ` object containing the same selection tree as the
current ` Selection  ` where each ` Selection  ` object ` s  ` is ` map_f(s)
`

Parameters  :

    

**map_f** ( _Callable_ _[_ _[_ _Selection_ _]_ _,_ _Selection_ _]_ ) --
Mapping function to apply to each ` Selection  `

Returns  :

    

_description_

Return type  :

    

Selection

map_args  (  _ map_f  _ , _ recurse  =  True  _ )  #

    

Replaces each ` Argument  ` ` arg  ` in the current ` Selection  ` with `
map_f(arg)  ` and returns a new ` Selection  ` object containinf the modified
arguments.

If ` recurse  ==  True  ` , then the function is applied recursively to inner
` Selections  ` .

Parameters  :

    

  * **map_f** ( _Callable_ _[_ _[_ _Argument_ _]_ _,_ _Argument_ _|_ [ _list_ ](https://docs.python.org/3/library/stdtypes.html#list "\(in Python v3.11\)") _[_ _Argument_ _]_ _]_ ) -- _description_ 

  * **recurse** ( [ _bool_ ](https://docs.python.org/3/library/functions.html#bool "\(in Python v3.11\)") _,_ _optional_ ) -- _description_. Defaults to True. 

Returns  :

    

_description_

Return type  :

    

Selection

contains_list  (  )  #

    

Returns True i.f.f. the selection ` self  ` selects a field of type list.

Parameters  :

    

**self** (  _Selection_ ) -- The selection to traverse

Returns  :

    

True if selection or nested selections selects a list field. False otherwise.

Return type  :

    

[ bool ](https://docs.python.org/3/library/functions.html#bool "\(in Python
v3.11\)")

split  (  )  #

    

Returns a list of selections where each of the selections corresponds to a
single selection path from the root to a leaf for each leaf selected in ` self
` .

Example (simplified, does not show all attributes):

    
    
    >>> select = Selection('foo', inner=[
    ...   Selection('bar', inner=[
    ...     Selection('field0', inner=[]),
    ...     Selection('field1', inner=[]),
    ...   ]),
    ...   Selection('x', inner=[])
    ... ])
    >>> split(select)
    [
      Selection('foo', inner=[Selection('bar', inner=[Selection('field0', inner=[])])]),
      Selection('foo', inner=[Selection('bar', inner=[Selection('field1', inner=[])])]),
      Selection('foo', inner=[Selection('x', inner=[])]),
    ]
    

Parameters  :

    

**self** (  _Selection_ ) -- The selection to split

Returns  :

    

The split selections

Return type  :

    

[ list ](https://docs.python.org/3/library/stdtypes.html#list "\(in Python
v3.11\)") [  Selection  ]

add  (  _ new_selections  _ )  #

    

Returns a new selection consisting of a copy of ` self  ` expanded with the
selection(s) ` new_selections  ` . It is assumed that ` new_selections  ` are
inner selections of the root selection ` self  ` .

Parameters  :

    

  * **self** (  _Selection_ ) -- The Selection object to be expanded 

  * **new_selections** (  _Selection_ _|_ [ _list_ ](https://docs.python.org/3/library/stdtypes.html#list "\(in Python v3.11\)") _[_ _Selection_ _]_ ) -- A single or multiple Selection object(s) to be added to ` self  `

Returns  :

    

The resulting new selection, i.e.: ` self  `

    

expanded with ` new_selections  `

Return type  :

    

Selection

remove  (  _ to_remove  _ )  #

    

Returns a new Selection object consisting of a copy of ` self  ` without the
selections in ` selections_to_remove  ` .

Parameters  :

    

**to_remove** (  _Selection_ _|_ [ _list_
](https://docs.python.org/3/library/stdtypes.html#list "\(in Python v3.11\)")
_[_ _Selection_ _]_ ) -- The selection(s) to remove from ` self  `

Returns  :

    

The new trimmed down selection, i.e.: ` self  ` without

    

` selections_to_remove  `

Return type  :

    

Selection

variable_args  (  _ recurse  =  True  _ )  #

    

Returns all arguments in the current selection which have been given a
variable as value.

If ` recurse  ==  True  ` , then the function is applied recursively to inner
selections.

Parameters  :

    

**recurse** ( [ _bool_ ](https://docs.python.org/3/library/functions.html#bool
"\(in Python v3.11\)") _,_ _optional_ ) -- _description_. Defaults to True.

Returns  :

    

_description_

Return type  :

    

[ list ](https://docs.python.org/3/library/stdtypes.html#list "\(in Python
v3.11\)") [  Argument  ]

_ static  _ merge  (  _ selections  _ )  #

    

Returns a list of Selection objects resulting from merging ` selections  ` to
the extent possible.

Parameters  :

    

**selections** ( [ _list_
](https://docs.python.org/3/library/stdtypes.html#list "\(in Python v3.11\)")
_[_ _Selection_ _]_ ) -- The selections to be merged

Returns  :

    

_description_

Return type  :

    

[ list ](https://docs.python.org/3/library/stdtypes.html#list "\(in Python
v3.11\)") [  Selection  ]

contains  (  _ other  _ )  #

    

Returns True i.f.f. the Selection ` other  ` is a subtree of the Selection `
self  ` and False otherwise

Parameters  :

    

  * **self** (  _Selection_ ) -- The selection 

  * **other** (  _Selection_ ) -- The subselection 

Returns  :

    

True i.f.f. ` other  ` is in ` self  `

Return type  :

    

[ bool ](https://docs.python.org/3/library/functions.html#bool "\(in Python
v3.11\)")

contains_argument  (  _ argname  _ , _ recurse  =  True  _ )  #

    

Returns True i.f.f. there is an Argument object in ` self  ` named ` argname
` . If ` recurse  ` is True, then the method also checks the nested selections
for an argument named ` argname  ` .

Parameters  :

    

  * **self** (  _Selection_ ) -- The selection 

  * **argname** ( [ _str_ ](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.11\)") ) -- The name of the argument 

  * **recurse** ( [ _bool_ ](https://docs.python.org/3/library/functions.html#bool "\(in Python v3.11\)") _,_ _optional_ ) -- Flag indicating whether or not the method should be run recursively on nested selections. Defaults to True. 

Returns  :

    

True i.f.f. there is an argument named ` argname  ` in ` self  `

Return type  :

    

[ bool ](https://docs.python.org/3/library/functions.html#bool "\(in Python
v3.11\)")

get_argument  (  _ argname  _ , _ recurse  =  True  _ )  #

    

Returns an Argument object corresponding to the argument in the Selection
object ` select  ` with name ` argname  ` . If ` select  ` does not contain
such an argument and ` recurse  ` is True, then the function is called
recursively on ` select  ` 's inner selections. If no such argument is found
in ` select  ` or its inner selections, then the function raises an exception.

Parameters  :

    

  * **select** (  _Selection_ ) -- The selection to scan 

  * **argname** ( [ _str_ ](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.11\)") ) -- The name of the argument to find 

  * **recurse** ( [ _bool_ ](https://docs.python.org/3/library/functions.html#bool "\(in Python v3.11\)") _,_ _optional_ ) -- Flag indicating whether or not the method should be run recursively on nested selections. Defaults to True. 

Raises  :

    

[ **KeyError** ](https://docs.python.org/3/library/exceptions.html#KeyError
"\(in Python v3.11\)") \-- If no argument named ` argname  ` exists in the
selection ` self  ` .

Returns  :

    

The argument in ` select  ` with name ` argname  ` (if any).

Return type  :

    

Argument

get_argument_by_variable  (  _ varname  _ , _ recurse  =  True  _ )  #

    

Returns an Argument object corresponding to the argument in the Selection
object ` select  ` whose value is a variable named ` varname  ` . If ` select
` does not contain such an argument and ` recurse  ` is True, then the
function is called recursively on ` select  ` 's inner selections. If no such
argument is found in ` select  ` or its inner selections, then the function
raises an exception

Parameters  :

    

  * **select** (  _Selection_ ) -- The selection to scan 

  * **varname** ( [ _str_ ](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.11\)") ) -- The name of the variable to find 

  * **recurse** ( [ _bool_ ](https://docs.python.org/3/library/functions.html#bool "\(in Python v3.11\)") _,_ _optional_ ) -- Flag indicating whether or not the function should be run recursively. Defaults to True. 

Raises  :

    

[ **KeyError** ](https://docs.python.org/3/library/exceptions.html#KeyError
"\(in Python v3.11\)") \-- If no argument with variable value named ` varname
` exists in the selection ` self  ` .

Returns  :

    

The argument in ` select  ` with variable value named

    

` varname  ` if it exists

Return type  :

    

Argument

substitute_arg  (  _ argname  _ , _ replacement  _ , _ recurse  =  True  _ )
#

    

Returns a new Selection object containing the same data as ` self  ` with the
argument named ` argname  ` replaced with ` replacement  ` . If ` recurse  `
is True, then the method is called recursively on ` self  ` 's inner
selections and the substitution is also applied to the latter.

Parameters  :

    

  * **self** (  _Selection_ ) -- _description_ 

  * **argname** ( [ _str_ ](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.11\)") ) -- The name of the argument to substitute. 

  * **replacement** (  _Argument_ _|_ [ _list_ ](https://docs.python.org/3/library/stdtypes.html#list "\(in Python v3.11\)") _[_ _Argument_ _]_ ) -- The argument(s) replacement 

  * **recurse** ( [ _bool_ ](https://docs.python.org/3/library/functions.html#bool "\(in Python v3.11\)") _,_ _optional_ ) -- Flag indicating whether or not the method should be run recursively. Defaults to True. 

Returns  :

    

_description_

Return type  :

    

Selection

prune_undefined  (  _ variables  _ )  #

    

Return a new ` Selection  ` containing the subtree of the current ` Selection
` where all argument ` InputValues  ` are defined, i.e.: each argument's `
InputValue  ` is either

> 1) not of type ` InputValue.Variable  ` or 2) of type ` InputValue.Variable
> ` and the variable name is contained in ` variables  ` .

Parameters  :

    

**variables** ( _Iterator_ _[_ [ _str_
](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.11\)")
_]_ ) -- An iterator over defined variables

Returns  :

    

A new pruned ` Selection  ` object

Return type  :

    

Selection

_ class  _ subgrounds.query.  Query  (  _ name:  'Optional[str]'  =  None  _ ,
_ selection:  'list[Selection]'  =  <factory> _ , _ variables:
'list[VariableDefinition]'  =  <factory> _ )  #

    

_ property  _ graphql  _ :  [ str
](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.11\)") _
#

    

Returns a string containing a GraphQL query matching the current query

Returns  :

    

The string containing the GraphQL query

Return type  :

    

[ str ](https://docs.python.org/3/library/stdtypes.html#str "\(in Python
v3.11\)")

iter  (  )  #

    

Returns an iterator over all ` Selections  ` of the selection tree of the
current ` Query  ` .

iter_args  (  )  #

    

Returns an iterator over all ` Arguments  ` of the selection tree of the
current ` Query  ` .

iter_vardefs  (  )  #

    

Returns an iterator over all ` VariableDefinitions  ` of the selection tree of
the current ` Query  ` .

filter  (  _ predicate  _ )  #

    

Returns a new ` Query  ` object containing all selections ` s  ` that satisfy
` predicate(s)  ==  True  ` .

Parameters  :

    

**predicate** ( _Callable_ _[_ _[_ _Selection_ _]_ _,_ [ _bool_
](https://docs.python.org/3/library/functions.html#bool "\(in Python v3.11\)")
_]_ ) -- _description_

Returns  :

    

_description_

Return type  :

    

Query

filter_args  (  _ predicate  _ )  #

    

Returns a new ` Query  ` object containing all selections arguments ` arg  `
that satisfy ` predicate(arg)  ==  True  ` .

Parameters  :

    

**predicate** ( _Callable_ _[_ _[_ _Argument_ _]_ _,_ [ _bool_
](https://docs.python.org/3/library/functions.html#bool "\(in Python v3.11\)")
_]_ ) -- _description_

Returns  :

    

_description_

Return type  :

    

Query

map  (  _ map_f  _ , _ priority  =  'self'  _ )  #

    

Applies the function ` map_f  ` to each ` Selection  ` in the current ` Query
` and returns a new ` Query  ` object containing the resulting ` Selections  `
.

Parameters  :

    

**map_f** ( _Callable_ _[_ _[_ _Selection_ _]_ _,_ _Selection_ _]_ ) --
Mapping function to apply to each ` Selection  `

Returns  :

    

_description_

Return type  :

    

Query

map_args  (  _ map_f  _ )  #

    

Applies the function ` map_f  ` to each ` Argument  ` in the current ` Query
` and returns a new ` Query  ` object containing the resulting ` Arguments  `
.

Parameters  :

    

**map_f** ( _Callable_ _[_ _[_ _Argument_ _]_ _,_ _Argument_ _]_ ) --
_description_

Returns  :

    

_description_

Return type  :

    

Selection

add  (  _ other  _ )  #

    

Returns a new Query containing all selections in :attr:'self' along with the
new selections in ` other  `

Parameters  :

    

  * **self** (  _Query_ ) -- The query to which new selection(s) or query are to be added 

  * **other** (  _Query_ _|_ _Selection_ _|_ [ _list_ ](https://docs.python.org/3/library/stdtypes.html#list "\(in Python v3.11\)") _[_ _Selection_ _]_ ) -- The new selection(s) 

  * **query** ( _or query to be added to the_ ) -- 

Returns  :

    

A new  Query  objects containing all selections

Return type  :

    

Query

remove  (  _ other  _ )  #

    

Returns a new  ` Query  ` object containing all selections in ` self  ` minus
the subquery or selection(s) specified in ` other  ` .

Note: ` other  ` does not need to be a "full" selection (i.e.: a selection all
the way to leaves of the GraphQL schema).

Example:

    
    
    >>> og_selection = Selection(TypeMeta.FieldMeta('pair', description="", args=[], type=TypeRef.non_null_list("Pair", kind="OBJECT")), None, [], [
    ...   Selection(TypeMeta.FieldMeta('token0', description="", args=[], type=TypeRef.Named(name="Token", kind="OBJECT")), None, [], [
    ...     Selection(TypeMeta.FieldMeta('id', description="", args=[], type=TypeRef.Named(name="String", kind="SCALAR")), None, [], []),
    ...     Selection(TypeMeta.FieldMeta('name', description="", args=[], type=TypeRef.Named(name="String", kind="SCALAR")), None, [], []),
    ...     Selection(TypeMeta.FieldMeta('symbol', description="", args=[], type=TypeRef.Named(name="String", kind="SCALAR")), None, [], []),
    ...   ])
    ... ])
    >>> selection_to_remove = Selection(TypeMeta.FieldMeta('token0', description="", args=[], type=TypeRef.Named(name="Token", kind="OBJECT")), None, [], [])
    >>> og_selection.remove(selection_to_remove)
    Selection(TypeMeta.FieldMeta('pair', description="", args=[], type=TypeRef.non_null_list("Pair", kind="OBJECT")), None, [], [])
    

Parameters  :

    

  * **query** (  _Query_ ) -- The query to which a selection has to be removed 

  * **other** (  _Query_ _|_ _Selection_ _|_ [ _list_ ](https://docs.python.org/3/library/stdtypes.html#list "\(in Python v3.11\)") _[_ _Selection_ _]_ ) -- The subquery or selection(s) to remove from ` self  `

Returns  :

    

A new  Query  object containing the original query selections

    

minus ` other  `

Return type  :

    

Query

contains_selection  (  _ selection  _ )  #

    

Returns True i.f.f. the selection tree ` selection  ` is present in ` query  `
.

Parameters  :

    

  * **query** (  _Query_ ) -- A query object 

  * **selection** (  _Selection_ ) -- The selection to be found (or not) in ` query  `

Returns  :

    

True if the ` selection  ` is present in ` query  ` , False

    

otherwise.

Return type  :

    

[ bool ](https://docs.python.org/3/library/functions.html#bool "\(in Python
v3.11\)")

_ static  _ contains  (  _ query  _ , _ other  _ )  #

    

Returns True i.f.f. all selections in  other  are contained in  query  . In
other words, returns true i.f.f.  other  is a subset of  query  .

Note:  other  does not need to include "full" selections (i.e.: selections all
the way to leaves of the GraphQL schema).

Parameters  :

    

  * **query** (  _Query_ ) -- The query that is to be checked 

  * **other** (  _Query_ ) -- The query that has to be in  query 

Returns  :

    

True i.f.f. all selections in  other  are contained in  query  , otherwise
False

Return type  :

    

[ bool ](https://docs.python.org/3/library/functions.html#bool "\(in Python
v3.11\)")

_ static  _ select  (  _ query  _ , _ other  _ )  #

    

Returns a new Query

Parameters  :

    

  * **query** (  _Query_ ) -- [description] 

  * **other** (  _Query_ ) -- [description] 

Returns  :

    

[description]

Return type  :

    

Query

_ class  _ subgrounds.query.  Fragment  (  _ name:  'str'  _ , _ type_:
'TypeRef.T'  _ , _ selection:  'list[Selection]'  =  <factory> _ , _
variables:  'list[VariableDefinition]'  =  <factory> _ )  #

    

_ class  _ subgrounds.query.  Document  (  _ url:  'str'  _ , _ query:
'Query'  _ , _ fragments:  'list[Fragment]'  =  <factory> _ , _ variables:
'dict[str  _ , _ Any]'  =  <factory> _ )  #

    

map  (  _ map_f  _ )  #

    

Applies the function ` map_f  ` to each ` Selection  ` in the current `
Document  ` and returns a new ` Document  ` object containing the resulting `
Selections  ` .

Parameters  :

    

**map_f** ( _Callable_ _[_ _[_ _Selection_ _]_ _,_ _Selection_ _]_ ) --
Mapping function to apply to each ` Selection  `

Returns  :

    

_description_

Return type  :

    

Query

map_args  (  _ map_f  _ )  #

    

Applies the function ` map_f  ` to each ` Argument  ` in the current `
Document  ` and returns a new ` Document  ` object containing the resulting `
Arguments  ` .

Parameters  :

    

**map_f** ( _Callable_ _[_ _[_ _Argument_ _]_ _,_ _Argument_ _]_ ) --
_description_

Returns  :

    

_description_

Return type  :

    

Selection

prune_undefined  (  _ variables  _ )  #

    

Returns a new ` Document  ` object that contains the subset of the current `
Document  ` 's query containing only the ` Selections  ` for which all its
arguments are defined (i.e.: either constants or variables in ` variables  `
).

Parameters  :

    

**variables** ( [ _dict_
](https://docs.python.org/3/library/stdtypes.html#dict "\(in Python v3.11\)")
_[_ [ _str_ ](https://docs.python.org/3/library/stdtypes.html#str "\(in Python
v3.11\)") _,_ _Any_ _]_ ) -- _description_

Returns  :

    

_description_

Return type  :

    

Document

_ class  _ subgrounds.query.  DataRequest  (  _ documents:  'list[Document]'
=  <factory> _ )  #

    

subgrounds.query.  selections_of_object  (  _ schema  _ , _ object_  _ )  #

    

Returns generator of Selection objects that selects all non-list fields of
GraphQL Object of Interface ` object_  ` .

Parameters  :

    

  * **schema** ( [ _SchemaMeta_ ](../schema/#subgrounds.schema.SchemaMeta "subgrounds.schema.SchemaMeta") ) -- _description_ 

  * **object** ( _TypeMeta.ObjectMeta_ _|_ _TypeMeta.InterfaceMeta_ ) -- _description_ 

Yields  :

    

__type__ \-- _description_

[ Next  Schema  ](../schema/) [ Previous  Errors  ](../errors/)

Made with [ Furo ](https://github.com/pradyunsg/furo)

[ ](https://github.com/0xPlaygrounds/subgrounds) [
](https://discord.gg/v4r4zhBAh2) [ ](https://twitter.com/Playgrounds0x)

On this page

  * Query 
    * ` VariableDefinition  `
      * ` VariableDefinition.name  `
      * ` VariableDefinition.type_  `
      * ` VariableDefinition.default  `
      * ` VariableDefinition.graphql  `
    * ` Argument  `
    * ` Selection  `
      * ` Selection.fmeta  `
      * ` Selection.alias  `
      * ` Selection.arguments  `
      * ` Selection.selection  `
      * ` Selection.iter()  `
      * ` Selection.iter_args()  `
      * ` Selection.filter()  `
      * ` Selection.filter_args()  `
      * ` Selection.map()  `
      * ` Selection.map_args()  `
      * ` Selection.contains_list()  `
      * ` Selection.split()  `
      * ` Selection.add()  `
      * ` Selection.remove()  `
      * ` Selection.variable_args()  `
      * ` Selection.merge()  `
      * ` Selection.contains()  `
      * ` Selection.contains_argument()  `
      * ` Selection.get_argument()  `
      * ` Selection.get_argument_by_variable()  `
      * ` Selection.substitute_arg()  `
      * ` Selection.prune_undefined()  `
    * ` Query  `
      * ` Query.graphql  `
      * ` Query.iter()  `
      * ` Query.iter_args()  `
      * ` Query.iter_vardefs()  `
      * ` Query.filter()  `
      * ` Query.filter_args()  `
      * ` Query.map()  `
      * ` Query.map_args()  `
      * ` Query.add()  `
      * ` Query.remove()  `
      * ` Query.contains_selection()  `
      * ` Query.contains()  `
      * ` Query.select()  `
    * ` Fragment  `
    * ` Document  `
      * ` Document.map()  `
      * ` Document.map_args()  `
      * ` Document.prune_undefined()  `
    * ` DataRequest  `
    * ` selections_of_object()  `



Contents  Menu  Expand  Light mode  Dark mode  Auto light/dark mode

Hide navigation sidebar

Hide table of contents sidebar

Give us a ⭐️ on [ Github ](https://github.com/0xPlaygrounds/subgrounds)

Toggle site navigation sidebar

_ _

[ Playgrounds  ](../../../../)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

_ _

[ ![Light Logo](../../../../_static/assets/pg-logotype-dark.svg) ![Dark
Logo](../../../../_static/assets/pg-logotype-primary.svg)
](https://playgrounds.network)

Playgrounds API

  * [ Overview ](../../../../api/)
  * [ Getting an API Key ](../../../../api/key/)
  * [ Subgraph Proxy ](../../../../api/subgraph-proxy/)
  * [ Subgrounds Integration ](../../../../api/subgrounds/)
  * [ FAQ ](../../../../api/faq/)

Toggle child pages in navigation

_ _

    * [ What is a Query? ](../../../../api/faq/query/)
  * [ API Reference ](../../../../api/api-reference/)

Toggle child pages in navigation

_ _

    * [ Subgraph Proxy ](../../../../api/reference/proxy/)

Toggle child pages in navigation

_ _

      * [ Subgraph ID ](../../../../api/reference/proxy/subgraph_id/)
      * [ Deployment ID ](../../../../api/reference/proxy/deployment_id/)

Subgrounds

  * [ Overview ](../../../)
  * [ Getting Started ](../../../getting_started/)

Toggle child pages in navigation

_ _

    * [ The Basics ](../../../getting_started/basics/)
    * [ Field Paths ](../../../getting_started/field_paths/)

Toggle child pages in navigation

_ _

      * [ Arguments ](../../../getting_started/field_paths/arguments/)
      * [ Filtering ](../../../getting_started/field_paths/filtering/)
      * [ Sorting ](../../../getting_started/field_paths/sorting/)
      * [ Merging ](../../../getting_started/field_paths/merging/)
    * [ Querying ](../../../getting_started/querying/)

Toggle child pages in navigation

_ _

    * [ Synthetic Fields ](../../../getting_started/synthetic_fields/)
  * [ Advanced Topics ](../../../advanced_topics/)

Toggle child pages in navigation

_ _

    * [ Contrib ](../../../advanced_topics/contrib/)

Toggle child pages in navigation

_ _

      * [ Plotly ](../../../advanced_topics/contrib/plotly/)
    * [ Pagination ](../../../advanced_topics/pagination/)

Toggle child pages in navigation

_ _

      * [ Custom Strategies ](../../../advanced_topics/pagination/custom/)
  * [ FAQ ](../../../faq/)

Toggle child pages in navigation

_ _

    * [ Exporting to Disk ](../../../faq/exporting/)
    * [ Getting More Data ](../../../faq/more_data/)
    * [ Python Setup ](../../../faq/setup/)

Toggle child pages in navigation

_ _

      * [ Python Versioning ](../../../faq/setup/version_management/)
  * [ Examples ](../../../examples/)

Toggle child pages in navigation

_ _

    * [ Exchanges ](../../../examples/exchanges/)
    * [ Bridges ](../../../examples/bridges/)
    * [ Liquid Staking ](../../../examples/liquid_staking/)
    * [ Governance ](../../../examples/governance/)
    * [ Advanced Research ](../../../examples/advanced_research/)
    * [ Vaults ](../../../examples/vaults/)
  * [ Videos ](../../../videos/)
  * [ Changelog ](../../../changelog/)
  * [ Contributing ](../../../contributing/)
  * [ API Reference ](../../)

Toggle child pages in navigation

_ _

    * [ Top Level APIs ](../../top_level/)
    * [ Internal ](../)

Toggle child pages in navigation

_ _

      * [ Client ](../client/)

Toggle child pages in navigation

_ _

        * [ Base ](../client/base/)
        * [ Sync ](../client/sync/)
        * [ Async_ ](../client/async_/)
      * [ Contrib ](../contrib/)

Toggle child pages in navigation

_ _

        * [ Plotly ](../contrib/plotly/)
        * [ Dash ](../contrib/dash/)
      * [ Pagination ](../pagination/)

Toggle child pages in navigation

_ _

        * [ Strategies ](../pagination/strategies/)
        * [ Preprocess ](../pagination/preprocess/)
        * [ Pagination ](../pagination/pagination/)
        * [ Utils ](../pagination/utils/)
      * [ Transform ](../transform/)

Toggle child pages in navigation

_ _

        * [ ABCs ](../transform/abcs/)
        * [ Apply ](../transform/apply/)
        * [ Defaults ](../transform/defaults/)
        * [ Transforms ](../transform/transforms/)
        * [ Utils ](../transform/utils/)
      * [ Subgraph ](../subgraph/)

Toggle child pages in navigation

_ _

        * [ Fieldpath ](../subgraph/fieldpath/)
        * [ Filter ](../subgraph/filter/)
        * [ Object ](../subgraph/object/)
        * [ Subgraph ](../subgraph/subgraph/)
      * [ Errors ](../errors/)
      * [ Query ](../query/)
      * [ Schema ](../schema/)
      * Utils 

Meta

  * [ Improving the Docs ](../../../../meta/contributing/)

Back to top

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

_ _

#  Utils  #

Utility module for Subgrounds

subgrounds.utils.  flatten_dict  (  _ data  _ , _ keys  =  []  _ )  #

    

Takes a dictionary containing key-value pairs where all values are of type
other than  list  and flattens it such that all key-value pairs in nested
dictionaries are now at depth 1.

Parameters  :

    

  * **data** ( [ _dict_ ](https://docs.python.org/3/library/stdtypes.html#dict "\(in Python v3.11\)") ) -- Dictionary containing non-list values 

  * **keys** ( [ _list_ ](https://docs.python.org/3/library/stdtypes.html#list "\(in Python v3.11\)") _[_ [ _str_ ](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.11\)") _]_ _,_ _optional_ ) -- Keys of  data  if  data  is a nested  dict  (  len(keys)  == depth of  data  ). Defaults to []. 

Returns  :

    

Flat dictionary containing all key-value pairs in  data  and its nested
dictionaries

Return type  :

    

[ dict ](https://docs.python.org/3/library/stdtypes.html#dict "\(in Python
v3.11\)")

subgrounds.utils.  contains_list  (  _ data  _ )  #

    

Returns  True  if  data  contains a value of type  list  in its nested data
and  False  otherwise

Parameters  :

    

**data** ( [ _dict_ ](https://docs.python.org/3/library/stdtypes.html#dict
"\(in Python v3.11\)") _|_ [ _list_
](https://docs.python.org/3/library/stdtypes.html#list "\(in Python v3.11\)")
_|_ [ _str_ ](https://docs.python.org/3/library/stdtypes.html#str "\(in Python
v3.11\)") _|_ [ _int_ ](https://docs.python.org/3/library/functions.html#int
"\(in Python v3.11\)") _|_ [ _float_
](https://docs.python.org/3/library/functions.html#float "\(in Python
v3.11\)") _|_ [ _bool_ ](https://docs.python.org/3/library/functions.html#bool
"\(in Python v3.11\)") ) -- Data

Returns  :

    

True  if  data  contains a list,  False  otherwise

Return type  :

    

[ bool ](https://docs.python.org/3/library/functions.html#bool "\(in Python
v3.11\)")

subgrounds.utils.  default_header  (  _ url  _ )  #

    

Contains the default header information for requests made by subgrounds

Inserts the Playgrounds API Key iff:

    

a) targetting the Playgrounds API AND b) if the  PLAYGROUNDS_API_KEY
environment variable is set

subgrounds.utils.  user_agent  (  )  #

    

A basic user agent describing the following details:

  * "Subgrounds" (and version) 

  * Platform/OS (and architecture) 

  * Python Type (and version) 

Examples: \- Subgrounds/1.1.2 (Darwin; arm64) CPython/3.11.2 \-
Subgrounds/1.1.2 (Emscripten; wasm32) CPython/3.10.2

⚠️ To override this, construct your [ ` Subgrounds  `
](../../top_level/#subgrounds.Subgrounds "subgrounds.Subgrounds") with a
headers

    

parameter with a dictionary containing an empty "User-Agent" key-value
pairing.

Pandas DataFrame utility module containing functions related to the formatting
of GraphQL JSON data into DataFrames.

_ class  _ subgrounds.dataframe_utils.  DataFrameColumns  (  _ key  _ , _
fpaths  _ )  #

    

Helper class that holds data related to the shape of a DataFrame

combine  (  _ other  _ )  #

    

Returns new DataFrameColumns containing the union of ` self  ` and ` other  `
's columns

Parameters  :

    

**other** (  _DataFrameColumns_ ) -- Columns to be combined to ` self  `

Returns  :

    

New  ` DataFrameColumns  ` containing the union of

    

` self  ` and ` other  `

Return type  :

    

DataFrameColumns

mk_df  (  _ data  _ , _ path_map  _ )  #

    

Formats the JSON data ` data  ` into a DataFrame containing the columns
defined in ` self  ` .

Parameters  :

    

  * **data** ( [ _list_ ](https://docs.python.org/3/library/stdtypes.html#list "\(in Python v3.11\)") _[_ [ _dict_ ](https://docs.python.org/3/library/stdtypes.html#dict "\(in Python v3.11\)") _[_ [ _str_ ](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.11\)") _,_ _Any_ _]_ _]_ ) -- The JSON data to be formatted into a dataframe 

  * **path_map** ( [ _dict_ ](https://docs.python.org/3/library/stdtypes.html#dict "\(in Python v3.11\)") _[_ [ _str_ ](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.11\)") _,_ [ _FieldPath_ ](../../top_level/#subgrounds.FieldPath "subgrounds.FieldPath") _]_ ) -- A dictionary of ` (key-FieldPath)  ` pairs 

Returns  :

    

The JSON data formatted into a DataFrame

Return type  :

    

pd.DataFrame

subgrounds.dataframe_utils.  columns_of_selections  (  _ selections  _ )  #

    

Generates a list of DataFrame columns specifications based on a list of `
Selection  ` trees.

Parameters  :

    

**selections** ( [ _list_
](https://docs.python.org/3/library/stdtypes.html#list "\(in Python v3.11\)")
_[_ [ _Selection_ ](../query/#subgrounds.query.Selection
"subgrounds.query.Selection") _]_ ) -- The selection trees

Returns  :

    

The list of DataFrame columns specifications

Return type  :

    

[ list ](https://docs.python.org/3/library/stdtypes.html#list "\(in Python
v3.11\)") [  DataFrameColumns  ]

subgrounds.dataframe_utils.  df_of_json  (  _ json_data  _ , _ fpaths  _ , _
columns  =  None  _ , _ concat  =  False  _ )  #

    

Formats the JSON data ` json_data  ` into Pandas DataFrames, flattening the
data in the process.

Depending on the request's fieldpaths, either one or multiple dataframes will
be returned based on how flattenable the response data is.

` fpaths  ` is a list of ` FieldPath  ` objects corresponding to the set of
fieldpaths that were used to get the response data ` json_data  ` .

` columns  ` is an optional argument used to rename the dataframes(s) columns.
The length of ` columns  ` must be the same as the number of columns of all
returned dataframes.

` concat  ` indicates whether or not the resulting dataframes should be
concatenated together. The dataframes must have the same number of columns, as
well as the same column names (which can be set using the ` columns  `
argument).

Parameters  :

    

  * **json_data** ( [ _list_ ](https://docs.python.org/3/library/stdtypes.html#list "\(in Python v3.11\)") _[_ [ _dict_ ](https://docs.python.org/3/library/stdtypes.html#dict "\(in Python v3.11\)") _[_ [ _str_ ](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.11\)") _,_ _Any_ _]_ _]_ ) -- Response data 

  * **fpaths** ( [ _list_ ](https://docs.python.org/3/library/stdtypes.html#list "\(in Python v3.11\)") _[_ [ _FieldPath_ ](../../top_level/#subgrounds.FieldPath "subgrounds.FieldPath") _]_ ) -- Fieldpaths that yielded the response data 

  * **columns** ( _Optional_ _[_ [ _list_ ](https://docs.python.org/3/library/stdtypes.html#list "\(in Python v3.11\)") _[_ [ _str_ ](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.11\)") _]_ _]_ _,_ _optional_ ) -- Column names. Defaults to None. 

  * **concat** ( [ _bool_ ](https://docs.python.org/3/library/functions.html#bool "\(in Python v3.11\)") _,_ _optional_ ) -- Flag indicating whether or not to concatenate the resulting dataframes, if there are more than one. Defaults to False. 

Returns  :

    

The resulting dataframe(s)

Return type  :

    

pd.DataFrame | [ list ](https://docs.python.org/3/library/stdtypes.html#list
"\(in Python v3.11\)") [pd.DataFrame]

[ Next  Contributing: Docs  ](../../../../meta/contributing/) [ Previous
Schema  ](../schema/)

Made with [ Furo ](https://github.com/pradyunsg/furo)

[ ](https://github.com/0xPlaygrounds/subgrounds) [
](https://discord.gg/v4r4zhBAh2) [ ](https://twitter.com/Playgrounds0x)

On this page

  * Utils 
    * ` flatten_dict()  `
    * ` contains_list()  `
    * ` default_header()  `
    * ` user_agent()  `
    * ` DataFrameColumns  `
      * ` DataFrameColumns.combine()  `
      * ` DataFrameColumns.mk_df()  `
    * ` columns_of_selections()  `
    * ` df_of_json()  `



Contents  Menu  Expand  Light mode  Dark mode  Auto light/dark mode

Hide navigation sidebar

Hide table of contents sidebar

Give us a ⭐️ on [ Github ](https://github.com/0xPlaygrounds/subgrounds)

Toggle site navigation sidebar

_ _

[ Playgrounds  ](../../../../)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

_ _

[ ![Light Logo](../../../../_static/assets/pg-logotype-dark.svg) ![Dark
Logo](../../../../_static/assets/pg-logotype-primary.svg)
](https://playgrounds.network)

Playgrounds API

  * [ Overview ](../../../../api/)
  * [ Getting an API Key ](../../../../api/key/)
  * [ Subgraph Proxy ](../../../../api/subgraph-proxy/)
  * [ Subgrounds Integration ](../../../../api/subgrounds/)
  * [ FAQ ](../../../../api/faq/)

Toggle child pages in navigation

_ _

    * [ What is a Query? ](../../../../api/faq/query/)
  * [ API Reference ](../../../../api/api-reference/)

Toggle child pages in navigation

_ _

    * [ Subgraph Proxy ](../../../../api/reference/proxy/)

Toggle child pages in navigation

_ _

      * [ Subgraph ID ](../../../../api/reference/proxy/subgraph_id/)
      * [ Deployment ID ](../../../../api/reference/proxy/deployment_id/)

Subgrounds

  * [ Overview ](../../../)
  * [ Getting Started ](../../../getting_started/)

Toggle child pages in navigation

_ _

    * [ The Basics ](../../../getting_started/basics/)
    * [ Field Paths ](../../../getting_started/field_paths/)

Toggle child pages in navigation

_ _

      * [ Arguments ](../../../getting_started/field_paths/arguments/)
      * [ Filtering ](../../../getting_started/field_paths/filtering/)
      * [ Sorting ](../../../getting_started/field_paths/sorting/)
      * [ Merging ](../../../getting_started/field_paths/merging/)
    * [ Querying ](../../../getting_started/querying/)

Toggle child pages in navigation

_ _

    * [ Synthetic Fields ](../../../getting_started/synthetic_fields/)
  * [ Advanced Topics ](../../../advanced_topics/)

Toggle child pages in navigation

_ _

    * [ Contrib ](../../../advanced_topics/contrib/)

Toggle child pages in navigation

_ _

      * [ Plotly ](../../../advanced_topics/contrib/plotly/)
    * [ Pagination ](../../../advanced_topics/pagination/)

Toggle child pages in navigation

_ _

      * [ Custom Strategies ](../../../advanced_topics/pagination/custom/)
  * [ FAQ ](../../../faq/)

Toggle child pages in navigation

_ _

    * [ Exporting to Disk ](../../../faq/exporting/)
    * [ Getting More Data ](../../../faq/more_data/)
    * [ Python Setup ](../../../faq/setup/)

Toggle child pages in navigation

_ _

      * [ Python Versioning ](../../../faq/setup/version_management/)
  * [ Examples ](../../../examples/)

Toggle child pages in navigation

_ _

    * [ Exchanges ](../../../examples/exchanges/)
    * [ Bridges ](../../../examples/bridges/)
    * [ Liquid Staking ](../../../examples/liquid_staking/)
    * [ Governance ](../../../examples/governance/)
    * [ Advanced Research ](../../../examples/advanced_research/)
    * [ Vaults ](../../../examples/vaults/)
  * [ Videos ](../../../videos/)
  * [ Changelog ](../../../changelog/)
  * [ Contributing ](../../../contributing/)
  * [ API Reference ](../../)

Toggle child pages in navigation

_ _

    * [ Top Level APIs ](../../top_level/)
    * [ Internal ](../)

Toggle child pages in navigation

_ _

      * [ Client ](../client/)

Toggle child pages in navigation

_ _

        * [ Base ](../client/base/)
        * [ Sync ](../client/sync/)
        * [ Async_ ](../client/async_/)
      * [ Contrib ](../contrib/)

Toggle child pages in navigation

_ _

        * [ Plotly ](../contrib/plotly/)
        * [ Dash ](../contrib/dash/)
      * [ Pagination ](../pagination/)

Toggle child pages in navigation

_ _

        * [ Strategies ](../pagination/strategies/)
        * [ Preprocess ](../pagination/preprocess/)
        * [ Pagination ](../pagination/pagination/)
        * [ Utils ](../pagination/utils/)
      * [ Transform ](../transform/)

Toggle child pages in navigation

_ _

        * [ ABCs ](../transform/abcs/)
        * [ Apply ](../transform/apply/)
        * [ Defaults ](../transform/defaults/)
        * [ Transforms ](../transform/transforms/)
        * [ Utils ](../transform/utils/)
      * [ Subgraph ](../subgraph/)

Toggle child pages in navigation

_ _

        * [ Fieldpath ](../subgraph/fieldpath/)
        * [ Filter ](../subgraph/filter/)
        * [ Object ](../subgraph/object/)
        * [ Subgraph ](../subgraph/subgraph/)
      * [ Errors ](../errors/)
      * [ Query ](../query/)
      * Schema 
      * [ Utils ](../utils/)

Meta

  * [ Improving the Docs ](../../../../meta/contributing/)

Back to top

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

_ _

#  Schema  #

Schema data structure module

This module contains various data structures in the form of dataclasses that
are used to represent GraphQL schemas in Subgrounds using an AST-like
approach.

_ class  _ subgrounds.schema.  SchemaMeta  (  _ *  _ , _ queryType  _ , _
types  _ , _ type_map  =  None  _ , _ mutationType  =  None  _ , _
subscriptionType  =  None  _ )  #

    

Class representing a GraphQL schema.

Contains all type definitions.

Create a new model by parsing and validating input data from keyword
arguments.

Raises ValidationError if the input data cannot be parsed to form a valid
model.

type_of_typeref  (  _ typeref  _ )  #

    

Returns the type information of the type reference  typeref

Args: self (SchemaMeta): The schema. typeref (TypeRef.T): The type reference
pointing to the type of interest.

Raises: KeyError: If the type reference refers to a non-existant type

Returns: TypeMeta.T: _description_

type_of  (  _ tmeta  _ )  #

    

Returns the argument or field definition's underlying type

type_of_input_object_meta  (  _ tmeta  _ , _ args  _ )  #

    

Recursively finds the nested type

[ Next  Utils  ](../utils/) [ Previous  Query  ](../query/)

Made with [ Furo ](https://github.com/pradyunsg/furo)

[ ](https://github.com/0xPlaygrounds/subgrounds) [
](https://discord.gg/v4r4zhBAh2) [ ](https://twitter.com/Playgrounds0x)

On this page

  * Schema 
    * ` SchemaMeta  `
      * ` SchemaMeta.type_of_typeref()  `
      * ` SchemaMeta.type_of()  `
      * ` SchemaMeta.type_of_input_object_meta()  `



Contents  Menu  Expand  Light mode  Dark mode  Auto light/dark mode

Hide navigation sidebar

Hide table of contents sidebar

Give us a ⭐️ on [ Github ](https://github.com/0xPlaygrounds/subgrounds)

Toggle site navigation sidebar

_ _

[ Playgrounds  ](../)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

_ _

[ ![Light Logo](../_static/assets/pg-logotype-dark.svg) ![Dark
Logo](../_static/assets/pg-logotype-primary.svg)
](https://playgrounds.network)

Playgrounds API

  * Overview 
  * [ Getting an API Key ](key/)
  * [ Subgraph Proxy ](subgraph-proxy/)
  * [ Subgrounds Integration ](subgrounds/)
  * [ FAQ ](faq/)

Toggle child pages in navigation

_ _

    * [ What is a Query? ](faq/query/)
  * [ API Reference ](api-reference/)

Toggle child pages in navigation

_ _

    * [ Subgraph Proxy ](reference/proxy/)

Toggle child pages in navigation

_ _

      * [ Subgraph ID ](reference/proxy/subgraph_id/)
      * [ Deployment ID ](reference/proxy/deployment_id/)

Subgrounds

  * [ Overview ](../subgrounds/)
  * [ Getting Started ](../subgrounds/getting_started/)

Toggle child pages in navigation

_ _

    * [ The Basics ](../subgrounds/getting_started/basics/)
    * [ Field Paths ](../subgrounds/getting_started/field_paths/)

Toggle child pages in navigation

_ _

      * [ Arguments ](../subgrounds/getting_started/field_paths/arguments/)
      * [ Filtering ](../subgrounds/getting_started/field_paths/filtering/)
      * [ Sorting ](../subgrounds/getting_started/field_paths/sorting/)
      * [ Merging ](../subgrounds/getting_started/field_paths/merging/)
    * [ Querying ](../subgrounds/getting_started/querying/)

Toggle child pages in navigation

_ _

    * [ Synthetic Fields ](../subgrounds/getting_started/synthetic_fields/)
  * [ Advanced Topics ](../subgrounds/advanced_topics/)

Toggle child pages in navigation

_ _

    * [ Contrib ](../subgrounds/advanced_topics/contrib/)

Toggle child pages in navigation

_ _

      * [ Plotly ](../subgrounds/advanced_topics/contrib/plotly/)
    * [ Pagination ](../subgrounds/advanced_topics/pagination/)

Toggle child pages in navigation

_ _

      * [ Custom Strategies ](../subgrounds/advanced_topics/pagination/custom/)
  * [ FAQ ](../subgrounds/faq/)

Toggle child pages in navigation

_ _

    * [ Exporting to Disk ](../subgrounds/faq/exporting/)
    * [ Getting More Data ](../subgrounds/faq/more_data/)
    * [ Python Setup ](../subgrounds/faq/setup/)

Toggle child pages in navigation

_ _

      * [ Python Versioning ](../subgrounds/faq/setup/version_management/)
  * [ Examples ](../subgrounds/examples/)

Toggle child pages in navigation

_ _

    * [ Exchanges ](../subgrounds/examples/exchanges/)
    * [ Bridges ](../subgrounds/examples/bridges/)
    * [ Liquid Staking ](../subgrounds/examples/liquid_staking/)
    * [ Governance ](../subgrounds/examples/governance/)
    * [ Advanced Research ](../subgrounds/examples/advanced_research/)
    * [ Vaults ](../subgrounds/examples/vaults/)
  * [ Videos ](../subgrounds/videos/)
  * [ Changelog ](../subgrounds/changelog/)
  * [ Contributing ](../subgrounds/contributing/)
  * [ API Reference ](../subgrounds/api_reference/)

Toggle child pages in navigation

_ _

    * [ Top Level APIs ](../subgrounds/api_reference/top_level/)
    * [ Internal ](../subgrounds/api_reference/internal/)

Toggle child pages in navigation

_ _

      * [ Client ](../subgrounds/api_reference/internal/client/)

Toggle child pages in navigation

_ _

        * [ Base ](../subgrounds/api_reference/internal/client/base/)
        * [ Sync ](../subgrounds/api_reference/internal/client/sync/)
        * [ Async_ ](../subgrounds/api_reference/internal/client/async_/)
      * [ Contrib ](../subgrounds/api_reference/internal/contrib/)

Toggle child pages in navigation

_ _

        * [ Plotly ](../subgrounds/api_reference/internal/contrib/plotly/)
        * [ Dash ](../subgrounds/api_reference/internal/contrib/dash/)
      * [ Pagination ](../subgrounds/api_reference/internal/pagination/)

Toggle child pages in navigation

_ _

        * [ Strategies ](../subgrounds/api_reference/internal/pagination/strategies/)
        * [ Preprocess ](../subgrounds/api_reference/internal/pagination/preprocess/)
        * [ Pagination ](../subgrounds/api_reference/internal/pagination/pagination/)
        * [ Utils ](../subgrounds/api_reference/internal/pagination/utils/)
      * [ Transform ](../subgrounds/api_reference/internal/transform/)

Toggle child pages in navigation

_ _

        * [ ABCs ](../subgrounds/api_reference/internal/transform/abcs/)
        * [ Apply ](../subgrounds/api_reference/internal/transform/apply/)
        * [ Defaults ](../subgrounds/api_reference/internal/transform/defaults/)
        * [ Transforms ](../subgrounds/api_reference/internal/transform/transforms/)
        * [ Utils ](../subgrounds/api_reference/internal/transform/utils/)
      * [ Subgraph ](../subgrounds/api_reference/internal/subgraph/)

Toggle child pages in navigation

_ _

        * [ Fieldpath ](../subgrounds/api_reference/internal/subgraph/fieldpath/)
        * [ Filter ](../subgrounds/api_reference/internal/subgraph/filter/)
        * [ Object ](../subgrounds/api_reference/internal/subgraph/object/)
        * [ Subgraph ](../subgrounds/api_reference/internal/subgraph/subgraph/)
      * [ Errors ](../subgrounds/api_reference/internal/errors/)
      * [ Query ](../subgrounds/api_reference/internal/query/)
      * [ Schema ](../subgrounds/api_reference/internal/schema/)
      * [ Utils ](../subgrounds/api_reference/internal/utils/)

Meta

  * [ Improving the Docs ](../meta/contributing/)

Back to top

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

_ _

#  Playgrounds API  #

Simplify your subgraph queries to the The Graph's decentralized network!

The Playgrounds API is a solution aimed at streamlining the user experience
with The Graph's decentralized network. It eliminates the need for traditional
wallet and GRT management by providing a convenient and straightforward API
key and URL. Users can effortlessly harness the full potential of the
decentralized ecosystem.

The Playgrounds API also allows users to download datasets from The Graph's
decentralized service via a REST API.

##  Advantages  #

  * SaaS-like experience for decentralized subgraphs 

  * Fully Integrated with [ Subgrounds  ](subgrounds/)

  * Monitor your API key usage 

* * *

###  Launch Playgrounds

Access our app to create API keys

[ ](https://app.playgrounds.network)

###  Getting Started

Get started in less than **five minutes**

[ ](key/)

###  FAQ

Common questions about the Playgrounds API

[ ](faq/)

###  API Reference

Full reference on each endpoint we offer

[ ](api-reference/)

* * *

[ Next  Getting a Playgrounds API Key  ](key/) [ Previous  Home  ](../)

Made with [ Furo ](https://github.com/pradyunsg/furo)

[ ](https://github.com/0xPlaygrounds/subgrounds) [
](https://discord.gg/v4r4zhBAh2) [ ](https://twitter.com/Playgrounds0x)

On this page

  * Playgrounds API 
    * Advantages 



Contents  Menu  Expand  Light mode  Dark mode  Auto light/dark mode

Hide navigation sidebar

Hide table of contents sidebar

Give us a ⭐️ on [ Github ](https://github.com/0xPlaygrounds/subgrounds)

Toggle site navigation sidebar

_ _

[ Playgrounds  ](../../)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

_ _

[ ![Light Logo](../../_static/assets/pg-logotype-dark.svg) ![Dark
Logo](../../_static/assets/pg-logotype-primary.svg)
](https://playgrounds.network)

Playgrounds API

  * [ Overview ](../)
  * Getting an API Key 
  * [ Subgraph Proxy ](../subgraph-proxy/)
  * [ Subgrounds Integration ](../subgrounds/)
  * [ FAQ ](../faq/)

Toggle child pages in navigation

_ _

    * [ What is a Query? ](../faq/query/)
  * [ API Reference ](../api-reference/)

Toggle child pages in navigation

_ _

    * [ Subgraph Proxy ](../reference/proxy/)

Toggle child pages in navigation

_ _

      * [ Subgraph ID ](../reference/proxy/subgraph_id/)
      * [ Deployment ID ](../reference/proxy/deployment_id/)

Subgrounds

  * [ Overview ](../../subgrounds/)
  * [ Getting Started ](../../subgrounds/getting_started/)

Toggle child pages in navigation

_ _

    * [ The Basics ](../../subgrounds/getting_started/basics/)
    * [ Field Paths ](../../subgrounds/getting_started/field_paths/)

Toggle child pages in navigation

_ _

      * [ Arguments ](../../subgrounds/getting_started/field_paths/arguments/)
      * [ Filtering ](../../subgrounds/getting_started/field_paths/filtering/)
      * [ Sorting ](../../subgrounds/getting_started/field_paths/sorting/)
      * [ Merging ](../../subgrounds/getting_started/field_paths/merging/)
    * [ Querying ](../../subgrounds/getting_started/querying/)

Toggle child pages in navigation

_ _

    * [ Synthetic Fields ](../../subgrounds/getting_started/synthetic_fields/)
  * [ Advanced Topics ](../../subgrounds/advanced_topics/)

Toggle child pages in navigation

_ _

    * [ Contrib ](../../subgrounds/advanced_topics/contrib/)

Toggle child pages in navigation

_ _

      * [ Plotly ](../../subgrounds/advanced_topics/contrib/plotly/)
    * [ Pagination ](../../subgrounds/advanced_topics/pagination/)

Toggle child pages in navigation

_ _

      * [ Custom Strategies ](../../subgrounds/advanced_topics/pagination/custom/)
  * [ FAQ ](../../subgrounds/faq/)

Toggle child pages in navigation

_ _

    * [ Exporting to Disk ](../../subgrounds/faq/exporting/)
    * [ Getting More Data ](../../subgrounds/faq/more_data/)
    * [ Python Setup ](../../subgrounds/faq/setup/)

Toggle child pages in navigation

_ _

      * [ Python Versioning ](../../subgrounds/faq/setup/version_management/)
  * [ Examples ](../../subgrounds/examples/)

Toggle child pages in navigation

_ _

    * [ Exchanges ](../../subgrounds/examples/exchanges/)
    * [ Bridges ](../../subgrounds/examples/bridges/)
    * [ Liquid Staking ](../../subgrounds/examples/liquid_staking/)
    * [ Governance ](../../subgrounds/examples/governance/)
    * [ Advanced Research ](../../subgrounds/examples/advanced_research/)
    * [ Vaults ](../../subgrounds/examples/vaults/)
  * [ Videos ](../../subgrounds/videos/)
  * [ Changelog ](../../subgrounds/changelog/)
  * [ Contributing ](../../subgrounds/contributing/)
  * [ API Reference ](../../subgrounds/api_reference/)

Toggle child pages in navigation

_ _

    * [ Top Level APIs ](../../subgrounds/api_reference/top_level/)
    * [ Internal ](../../subgrounds/api_reference/internal/)

Toggle child pages in navigation

_ _

      * [ Client ](../../subgrounds/api_reference/internal/client/)

Toggle child pages in navigation

_ _

        * [ Base ](../../subgrounds/api_reference/internal/client/base/)
        * [ Sync ](../../subgrounds/api_reference/internal/client/sync/)
        * [ Async_ ](../../subgrounds/api_reference/internal/client/async_/)
      * [ Contrib ](../../subgrounds/api_reference/internal/contrib/)

Toggle child pages in navigation

_ _

        * [ Plotly ](../../subgrounds/api_reference/internal/contrib/plotly/)
        * [ Dash ](../../subgrounds/api_reference/internal/contrib/dash/)
      * [ Pagination ](../../subgrounds/api_reference/internal/pagination/)

Toggle child pages in navigation

_ _

        * [ Strategies ](../../subgrounds/api_reference/internal/pagination/strategies/)
        * [ Preprocess ](../../subgrounds/api_reference/internal/pagination/preprocess/)
        * [ Pagination ](../../subgrounds/api_reference/internal/pagination/pagination/)
        * [ Utils ](../../subgrounds/api_reference/internal/pagination/utils/)
      * [ Transform ](../../subgrounds/api_reference/internal/transform/)

Toggle child pages in navigation

_ _

        * [ ABCs ](../../subgrounds/api_reference/internal/transform/abcs/)
        * [ Apply ](../../subgrounds/api_reference/internal/transform/apply/)
        * [ Defaults ](../../subgrounds/api_reference/internal/transform/defaults/)
        * [ Transforms ](../../subgrounds/api_reference/internal/transform/transforms/)
        * [ Utils ](../../subgrounds/api_reference/internal/transform/utils/)
      * [ Subgraph ](../../subgrounds/api_reference/internal/subgraph/)

Toggle child pages in navigation

_ _

        * [ Fieldpath ](../../subgrounds/api_reference/internal/subgraph/fieldpath/)
        * [ Filter ](../../subgrounds/api_reference/internal/subgraph/filter/)
        * [ Object ](../../subgrounds/api_reference/internal/subgraph/object/)
        * [ Subgraph ](../../subgrounds/api_reference/internal/subgraph/subgraph/)
      * [ Errors ](../../subgrounds/api_reference/internal/errors/)
      * [ Query ](../../subgrounds/api_reference/internal/query/)
      * [ Schema ](../../subgrounds/api_reference/internal/schema/)
      * [ Utils ](../../subgrounds/api_reference/internal/utils/)

Meta

  * [ Improving the Docs ](../../meta/contributing/)

Back to top

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

_ _

#  Getting a Playgrounds API Key  #

To start using the Playgrounds API, you'll first need to aquire an API key
from our platform.

##  1\. Creating your Playgrounds account  #

The first step in acquiring a Playgrounds API key is to create a Playgrounds
account via our signup [ page ](https://app.playgrounds.network/signup) .

** Create Account  Verify Email  **

##  2\. Create your Playgrounds API key  #

Once you have created your Playgrounds account and are logged into the
Playgrounds app, create a new API key.

** Generate API Key  **

![](../../_images/pg-app-create-api-key.png)

##  3\. Copy your Playgrounds API key  #

Congratulations, you now have a Playgrounds API key that you can use to query
decentralized network subgraphs through our proxy API! To copy the actual key
to your clipboard:

** Copy API Key  **

OR

**Token: ••••••••••  **

![](../../_images/pg-app-copy-api-key.png)

See also

All Playgrounds API keys start with the sequence ` pg-  ` to differentiate
them from other API keys (such as The Graph's keys).

[ Next  Subgraph Proxy  ](../subgraph-proxy/) [ Previous  Playgrounds API
](../)

Made with [ Furo ](https://github.com/pradyunsg/furo)

[ ](https://github.com/0xPlaygrounds/subgrounds) [
](https://discord.gg/v4r4zhBAh2) [ ](https://twitter.com/Playgrounds0x)

On this page

  * Getting a Playgrounds API Key 
    * 1\. Creating your Playgrounds account 
    * 2\. Create your Playgrounds API key 
    * 3\. Copy your Playgrounds API key 



Contents  Menu  Expand  Light mode  Dark mode  Auto light/dark mode

Hide navigation sidebar

Hide table of contents sidebar

Give us a ⭐️ on [ Github ](https://github.com/0xPlaygrounds/subgrounds)

Toggle site navigation sidebar

_ _

[ Playgrounds  ](../../)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

_ _

[ ![Light Logo](../../_static/assets/pg-logotype-dark.svg) ![Dark
Logo](../../_static/assets/pg-logotype-primary.svg)
](https://playgrounds.network)

Playgrounds API

  * [ Overview ](../)
  * [ Getting an API Key ](../key/)
  * Subgraph Proxy 
  * [ Subgrounds Integration ](../subgrounds/)
  * [ FAQ ](../faq/)

Toggle child pages in navigation

_ _

    * [ What is a Query? ](../faq/query/)
  * [ API Reference ](../api-reference/)

Toggle child pages in navigation

_ _

    * [ Subgraph Proxy ](../reference/proxy/)

Toggle child pages in navigation

_ _

      * [ Subgraph ID ](../reference/proxy/subgraph_id/)
      * [ Deployment ID ](../reference/proxy/deployment_id/)

Subgrounds

  * [ Overview ](../../subgrounds/)
  * [ Getting Started ](../../subgrounds/getting_started/)

Toggle child pages in navigation

_ _

    * [ The Basics ](../../subgrounds/getting_started/basics/)
    * [ Field Paths ](../../subgrounds/getting_started/field_paths/)

Toggle child pages in navigation

_ _

      * [ Arguments ](../../subgrounds/getting_started/field_paths/arguments/)
      * [ Filtering ](../../subgrounds/getting_started/field_paths/filtering/)
      * [ Sorting ](../../subgrounds/getting_started/field_paths/sorting/)
      * [ Merging ](../../subgrounds/getting_started/field_paths/merging/)
    * [ Querying ](../../subgrounds/getting_started/querying/)

Toggle child pages in navigation

_ _

    * [ Synthetic Fields ](../../subgrounds/getting_started/synthetic_fields/)
  * [ Advanced Topics ](../../subgrounds/advanced_topics/)

Toggle child pages in navigation

_ _

    * [ Contrib ](../../subgrounds/advanced_topics/contrib/)

Toggle child pages in navigation

_ _

      * [ Plotly ](../../subgrounds/advanced_topics/contrib/plotly/)
    * [ Pagination ](../../subgrounds/advanced_topics/pagination/)

Toggle child pages in navigation

_ _

      * [ Custom Strategies ](../../subgrounds/advanced_topics/pagination/custom/)
  * [ FAQ ](../../subgrounds/faq/)

Toggle child pages in navigation

_ _

    * [ Exporting to Disk ](../../subgrounds/faq/exporting/)
    * [ Getting More Data ](../../subgrounds/faq/more_data/)
    * [ Python Setup ](../../subgrounds/faq/setup/)

Toggle child pages in navigation

_ _

      * [ Python Versioning ](../../subgrounds/faq/setup/version_management/)
  * [ Examples ](../../subgrounds/examples/)

Toggle child pages in navigation

_ _

    * [ Exchanges ](../../subgrounds/examples/exchanges/)
    * [ Bridges ](../../subgrounds/examples/bridges/)
    * [ Liquid Staking ](../../subgrounds/examples/liquid_staking/)
    * [ Governance ](../../subgrounds/examples/governance/)
    * [ Advanced Research ](../../subgrounds/examples/advanced_research/)
    * [ Vaults ](../../subgrounds/examples/vaults/)
  * [ Videos ](../../subgrounds/videos/)
  * [ Changelog ](../../subgrounds/changelog/)
  * [ Contributing ](../../subgrounds/contributing/)
  * [ API Reference ](../../subgrounds/api_reference/)

Toggle child pages in navigation

_ _

    * [ Top Level APIs ](../../subgrounds/api_reference/top_level/)
    * [ Internal ](../../subgrounds/api_reference/internal/)

Toggle child pages in navigation

_ _

      * [ Client ](../../subgrounds/api_reference/internal/client/)

Toggle child pages in navigation

_ _

        * [ Base ](../../subgrounds/api_reference/internal/client/base/)
        * [ Sync ](../../subgrounds/api_reference/internal/client/sync/)
        * [ Async_ ](../../subgrounds/api_reference/internal/client/async_/)
      * [ Contrib ](../../subgrounds/api_reference/internal/contrib/)

Toggle child pages in navigation

_ _

        * [ Plotly ](../../subgrounds/api_reference/internal/contrib/plotly/)
        * [ Dash ](../../subgrounds/api_reference/internal/contrib/dash/)
      * [ Pagination ](../../subgrounds/api_reference/internal/pagination/)

Toggle child pages in navigation

_ _

        * [ Strategies ](../../subgrounds/api_reference/internal/pagination/strategies/)
        * [ Preprocess ](../../subgrounds/api_reference/internal/pagination/preprocess/)
        * [ Pagination ](../../subgrounds/api_reference/internal/pagination/pagination/)
        * [ Utils ](../../subgrounds/api_reference/internal/pagination/utils/)
      * [ Transform ](../../subgrounds/api_reference/internal/transform/)

Toggle child pages in navigation

_ _

        * [ ABCs ](../../subgrounds/api_reference/internal/transform/abcs/)
        * [ Apply ](../../subgrounds/api_reference/internal/transform/apply/)
        * [ Defaults ](../../subgrounds/api_reference/internal/transform/defaults/)
        * [ Transforms ](../../subgrounds/api_reference/internal/transform/transforms/)
        * [ Utils ](../../subgrounds/api_reference/internal/transform/utils/)
      * [ Subgraph ](../../subgrounds/api_reference/internal/subgraph/)

Toggle child pages in navigation

_ _

        * [ Fieldpath ](../../subgrounds/api_reference/internal/subgraph/fieldpath/)
        * [ Filter ](../../subgrounds/api_reference/internal/subgraph/filter/)
        * [ Object ](../../subgrounds/api_reference/internal/subgraph/object/)
        * [ Subgraph ](../../subgrounds/api_reference/internal/subgraph/subgraph/)
      * [ Errors ](../../subgrounds/api_reference/internal/errors/)
      * [ Query ](../../subgrounds/api_reference/internal/query/)
      * [ Schema ](../../subgrounds/api_reference/internal/schema/)
      * [ Utils ](../../subgrounds/api_reference/internal/utils/)

Meta

  * [ Improving the Docs ](../../meta/contributing/)

Back to top

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

_ _

#  Subgraph Proxy  #

After obtaining your API key, use our proxy API endpoint to query
decentralized subgraphs. You can do this in two ways:

  1. Via the subgraph id _(compatible with Ethereum only)_

  2. Via the subgraph deployment id 

##  Finding a subgraph's ID  #

You can quickly find the IDs of decentralized subgraphs via [ The Graph
Explorer ](https://thegraph.com/explorer) (via  SUBGRAPH-ID  ).

![](../../_images/graph-explorer-id.png)

##  Query by Subgraph id  #

To query a subgraph by its id, send a POST request to the Playgrounds proxy
endpoint:

    
    
    https://api.playgrounds.network/v1/proxy/subgraphs/id/[subgraph-id]
    

For example, to access the latest Uniswap V3 subgraph data using its subgraph
id, use:

    
    
    https://api.playgrounds.network/v1/proxy/subgraphs/id/ELUcwgpm14LKPLrBRuVvPvNKHQ9HvwmtKgKSH6123cr7
    

Important

This approach is for Ethereum-based subgraphs only. To query a subgraph hosted
on Arbitrum, refer to the 'Query by Deployment ID' section  below  .

Your POST request must include your Playgrounds API key, used as the
Playgrounds-Api-Token header value. The remainder of the request mirrors what
you'd typically send to The Graph's decentralized network.  

Here's an example request for the Uniswap V3 subgraph id ( `
ELUcwgpm14LKPLrBRuVvPvNKHQ9HvwmtKgKSH6123cr7  ` ) on The Graph's decentralized
network:

cURL

Querying a subgraph via the proxy endpoint using cURL  #

    
    
    curl https://api.playgrounds.network/v1/proxy/subgraphs/id/ELUcwgpm14LKPLrBRuVvPvNKHQ9HvwmtKgKSH6123cr7 \
        -H 'Content-Type: application/json' \
        -H 'Playgrounds-Api-Key: PG_API_KEY' \
        -d '{"query":"{protocols {name totalPoolCount}}"}'
    

Python

Querying a subgraph via the proxy endpoint using Python  #

    
    
    resp = requests.post(
        url="https://api.playgrounds.network/v1/proxy/subgraphs/id/ELUcwgpm14LKPLrBRuVvPvNKHQ9HvwmtKgKSH6123cr7",
        headers={
            "Content-Type": "application/json",
            "Playgrounds-Api-Key": "PG_API_KEY"
        },
        json={
            "query": "{protocols {name totalPoolCount}}"
        }
    )
    
    resp.json()
    

Equivalent GraphQL

This is the GraphQL query being sent to the subgraph  #

    
    
    query {
        protocols {
            name
            totalPoolCount
        }
    }
    

Response

The is the response (at time of writing)  #

    
    
    {
        "data": {
            "protocols": [
                {
                    "name": "Uniswap V3",
                    "totalPoolCount": 13767
                }
            ]
        }
    }
    

Important

Unlike The Graph's endpoint where the Graph API key is inserted in the URL,
Playgrounds API endpoints do **NOT** contain the user's API key in the URL
itself. Instead, the API key is provided via a header value.

Note

This endpoint mirrors the Graph's decentralized network gateway endpoint (see
below) with one key difference: the API key is **NOT** part of the URL.

https://gateway.thegraph.com/api/[api-key]/subgraphs/id/[subgraph-id]

##  Finding a subgraph's deployment ID  #

A decentralized subgraph's deployment ID can easily be obtained from [ The
Graph Explorer ](https://thegraph.com/explorer) (via  DEPLOYMENT-ID  ).

![](../../_images/graph-explorer-deployment-id.png)

##  Querying by deployment id  #

To request data from a subgraph via its deployment ID, make a POST request to
this Playgrounds proxy endpoint:

    
    
    https://api.playgrounds.network/v1/proxy/deployments/id/[deployment-id]
    

For instance, to request the latest Uniswap V3 subgraph data using its
deployment id, use:

    
    
    https://api.playgrounds.network/v1/proxy/deployments/id/QmcPHxcC2ZN7m79XfYZ77YmF4t9UCErv87a9NFKrSLWKtJ
    

Both methods function similarly, differing only in the URL. As with the
subgraph ID method, set your API key as the Playgrounds-Api-Token header
value, and make a POST request that includes your GraphQL query.

Here's an example request for the latest Uniswap V3 subgraph (deployment ID `
QmcPHxcC2ZN7m79XfYZ77YmF4t9UCErv87a9NFKrSLWKtJ  ` ) on Decentralized
Subgraphs:

cURL

Querying a subgraph via the proxy endpoint using cURL  #

    
    
    curl https://api.playgrounds.network/v1/proxy/deployments/id/QmcPHxcC2ZN7m79XfYZ77YmF4t9UCErv87a9NFKrSLWKtJ \
        -H 'Content-Type: application/json' \
        -H 'Playgrounds-Api-Key: PG_API_KEY' \
        -d '{"query":"{protocols {name totalPoolCount}}"}'
    

Python

Querying a subgraph via the proxy endpoint using Python  #

    
    
    resp = requests.post(
        url="https://api.playgrounds.network/v1/proxy/deployments/id/QmcPHxcC2ZN7m79XfYZ77YmF4t9UCErv87a9NFKrSLWKtJ",
        headers={
            "Content-Type": "application/json",
            "Playgrounds-Api-Key": "PG_API_KEY"
        },
        json={
            "query": "{protocols {name totalPoolCount}}"
        }
    )
    
    resp.json()
    

Equivalent GraphQL

This is the GraphQL query being sent to the subgraph  #

    
    
    query {
        protocols {
            name
            totalPoolCount
        }
    }
    

Response

The is the response (at time of writing)  #

    
    
    {
        "data": {
            "protocols": [
                {
                    "name": "Uniswap V3",
                    "totalPoolCount": 13767
                }
            ]
        }
    }
    

[ Next  Subgrounds Integration  ](../subgrounds/) [ Previous  Getting a
Playgrounds API Key  ](../key/)

Made with [ Furo ](https://github.com/pradyunsg/furo)

[ ](https://github.com/0xPlaygrounds/subgrounds) [
](https://discord.gg/v4r4zhBAh2) [ ](https://twitter.com/Playgrounds0x)

On this page

  * Subgraph Proxy 
    * Finding a subgraph's ID 
    * Query by Subgraph id 
    * Finding a subgraph's deployment ID 
    * Querying by deployment id 



Contents  Menu  Expand  Light mode  Dark mode  Auto light/dark mode

Hide navigation sidebar

Hide table of contents sidebar

Give us a ⭐️ on [ Github ](https://github.com/0xPlaygrounds/subgrounds)

Toggle site navigation sidebar

_ _

[ Playgrounds  ](../../)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

_ _

[ ![Light Logo](../../_static/assets/pg-logotype-dark.svg) ![Dark
Logo](../../_static/assets/pg-logotype-primary.svg)
](https://playgrounds.network)

Playgrounds API

  * [ Overview ](../)
  * [ Getting an API Key ](../key/)
  * [ Subgraph Proxy ](../subgraph-proxy/)
  * Subgrounds Integration 
  * [ FAQ ](../faq/)

Toggle child pages in navigation

_ _

    * [ What is a Query? ](../faq/query/)
  * [ API Reference ](../api-reference/)

Toggle child pages in navigation

_ _

    * [ Subgraph Proxy ](../reference/proxy/)

Toggle child pages in navigation

_ _

      * [ Subgraph ID ](../reference/proxy/subgraph_id/)
      * [ Deployment ID ](../reference/proxy/deployment_id/)

Subgrounds

  * [ Overview ](../../subgrounds/)
  * [ Getting Started ](../../subgrounds/getting_started/)

Toggle child pages in navigation

_ _

    * [ The Basics ](../../subgrounds/getting_started/basics/)
    * [ Field Paths ](../../subgrounds/getting_started/field_paths/)

Toggle child pages in navigation

_ _

      * [ Arguments ](../../subgrounds/getting_started/field_paths/arguments/)
      * [ Filtering ](../../subgrounds/getting_started/field_paths/filtering/)
      * [ Sorting ](../../subgrounds/getting_started/field_paths/sorting/)
      * [ Merging ](../../subgrounds/getting_started/field_paths/merging/)
    * [ Querying ](../../subgrounds/getting_started/querying/)

Toggle child pages in navigation

_ _

    * [ Synthetic Fields ](../../subgrounds/getting_started/synthetic_fields/)
  * [ Advanced Topics ](../../subgrounds/advanced_topics/)

Toggle child pages in navigation

_ _

    * [ Contrib ](../../subgrounds/advanced_topics/contrib/)

Toggle child pages in navigation

_ _

      * [ Plotly ](../../subgrounds/advanced_topics/contrib/plotly/)
    * [ Pagination ](../../subgrounds/advanced_topics/pagination/)

Toggle child pages in navigation

_ _

      * [ Custom Strategies ](../../subgrounds/advanced_topics/pagination/custom/)
  * [ FAQ ](../../subgrounds/faq/)

Toggle child pages in navigation

_ _

    * [ Exporting to Disk ](../../subgrounds/faq/exporting/)
    * [ Getting More Data ](../../subgrounds/faq/more_data/)
    * [ Python Setup ](../../subgrounds/faq/setup/)

Toggle child pages in navigation

_ _

      * [ Python Versioning ](../../subgrounds/faq/setup/version_management/)
  * [ Examples ](../../subgrounds/examples/)

Toggle child pages in navigation

_ _

    * [ Exchanges ](../../subgrounds/examples/exchanges/)
    * [ Bridges ](../../subgrounds/examples/bridges/)
    * [ Liquid Staking ](../../subgrounds/examples/liquid_staking/)
    * [ Governance ](../../subgrounds/examples/governance/)
    * [ Advanced Research ](../../subgrounds/examples/advanced_research/)
    * [ Vaults ](../../subgrounds/examples/vaults/)
  * [ Videos ](../../subgrounds/videos/)
  * [ Changelog ](../../subgrounds/changelog/)
  * [ Contributing ](../../subgrounds/contributing/)
  * [ API Reference ](../../subgrounds/api_reference/)

Toggle child pages in navigation

_ _

    * [ Top Level APIs ](../../subgrounds/api_reference/top_level/)
    * [ Internal ](../../subgrounds/api_reference/internal/)

Toggle child pages in navigation

_ _

      * [ Client ](../../subgrounds/api_reference/internal/client/)

Toggle child pages in navigation

_ _

        * [ Base ](../../subgrounds/api_reference/internal/client/base/)
        * [ Sync ](../../subgrounds/api_reference/internal/client/sync/)
        * [ Async_ ](../../subgrounds/api_reference/internal/client/async_/)
      * [ Contrib ](../../subgrounds/api_reference/internal/contrib/)

Toggle child pages in navigation

_ _

        * [ Plotly ](../../subgrounds/api_reference/internal/contrib/plotly/)
        * [ Dash ](../../subgrounds/api_reference/internal/contrib/dash/)
      * [ Pagination ](../../subgrounds/api_reference/internal/pagination/)

Toggle child pages in navigation

_ _

        * [ Strategies ](../../subgrounds/api_reference/internal/pagination/strategies/)
        * [ Preprocess ](../../subgrounds/api_reference/internal/pagination/preprocess/)
        * [ Pagination ](../../subgrounds/api_reference/internal/pagination/pagination/)
        * [ Utils ](../../subgrounds/api_reference/internal/pagination/utils/)
      * [ Transform ](../../subgrounds/api_reference/internal/transform/)

Toggle child pages in navigation

_ _

        * [ ABCs ](../../subgrounds/api_reference/internal/transform/abcs/)
        * [ Apply ](../../subgrounds/api_reference/internal/transform/apply/)
        * [ Defaults ](../../subgrounds/api_reference/internal/transform/defaults/)
        * [ Transforms ](../../subgrounds/api_reference/internal/transform/transforms/)
        * [ Utils ](../../subgrounds/api_reference/internal/transform/utils/)
      * [ Subgraph ](../../subgrounds/api_reference/internal/subgraph/)

Toggle child pages in navigation

_ _

        * [ Fieldpath ](../../subgrounds/api_reference/internal/subgraph/fieldpath/)
        * [ Filter ](../../subgrounds/api_reference/internal/subgraph/filter/)
        * [ Object ](../../subgrounds/api_reference/internal/subgraph/object/)
        * [ Subgraph ](../../subgrounds/api_reference/internal/subgraph/subgraph/)
      * [ Errors ](../../subgrounds/api_reference/internal/errors/)
      * [ Query ](../../subgrounds/api_reference/internal/query/)
      * [ Schema ](../../subgrounds/api_reference/internal/schema/)
      * [ Utils ](../../subgrounds/api_reference/internal/utils/)

Meta

  * [ Improving the Docs ](../../meta/contributing/)

Back to top

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

_ _

#  Subgrounds Integration  #

While you can certainly use the Playgrounds proxy alone by submitting requests
with a valid Playgrounds API key, pairing it with Subgrounds simplifies and
streamlines the querying and data analysis from decentralized subgraphs.

Click for Interactive Documentation

Clicking this button will enable editing and execution of the code-blocks on
this page. Learn more [ here  ](../../subgrounds/getting_started/basics/) .

Run code

##  1\. Using your Playgrounds API Key in Subgrounds  #

There are two main ways to validate your API key with subgrounds.

Note

Replace ` "PG_API_KEY"  ` with API key gathered from  earlier  !

Constructor

Initialize [ ` Subgrounds  `
](../../subgrounds/api_reference/top_level/#subgrounds.Subgrounds
"subgrounds.Subgrounds") object with a playgrounds api key  #

    
    
    from subgrounds import Subgrounds
    
    sg = Subgrounds.from_pg_key("PG_API_KEY")
    

Environment Var

The environment variable can be set any way you like!  #

    
    
    PLAYGROUNDS_API_KEY="PG_API_KEY"
    

This method is great since you don't need to change your code at all!  #

    
    
    from subgrounds import Subgrounds
    
    sg = Subgrounds()
    

Warning

This method will produce a [ ` RuntimeWarning  `
](https://docs.python.org/3/library/exceptions.html#RuntimeWarning "\(in
Python v3.11\)") if ` $PLAYGROUNDS_API_KEY  ` does _not_ look like valid.

It will also be overriden if the headers are set manually, or via `
Subgrounds.from_pg_key()  `

Under the Hood

Internally, both method sets the request headers  #

    
    
    from subgrounds import Subgrounds
    
    sg = Subgrounds(headers={"Playgrounds-Api-Key": "PG_API_KEY"})
    

##  2\. Query a decentralized subgraph  #

Once the [ ` Subgrounds  `
](../../subgrounds/api_reference/top_level/#subgrounds.Subgrounds
"subgrounds.Subgrounds") object has been initialized with the custom header
containing your API key, you can query a decentralized network subgraph
through our proxy endpoint just like you would query any other subgraph.

    
    
    subgraph = sg.load_subgraph(
        "https://api.playgrounds.network/v1/proxy/subgraphs/id/ELUcwgpm14LKPLrBRuVvPvNKHQ9HvwmtKgKSH6123cr7"
    )
    
    sg.query_df([
        subgraph.Query.tokens.id,
        subgraph.Query.tokens.symbol,
    ])
    

[ Next  FAQ  ](../faq/) [ Previous  Subgraph Proxy  ](../subgraph-proxy/)

Made with [ Furo ](https://github.com/pradyunsg/furo)

[ ](https://github.com/0xPlaygrounds/subgrounds) [
](https://discord.gg/v4r4zhBAh2) [ ](https://twitter.com/Playgrounds0x)

On this page

  * Subgrounds Integration 
    * 1\. Using your Playgrounds API Key in Subgrounds 
    * 2\. Query a decentralized subgraph 



Contents  Menu  Expand  Light mode  Dark mode  Auto light/dark mode

Hide navigation sidebar

Hide table of contents sidebar

Give us a ⭐️ on [ Github ](https://github.com/0xPlaygrounds/subgrounds)

Toggle site navigation sidebar

_ _

[ Playgrounds  ](../../../)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

_ _

[ ![Light Logo](../../../_static/assets/pg-logotype-dark.svg) ![Dark
Logo](../../../_static/assets/pg-logotype-primary.svg)
](https://playgrounds.network)

Playgrounds API

  * [ Overview ](../../)
  * [ Getting an API Key ](../../key/)
  * [ Subgraph Proxy ](../../subgraph-proxy/)
  * [ Subgrounds Integration ](../../subgrounds/)
  * [ FAQ ](../)

Toggle child pages in navigation

_ _

    * What is a Query? 
  * [ API Reference ](../../api-reference/)

Toggle child pages in navigation

_ _

    * [ Subgraph Proxy ](../../reference/proxy/)

Toggle child pages in navigation

_ _

      * [ Subgraph ID ](../../reference/proxy/subgraph_id/)
      * [ Deployment ID ](../../reference/proxy/deployment_id/)

Subgrounds

  * [ Overview ](../../../subgrounds/)
  * [ Getting Started ](../../../subgrounds/getting_started/)

Toggle child pages in navigation

_ _

    * [ The Basics ](../../../subgrounds/getting_started/basics/)
    * [ Field Paths ](../../../subgrounds/getting_started/field_paths/)

Toggle child pages in navigation

_ _

      * [ Arguments ](../../../subgrounds/getting_started/field_paths/arguments/)
      * [ Filtering ](../../../subgrounds/getting_started/field_paths/filtering/)
      * [ Sorting ](../../../subgrounds/getting_started/field_paths/sorting/)
      * [ Merging ](../../../subgrounds/getting_started/field_paths/merging/)
    * [ Querying ](../../../subgrounds/getting_started/querying/)

Toggle child pages in navigation

_ _

    * [ Synthetic Fields ](../../../subgrounds/getting_started/synthetic_fields/)
  * [ Advanced Topics ](../../../subgrounds/advanced_topics/)

Toggle child pages in navigation

_ _

    * [ Contrib ](../../../subgrounds/advanced_topics/contrib/)

Toggle child pages in navigation

_ _

      * [ Plotly ](../../../subgrounds/advanced_topics/contrib/plotly/)
    * [ Pagination ](../../../subgrounds/advanced_topics/pagination/)

Toggle child pages in navigation

_ _

      * [ Custom Strategies ](../../../subgrounds/advanced_topics/pagination/custom/)
  * [ FAQ ](../../../subgrounds/faq/)

Toggle child pages in navigation

_ _

    * [ Exporting to Disk ](../../../subgrounds/faq/exporting/)
    * [ Getting More Data ](../../../subgrounds/faq/more_data/)
    * [ Python Setup ](../../../subgrounds/faq/setup/)

Toggle child pages in navigation

_ _

      * [ Python Versioning ](../../../subgrounds/faq/setup/version_management/)
  * [ Examples ](../../../subgrounds/examples/)

Toggle child pages in navigation

_ _

    * [ Exchanges ](../../../subgrounds/examples/exchanges/)
    * [ Bridges ](../../../subgrounds/examples/bridges/)
    * [ Liquid Staking ](../../../subgrounds/examples/liquid_staking/)
    * [ Governance ](../../../subgrounds/examples/governance/)
    * [ Advanced Research ](../../../subgrounds/examples/advanced_research/)
    * [ Vaults ](../../../subgrounds/examples/vaults/)
  * [ Videos ](../../../subgrounds/videos/)
  * [ Changelog ](../../../subgrounds/changelog/)
  * [ Contributing ](../../../subgrounds/contributing/)
  * [ API Reference ](../../../subgrounds/api_reference/)

Toggle child pages in navigation

_ _

    * [ Top Level APIs ](../../../subgrounds/api_reference/top_level/)
    * [ Internal ](../../../subgrounds/api_reference/internal/)

Toggle child pages in navigation

_ _

      * [ Client ](../../../subgrounds/api_reference/internal/client/)

Toggle child pages in navigation

_ _

        * [ Base ](../../../subgrounds/api_reference/internal/client/base/)
        * [ Sync ](../../../subgrounds/api_reference/internal/client/sync/)
        * [ Async_ ](../../../subgrounds/api_reference/internal/client/async_/)
      * [ Contrib ](../../../subgrounds/api_reference/internal/contrib/)

Toggle child pages in navigation

_ _

        * [ Plotly ](../../../subgrounds/api_reference/internal/contrib/plotly/)
        * [ Dash ](../../../subgrounds/api_reference/internal/contrib/dash/)
      * [ Pagination ](../../../subgrounds/api_reference/internal/pagination/)

Toggle child pages in navigation

_ _

        * [ Strategies ](../../../subgrounds/api_reference/internal/pagination/strategies/)
        * [ Preprocess ](../../../subgrounds/api_reference/internal/pagination/preprocess/)
        * [ Pagination ](../../../subgrounds/api_reference/internal/pagination/pagination/)
        * [ Utils ](../../../subgrounds/api_reference/internal/pagination/utils/)
      * [ Transform ](../../../subgrounds/api_reference/internal/transform/)

Toggle child pages in navigation

_ _

        * [ ABCs ](../../../subgrounds/api_reference/internal/transform/abcs/)
        * [ Apply ](../../../subgrounds/api_reference/internal/transform/apply/)
        * [ Defaults ](../../../subgrounds/api_reference/internal/transform/defaults/)
        * [ Transforms ](../../../subgrounds/api_reference/internal/transform/transforms/)
        * [ Utils ](../../../subgrounds/api_reference/internal/transform/utils/)
      * [ Subgraph ](../../../subgrounds/api_reference/internal/subgraph/)

Toggle child pages in navigation

_ _

        * [ Fieldpath ](../../../subgrounds/api_reference/internal/subgraph/fieldpath/)
        * [ Filter ](../../../subgrounds/api_reference/internal/subgraph/filter/)
        * [ Object ](../../../subgrounds/api_reference/internal/subgraph/object/)
        * [ Subgraph ](../../../subgrounds/api_reference/internal/subgraph/subgraph/)
      * [ Errors ](../../../subgrounds/api_reference/internal/errors/)
      * [ Query ](../../../subgrounds/api_reference/internal/query/)
      * [ Schema ](../../../subgrounds/api_reference/internal/schema/)
      * [ Utils ](../../../subgrounds/api_reference/internal/utils/)

Meta

  * [ Improving the Docs ](../../../meta/contributing/)

Back to top

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

_ _

#  What is a Query?  #

In the Playgrounds API, queries are 1:1 to the number of requests made to the
underlying decentralized API. Queries are **not** 1:1 with a singular `
subgrounds  ` ' snippet as a single ` subgrounds  ` request could be getting
hundreds of thousands of rows with a single line of code. Since ` subgrounds
` automatically handles pagination, it makes multiple GraphQL queries behind
the scenes.

##  Examples  #

Generally, whatever is placed in the ` first  ` argument correlates to the
number of expected pages.

Click for Interactive Documentation

Clicking this button will enable editing and execution of the code-blocks on
this page. Learn more [ here  ](../../../subgrounds/getting_started/basics/) .

Run code

Common setup for the examples (using the hosted service as an example)  #

    
    
    from subgrounds import Subgrounds
    
    sg = Subgrounds()
    curve = sg.load_subgraph(
        "https://api.thegraph.com/subgraphs/name/messari/curve-finance-ethereum")
    

The following example will result in a single query:

Grabbing liquidity pool data  #

    
    
    # default for `first` is 100
    sg.query_df(
        curve.Query.liquidityPools
    )
    

The following example will result in 10 queries:

Grabbing liquidity pool data  #

    
    
    sg.query_df(
        curve.Query.liquidityPools(first=9000)
    )
    

This would still be 10 queries as both of these entities would get [ merged
](../../../subgrounds/getting_started/field_paths/merging/) .  #

    
    
    sg.query_df(
        curve.Query.liquidityPools(first=9000),
        curve.Query.liquidityGauges(first=9000),
    )
    

Note

Just because you put a very high number for ` first  ` (such as ` 1_000_000  `
), it doesn't mean it'll actually result in that many queries since there
might be less than that many rows of data.

##  Nested Pagination  #

Since nested fields can also have their own set of arguments, defining ` first
` in them will result in nested pagination. This can **greatly** increase the
number of queries made as each nested field will be multiplicative

The number of queries directly is related to the argument you put in ` first
` . If you only define ` first  ` for the most top-level entities, than
pagination is summed across all those fields. If you start defining ` first  `
for sub-fields, then pagination can get multiplicative as for each top-level
page, the whole series of sub-pages would be queried.

This would still be 100 (10・10) queries due to nested pagination and return 81
million (9000・9000) rows.  #

    
    
    pools = curve.Query.liquidityPools(first=9000)
    
    sg.query_df(
        pools.dailySnapshots(first=9000)
    )
    

[ Next  API Reference  ](../../api-reference/) [ Previous  FAQ  ](../)

Made with [ Furo ](https://github.com/pradyunsg/furo)

[ ](https://github.com/0xPlaygrounds/subgrounds) [
](https://discord.gg/v4r4zhBAh2) [ ](https://twitter.com/Playgrounds0x)

On this page

  * What is a Query? 
    * Examples 
    * Nested Pagination 



Contents  Menu  Expand  Light mode  Dark mode  Auto light/dark mode

Hide navigation sidebar

Hide table of contents sidebar

Give us a ⭐️ on [ Github ](https://github.com/0xPlaygrounds/subgrounds)

Toggle site navigation sidebar

_ _

[ Playgrounds  ](../../)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

_ _

[ ![Light Logo](../../_static/assets/pg-logotype-dark.svg) ![Dark
Logo](../../_static/assets/pg-logotype-primary.svg)
](https://playgrounds.network)

Playgrounds API

  * [ Overview ](../)
  * [ Getting an API Key ](../key/)
  * [ Subgraph Proxy ](../subgraph-proxy/)
  * [ Subgrounds Integration ](../subgrounds/)
  * [ FAQ ](../faq/)

Toggle child pages in navigation

_ _

    * [ What is a Query? ](../faq/query/)
  * API Reference 

Toggle child pages in navigation

_ _

    * [ Subgraph Proxy ](../reference/proxy/)

Toggle child pages in navigation

_ _

      * [ Subgraph ID ](../reference/proxy/subgraph_id/)
      * [ Deployment ID ](../reference/proxy/deployment_id/)

Subgrounds

  * [ Overview ](../../subgrounds/)
  * [ Getting Started ](../../subgrounds/getting_started/)

Toggle child pages in navigation

_ _

    * [ The Basics ](../../subgrounds/getting_started/basics/)
    * [ Field Paths ](../../subgrounds/getting_started/field_paths/)

Toggle child pages in navigation

_ _

      * [ Arguments ](../../subgrounds/getting_started/field_paths/arguments/)
      * [ Filtering ](../../subgrounds/getting_started/field_paths/filtering/)
      * [ Sorting ](../../subgrounds/getting_started/field_paths/sorting/)
      * [ Merging ](../../subgrounds/getting_started/field_paths/merging/)
    * [ Querying ](../../subgrounds/getting_started/querying/)

Toggle child pages in navigation

_ _

    * [ Synthetic Fields ](../../subgrounds/getting_started/synthetic_fields/)
  * [ Advanced Topics ](../../subgrounds/advanced_topics/)

Toggle child pages in navigation

_ _

    * [ Contrib ](../../subgrounds/advanced_topics/contrib/)

Toggle child pages in navigation

_ _

      * [ Plotly ](../../subgrounds/advanced_topics/contrib/plotly/)
    * [ Pagination ](../../subgrounds/advanced_topics/pagination/)

Toggle child pages in navigation

_ _

      * [ Custom Strategies ](../../subgrounds/advanced_topics/pagination/custom/)
  * [ FAQ ](../../subgrounds/faq/)

Toggle child pages in navigation

_ _

    * [ Exporting to Disk ](../../subgrounds/faq/exporting/)
    * [ Getting More Data ](../../subgrounds/faq/more_data/)
    * [ Python Setup ](../../subgrounds/faq/setup/)

Toggle child pages in navigation

_ _

      * [ Python Versioning ](../../subgrounds/faq/setup/version_management/)
  * [ Examples ](../../subgrounds/examples/)

Toggle child pages in navigation

_ _

    * [ Exchanges ](../../subgrounds/examples/exchanges/)
    * [ Bridges ](../../subgrounds/examples/bridges/)
    * [ Liquid Staking ](../../subgrounds/examples/liquid_staking/)
    * [ Governance ](../../subgrounds/examples/governance/)
    * [ Advanced Research ](../../subgrounds/examples/advanced_research/)
    * [ Vaults ](../../subgrounds/examples/vaults/)
  * [ Videos ](../../subgrounds/videos/)
  * [ Changelog ](../../subgrounds/changelog/)
  * [ Contributing ](../../subgrounds/contributing/)
  * [ API Reference ](../../subgrounds/api_reference/)

Toggle child pages in navigation

_ _

    * [ Top Level APIs ](../../subgrounds/api_reference/top_level/)
    * [ Internal ](../../subgrounds/api_reference/internal/)

Toggle child pages in navigation

_ _

      * [ Client ](../../subgrounds/api_reference/internal/client/)

Toggle child pages in navigation

_ _

        * [ Base ](../../subgrounds/api_reference/internal/client/base/)
        * [ Sync ](../../subgrounds/api_reference/internal/client/sync/)
        * [ Async_ ](../../subgrounds/api_reference/internal/client/async_/)
      * [ Contrib ](../../subgrounds/api_reference/internal/contrib/)

Toggle child pages in navigation

_ _

        * [ Plotly ](../../subgrounds/api_reference/internal/contrib/plotly/)
        * [ Dash ](../../subgrounds/api_reference/internal/contrib/dash/)
      * [ Pagination ](../../subgrounds/api_reference/internal/pagination/)

Toggle child pages in navigation

_ _

        * [ Strategies ](../../subgrounds/api_reference/internal/pagination/strategies/)
        * [ Preprocess ](../../subgrounds/api_reference/internal/pagination/preprocess/)
        * [ Pagination ](../../subgrounds/api_reference/internal/pagination/pagination/)
        * [ Utils ](../../subgrounds/api_reference/internal/pagination/utils/)
      * [ Transform ](../../subgrounds/api_reference/internal/transform/)

Toggle child pages in navigation

_ _

        * [ ABCs ](../../subgrounds/api_reference/internal/transform/abcs/)
        * [ Apply ](../../subgrounds/api_reference/internal/transform/apply/)
        * [ Defaults ](../../subgrounds/api_reference/internal/transform/defaults/)
        * [ Transforms ](../../subgrounds/api_reference/internal/transform/transforms/)
        * [ Utils ](../../subgrounds/api_reference/internal/transform/utils/)
      * [ Subgraph ](../../subgrounds/api_reference/internal/subgraph/)

Toggle child pages in navigation

_ _

        * [ Fieldpath ](../../subgrounds/api_reference/internal/subgraph/fieldpath/)
        * [ Filter ](../../subgrounds/api_reference/internal/subgraph/filter/)
        * [ Object ](../../subgrounds/api_reference/internal/subgraph/object/)
        * [ Subgraph ](../../subgrounds/api_reference/internal/subgraph/subgraph/)
      * [ Errors ](../../subgrounds/api_reference/internal/errors/)
      * [ Query ](../../subgrounds/api_reference/internal/query/)
      * [ Schema ](../../subgrounds/api_reference/internal/schema/)
      * [ Utils ](../../subgrounds/api_reference/internal/utils/)

Meta

  * [ Improving the Docs ](../../meta/contributing/)

Back to top

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

_ _

#  API Reference  #

The Playgrounds API is organized around REST and currently features only one
top-level resource accessible with an API key: the ` proxy  ` resource.

Our API accepts request parameters either via a JSON-encoded request body (for
POST requests) or query parameters (for GET requests). Unless explicitly
mentioned, all API endpoints return JSON-encoded responses.

##  Authentication  #

The Playgrounds API uses API keys to authenticate requests. You can view and
manage your API keys in the [ Playgrounds App
](https://app.playgrounds.network) .

Your API keys carry many privileges, so be sure to keep them secure! Do not
share your secret API keys in publicly accessible areas such as GitHub,
client-side code, and so forth.

Authentication to the API is performed via the custom Playgrounds
authorization header ` Playgrounds-Api-Key  ` . To authenticate, include the
following into the header of your request (replacing ` pg-abcdefghijk  ` with
your own)!

    
    
    Playgrounds-Api-Key: pg-abcdefghijk
    

Note

In ` subgrounds  ` , you can set the ` $PLAYGROUNDS_API_KEY  ` environment
variable to your API key and use our endpoints — the library will handle all
of the authentication on your behalf!

##  Endpoints  #

We currently only host a _single_ endpoint.

###  Subgraph Proxy

/v1/proxy

[ ](../reference/proxy/)

[ Next  Subgraph Proxy  ](../reference/proxy/) [ Previous  What is a Query?
](../faq/query/)

Made with [ Furo ](https://github.com/pradyunsg/furo)

[ ](https://github.com/0xPlaygrounds/subgrounds) [
](https://discord.gg/v4r4zhBAh2) [ ](https://twitter.com/Playgrounds0x)

On this page

  * API Reference 
    * Authentication 
    * Endpoints 



Contents  Menu  Expand  Light mode  Dark mode  Auto light/dark mode

Hide navigation sidebar

Hide table of contents sidebar

Give us a ⭐️ on [ Github ](https://github.com/0xPlaygrounds/subgrounds)

Toggle site navigation sidebar

_ _

[ Playgrounds  ](../../../)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

_ _

[ ![Light Logo](../../../_static/assets/pg-logotype-dark.svg) ![Dark
Logo](../../../_static/assets/pg-logotype-primary.svg)
](https://playgrounds.network)

Playgrounds API

  * [ Overview ](../../)
  * [ Getting an API Key ](../../key/)
  * [ Subgraph Proxy ](../../subgraph-proxy/)
  * [ Subgrounds Integration ](../../subgrounds/)
  * [ FAQ ](../../faq/)

Toggle child pages in navigation

_ _

    * [ What is a Query? ](../../faq/query/)
  * [ API Reference ](../../api-reference/)

Toggle child pages in navigation

_ _

    * Subgraph Proxy 

Toggle child pages in navigation

_ _

      * [ Subgraph ID ](subgraph_id/)
      * [ Deployment ID ](deployment_id/)

Subgrounds

  * [ Overview ](../../../subgrounds/)
  * [ Getting Started ](../../../subgrounds/getting_started/)

Toggle child pages in navigation

_ _

    * [ The Basics ](../../../subgrounds/getting_started/basics/)
    * [ Field Paths ](../../../subgrounds/getting_started/field_paths/)

Toggle child pages in navigation

_ _

      * [ Arguments ](../../../subgrounds/getting_started/field_paths/arguments/)
      * [ Filtering ](../../../subgrounds/getting_started/field_paths/filtering/)
      * [ Sorting ](../../../subgrounds/getting_started/field_paths/sorting/)
      * [ Merging ](../../../subgrounds/getting_started/field_paths/merging/)
    * [ Querying ](../../../subgrounds/getting_started/querying/)

Toggle child pages in navigation

_ _

    * [ Synthetic Fields ](../../../subgrounds/getting_started/synthetic_fields/)
  * [ Advanced Topics ](../../../subgrounds/advanced_topics/)

Toggle child pages in navigation

_ _

    * [ Contrib ](../../../subgrounds/advanced_topics/contrib/)

Toggle child pages in navigation

_ _

      * [ Plotly ](../../../subgrounds/advanced_topics/contrib/plotly/)
    * [ Pagination ](../../../subgrounds/advanced_topics/pagination/)

Toggle child pages in navigation

_ _

      * [ Custom Strategies ](../../../subgrounds/advanced_topics/pagination/custom/)
  * [ FAQ ](../../../subgrounds/faq/)

Toggle child pages in navigation

_ _

    * [ Exporting to Disk ](../../../subgrounds/faq/exporting/)
    * [ Getting More Data ](../../../subgrounds/faq/more_data/)
    * [ Python Setup ](../../../subgrounds/faq/setup/)

Toggle child pages in navigation

_ _

      * [ Python Versioning ](../../../subgrounds/faq/setup/version_management/)
  * [ Examples ](../../../subgrounds/examples/)

Toggle child pages in navigation

_ _

    * [ Exchanges ](../../../subgrounds/examples/exchanges/)
    * [ Bridges ](../../../subgrounds/examples/bridges/)
    * [ Liquid Staking ](../../../subgrounds/examples/liquid_staking/)
    * [ Governance ](../../../subgrounds/examples/governance/)
    * [ Advanced Research ](../../../subgrounds/examples/advanced_research/)
    * [ Vaults ](../../../subgrounds/examples/vaults/)
  * [ Videos ](../../../subgrounds/videos/)
  * [ Changelog ](../../../subgrounds/changelog/)
  * [ Contributing ](../../../subgrounds/contributing/)
  * [ API Reference ](../../../subgrounds/api_reference/)

Toggle child pages in navigation

_ _

    * [ Top Level APIs ](../../../subgrounds/api_reference/top_level/)
    * [ Internal ](../../../subgrounds/api_reference/internal/)

Toggle child pages in navigation

_ _

      * [ Client ](../../../subgrounds/api_reference/internal/client/)

Toggle child pages in navigation

_ _

        * [ Base ](../../../subgrounds/api_reference/internal/client/base/)
        * [ Sync ](../../../subgrounds/api_reference/internal/client/sync/)
        * [ Async_ ](../../../subgrounds/api_reference/internal/client/async_/)
      * [ Contrib ](../../../subgrounds/api_reference/internal/contrib/)

Toggle child pages in navigation

_ _

        * [ Plotly ](../../../subgrounds/api_reference/internal/contrib/plotly/)
        * [ Dash ](../../../subgrounds/api_reference/internal/contrib/dash/)
      * [ Pagination ](../../../subgrounds/api_reference/internal/pagination/)

Toggle child pages in navigation

_ _

        * [ Strategies ](../../../subgrounds/api_reference/internal/pagination/strategies/)
        * [ Preprocess ](../../../subgrounds/api_reference/internal/pagination/preprocess/)
        * [ Pagination ](../../../subgrounds/api_reference/internal/pagination/pagination/)
        * [ Utils ](../../../subgrounds/api_reference/internal/pagination/utils/)
      * [ Transform ](../../../subgrounds/api_reference/internal/transform/)

Toggle child pages in navigation

_ _

        * [ ABCs ](../../../subgrounds/api_reference/internal/transform/abcs/)
        * [ Apply ](../../../subgrounds/api_reference/internal/transform/apply/)
        * [ Defaults ](../../../subgrounds/api_reference/internal/transform/defaults/)
        * [ Transforms ](../../../subgrounds/api_reference/internal/transform/transforms/)
        * [ Utils ](../../../subgrounds/api_reference/internal/transform/utils/)
      * [ Subgraph ](../../../subgrounds/api_reference/internal/subgraph/)

Toggle child pages in navigation

_ _

        * [ Fieldpath ](../../../subgrounds/api_reference/internal/subgraph/fieldpath/)
        * [ Filter ](../../../subgrounds/api_reference/internal/subgraph/filter/)
        * [ Object ](../../../subgrounds/api_reference/internal/subgraph/object/)
        * [ Subgraph ](../../../subgrounds/api_reference/internal/subgraph/subgraph/)
      * [ Errors ](../../../subgrounds/api_reference/internal/errors/)
      * [ Query ](../../../subgrounds/api_reference/internal/query/)
      * [ Schema ](../../../subgrounds/api_reference/internal/schema/)
      * [ Utils ](../../../subgrounds/api_reference/internal/utils/)

Meta

  * [ Improving the Docs ](../../../meta/contributing/)

Back to top

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

_ _

#  Subgraph Proxy  #

/v1/proxy/

* * *

The proxy endpoints provide access to subgraphs hosted on The Graph's
decentralized network without the need to manage GRT tokens or interact with
smart contracts.

The proxy endpoint gets its name from the fact that all endpoints originating
from it mirror an equivalent endpoint available on The Graph.

For example, consider the following query URL:

    
    
    https://gateway.thegraph.com/api/[api-key]/subgraphs/id/3nXfK3RbFrj6mhkGdoKRowEEti2WvmUdxmz73tben6Mb
    

The equivalent Playgrounds API URL going through our proxy endpoint would be:

    
    
    https://api.playgrounds.network/v1/proxy/subgraphs/id/ELUcwgpm14LKPLrBRuVvPvNKHQ9HvwmtKgKSH6123cr7
    

Note

Notice that the URL is mirrored: both URLs contain the `
subgraphs/id/3nXfK3RbFrj6mhkGdoKRowEEti2WvmUdxmz73tben6Mb  ` path!

Important

Unlike The Graph's endpoint where the Graph API key is inserted in the URL,
Playgrounds API endpoints do not contain the user's API key in the URL itself.
Instead, the API key is provided via a header value.

* * *

###  Subgraph ID

/v1/proxy/subgraphs/id

[ ](subgraph_id/)

###  Deployment ID

/v1/proxy/deployments/id

[ ](deployment_id/)

[ Next  Subgraph ID  ](subgraph_id/) [ Previous  API Reference  ](../../api-
reference/)

Made with [ Furo ](https://github.com/pradyunsg/furo)

[ ](https://github.com/0xPlaygrounds/subgrounds) [
](https://discord.gg/v4r4zhBAh2) [ ](https://twitter.com/Playgrounds0x)



Contents  Menu  Expand  Light mode  Dark mode  Auto light/dark mode

Hide navigation sidebar

Hide table of contents sidebar

Give us a ⭐️ on [ Github ](https://github.com/0xPlaygrounds/subgrounds)

Toggle site navigation sidebar

_ _

[ Playgrounds  ](../../../../)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

_ _

[ ![Light Logo](../../../../_static/assets/pg-logotype-dark.svg) ![Dark
Logo](../../../../_static/assets/pg-logotype-primary.svg)
](https://playgrounds.network)

Playgrounds API

  * [ Overview ](../../../)
  * [ Getting an API Key ](../../../key/)
  * [ Subgraph Proxy ](../../../subgraph-proxy/)
  * [ Subgrounds Integration ](../../../subgrounds/)
  * [ FAQ ](../../../faq/)

Toggle child pages in navigation

_ _

    * [ What is a Query? ](../../../faq/query/)
  * [ API Reference ](../../../api-reference/)

Toggle child pages in navigation

_ _

    * [ Subgraph Proxy ](../)

Toggle child pages in navigation

_ _

      * Subgraph ID 
      * [ Deployment ID ](../deployment_id/)

Subgrounds

  * [ Overview ](../../../../subgrounds/)
  * [ Getting Started ](../../../../subgrounds/getting_started/)

Toggle child pages in navigation

_ _

    * [ The Basics ](../../../../subgrounds/getting_started/basics/)
    * [ Field Paths ](../../../../subgrounds/getting_started/field_paths/)

Toggle child pages in navigation

_ _

      * [ Arguments ](../../../../subgrounds/getting_started/field_paths/arguments/)
      * [ Filtering ](../../../../subgrounds/getting_started/field_paths/filtering/)
      * [ Sorting ](../../../../subgrounds/getting_started/field_paths/sorting/)
      * [ Merging ](../../../../subgrounds/getting_started/field_paths/merging/)
    * [ Querying ](../../../../subgrounds/getting_started/querying/)

Toggle child pages in navigation

_ _

    * [ Synthetic Fields ](../../../../subgrounds/getting_started/synthetic_fields/)
  * [ Advanced Topics ](../../../../subgrounds/advanced_topics/)

Toggle child pages in navigation

_ _

    * [ Contrib ](../../../../subgrounds/advanced_topics/contrib/)

Toggle child pages in navigation

_ _

      * [ Plotly ](../../../../subgrounds/advanced_topics/contrib/plotly/)
    * [ Pagination ](../../../../subgrounds/advanced_topics/pagination/)

Toggle child pages in navigation

_ _

      * [ Custom Strategies ](../../../../subgrounds/advanced_topics/pagination/custom/)
  * [ FAQ ](../../../../subgrounds/faq/)

Toggle child pages in navigation

_ _

    * [ Exporting to Disk ](../../../../subgrounds/faq/exporting/)
    * [ Getting More Data ](../../../../subgrounds/faq/more_data/)
    * [ Python Setup ](../../../../subgrounds/faq/setup/)

Toggle child pages in navigation

_ _

      * [ Python Versioning ](../../../../subgrounds/faq/setup/version_management/)
  * [ Examples ](../../../../subgrounds/examples/)

Toggle child pages in navigation

_ _

    * [ Exchanges ](../../../../subgrounds/examples/exchanges/)
    * [ Bridges ](../../../../subgrounds/examples/bridges/)
    * [ Liquid Staking ](../../../../subgrounds/examples/liquid_staking/)
    * [ Governance ](../../../../subgrounds/examples/governance/)
    * [ Advanced Research ](../../../../subgrounds/examples/advanced_research/)
    * [ Vaults ](../../../../subgrounds/examples/vaults/)
  * [ Videos ](../../../../subgrounds/videos/)
  * [ Changelog ](../../../../subgrounds/changelog/)
  * [ Contributing ](../../../../subgrounds/contributing/)
  * [ API Reference ](../../../../subgrounds/api_reference/)

Toggle child pages in navigation

_ _

    * [ Top Level APIs ](../../../../subgrounds/api_reference/top_level/)
    * [ Internal ](../../../../subgrounds/api_reference/internal/)

Toggle child pages in navigation

_ _

      * [ Client ](../../../../subgrounds/api_reference/internal/client/)

Toggle child pages in navigation

_ _

        * [ Base ](../../../../subgrounds/api_reference/internal/client/base/)
        * [ Sync ](../../../../subgrounds/api_reference/internal/client/sync/)
        * [ Async_ ](../../../../subgrounds/api_reference/internal/client/async_/)
      * [ Contrib ](../../../../subgrounds/api_reference/internal/contrib/)

Toggle child pages in navigation

_ _

        * [ Plotly ](../../../../subgrounds/api_reference/internal/contrib/plotly/)
        * [ Dash ](../../../../subgrounds/api_reference/internal/contrib/dash/)
      * [ Pagination ](../../../../subgrounds/api_reference/internal/pagination/)

Toggle child pages in navigation

_ _

        * [ Strategies ](../../../../subgrounds/api_reference/internal/pagination/strategies/)
        * [ Preprocess ](../../../../subgrounds/api_reference/internal/pagination/preprocess/)
        * [ Pagination ](../../../../subgrounds/api_reference/internal/pagination/pagination/)
        * [ Utils ](../../../../subgrounds/api_reference/internal/pagination/utils/)
      * [ Transform ](../../../../subgrounds/api_reference/internal/transform/)

Toggle child pages in navigation

_ _

        * [ ABCs ](../../../../subgrounds/api_reference/internal/transform/abcs/)
        * [ Apply ](../../../../subgrounds/api_reference/internal/transform/apply/)
        * [ Defaults ](../../../../subgrounds/api_reference/internal/transform/defaults/)
        * [ Transforms ](../../../../subgrounds/api_reference/internal/transform/transforms/)
        * [ Utils ](../../../../subgrounds/api_reference/internal/transform/utils/)
      * [ Subgraph ](../../../../subgrounds/api_reference/internal/subgraph/)

Toggle child pages in navigation

_ _

        * [ Fieldpath ](../../../../subgrounds/api_reference/internal/subgraph/fieldpath/)
        * [ Filter ](../../../../subgrounds/api_reference/internal/subgraph/filter/)
        * [ Object ](../../../../subgrounds/api_reference/internal/subgraph/object/)
        * [ Subgraph ](../../../../subgrounds/api_reference/internal/subgraph/subgraph/)
      * [ Errors ](../../../../subgrounds/api_reference/internal/errors/)
      * [ Query ](../../../../subgrounds/api_reference/internal/query/)
      * [ Schema ](../../../../subgrounds/api_reference/internal/schema/)
      * [ Utils ](../../../../subgrounds/api_reference/internal/utils/)

Meta

  * [ Improving the Docs ](../../../../meta/contributing/)

Back to top

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

_ _

#  Subgraph ID  #

/v1/proxy/

##  ` subgraphs/id/:subgraph_id  ` #

###  POST  #

Make a graphql request to the subgraph identified by the id ` subgraph_id  ` .

Important

This endpoint only works with subgraphs deployed on The Graph's Ethereum
decentralized service and **not** the Arbitrum decentralized service.

If you want to query a subgraph hosted on the Arbitrum decentralized service,
use the [ proxy by deployment id  ](../deployment_id/) endpoint.

  

####  URL Parameters  #

subgraph_id  ` string ` The decentralized network subgraph ID you are querying

  

####  Request Body (JSON)  #

query  ` string ` The GraphQL query itself

variables  ` dict? ` Values for the variables used within the GraphQL query
_(if any)_

  

####  Example  #

    
    
    curl https://api.playgrounds.network/v1/proxy/subgraphs/id/ELUcwgpm14LKPLrBRuVvPvNKHQ9HvwmtKgKSH6123cr7 \
        -H 'Content-Type: application/json' \
        -H 'Playgrounds-Api-Key: PG_API_KEY' \
        -d '{"query":"{protocols {name totalPoolCount}}"}'
    

Response:

    
    
    {
        "data": {
            "protocols": [
                {
                    "name": "Uniswap V3",
                    "totalPoolCount": 13767
                }
            ]
        }
    }
    

[ Next  Deployment ID  ](../deployment_id/) [ Previous  Subgraph Proxy  ](../)

Made with [ Furo ](https://github.com/pradyunsg/furo)

[ ](https://github.com/0xPlaygrounds/subgrounds) [
](https://discord.gg/v4r4zhBAh2) [ ](https://twitter.com/Playgrounds0x)

On this page

  * Subgraph ID 
    * ` subgraphs/id/:subgraph_id  `
      * POST 
        * URL Parameters 
        * Request Body (JSON) 
        * Example 



Contents  Menu  Expand  Light mode  Dark mode  Auto light/dark mode

Hide navigation sidebar

Hide table of contents sidebar

Give us a ⭐️ on [ Github ](https://github.com/0xPlaygrounds/subgrounds)

Toggle site navigation sidebar

_ _

[ Playgrounds  ](../../../../)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

_ _

[ ![Light Logo](../../../../_static/assets/pg-logotype-dark.svg) ![Dark
Logo](../../../../_static/assets/pg-logotype-primary.svg)
](https://playgrounds.network)

Playgrounds API

  * [ Overview ](../../../)
  * [ Getting an API Key ](../../../key/)
  * [ Subgraph Proxy ](../../../subgraph-proxy/)
  * [ Subgrounds Integration ](../../../subgrounds/)
  * [ FAQ ](../../../faq/)

Toggle child pages in navigation

_ _

    * [ What is a Query? ](../../../faq/query/)
  * [ API Reference ](../../../api-reference/)

Toggle child pages in navigation

_ _

    * [ Subgraph Proxy ](../)

Toggle child pages in navigation

_ _

      * [ Subgraph ID ](../subgraph_id/)
      * Deployment ID 

Subgrounds

  * [ Overview ](../../../../subgrounds/)
  * [ Getting Started ](../../../../subgrounds/getting_started/)

Toggle child pages in navigation

_ _

    * [ The Basics ](../../../../subgrounds/getting_started/basics/)
    * [ Field Paths ](../../../../subgrounds/getting_started/field_paths/)

Toggle child pages in navigation

_ _

      * [ Arguments ](../../../../subgrounds/getting_started/field_paths/arguments/)
      * [ Filtering ](../../../../subgrounds/getting_started/field_paths/filtering/)
      * [ Sorting ](../../../../subgrounds/getting_started/field_paths/sorting/)
      * [ Merging ](../../../../subgrounds/getting_started/field_paths/merging/)
    * [ Querying ](../../../../subgrounds/getting_started/querying/)

Toggle child pages in navigation

_ _

    * [ Synthetic Fields ](../../../../subgrounds/getting_started/synthetic_fields/)
  * [ Advanced Topics ](../../../../subgrounds/advanced_topics/)

Toggle child pages in navigation

_ _

    * [ Contrib ](../../../../subgrounds/advanced_topics/contrib/)

Toggle child pages in navigation

_ _

      * [ Plotly ](../../../../subgrounds/advanced_topics/contrib/plotly/)
    * [ Pagination ](../../../../subgrounds/advanced_topics/pagination/)

Toggle child pages in navigation

_ _

      * [ Custom Strategies ](../../../../subgrounds/advanced_topics/pagination/custom/)
  * [ FAQ ](../../../../subgrounds/faq/)

Toggle child pages in navigation

_ _

    * [ Exporting to Disk ](../../../../subgrounds/faq/exporting/)
    * [ Getting More Data ](../../../../subgrounds/faq/more_data/)
    * [ Python Setup ](../../../../subgrounds/faq/setup/)

Toggle child pages in navigation

_ _

      * [ Python Versioning ](../../../../subgrounds/faq/setup/version_management/)
  * [ Examples ](../../../../subgrounds/examples/)

Toggle child pages in navigation

_ _

    * [ Exchanges ](../../../../subgrounds/examples/exchanges/)
    * [ Bridges ](../../../../subgrounds/examples/bridges/)
    * [ Liquid Staking ](../../../../subgrounds/examples/liquid_staking/)
    * [ Governance ](../../../../subgrounds/examples/governance/)
    * [ Advanced Research ](../../../../subgrounds/examples/advanced_research/)
    * [ Vaults ](../../../../subgrounds/examples/vaults/)
  * [ Videos ](../../../../subgrounds/videos/)
  * [ Changelog ](../../../../subgrounds/changelog/)
  * [ Contributing ](../../../../subgrounds/contributing/)
  * [ API Reference ](../../../../subgrounds/api_reference/)

Toggle child pages in navigation

_ _

    * [ Top Level APIs ](../../../../subgrounds/api_reference/top_level/)
    * [ Internal ](../../../../subgrounds/api_reference/internal/)

Toggle child pages in navigation

_ _

      * [ Client ](../../../../subgrounds/api_reference/internal/client/)

Toggle child pages in navigation

_ _

        * [ Base ](../../../../subgrounds/api_reference/internal/client/base/)
        * [ Sync ](../../../../subgrounds/api_reference/internal/client/sync/)
        * [ Async_ ](../../../../subgrounds/api_reference/internal/client/async_/)
      * [ Contrib ](../../../../subgrounds/api_reference/internal/contrib/)

Toggle child pages in navigation

_ _

        * [ Plotly ](../../../../subgrounds/api_reference/internal/contrib/plotly/)
        * [ Dash ](../../../../subgrounds/api_reference/internal/contrib/dash/)
      * [ Pagination ](../../../../subgrounds/api_reference/internal/pagination/)

Toggle child pages in navigation

_ _

        * [ Strategies ](../../../../subgrounds/api_reference/internal/pagination/strategies/)
        * [ Preprocess ](../../../../subgrounds/api_reference/internal/pagination/preprocess/)
        * [ Pagination ](../../../../subgrounds/api_reference/internal/pagination/pagination/)
        * [ Utils ](../../../../subgrounds/api_reference/internal/pagination/utils/)
      * [ Transform ](../../../../subgrounds/api_reference/internal/transform/)

Toggle child pages in navigation

_ _

        * [ ABCs ](../../../../subgrounds/api_reference/internal/transform/abcs/)
        * [ Apply ](../../../../subgrounds/api_reference/internal/transform/apply/)
        * [ Defaults ](../../../../subgrounds/api_reference/internal/transform/defaults/)
        * [ Transforms ](../../../../subgrounds/api_reference/internal/transform/transforms/)
        * [ Utils ](../../../../subgrounds/api_reference/internal/transform/utils/)
      * [ Subgraph ](../../../../subgrounds/api_reference/internal/subgraph/)

Toggle child pages in navigation

_ _

        * [ Fieldpath ](../../../../subgrounds/api_reference/internal/subgraph/fieldpath/)
        * [ Filter ](../../../../subgrounds/api_reference/internal/subgraph/filter/)
        * [ Object ](../../../../subgrounds/api_reference/internal/subgraph/object/)
        * [ Subgraph ](../../../../subgrounds/api_reference/internal/subgraph/subgraph/)
      * [ Errors ](../../../../subgrounds/api_reference/internal/errors/)
      * [ Query ](../../../../subgrounds/api_reference/internal/query/)
      * [ Schema ](../../../../subgrounds/api_reference/internal/schema/)
      * [ Utils ](../../../../subgrounds/api_reference/internal/utils/)

Meta

  * [ Improving the Docs ](../../../../meta/contributing/)

Back to top

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

_ _

#  Deployment ID  #

/v1/proxy/

##  ` deployments/id/:deployment_id  ` #

###  POST  #

Make a graphql request to the subgraph identified by the id ` deployment_id  `
.

  

####  URL Parameters  #

deployment_id  ` string ` The decentralized network deployment ID you are
querying

  

####  Request Body (JSON)  #

query  ` string ` The GraphQL query itself

variables  ` dict? ` Values for the variables used within the GraphQL query
_(if any)_

  

####  Example  #

    
    
    curl https://api.playgrounds.network/v1/proxy/deployments/id/QmcPHxcC2ZN7m79XfYZ77YmF4t9UCErv87a9NFKrSLWKtJ \
        -H 'Content-Type: application/json' \
        -H 'Playgrounds-Api-Key: PG_API_KEY' \
        -d '{"query":"{protocols {name totalPoolCount}}"}'
    

Response:

    
    
    {
        "data": {
            "protocols": [
                {
                    "name": "Uniswap V3",
                    "totalPoolCount": 13767
                }
            ]
        }
    }
    

[ Next  Subgrounds  ](../../../../subgrounds/) [ Previous  Subgraph ID
](../subgraph_id/)

Made with [ Furo ](https://github.com/pradyunsg/furo)

[ ](https://github.com/0xPlaygrounds/subgrounds) [
](https://discord.gg/v4r4zhBAh2) [ ](https://twitter.com/Playgrounds0x)

On this page

  * Deployment ID 
    * ` deployments/id/:deployment_id  `
      * POST 
        * URL Parameters 
        * Request Body (JSON) 
        * Example 



