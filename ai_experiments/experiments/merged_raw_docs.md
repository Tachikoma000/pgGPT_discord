
#  subgrounds package  #

##  Subpackages  #

  * [ subgrounds.pagination package ](../subgrounds.pagination/)
    * [ Submodules ](../subgrounds.pagination/#submodules)
      * [ subgrounds.pagination.pagination module ](../subgrounds.pagination.pagination/)
        * [ ` PaginationError  ` ](../subgrounds.pagination.pagination/#subgrounds.pagination.pagination.PaginationError)
        * [ ` PaginationStrategy  ` ](../subgrounds.pagination.pagination/#subgrounds.pagination.pagination.PaginationStrategy)
        * [ ` paginate()  ` ](../subgrounds.pagination.pagination/#subgrounds.pagination.pagination.paginate)
        * [ ` paginate_iter()  ` ](../subgrounds.pagination.pagination/#subgrounds.pagination.pagination.paginate_iter)
      * [ subgrounds.pagination.preprocess module ](../subgrounds.pagination.preprocess/)
        * [ ` PaginationNode  ` ](../subgrounds.pagination.preprocess/#subgrounds.pagination.preprocess.PaginationNode)
        * [ ` is_pagination_node()  ` ](../subgrounds.pagination.preprocess/#subgrounds.pagination.preprocess.is_pagination_node)
        * [ ` get_orderBy_value()  ` ](../subgrounds.pagination.preprocess/#subgrounds.pagination.preprocess.get_orderBy_value)
        * [ ` get_orderDirection_value()  ` ](../subgrounds.pagination.preprocess/#subgrounds.pagination.preprocess.get_orderDirection_value)
        * [ ` get_filtering_args()  ` ](../subgrounds.pagination.preprocess/#subgrounds.pagination.preprocess.get_filtering_args)
        * [ ` get_filtering_value()  ` ](../subgrounds.pagination.preprocess/#subgrounds.pagination.preprocess.get_filtering_value)
        * [ ` generate_pagination_nodes()  ` ](../subgrounds.pagination.preprocess/#subgrounds.pagination.preprocess.generate_pagination_nodes)
        * [ ` normalize()  ` ](../subgrounds.pagination.preprocess/#subgrounds.pagination.preprocess.normalize)
        * [ ` prune_doc()  ` ](../subgrounds.pagination.preprocess/#subgrounds.pagination.preprocess.prune_doc)
      * [ subgrounds.pagination.strategies module ](../subgrounds.pagination.strategies/)
        * [ ` StopPagination  ` ](../subgrounds.pagination.strategies/#subgrounds.pagination.strategies.StopPagination)
        * [ ` SkipPagination  ` ](../subgrounds.pagination.strategies/#subgrounds.pagination.strategies.SkipPagination)
        * [ ` LegacyStrategyArgGenerator  ` ](../subgrounds.pagination.strategies/#subgrounds.pagination.strategies.LegacyStrategyArgGenerator)
        * [ ` LegacyStrategy  ` ](../subgrounds.pagination.strategies/#subgrounds.pagination.strategies.LegacyStrategy)
        * [ ` ShallowStrategyArgGenerator  ` ](../subgrounds.pagination.strategies/#subgrounds.pagination.strategies.ShallowStrategyArgGenerator)
        * [ ` ShallowStrategy  ` ](../subgrounds.pagination.strategies/#subgrounds.pagination.strategies.ShallowStrategy)
      * [ subgrounds.pagination.utils module ](../subgrounds.pagination.utils/)
        * [ ` merge()  ` ](../subgrounds.pagination.utils/#subgrounds.pagination.utils.merge)
        * [ ` merge_input_value_object_metas()  ` ](../subgrounds.pagination.utils/#subgrounds.pagination.utils.merge_input_value_object_metas)
    * [ Module contents ](../subgrounds.pagination/#module-subgrounds.pagination)
      * [ ` generate_pagination_nodes()  ` ](../subgrounds.pagination/#subgrounds.pagination.generate_pagination_nodes)
      * [ ` LegacyStrategy  ` ](../subgrounds.pagination/#subgrounds.pagination.LegacyStrategy)
        * [ ` LegacyStrategy.schema  ` ](../subgrounds.pagination/#subgrounds.pagination.LegacyStrategy.schema)
        * [ ` LegacyStrategy.arg_generator  ` ](../subgrounds.pagination/#subgrounds.pagination.LegacyStrategy.arg_generator)
        * [ ` LegacyStrategy.normalized_doc  ` ](../subgrounds.pagination/#subgrounds.pagination.LegacyStrategy.normalized_doc)
        * [ ` LegacyStrategy.step()  ` ](../subgrounds.pagination/#subgrounds.pagination.LegacyStrategy.step)
      * [ ` normalize()  ` ](../subgrounds.pagination/#subgrounds.pagination.normalize)
      * [ ` paginate_iter()  ` ](../subgrounds.pagination/#subgrounds.pagination.paginate_iter)
      * [ ` paginate()  ` ](../subgrounds.pagination/#subgrounds.pagination.paginate)
      * [ ` PaginationError  ` ](../subgrounds.pagination/#subgrounds.pagination.PaginationError)
      * [ ` PaginationNode  ` ](../subgrounds.pagination/#subgrounds.pagination.PaginationNode)
        * [ ` PaginationNode.node_idx  ` ](../subgrounds.pagination/#subgrounds.pagination.PaginationNode.node_idx)
        * [ ` PaginationNode.filter_field  ` ](../subgrounds.pagination/#subgrounds.pagination.PaginationNode.filter_field)
        * [ ` PaginationNode.first_value  ` ](../subgrounds.pagination/#subgrounds.pagination.PaginationNode.first_value)
        * [ ` PaginationNode.skip_value  ` ](../subgrounds.pagination/#subgrounds.pagination.PaginationNode.skip_value)
        * [ ` PaginationNode.filter_value  ` ](../subgrounds.pagination/#subgrounds.pagination.PaginationNode.filter_value)
        * [ ` PaginationNode.filter_value_type  ` ](../subgrounds.pagination/#subgrounds.pagination.PaginationNode.filter_value_type)
        * [ ` PaginationNode.key_path  ` ](../subgrounds.pagination/#subgrounds.pagination.PaginationNode.key_path)
        * [ ` PaginationNode.inner  ` ](../subgrounds.pagination/#subgrounds.pagination.PaginationNode.inner)
        * [ ` PaginationNode.node_idx  ` ](../subgrounds.pagination/#id0)
        * [ ` PaginationNode.filter_field  ` ](../subgrounds.pagination/#id1)
        * [ ` PaginationNode.first_value  ` ](../subgrounds.pagination/#id2)
        * [ ` PaginationNode.skip_value  ` ](../subgrounds.pagination/#id3)
        * [ ` PaginationNode.filter_value  ` ](../subgrounds.pagination/#id4)
        * [ ` PaginationNode.filter_value_type  ` ](../subgrounds.pagination/#id5)
        * [ ` PaginationNode.key_path  ` ](../subgrounds.pagination/#id6)
        * [ ` PaginationNode.inner  ` ](../subgrounds.pagination/#id7)
        * [ ` PaginationNode.get_vardefs()  ` ](../subgrounds.pagination/#subgrounds.pagination.PaginationNode.get_vardefs)
      * [ ` PaginationStrategy  ` ](../subgrounds.pagination/#subgrounds.pagination.PaginationStrategy)
        * [ ` PaginationStrategy.step()  ` ](../subgrounds.pagination/#subgrounds.pagination.PaginationStrategy.step)
      * [ ` prune_doc()  ` ](../subgrounds.pagination/#subgrounds.pagination.prune_doc)
      * [ ` ShallowStrategy  ` ](../subgrounds.pagination/#subgrounds.pagination.ShallowStrategy)
        * [ ` ShallowStrategy.schema  ` ](../subgrounds.pagination/#subgrounds.pagination.ShallowStrategy.schema)
        * [ ` ShallowStrategy.arg_generator  ` ](../subgrounds.pagination/#subgrounds.pagination.ShallowStrategy.arg_generator)
        * [ ` ShallowStrategy.normalized_doc  ` ](../subgrounds.pagination/#subgrounds.pagination.ShallowStrategy.normalized_doc)
        * [ ` ShallowStrategy.step()  ` ](../subgrounds.pagination/#subgrounds.pagination.ShallowStrategy.step)
  * [ subgrounds.subgraph package ](../subgrounds.subgraph/)
    * [ Submodules ](../subgrounds.subgraph/#submodules)
      * [ subgrounds.subgraph.fieldpath module ](../subgrounds.subgraph.fieldpath/)
        * [ ` typeref_of_binary_op()  ` ](../subgrounds.subgraph.fieldpath/#subgrounds.subgraph.fieldpath.typeref_of_binary_op)
        * [ ` type_ref_of_unary_op()  ` ](../subgrounds.subgraph.fieldpath/#subgrounds.subgraph.fieldpath.type_ref_of_unary_op)
        * [ ` FieldOperatorMixin  ` ](../subgrounds.subgraph.fieldpath/#subgrounds.subgraph.fieldpath.FieldOperatorMixin)
        * [ ` fieldpaths_of_object()  ` ](../subgrounds.subgraph.fieldpath/#subgrounds.subgraph.fieldpath.fieldpaths_of_object)
        * [ ` FieldPath  ` ](../subgrounds.subgraph.fieldpath/#subgrounds.subgraph.fieldpath.FieldPath)
        * [ ` SyntheticField  ` ](../subgrounds.subgraph.fieldpath/#subgrounds.subgraph.fieldpath.SyntheticField)
      * [ subgrounds.subgraph.filter module ](../subgrounds.subgraph.filter/)
        * [ ` Filter  ` ](../subgrounds.subgraph.filter/#subgrounds.subgraph.filter.Filter)
      * [ subgrounds.subgraph.object module ](../subgrounds.subgraph.object/)
        * [ ` Object  ` ](../subgrounds.subgraph.object/#subgrounds.subgraph.object.Object)
      * [ subgrounds.subgraph.subgraph module ](../subgrounds.subgraph.subgraph/)
        * [ ` Subgraph  ` ](../subgrounds.subgraph.subgraph/#subgrounds.subgraph.subgraph.Subgraph)
    * [ Module contents ](../subgrounds.subgraph/#module-subgrounds.subgraph)
      * [ ` FieldPath  ` ](../subgrounds.subgraph/#subgrounds.subgraph.FieldPath)
      * [ ` Filter  ` ](../subgrounds.subgraph/#subgrounds.subgraph.Filter)
        * [ ` Filter.field  ` ](../subgrounds.subgraph/#subgrounds.subgraph.Filter.field)
        * [ ` Filter.op  ` ](../subgrounds.subgraph/#subgrounds.subgraph.Filter.op)
        * [ ` Filter.value  ` ](../subgrounds.subgraph/#subgrounds.subgraph.Filter.value)
        * [ ` Filter.Operator  ` ](../subgrounds.subgraph/#subgrounds.subgraph.Filter.Operator)
        * [ ` Filter.mk_filter()  ` ](../subgrounds.subgraph/#subgrounds.subgraph.Filter.mk_filter)
        * [ ` Filter.name  ` ](../subgrounds.subgraph/#subgrounds.subgraph.Filter.name)
        * [ ` Filter.to_dict()  ` ](../subgrounds.subgraph/#subgrounds.subgraph.Filter.to_dict)
      * [ ` Object  ` ](../subgrounds.subgraph/#subgrounds.subgraph.Object)
      * [ ` Subgraph  ` ](../subgrounds.subgraph/#subgrounds.subgraph.Subgraph)
      * [ ` SyntheticField  ` ](../subgrounds.subgraph/#subgrounds.subgraph.SyntheticField)
        * [ ` SyntheticField.STRING  ` ](../subgrounds.subgraph/#subgrounds.subgraph.SyntheticField.STRING)
        * [ ` SyntheticField.INT  ` ](../subgrounds.subgraph/#subgrounds.subgraph.SyntheticField.INT)
        * [ ` SyntheticField.FLOAT  ` ](../subgrounds.subgraph/#subgrounds.subgraph.SyntheticField.FLOAT)
        * [ ` SyntheticField.BOOL  ` ](../subgrounds.subgraph/#subgrounds.subgraph.SyntheticField.BOOL)
        * [ ` SyntheticField.default_of_type()  ` ](../subgrounds.subgraph/#subgrounds.subgraph.SyntheticField.default_of_type)
        * [ ` SyntheticField.constant()  ` ](../subgrounds.subgraph/#subgrounds.subgraph.SyntheticField.constant)
        * [ ` SyntheticField.datetime_of_timestamp()  ` ](../subgrounds.subgraph/#subgrounds.subgraph.SyntheticField.datetime_of_timestamp)
        * [ ` SyntheticField.map()  ` ](../subgrounds.subgraph/#subgrounds.subgraph.SyntheticField.map)

##  Submodules  #

  * [ subgrounds.client module ](../subgrounds.client/)
    * [ ` get_schema()  ` ](../subgrounds.client/#subgrounds.client.get_schema)
    * [ ` query()  ` ](../subgrounds.client/#subgrounds.client.query)
  * [ subgrounds.dash_wrappers module ](../subgrounds.dash_wrappers/)
    * [ ` Refreshable  ` ](../subgrounds.dash_wrappers/#subgrounds.dash_wrappers.Refreshable)
      * [ ` Refreshable.dash_dependencies  ` ](../subgrounds.dash_wrappers/#subgrounds.dash_wrappers.Refreshable.dash_dependencies)
      * [ ` Refreshable.dash_dependencies_outputs  ` ](../subgrounds.dash_wrappers/#subgrounds.dash_wrappers.Refreshable.dash_dependencies_outputs)
    * [ ` Graph  ` ](../subgrounds.dash_wrappers/#subgrounds.dash_wrappers.Graph)
      * [ ` Graph.counter  ` ](../subgrounds.dash_wrappers/#subgrounds.dash_wrappers.Graph.counter)
      * [ ` Graph.wrapped_figure  ` ](../subgrounds.dash_wrappers/#subgrounds.dash_wrappers.Graph.wrapped_figure)
      * [ ` Graph.dash_dependencies  ` ](../subgrounds.dash_wrappers/#subgrounds.dash_wrappers.Graph.dash_dependencies)
      * [ ` Graph.dash_dependencies_outputs  ` ](../subgrounds.dash_wrappers/#subgrounds.dash_wrappers.Graph.dash_dependencies_outputs)
    * [ ` DataTable  ` ](../subgrounds.dash_wrappers/#subgrounds.dash_wrappers.DataTable)
      * [ ` DataTable.counter  ` ](../subgrounds.dash_wrappers/#subgrounds.dash_wrappers.DataTable.counter)
      * [ ` DataTable.data  ` ](../subgrounds.dash_wrappers/#subgrounds.dash_wrappers.DataTable.data)
      * [ ` DataTable.columns  ` ](../subgrounds.dash_wrappers/#subgrounds.dash_wrappers.DataTable.columns)
      * [ ` DataTable.subgrounds  ` ](../subgrounds.dash_wrappers/#subgrounds.dash_wrappers.DataTable.subgrounds)
      * [ ` DataTable.concat  ` ](../subgrounds.dash_wrappers/#subgrounds.dash_wrappers.DataTable.concat)
      * [ ` DataTable.append  ` ](../subgrounds.dash_wrappers/#subgrounds.dash_wrappers.DataTable.append)
      * [ ` DataTable.df  ` ](../subgrounds.dash_wrappers/#subgrounds.dash_wrappers.DataTable.df)
      * [ ` DataTable.refresh()  ` ](../subgrounds.dash_wrappers/#subgrounds.dash_wrappers.DataTable.refresh)
      * [ ` DataTable.dash_dependencies  ` ](../subgrounds.dash_wrappers/#subgrounds.dash_wrappers.DataTable.dash_dependencies)
      * [ ` DataTable.dash_dependencies_outputs  ` ](../subgrounds.dash_wrappers/#subgrounds.dash_wrappers.DataTable.dash_dependencies_outputs)
    * [ ` AutoUpdate  ` ](../subgrounds.dash_wrappers/#subgrounds.dash_wrappers.AutoUpdate)
      * [ ` AutoUpdate.counter  ` ](../subgrounds.dash_wrappers/#subgrounds.dash_wrappers.AutoUpdate.counter)
  * [ subgrounds.dataframe_utils module ](../subgrounds.dataframe_utils/)
    * [ ` gen_columns()  ` ](../subgrounds.dataframe_utils/#subgrounds.dataframe_utils.gen_columns)
    * [ ` fmt_cols()  ` ](../subgrounds.dataframe_utils/#subgrounds.dataframe_utils.fmt_cols)
    * [ ` DataFrameColumns  ` ](../subgrounds.dataframe_utils/#subgrounds.dataframe_utils.DataFrameColumns)
      * [ ` DataFrameColumns.key  ` ](../subgrounds.dataframe_utils/#subgrounds.dataframe_utils.DataFrameColumns.key)
      * [ ` DataFrameColumns.fpaths  ` ](../subgrounds.dataframe_utils/#subgrounds.dataframe_utils.DataFrameColumns.fpaths)
      * [ ` DataFrameColumns.combine()  ` ](../subgrounds.dataframe_utils/#subgrounds.dataframe_utils.DataFrameColumns.combine)
      * [ ` DataFrameColumns.mk_df()  ` ](../subgrounds.dataframe_utils/#subgrounds.dataframe_utils.DataFrameColumns.mk_df)
    * [ ` columns_of_selections()  ` ](../subgrounds.dataframe_utils/#subgrounds.dataframe_utils.columns_of_selections)
    * [ ` df_of_json()  ` ](../subgrounds.dataframe_utils/#subgrounds.dataframe_utils.df_of_json)
  * [ subgrounds.plotly_wrappers module ](../subgrounds.plotly_wrappers/)
    * [ ` Figure  ` ](../subgrounds.plotly_wrappers/#subgrounds.plotly_wrappers.Figure)
      * [ ` Figure.figure  ` ](../subgrounds.plotly_wrappers/#subgrounds.plotly_wrappers.Figure.figure)
      * [ ` Figure.subgrounds  ` ](../subgrounds.plotly_wrappers/#subgrounds.plotly_wrappers.Figure.subgrounds)
      * [ ` Figure.traces  ` ](../subgrounds.plotly_wrappers/#subgrounds.plotly_wrappers.Figure.traces)
      * [ ` Figure.req  ` ](../subgrounds.plotly_wrappers/#subgrounds.plotly_wrappers.Figure.req)
      * [ ` Figure.data  ` ](../subgrounds.plotly_wrappers/#subgrounds.plotly_wrappers.Figure.data)
      * [ ` Figure.args  ` ](../subgrounds.plotly_wrappers/#subgrounds.plotly_wrappers.Figure.args)
      * [ ` Figure.refresh()  ` ](../subgrounds.plotly_wrappers/#subgrounds.plotly_wrappers.Figure.refresh)
    * [ ` TraceWrapper  ` ](../subgrounds.plotly_wrappers/#subgrounds.plotly_wrappers.TraceWrapper)
      * [ ` TraceWrapper.graph_object  ` ](../subgrounds.plotly_wrappers/#subgrounds.plotly_wrappers.TraceWrapper.graph_object)
      * [ ` TraceWrapper.fpaths  ` ](../subgrounds.plotly_wrappers/#subgrounds.plotly_wrappers.TraceWrapper.fpaths)
      * [ ` TraceWrapper.args  ` ](../subgrounds.plotly_wrappers/#subgrounds.plotly_wrappers.TraceWrapper.args)
      * [ ` TraceWrapper.mk_trace()  ` ](../subgrounds.plotly_wrappers/#subgrounds.plotly_wrappers.TraceWrapper.mk_trace)
      * [ ` TraceWrapper.field_paths  ` ](../subgrounds.plotly_wrappers/#subgrounds.plotly_wrappers.TraceWrapper.field_paths)
    * [ ` Scatter  ` ](../subgrounds.plotly_wrappers/#subgrounds.plotly_wrappers.Scatter)
      * [ ` Scatter.graph_object  ` ](../subgrounds.plotly_wrappers/#subgrounds.plotly_wrappers.Scatter.graph_object)
    * [ ` Pie  ` ](../subgrounds.plotly_wrappers/#subgrounds.plotly_wrappers.Pie)
      * [ ` Pie.graph_object  ` ](../subgrounds.plotly_wrappers/#subgrounds.plotly_wrappers.Pie.graph_object)
    * [ ` Bar  ` ](../subgrounds.plotly_wrappers/#subgrounds.plotly_wrappers.Bar)
      * [ ` Bar.graph_object  ` ](../subgrounds.plotly_wrappers/#subgrounds.plotly_wrappers.Bar.graph_object)
    * [ ` Heatmap  ` ](../subgrounds.plotly_wrappers/#subgrounds.plotly_wrappers.Heatmap)
      * [ ` Heatmap.graph_object  ` ](../subgrounds.plotly_wrappers/#subgrounds.plotly_wrappers.Heatmap.graph_object)
    * [ ` Contour  ` ](../subgrounds.plotly_wrappers/#subgrounds.plotly_wrappers.Contour)
      * [ ` Contour.graph_object  ` ](../subgrounds.plotly_wrappers/#subgrounds.plotly_wrappers.Contour.graph_object)
    * [ ` Table  ` ](../subgrounds.plotly_wrappers/#subgrounds.plotly_wrappers.Table)
      * [ ` Table.graph_object  ` ](../subgrounds.plotly_wrappers/#subgrounds.plotly_wrappers.Table.graph_object)
    * [ ` Box  ` ](../subgrounds.plotly_wrappers/#subgrounds.plotly_wrappers.Box)
      * [ ` Box.graph_object  ` ](../subgrounds.plotly_wrappers/#subgrounds.plotly_wrappers.Box.graph_object)
    * [ ` Violin  ` ](../subgrounds.plotly_wrappers/#subgrounds.plotly_wrappers.Violin)
      * [ ` Violin.graph_object  ` ](../subgrounds.plotly_wrappers/#subgrounds.plotly_wrappers.Violin.graph_object)
    * [ ` Histogram  ` ](../subgrounds.plotly_wrappers/#subgrounds.plotly_wrappers.Histogram)
      * [ ` Histogram.graph_object  ` ](../subgrounds.plotly_wrappers/#subgrounds.plotly_wrappers.Histogram.graph_object)
    * [ ` Histogram2d  ` ](../subgrounds.plotly_wrappers/#subgrounds.plotly_wrappers.Histogram2d)
      * [ ` Histogram2d.graph_object  ` ](../subgrounds.plotly_wrappers/#subgrounds.plotly_wrappers.Histogram2d.graph_object)
    * [ ` Histogram2dContour  ` ](../subgrounds.plotly_wrappers/#subgrounds.plotly_wrappers.Histogram2dContour)
      * [ ` Histogram2dContour.graph_object  ` ](../subgrounds.plotly_wrappers/#subgrounds.plotly_wrappers.Histogram2dContour.graph_object)
    * [ ` Ohlc  ` ](../subgrounds.plotly_wrappers/#subgrounds.plotly_wrappers.Ohlc)
      * [ ` Ohlc.graph_object  ` ](../subgrounds.plotly_wrappers/#subgrounds.plotly_wrappers.Ohlc.graph_object)
    * [ ` Candlestick  ` ](../subgrounds.plotly_wrappers/#subgrounds.plotly_wrappers.Candlestick)
      * [ ` Candlestick.graph_object  ` ](../subgrounds.plotly_wrappers/#subgrounds.plotly_wrappers.Candlestick.graph_object)
    * [ ` Waterfall  ` ](../subgrounds.plotly_wrappers/#subgrounds.plotly_wrappers.Waterfall)
      * [ ` Waterfall.graph_object  ` ](../subgrounds.plotly_wrappers/#subgrounds.plotly_wrappers.Waterfall.graph_object)
    * [ ` Funnel  ` ](../subgrounds.plotly_wrappers/#subgrounds.plotly_wrappers.Funnel)
      * [ ` Funnel.graph_object  ` ](../subgrounds.plotly_wrappers/#subgrounds.plotly_wrappers.Funnel.graph_object)
    * [ ` Indicator  ` ](../subgrounds.plotly_wrappers/#subgrounds.plotly_wrappers.Indicator)
      * [ ` Indicator.graph_object  ` ](../subgrounds.plotly_wrappers/#subgrounds.plotly_wrappers.Indicator.graph_object)
    * [ ` Scatter3d  ` ](../subgrounds.plotly_wrappers/#subgrounds.plotly_wrappers.Scatter3d)
      * [ ` Scatter3d.graph_object  ` ](../subgrounds.plotly_wrappers/#subgrounds.plotly_wrappers.Scatter3d.graph_object)
    * [ ` Surface  ` ](../subgrounds.plotly_wrappers/#subgrounds.plotly_wrappers.Surface)
      * [ ` Surface.graph_object  ` ](../subgrounds.plotly_wrappers/#subgrounds.plotly_wrappers.Surface.graph_object)
    * [ ` Scattergeo  ` ](../subgrounds.plotly_wrappers/#subgrounds.plotly_wrappers.Scattergeo)
      * [ ` Scattergeo.graph_object  ` ](../subgrounds.plotly_wrappers/#subgrounds.plotly_wrappers.Scattergeo.graph_object)
    * [ ` Choropleth  ` ](../subgrounds.plotly_wrappers/#subgrounds.plotly_wrappers.Choropleth)
      * [ ` Choropleth.graph_object  ` ](../subgrounds.plotly_wrappers/#subgrounds.plotly_wrappers.Choropleth.graph_object)
    * [ ` Scattermapbox  ` ](../subgrounds.plotly_wrappers/#subgrounds.plotly_wrappers.Scattermapbox)
      * [ ` Scattermapbox.graph_object  ` ](../subgrounds.plotly_wrappers/#subgrounds.plotly_wrappers.Scattermapbox.graph_object)
    * [ ` Choroplethmapbox  ` ](../subgrounds.plotly_wrappers/#subgrounds.plotly_wrappers.Choroplethmapbox)
      * [ ` Choroplethmapbox.graph_object  ` ](../subgrounds.plotly_wrappers/#subgrounds.plotly_wrappers.Choroplethmapbox.graph_object)
    * [ ` Densitymapbox  ` ](../subgrounds.plotly_wrappers/#subgrounds.plotly_wrappers.Densitymapbox)
      * [ ` Densitymapbox.graph_object  ` ](../subgrounds.plotly_wrappers/#subgrounds.plotly_wrappers.Densitymapbox.graph_object)
    * [ ` Scatterpolar  ` ](../subgrounds.plotly_wrappers/#subgrounds.plotly_wrappers.Scatterpolar)
      * [ ` Scatterpolar.graph_object  ` ](../subgrounds.plotly_wrappers/#subgrounds.plotly_wrappers.Scatterpolar.graph_object)
    * [ ` Barpolar  ` ](../subgrounds.plotly_wrappers/#subgrounds.plotly_wrappers.Barpolar)
      * [ ` Barpolar.graph_object  ` ](../subgrounds.plotly_wrappers/#subgrounds.plotly_wrappers.Barpolar.graph_object)
    * [ ` Sunburst  ` ](../subgrounds.plotly_wrappers/#subgrounds.plotly_wrappers.Sunburst)
      * [ ` Sunburst.graph_object  ` ](../subgrounds.plotly_wrappers/#subgrounds.plotly_wrappers.Sunburst.graph_object)
    * [ ` Treemap  ` ](../subgrounds.plotly_wrappers/#subgrounds.plotly_wrappers.Treemap)
      * [ ` Treemap.graph_object  ` ](../subgrounds.plotly_wrappers/#subgrounds.plotly_wrappers.Treemap.graph_object)
    * [ ` Icicle  ` ](../subgrounds.plotly_wrappers/#subgrounds.plotly_wrappers.Icicle)
      * [ ` Icicle.graph_object  ` ](../subgrounds.plotly_wrappers/#subgrounds.plotly_wrappers.Icicle.graph_object)
    * [ ` Sankey  ` ](../subgrounds.plotly_wrappers/#subgrounds.plotly_wrappers.Sankey)
      * [ ` Sankey.graph_object  ` ](../subgrounds.plotly_wrappers/#subgrounds.plotly_wrappers.Sankey.graph_object)
    * [ ` Parcoords  ` ](../subgrounds.plotly_wrappers/#subgrounds.plotly_wrappers.Parcoords)
      * [ ` Parcoords.graph_object  ` ](../subgrounds.plotly_wrappers/#subgrounds.plotly_wrappers.Parcoords.graph_object)
    * [ ` Parcats  ` ](../subgrounds.plotly_wrappers/#subgrounds.plotly_wrappers.Parcats)
      * [ ` Parcats.graph_object  ` ](../subgrounds.plotly_wrappers/#subgrounds.plotly_wrappers.Parcats.graph_object)
    * [ ` Carpet  ` ](../subgrounds.plotly_wrappers/#subgrounds.plotly_wrappers.Carpet)
      * [ ` Carpet.graph_object  ` ](../subgrounds.plotly_wrappers/#subgrounds.plotly_wrappers.Carpet.graph_object)
    * [ ` Scattercarpet  ` ](../subgrounds.plotly_wrappers/#subgrounds.plotly_wrappers.Scattercarpet)
      * [ ` Scattercarpet.graph_object  ` ](../subgrounds.plotly_wrappers/#subgrounds.plotly_wrappers.Scattercarpet.graph_object)
    * [ ` Contourcarpet  ` ](../subgrounds.plotly_wrappers/#subgrounds.plotly_wrappers.Contourcarpet)
      * [ ` Contourcarpet.graph_object  ` ](../subgrounds.plotly_wrappers/#subgrounds.plotly_wrappers.Contourcarpet.graph_object)
  * [ subgrounds.query module ](../subgrounds.query/)
    * [ ` InputValue  ` ](../subgrounds.query/#subgrounds.query.InputValue)
      * [ ` InputValue.T  ` ](../subgrounds.query/#subgrounds.query.InputValue.T)
        * [ ` InputValue.T.graphql  ` ](../subgrounds.query/#subgrounds.query.InputValue.T.graphql)
        * [ ` InputValue.T.is_variable  ` ](../subgrounds.query/#subgrounds.query.InputValue.T.is_variable)
        * [ ` InputValue.T.is_number  ` ](../subgrounds.query/#subgrounds.query.InputValue.T.is_number)
        * [ ` InputValue.T.iter()  ` ](../subgrounds.query/#subgrounds.query.InputValue.T.iter)
      * [ ` InputValue.Null  ` ](../subgrounds.query/#subgrounds.query.InputValue.Null)
        * [ ` InputValue.Null.graphql  ` ](../subgrounds.query/#subgrounds.query.InputValue.Null.graphql)
        * [ ` InputValue.Null.is_variable  ` ](../subgrounds.query/#subgrounds.query.InputValue.Null.is_variable)
        * [ ` InputValue.Null.is_number  ` ](../subgrounds.query/#subgrounds.query.InputValue.Null.is_number)
        * [ ` InputValue.Null.iter()  ` ](../subgrounds.query/#subgrounds.query.InputValue.Null.iter)
      * [ ` InputValue.Int  ` ](../subgrounds.query/#subgrounds.query.InputValue.Int)
        * [ ` InputValue.Int.value  ` ](../subgrounds.query/#subgrounds.query.InputValue.Int.value)
        * [ ` InputValue.Int.graphql  ` ](../subgrounds.query/#subgrounds.query.InputValue.Int.graphql)
        * [ ` InputValue.Int.is_variable  ` ](../subgrounds.query/#subgrounds.query.InputValue.Int.is_variable)
        * [ ` InputValue.Int.is_number  ` ](../subgrounds.query/#subgrounds.query.InputValue.Int.is_number)
        * [ ` InputValue.Int.iter()  ` ](../subgrounds.query/#subgrounds.query.InputValue.Int.iter)
      * [ ` InputValue.Float  ` ](../subgrounds.query/#subgrounds.query.InputValue.Float)
        * [ ` InputValue.Float.value  ` ](../subgrounds.query/#subgrounds.query.InputValue.Float.value)
        * [ ` InputValue.Float.graphql  ` ](../subgrounds.query/#subgrounds.query.InputValue.Float.graphql)
        * [ ` InputValue.Float.is_variable  ` ](../subgrounds.query/#subgrounds.query.InputValue.Float.is_variable)
        * [ ` InputValue.Float.is_number  ` ](../subgrounds.query/#subgrounds.query.InputValue.Float.is_number)
        * [ ` InputValue.Float.iter()  ` ](../subgrounds.query/#subgrounds.query.InputValue.Float.iter)
      * [ ` InputValue.String  ` ](../subgrounds.query/#subgrounds.query.InputValue.String)
        * [ ` InputValue.String.value  ` ](../subgrounds.query/#subgrounds.query.InputValue.String.value)
        * [ ` InputValue.String.graphql  ` ](../subgrounds.query/#subgrounds.query.InputValue.String.graphql)
        * [ ` InputValue.String.is_variable  ` ](../subgrounds.query/#subgrounds.query.InputValue.String.is_variable)
        * [ ` InputValue.String.is_number  ` ](../subgrounds.query/#subgrounds.query.InputValue.String.is_number)
        * [ ` InputValue.String.iter()  ` ](../subgrounds.query/#subgrounds.query.InputValue.String.iter)
      * [ ` InputValue.Boolean  ` ](../subgrounds.query/#subgrounds.query.InputValue.Boolean)
        * [ ` InputValue.Boolean.value  ` ](../subgrounds.query/#subgrounds.query.InputValue.Boolean.value)
        * [ ` InputValue.Boolean.graphql  ` ](../subgrounds.query/#subgrounds.query.InputValue.Boolean.graphql)
        * [ ` InputValue.Boolean.is_variable  ` ](../subgrounds.query/#subgrounds.query.InputValue.Boolean.is_variable)
        * [ ` InputValue.Boolean.is_number  ` ](../subgrounds.query/#subgrounds.query.InputValue.Boolean.is_number)
        * [ ` InputValue.Boolean.iter()  ` ](../subgrounds.query/#subgrounds.query.InputValue.Boolean.iter)
      * [ ` InputValue.Enum  ` ](../subgrounds.query/#subgrounds.query.InputValue.Enum)
        * [ ` InputValue.Enum.value  ` ](../subgrounds.query/#subgrounds.query.InputValue.Enum.value)
        * [ ` InputValue.Enum.graphql  ` ](../subgrounds.query/#subgrounds.query.InputValue.Enum.graphql)
        * [ ` InputValue.Enum.is_variable  ` ](../subgrounds.query/#subgrounds.query.InputValue.Enum.is_variable)
        * [ ` InputValue.Enum.is_number  ` ](../subgrounds.query/#subgrounds.query.InputValue.Enum.is_number)
        * [ ` InputValue.Enum.iter()  ` ](../subgrounds.query/#subgrounds.query.InputValue.Enum.iter)
      * [ ` InputValue.Variable  ` ](../subgrounds.query/#subgrounds.query.InputValue.Variable)
        * [ ` InputValue.Variable.name  ` ](../subgrounds.query/#subgrounds.query.InputValue.Variable.name)
        * [ ` InputValue.Variable.graphql  ` ](../subgrounds.query/#subgrounds.query.InputValue.Variable.graphql)
        * [ ` InputValue.Variable.is_variable  ` ](../subgrounds.query/#subgrounds.query.InputValue.Variable.is_variable)
        * [ ` InputValue.Variable.is_number  ` ](../subgrounds.query/#subgrounds.query.InputValue.Variable.is_number)
        * [ ` InputValue.Variable.iter()  ` ](../subgrounds.query/#subgrounds.query.InputValue.Variable.iter)
      * [ ` InputValue.List  ` ](../subgrounds.query/#subgrounds.query.InputValue.List)
        * [ ` InputValue.List.value  ` ](../subgrounds.query/#subgrounds.query.InputValue.List.value)
        * [ ` InputValue.List.graphql  ` ](../subgrounds.query/#subgrounds.query.InputValue.List.graphql)
        * [ ` InputValue.List.is_variable  ` ](../subgrounds.query/#subgrounds.query.InputValue.List.is_variable)
        * [ ` InputValue.List.is_number  ` ](../subgrounds.query/#subgrounds.query.InputValue.List.is_number)
        * [ ` InputValue.List.iter()  ` ](../subgrounds.query/#subgrounds.query.InputValue.List.iter)
      * [ ` InputValue.Object  ` ](../subgrounds.query/#subgrounds.query.InputValue.Object)
        * [ ` InputValue.Object.value  ` ](../subgrounds.query/#subgrounds.query.InputValue.Object.value)
        * [ ` InputValue.Object.graphql  ` ](../subgrounds.query/#subgrounds.query.InputValue.Object.graphql)
        * [ ` InputValue.Object.is_variable  ` ](../subgrounds.query/#subgrounds.query.InputValue.Object.is_variable)
        * [ ` InputValue.Object.is_number  ` ](../subgrounds.query/#subgrounds.query.InputValue.Object.is_number)
        * [ ` InputValue.Object.iter()  ` ](../subgrounds.query/#subgrounds.query.InputValue.Object.iter)
    * [ ` VariableDefinition  ` ](../subgrounds.query/#subgrounds.query.VariableDefinition)
      * [ ` VariableDefinition.name  ` ](../subgrounds.query/#subgrounds.query.VariableDefinition.name)
      * [ ` VariableDefinition.type_  ` ](../subgrounds.query/#subgrounds.query.VariableDefinition.type_)
      * [ ` VariableDefinition.default  ` ](../subgrounds.query/#subgrounds.query.VariableDefinition.default)
      * [ ` VariableDefinition.name  ` ](../subgrounds.query/#id0)
      * [ ` VariableDefinition.type_  ` ](../subgrounds.query/#id1)
      * [ ` VariableDefinition.default  ` ](../subgrounds.query/#id2)
      * [ ` VariableDefinition.graphql  ` ](../subgrounds.query/#subgrounds.query.VariableDefinition.graphql)
    * [ ` Argument  ` ](../subgrounds.query/#subgrounds.query.Argument)
      * [ ` Argument.name  ` ](../subgrounds.query/#subgrounds.query.Argument.name)
      * [ ` Argument.value  ` ](../subgrounds.query/#subgrounds.query.Argument.value)
      * [ ` Argument.graphql  ` ](../subgrounds.query/#subgrounds.query.Argument.graphql)
      * [ ` Argument.iter()  ` ](../subgrounds.query/#subgrounds.query.Argument.iter)
      * [ ` Argument.iter_vars()  ` ](../subgrounds.query/#subgrounds.query.Argument.iter_vars)
      * [ ` Argument.for_all()  ` ](../subgrounds.query/#subgrounds.query.Argument.for_all)
      * [ ` Argument.for_all_vars()  ` ](../subgrounds.query/#subgrounds.query.Argument.for_all_vars)
      * [ ` Argument.exists()  ` ](../subgrounds.query/#subgrounds.query.Argument.exists)
      * [ ` Argument.exists_vars()  ` ](../subgrounds.query/#subgrounds.query.Argument.exists_vars)
      * [ ` Argument.find()  ` ](../subgrounds.query/#subgrounds.query.Argument.find)
      * [ ` Argument.find_var()  ` ](../subgrounds.query/#subgrounds.query.Argument.find_var)
      * [ ` Argument.all_defined()  ` ](../subgrounds.query/#subgrounds.query.Argument.all_defined)
    * [ ` Selection  ` ](../subgrounds.query/#subgrounds.query.Selection)
      * [ ` Selection.fmeta  ` ](../subgrounds.query/#subgrounds.query.Selection.fmeta)
      * [ ` Selection.alias  ` ](../subgrounds.query/#subgrounds.query.Selection.alias)
      * [ ` Selection.arguments  ` ](../subgrounds.query/#subgrounds.query.Selection.arguments)
      * [ ` Selection.selection  ` ](../subgrounds.query/#subgrounds.query.Selection.selection)
      * [ ` Selection.fmeta  ` ](../subgrounds.query/#id3)
      * [ ` Selection.alias  ` ](../subgrounds.query/#id4)
      * [ ` Selection.arguments  ` ](../subgrounds.query/#id5)
      * [ ` Selection.selection  ` ](../subgrounds.query/#id6)
      * [ ` Selection.key  ` ](../subgrounds.query/#subgrounds.query.Selection.key)
      * [ ` Selection.args_graphql  ` ](../subgrounds.query/#subgrounds.query.Selection.args_graphql)
      * [ ` Selection.graphql()  ` ](../subgrounds.query/#subgrounds.query.Selection.graphql)
      * [ ` Selection.data_path  ` ](../subgrounds.query/#subgrounds.query.Selection.data_path)
      * [ ` Selection.data_paths  ` ](../subgrounds.query/#subgrounds.query.Selection.data_paths)
      * [ ` Selection.iter()  ` ](../subgrounds.query/#subgrounds.query.Selection.iter)
      * [ ` Selection.iter_args()  ` ](../subgrounds.query/#subgrounds.query.Selection.iter_args)
      * [ ` Selection.filter()  ` ](../subgrounds.query/#subgrounds.query.Selection.filter)
      * [ ` Selection.filter_args()  ` ](../subgrounds.query/#subgrounds.query.Selection.filter_args)
      * [ ` Selection.map()  ` ](../subgrounds.query/#subgrounds.query.Selection.map)
      * [ ` Selection.map_args()  ` ](../subgrounds.query/#subgrounds.query.Selection.map_args)
      * [ ` Selection.filter_map()  ` ](../subgrounds.query/#subgrounds.query.Selection.filter_map)
      * [ ` Selection.filter_map_args()  ` ](../subgrounds.query/#subgrounds.query.Selection.filter_map_args)
      * [ ` Selection.for_all()  ` ](../subgrounds.query/#subgrounds.query.Selection.for_all)
      * [ ` Selection.for_all_args()  ` ](../subgrounds.query/#subgrounds.query.Selection.for_all_args)
      * [ ` Selection.exists()  ` ](../subgrounds.query/#subgrounds.query.Selection.exists)
      * [ ` Selection.exists_args()  ` ](../subgrounds.query/#subgrounds.query.Selection.exists_args)
      * [ ` Selection.find()  ` ](../subgrounds.query/#subgrounds.query.Selection.find)
      * [ ` Selection.find_args()  ` ](../subgrounds.query/#subgrounds.query.Selection.find_args)
      * [ ` Selection.find_all()  ` ](../subgrounds.query/#subgrounds.query.Selection.find_all)
      * [ ` Selection.find_all_args()  ` ](../subgrounds.query/#subgrounds.query.Selection.find_all_args)
      * [ ` Selection.T  ` ](../subgrounds.query/#subgrounds.query.Selection.T)
      * [ ` Selection.fold()  ` ](../subgrounds.query/#subgrounds.query.Selection.fold)
      * [ ` Selection.contains_list()  ` ](../subgrounds.query/#subgrounds.query.Selection.contains_list)
      * [ ` Selection.split()  ` ](../subgrounds.query/#subgrounds.query.Selection.split)
      * [ ` Selection.extract_data()  ` ](../subgrounds.query/#subgrounds.query.Selection.extract_data)
      * [ ` Selection.add()  ` ](../subgrounds.query/#subgrounds.query.Selection.add)
      * [ ` Selection.remove()  ` ](../subgrounds.query/#subgrounds.query.Selection.remove)
      * [ ` Selection.variable_args()  ` ](../subgrounds.query/#subgrounds.query.Selection.variable_args)
      * [ ` Selection.infer_variable_definitions()  ` ](../subgrounds.query/#subgrounds.query.Selection.infer_variable_definitions)
      * [ ` Selection.combine()  ` ](../subgrounds.query/#subgrounds.query.Selection.combine)
      * [ ` Selection.merge()  ` ](../subgrounds.query/#subgrounds.query.Selection.merge)
      * [ ` Selection.contains()  ` ](../subgrounds.query/#subgrounds.query.Selection.contains)
      * [ ` Selection.contains_argument()  ` ](../subgrounds.query/#subgrounds.query.Selection.contains_argument)
      * [ ` Selection.get_argument()  ` ](../subgrounds.query/#subgrounds.query.Selection.get_argument)
      * [ ` Selection.get_argument_by_variable()  ` ](../subgrounds.query/#subgrounds.query.Selection.get_argument_by_variable)
      * [ ` Selection.substitute_arg()  ` ](../subgrounds.query/#subgrounds.query.Selection.substitute_arg)
      * [ ` Selection.select()  ` ](../subgrounds.query/#subgrounds.query.Selection.select)
      * [ ` Selection.prune_undefined()  ` ](../subgrounds.query/#subgrounds.query.Selection.prune_undefined)
    * [ ` Query  ` ](../subgrounds.query/#subgrounds.query.Query)
      * [ ` Query.name  ` ](../subgrounds.query/#subgrounds.query.Query.name)
      * [ ` Query.selection  ` ](../subgrounds.query/#subgrounds.query.Query.selection)
      * [ ` Query.variables  ` ](../subgrounds.query/#subgrounds.query.Query.variables)
      * [ ` Query.graphql  ` ](../subgrounds.query/#subgrounds.query.Query.graphql)
      * [ ` Query.iter()  ` ](../subgrounds.query/#subgrounds.query.Query.iter)
      * [ ` Query.iter_args()  ` ](../subgrounds.query/#subgrounds.query.Query.iter_args)
      * [ ` Query.iter_vardefs()  ` ](../subgrounds.query/#subgrounds.query.Query.iter_vardefs)
      * [ ` Query.filter()  ` ](../subgrounds.query/#subgrounds.query.Query.filter)
      * [ ` Query.filter_args()  ` ](../subgrounds.query/#subgrounds.query.Query.filter_args)
      * [ ` Query.filter_vardefs()  ` ](../subgrounds.query/#subgrounds.query.Query.filter_vardefs)
      * [ ` Query.map()  ` ](../subgrounds.query/#subgrounds.query.Query.map)
      * [ ` Query.map_args()  ` ](../subgrounds.query/#subgrounds.query.Query.map_args)
      * [ ` Query.map_vardefs()  ` ](../subgrounds.query/#subgrounds.query.Query.map_vardefs)
      * [ ` Query.filter_map()  ` ](../subgrounds.query/#subgrounds.query.Query.filter_map)
      * [ ` Query.filter_map_args()  ` ](../subgrounds.query/#subgrounds.query.Query.filter_map_args)
      * [ ` Query.filter_map_vardefs()  ` ](../subgrounds.query/#subgrounds.query.Query.filter_map_vardefs)
      * [ ` Query.for_all()  ` ](../subgrounds.query/#subgrounds.query.Query.for_all)
      * [ ` Query.for_all_args()  ` ](../subgrounds.query/#subgrounds.query.Query.for_all_args)
      * [ ` Query.for_all_vardefs()  ` ](../subgrounds.query/#subgrounds.query.Query.for_all_vardefs)
      * [ ` Query.exists()  ` ](../subgrounds.query/#subgrounds.query.Query.exists)
      * [ ` Query.exists_args()  ` ](../subgrounds.query/#subgrounds.query.Query.exists_args)
      * [ ` Query.exists_vardefs()  ` ](../subgrounds.query/#subgrounds.query.Query.exists_vardefs)
      * [ ` Query.find()  ` ](../subgrounds.query/#subgrounds.query.Query.find)
      * [ ` Query.find_args()  ` ](../subgrounds.query/#subgrounds.query.Query.find_args)
      * [ ` Query.find_vardefs()  ` ](../subgrounds.query/#subgrounds.query.Query.find_vardefs)
      * [ ` Query.T  ` ](../subgrounds.query/#subgrounds.query.Query.T)
      * [ ` Query.fold()  ` ](../subgrounds.query/#subgrounds.query.Query.fold)
      * [ ` Query.infer_variable_definitions()  ` ](../subgrounds.query/#subgrounds.query.Query.infer_variable_definitions)
      * [ ` Query.add()  ` ](../subgrounds.query/#subgrounds.query.Query.add)
      * [ ` Query.add_vardefs()  ` ](../subgrounds.query/#subgrounds.query.Query.add_vardefs)
      * [ ` Query.remove()  ` ](../subgrounds.query/#subgrounds.query.Query.remove)
      * [ ` Query.transform()  ` ](../subgrounds.query/#subgrounds.query.Query.transform)
      * [ ` Query.contains_selection()  ` ](../subgrounds.query/#subgrounds.query.Query.contains_selection)
      * [ ` Query.contains_argument()  ` ](../subgrounds.query/#subgrounds.query.Query.contains_argument)
      * [ ` Query.get_argument()  ` ](../subgrounds.query/#subgrounds.query.Query.get_argument)
      * [ ` Query.substitute_arg()  ` ](../subgrounds.query/#subgrounds.query.Query.substitute_arg)
      * [ ` Query.contains()  ` ](../subgrounds.query/#subgrounds.query.Query.contains)
      * [ ` Query.select()  ` ](../subgrounds.query/#subgrounds.query.Query.select)
      * [ ` Query.prune_undefined()  ` ](../subgrounds.query/#subgrounds.query.Query.prune_undefined)
    * [ ` Fragment  ` ](../subgrounds.query/#subgrounds.query.Fragment)
      * [ ` Fragment.name  ` ](../subgrounds.query/#subgrounds.query.Fragment.name)
      * [ ` Fragment.type_  ` ](../subgrounds.query/#subgrounds.query.Fragment.type_)
      * [ ` Fragment.selection  ` ](../subgrounds.query/#subgrounds.query.Fragment.selection)
      * [ ` Fragment.variables  ` ](../subgrounds.query/#subgrounds.query.Fragment.variables)
      * [ ` Fragment.graphql  ` ](../subgrounds.query/#subgrounds.query.Fragment.graphql)
      * [ ` Fragment.combine()  ` ](../subgrounds.query/#subgrounds.query.Fragment.combine)
      * [ ` Fragment.transform()  ` ](../subgrounds.query/#subgrounds.query.Fragment.transform)
    * [ ` Document  ` ](../subgrounds.query/#subgrounds.query.Document)
      * [ ` Document.url  ` ](../subgrounds.query/#subgrounds.query.Document.url)
      * [ ` Document.query  ` ](../subgrounds.query/#subgrounds.query.Document.query)
      * [ ` Document.fragments  ` ](../subgrounds.query/#subgrounds.query.Document.fragments)
      * [ ` Document.variables  ` ](../subgrounds.query/#subgrounds.query.Document.variables)
      * [ ` Document.graphql  ` ](../subgrounds.query/#subgrounds.query.Document.graphql)
      * [ ` Document.mk_single_query()  ` ](../subgrounds.query/#subgrounds.query.Document.mk_single_query)
      * [ ` Document.filter()  ` ](../subgrounds.query/#subgrounds.query.Document.filter)
      * [ ` Document.filter_args()  ` ](../subgrounds.query/#subgrounds.query.Document.filter_args)
      * [ ` Document.map()  ` ](../subgrounds.query/#subgrounds.query.Document.map)
      * [ ` Document.map_args()  ` ](../subgrounds.query/#subgrounds.query.Document.map_args)
      * [ ` Document.filter_map()  ` ](../subgrounds.query/#subgrounds.query.Document.filter_map)
      * [ ` Document.combine()  ` ](../subgrounds.query/#subgrounds.query.Document.combine)
      * [ ` Document.transform()  ` ](../subgrounds.query/#subgrounds.query.Document.transform)
      * [ ` Document.prune_undefined()  ` ](../subgrounds.query/#subgrounds.query.Document.prune_undefined)
    * [ ` DataRequest  ` ](../subgrounds.query/#subgrounds.query.DataRequest)
      * [ ` DataRequest.documents  ` ](../subgrounds.query/#subgrounds.query.DataRequest.documents)
      * [ ` DataRequest.graphql  ` ](../subgrounds.query/#subgrounds.query.DataRequest.graphql)
      * [ ` DataRequest.combine()  ` ](../subgrounds.query/#subgrounds.query.DataRequest.combine)
      * [ ` DataRequest.transform()  ` ](../subgrounds.query/#subgrounds.query.DataRequest.transform)
      * [ ` DataRequest.single_query()  ` ](../subgrounds.query/#subgrounds.query.DataRequest.single_query)
      * [ ` DataRequest.single_document()  ` ](../subgrounds.query/#subgrounds.query.DataRequest.single_document)
      * [ ` DataRequest.add_documents()  ` ](../subgrounds.query/#subgrounds.query.DataRequest.add_documents)
    * [ ` selections_of_object()  ` ](../subgrounds.query/#subgrounds.query.selections_of_object)
    * [ ` input_value_of_argument()  ` ](../subgrounds.query/#subgrounds.query.input_value_of_argument)
    * [ ` arguments_of_field_args()  ` ](../subgrounds.query/#subgrounds.query.arguments_of_field_args)
  * [ subgrounds.schema module ](../subgrounds.schema/)
    * [ ` BaseModel  ` ](../subgrounds.schema/#subgrounds.schema.BaseModel)
      * [ ` BaseModel.Config  ` ](../subgrounds.schema/#subgrounds.schema.BaseModel.Config)
        * [ ` BaseModel.Config.allow_population_by_field_name  ` ](../subgrounds.schema/#subgrounds.schema.BaseModel.Config.allow_population_by_field_name)
    * [ ` TypeRef  ` ](../subgrounds.schema/#subgrounds.schema.TypeRef)
      * [ ` TypeRef.T  ` ](../subgrounds.schema/#subgrounds.schema.TypeRef.T)
        * [ ` TypeRef.T.name  ` ](../subgrounds.schema/#subgrounds.schema.TypeRef.T.name)
        * [ ` TypeRef.T.is_list  ` ](../subgrounds.schema/#subgrounds.schema.TypeRef.T.is_list)
        * [ ` TypeRef.T.is_non_null  ` ](../subgrounds.schema/#subgrounds.schema.TypeRef.T.is_non_null)
      * [ ` TypeRef.Named  ` ](../subgrounds.schema/#subgrounds.schema.TypeRef.Named)
        * [ ` TypeRef.Named.name_  ` ](../subgrounds.schema/#subgrounds.schema.TypeRef.Named.name_)
        * [ ` TypeRef.Named.kind  ` ](../subgrounds.schema/#subgrounds.schema.TypeRef.Named.kind)
        * [ ` TypeRef.Named.name  ` ](../subgrounds.schema/#subgrounds.schema.TypeRef.Named.name)
      * [ ` TypeRef.NonNull  ` ](../subgrounds.schema/#subgrounds.schema.TypeRef.NonNull)
        * [ ` TypeRef.NonNull.inner  ` ](../subgrounds.schema/#subgrounds.schema.TypeRef.NonNull.inner)
        * [ ` TypeRef.NonNull.kind  ` ](../subgrounds.schema/#subgrounds.schema.TypeRef.NonNull.kind)
        * [ ` TypeRef.NonNull.name  ` ](../subgrounds.schema/#subgrounds.schema.TypeRef.NonNull.name)
        * [ ` TypeRef.NonNull.is_list  ` ](../subgrounds.schema/#subgrounds.schema.TypeRef.NonNull.is_list)
        * [ ` TypeRef.NonNull.is_non_null  ` ](../subgrounds.schema/#subgrounds.schema.TypeRef.NonNull.is_non_null)
      * [ ` TypeRef.List  ` ](../subgrounds.schema/#subgrounds.schema.TypeRef.List)
        * [ ` TypeRef.List.inner  ` ](../subgrounds.schema/#subgrounds.schema.TypeRef.List.inner)
        * [ ` TypeRef.List.kind  ` ](../subgrounds.schema/#subgrounds.schema.TypeRef.List.kind)
        * [ ` TypeRef.List.name  ` ](../subgrounds.schema/#subgrounds.schema.TypeRef.List.name)
        * [ ` TypeRef.List.is_list  ` ](../subgrounds.schema/#subgrounds.schema.TypeRef.List.is_list)
        * [ ` TypeRef.List.is_non_null  ` ](../subgrounds.schema/#subgrounds.schema.TypeRef.List.is_non_null)
      * [ ` TypeRef.non_null()  ` ](../subgrounds.schema/#subgrounds.schema.TypeRef.non_null)
      * [ ` TypeRef.non_null_list()  ` ](../subgrounds.schema/#subgrounds.schema.TypeRef.non_null_list)
      * [ ` TypeRef.root_type_name()  ` ](../subgrounds.schema/#subgrounds.schema.TypeRef.root_type_name)
      * [ ` TypeRef.is_non_null()  ` ](../subgrounds.schema/#subgrounds.schema.TypeRef.is_non_null)
      * [ ` TypeRef.is_list()  ` ](../subgrounds.schema/#subgrounds.schema.TypeRef.is_list)
      * [ ` TypeRef.graphql()  ` ](../subgrounds.schema/#subgrounds.schema.TypeRef.graphql)
    * [ ` TypeMeta  ` ](../subgrounds.schema/#subgrounds.schema.TypeMeta)
      * [ ` TypeMeta.T  ` ](../subgrounds.schema/#subgrounds.schema.TypeMeta.T)
        * [ ` TypeMeta.T.name  ` ](../subgrounds.schema/#subgrounds.schema.TypeMeta.T.name)
        * [ ` TypeMeta.T.description  ` ](../subgrounds.schema/#subgrounds.schema.TypeMeta.T.description)
        * [ ` TypeMeta.T.is_object  ` ](../subgrounds.schema/#subgrounds.schema.TypeMeta.T.is_object)
      * [ ` TypeMeta.ArgumentMeta  ` ](../subgrounds.schema/#subgrounds.schema.TypeMeta.ArgumentMeta)
        * [ ` TypeMeta.ArgumentMeta.type_  ` ](../subgrounds.schema/#subgrounds.schema.TypeMeta.ArgumentMeta.type_)
        * [ ` TypeMeta.ArgumentMeta.default_value  ` ](../subgrounds.schema/#subgrounds.schema.TypeMeta.ArgumentMeta.default_value)
      * [ ` TypeMeta.FieldMeta  ` ](../subgrounds.schema/#subgrounds.schema.TypeMeta.FieldMeta)
        * [ ` TypeMeta.FieldMeta.arguments  ` ](../subgrounds.schema/#subgrounds.schema.TypeMeta.FieldMeta.arguments)
        * [ ` TypeMeta.FieldMeta.type_  ` ](../subgrounds.schema/#subgrounds.schema.TypeMeta.FieldMeta.type_)
        * [ ` TypeMeta.FieldMeta.has_arg()  ` ](../subgrounds.schema/#subgrounds.schema.TypeMeta.FieldMeta.has_arg)
        * [ ` TypeMeta.FieldMeta.type_of_arg()  ` ](../subgrounds.schema/#subgrounds.schema.TypeMeta.FieldMeta.type_of_arg)
      * [ ` TypeMeta.ScalarMeta  ` ](../subgrounds.schema/#subgrounds.schema.TypeMeta.ScalarMeta)
        * [ ` TypeMeta.ScalarMeta.kind  ` ](../subgrounds.schema/#subgrounds.schema.TypeMeta.ScalarMeta.kind)
      * [ ` TypeMeta.ObjectMeta  ` ](../subgrounds.schema/#subgrounds.schema.TypeMeta.ObjectMeta)
        * [ ` TypeMeta.ObjectMeta.kind  ` ](../subgrounds.schema/#subgrounds.schema.TypeMeta.ObjectMeta.kind)
        * [ ` TypeMeta.ObjectMeta.fields  ` ](../subgrounds.schema/#subgrounds.schema.TypeMeta.ObjectMeta.fields)
        * [ ` TypeMeta.ObjectMeta.interfaces_  ` ](../subgrounds.schema/#subgrounds.schema.TypeMeta.ObjectMeta.interfaces_)
        * [ ` TypeMeta.ObjectMeta.interfaces  ` ](../subgrounds.schema/#subgrounds.schema.TypeMeta.ObjectMeta.interfaces)
        * [ ` TypeMeta.ObjectMeta.is_object  ` ](../subgrounds.schema/#subgrounds.schema.TypeMeta.ObjectMeta.is_object)
        * [ ` TypeMeta.ObjectMeta.field()  ` ](../subgrounds.schema/#subgrounds.schema.TypeMeta.ObjectMeta.field)
        * [ ` TypeMeta.ObjectMeta.type_of_field()  ` ](../subgrounds.schema/#subgrounds.schema.TypeMeta.ObjectMeta.type_of_field)
      * [ ` TypeMeta.EnumValueMeta  ` ](../subgrounds.schema/#subgrounds.schema.TypeMeta.EnumValueMeta)
      * [ ` TypeMeta.EnumMeta  ` ](../subgrounds.schema/#subgrounds.schema.TypeMeta.EnumMeta)
        * [ ` TypeMeta.EnumMeta.kind  ` ](../subgrounds.schema/#subgrounds.schema.TypeMeta.EnumMeta.kind)
        * [ ` TypeMeta.EnumMeta.values  ` ](../subgrounds.schema/#subgrounds.schema.TypeMeta.EnumMeta.values)
      * [ ` TypeMeta.InterfaceMeta  ` ](../subgrounds.schema/#subgrounds.schema.TypeMeta.InterfaceMeta)
        * [ ` TypeMeta.InterfaceMeta.kind  ` ](../subgrounds.schema/#subgrounds.schema.TypeMeta.InterfaceMeta.kind)
        * [ ` TypeMeta.InterfaceMeta.fields  ` ](../subgrounds.schema/#subgrounds.schema.TypeMeta.InterfaceMeta.fields)
        * [ ` TypeMeta.InterfaceMeta.is_object  ` ](../subgrounds.schema/#subgrounds.schema.TypeMeta.InterfaceMeta.is_object)
        * [ ` TypeMeta.InterfaceMeta.field()  ` ](../subgrounds.schema/#subgrounds.schema.TypeMeta.InterfaceMeta.field)
      * [ ` TypeMeta.UnionMeta  ` ](../subgrounds.schema/#subgrounds.schema.TypeMeta.UnionMeta)
        * [ ` TypeMeta.UnionMeta.kind  ` ](../subgrounds.schema/#subgrounds.schema.TypeMeta.UnionMeta.kind)
        * [ ` TypeMeta.UnionMeta.types  ` ](../subgrounds.schema/#subgrounds.schema.TypeMeta.UnionMeta.types)
      * [ ` TypeMeta.InputObjectMeta  ` ](../subgrounds.schema/#subgrounds.schema.TypeMeta.InputObjectMeta)
        * [ ` TypeMeta.InputObjectMeta.kind  ` ](../subgrounds.schema/#subgrounds.schema.TypeMeta.InputObjectMeta.kind)
        * [ ` TypeMeta.InputObjectMeta.input_fields  ` ](../subgrounds.schema/#subgrounds.schema.TypeMeta.InputObjectMeta.input_fields)
        * [ ` TypeMeta.InputObjectMeta.type_of_input_field()  ` ](../subgrounds.schema/#subgrounds.schema.TypeMeta.InputObjectMeta.type_of_input_field)
    * [ ` SchemaMeta  ` ](../subgrounds.schema/#subgrounds.schema.SchemaMeta)
      * [ ` SchemaMeta.query_type_  ` ](../subgrounds.schema/#subgrounds.schema.SchemaMeta.query_type_)
      * [ ` SchemaMeta.types  ` ](../subgrounds.schema/#subgrounds.schema.SchemaMeta.types)
      * [ ` SchemaMeta.type_map  ` ](../subgrounds.schema/#subgrounds.schema.SchemaMeta.type_map)
      * [ ` SchemaMeta.mutation_type_  ` ](../subgrounds.schema/#subgrounds.schema.SchemaMeta.mutation_type_)
      * [ ` SchemaMeta.subscription_type_  ` ](../subgrounds.schema/#subgrounds.schema.SchemaMeta.subscription_type_)
      * [ ` SchemaMeta.query_type  ` ](../subgrounds.schema/#subgrounds.schema.SchemaMeta.query_type)
      * [ ` SchemaMeta.mutation_type  ` ](../subgrounds.schema/#subgrounds.schema.SchemaMeta.mutation_type)
      * [ ` SchemaMeta.subscription_type  ` ](../subgrounds.schema/#subgrounds.schema.SchemaMeta.subscription_type)
      * [ ` SchemaMeta.type_map_generator()  ` ](../subgrounds.schema/#subgrounds.schema.SchemaMeta.type_map_generator)
      * [ ` SchemaMeta.type_of_typeref()  ` ](../subgrounds.schema/#subgrounds.schema.SchemaMeta.type_of_typeref)
      * [ ` SchemaMeta.type_of()  ` ](../subgrounds.schema/#subgrounds.schema.SchemaMeta.type_of)
      * [ ` SchemaMeta.type_of_input_object_meta()  ` ](../subgrounds.schema/#subgrounds.schema.SchemaMeta.type_of_input_object_meta)
  * [ subgrounds.subgrounds module ](../subgrounds.subgrounds/)
    * [ ` store_schema()  ` ](../subgrounds.subgrounds/#subgrounds.subgrounds.store_schema)
    * [ ` load_schema()  ` ](../subgrounds.subgrounds/#subgrounds.subgrounds.load_schema)
    * [ ` subgraph_slug()  ` ](../subgrounds.subgrounds/#subgrounds.subgrounds.subgraph_slug)
    * [ ` Subgrounds  ` ](../subgrounds.subgrounds/#subgrounds.subgrounds.Subgrounds)
      * [ ` Subgrounds.headers  ` ](../subgrounds.subgrounds/#subgrounds.subgrounds.Subgrounds.headers)
      * [ ` Subgrounds.global_transforms  ` ](../subgrounds.subgrounds/#subgrounds.subgrounds.Subgrounds.global_transforms)
      * [ ` Subgrounds.subgraphs  ` ](../subgrounds.subgrounds/#subgrounds.subgrounds.Subgrounds.subgraphs)
      * [ ` Subgrounds.from_pg_key()  ` ](../subgrounds.subgrounds/#subgrounds.subgrounds.Subgrounds.from_pg_key)
      * [ ` Subgrounds.load()  ` ](../subgrounds.subgrounds/#subgrounds.subgrounds.Subgrounds.load)
      * [ ` Subgrounds.load_subgraph()  ` ](../subgrounds.subgrounds/#subgrounds.subgrounds.Subgrounds.load_subgraph)
      * [ ` Subgrounds.load_api()  ` ](../subgrounds.subgrounds/#subgrounds.subgrounds.Subgrounds.load_api)
      * [ ` Subgrounds.mk_request()  ` ](../subgrounds.subgrounds/#subgrounds.subgrounds.Subgrounds.mk_request)
      * [ ` Subgrounds.execute()  ` ](../subgrounds.subgrounds/#subgrounds.subgrounds.Subgrounds.execute)
      * [ ` Subgrounds.execute_iter()  ` ](../subgrounds.subgrounds/#subgrounds.subgrounds.Subgrounds.execute_iter)
      * [ ` Subgrounds.query_json()  ` ](../subgrounds.subgrounds/#subgrounds.subgrounds.Subgrounds.query_json)
      * [ ` Subgrounds.query_json_iter()  ` ](../subgrounds.subgrounds/#subgrounds.subgrounds.Subgrounds.query_json_iter)
      * [ ` Subgrounds.query_df()  ` ](../subgrounds.subgrounds/#subgrounds.subgrounds.Subgrounds.query_df)
      * [ ` Subgrounds.query_df_iter()  ` ](../subgrounds.subgrounds/#subgrounds.subgrounds.Subgrounds.query_df_iter)
      * [ ` Subgrounds.query()  ` ](../subgrounds.subgrounds/#subgrounds.subgrounds.Subgrounds.query)
      * [ ` Subgrounds.query_iter()  ` ](../subgrounds.subgrounds/#subgrounds.subgrounds.Subgrounds.query_iter)
  * [ subgrounds.transform module ](../subgrounds.transform/)
    * [ ` select_data()  ` ](../subgrounds.transform/#subgrounds.transform.select_data)
    * [ ` RequestTransform  ` ](../subgrounds.transform/#subgrounds.transform.RequestTransform)
      * [ ` RequestTransform.transform_request()  ` ](../subgrounds.transform/#subgrounds.transform.RequestTransform.transform_request)
      * [ ` RequestTransform.transform_response()  ` ](../subgrounds.transform/#subgrounds.transform.RequestTransform.transform_response)
    * [ ` DocumentTransform  ` ](../subgrounds.transform/#subgrounds.transform.DocumentTransform)
      * [ ` DocumentTransform.transform_document()  ` ](../subgrounds.transform/#subgrounds.transform.DocumentTransform.transform_document)
      * [ ` DocumentTransform.transform_response()  ` ](../subgrounds.transform/#subgrounds.transform.DocumentTransform.transform_response)
    * [ ` TypeTransform  ` ](../subgrounds.transform/#subgrounds.transform.TypeTransform)
      * [ ` TypeTransform.type_  ` ](../subgrounds.transform/#subgrounds.transform.TypeTransform.type_)
      * [ ` TypeTransform.f  ` ](../subgrounds.transform/#subgrounds.transform.TypeTransform.f)
      * [ ` TypeTransform.type_  ` ](../subgrounds.transform/#id0)
      * [ ` TypeTransform.f  ` ](../subgrounds.transform/#id1)
      * [ ` TypeTransform.transform_document()  ` ](../subgrounds.transform/#subgrounds.transform.TypeTransform.transform_document)
      * [ ` TypeTransform.transform_response()  ` ](../subgrounds.transform/#subgrounds.transform.TypeTransform.transform_response)
    * [ ` LocalSyntheticField  ` ](../subgrounds.transform/#subgrounds.transform.LocalSyntheticField)
      * [ ` LocalSyntheticField.subgraph  ` ](../subgrounds.transform/#subgrounds.transform.LocalSyntheticField.subgraph)
      * [ ` LocalSyntheticField.fmeta  ` ](../subgrounds.transform/#subgrounds.transform.LocalSyntheticField.fmeta)
      * [ ` LocalSyntheticField.type_  ` ](../subgrounds.transform/#subgrounds.transform.LocalSyntheticField.type_)
      * [ ` LocalSyntheticField.f  ` ](../subgrounds.transform/#subgrounds.transform.LocalSyntheticField.f)
      * [ ` LocalSyntheticField.default  ` ](../subgrounds.transform/#subgrounds.transform.LocalSyntheticField.default)
      * [ ` LocalSyntheticField.args  ` ](../subgrounds.transform/#subgrounds.transform.LocalSyntheticField.args)
      * [ ` LocalSyntheticField.subgraph  ` ](../subgrounds.transform/#id2)
      * [ ` LocalSyntheticField.fmeta  ` ](../subgrounds.transform/#id3)
      * [ ` LocalSyntheticField.type_  ` ](../subgrounds.transform/#id4)
      * [ ` LocalSyntheticField.f  ` ](../subgrounds.transform/#id5)
      * [ ` LocalSyntheticField.default  ` ](../subgrounds.transform/#id6)
      * [ ` LocalSyntheticField.args  ` ](../subgrounds.transform/#id7)
      * [ ` LocalSyntheticField.transform_document()  ` ](../subgrounds.transform/#subgrounds.transform.LocalSyntheticField.transform_document)
      * [ ` LocalSyntheticField.transform_response()  ` ](../subgrounds.transform/#subgrounds.transform.LocalSyntheticField.transform_response)
    * [ ` SplitTransform  ` ](../subgrounds.transform/#subgrounds.transform.SplitTransform)
      * [ ` SplitTransform.transform_request()  ` ](../subgrounds.transform/#subgrounds.transform.SplitTransform.transform_request)
      * [ ` SplitTransform.transform_response()  ` ](../subgrounds.transform/#subgrounds.transform.SplitTransform.transform_response)
  * [ subgrounds.utils module ](../subgrounds.utils/)
    * [ ` flatten()  ` ](../subgrounds.utils/#subgrounds.utils.flatten)
    * [ ` identity()  ` ](../subgrounds.utils/#subgrounds.utils.identity)
    * [ ` fst()  ` ](../subgrounds.utils/#subgrounds.utils.fst)
    * [ ` snd()  ` ](../subgrounds.utils/#subgrounds.utils.snd)
    * [ ` intersection()  ` ](../subgrounds.utils/#subgrounds.utils.intersection)
    * [ ` rel_complement()  ` ](../subgrounds.utils/#subgrounds.utils.rel_complement)
    * [ ` sym_diff()  ` ](../subgrounds.utils/#subgrounds.utils.sym_diff)
    * [ ` union()  ` ](../subgrounds.utils/#subgrounds.utils.union)
    * [ ` filter_none()  ` ](../subgrounds.utils/#subgrounds.utils.filter_none)
    * [ ` loop_generator()  ` ](../subgrounds.utils/#subgrounds.utils.loop_generator)
    * [ ` repeat()  ` ](../subgrounds.utils/#subgrounds.utils.repeat)
    * [ ` extract_data()  ` ](../subgrounds.utils/#subgrounds.utils.extract_data)
    * [ ` flatten_dict()  ` ](../subgrounds.utils/#subgrounds.utils.flatten_dict)
    * [ ` contains_list()  ` ](../subgrounds.utils/#subgrounds.utils.contains_list)
    * [ ` default_header()  ` ](../subgrounds.utils/#subgrounds.utils.default_header)
    * [ ` user_agent()  ` ](../subgrounds.utils/#subgrounds.utils.user_agent)

##  Module contents  #

_ class  _ subgrounds.  FieldPath  (  _ subgraph  :  'Subgraph'  _ , _
root_type  :  'TypeRef.T'  _ , _ type_  :  'TypeRef.T'  _ , _ path  :
'list[Tuple[Optional[dict[str,  Any]],  TypeMeta.FieldMeta]]'  _ )  #

    

Bases: [ ` FieldOperatorMixin  `
](../subgrounds.subgraph.fieldpath/#subgrounds.subgraph.fieldpath.FieldOperatorMixin
"subgrounds.subgraph.fieldpath.FieldOperatorMixin")

_ class  _ subgrounds.  Subgraph  (  _ url:  'str',  schema:  'SchemaMeta',
transforms:  'list[DocumentTransform]'  =
[<subgrounds.transform.TypeTransform  object  at  0x7f4e4c37f850>,
<subgrounds.transform.TypeTransform  object  at  0x7f4e4c37e5c0>],
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
](../subgrounds.transform/#subgrounds.transform.RequestTransform
"subgrounds.transform.RequestTransform") ]  _ #

    

subgraphs  _ :  [ dict  ](https://docs.python.org/3/library/stdtypes.html#dict
"\(in Python v3.11\)") [  [ str
](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.11\)") ,
[ subgrounds.subgraph.subgraph.Subgraph
](../subgrounds.subgraph.subgraph/#subgrounds.subgraph.subgraph.Subgraph
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

    

[ DataRequest ](../subgrounds.query/#subgrounds.query.DataRequest
"subgrounds.query.DataRequest")

execute  (  _ req  _ , _ pagination_strategy=<class
'subgrounds.pagination.strategies.LegacyStrategy'> _ )  #

    

Executes a ` DataRequest  ` object, sending the underlying query(ies) to the
server and returning a data blob (list of Python dictionaries, one per actual
query).

Parameters  :

    

  * **req** ( [ _DataRequest_ ](../subgrounds.query/#subgrounds.query.DataRequest "subgrounds.query.DataRequest") ) -- The ` DataRequest  ` object to be executed 

  * **pagination_strategy** ( _Optional_ _[_ _Type_ _[_ [ _PaginationStrategy_ ](../subgrounds.pagination/#subgrounds.pagination.PaginationStrategy "subgrounds.pagination.PaginationStrategy") _]_ _]_ _,_ _optional_ ) -- A Class implementing the ` PaginationStrategy  ` ` Protocol  ` . If ` None  ` , then automatic pagination is disabled. Defaults to ` LegacyStrategy  ` . 

Returns  :

    

The reponse data

Return type  :

    

[ list ](https://docs.python.org/3/library/stdtypes.html#list "\(in Python
v3.11\)") [ [ dict ](https://docs.python.org/3/library/stdtypes.html#dict
"\(in Python v3.11\)") ]

execute_iter  (  _ req  _ , _ pagination_strategy=<class
'subgrounds.pagination.strategies.LegacyStrategy'> _ )  #

    

Same as  execute  , except that an iterator is returned which will iterate the
data pages.

Parameters  :

    

  * **req** ( [ _DataRequest_ ](../subgrounds.query/#subgrounds.query.DataRequest "subgrounds.query.DataRequest") ) -- The ` DataRequest  ` object to be executed 

  * **pagination_strategy** ( _Optional_ _[_ _Type_ _[_ [ _PaginationStrategy_ ](../subgrounds.pagination/#subgrounds.pagination.PaginationStrategy "subgrounds.pagination.PaginationStrategy") _]_ _]_ _,_ _optional_ ) -- A Class implementing the ` PaginationStrategy  ` ` Protocol  ` . If ` None  ` , then automatic pagination is disabled. Defaults to ` LegacyStrategy  ` . 

Returns  :

    

An iterator over the reponse data pages

Return type  :

    

Iterator[ [ dict ](https://docs.python.org/3/library/stdtypes.html#dict "\(in
Python v3.11\)") ]

query_json  (  _ fpaths  _ , _ pagination_strategy=<class
'subgrounds.pagination.strategies.LegacyStrategy'> _ )  #

    

Equivalent to ` Subgrounds.execute(Subgrounds.mk_request(fpaths),
pagination_strategy)  ` .

Parameters  :

    

  * **fpaths** (  _FieldPath_ _|_ [ _list_ ](https://docs.python.org/3/library/stdtypes.html#list "\(in Python v3.11\)") _[_ _FieldPath_ _]_ ) -- One or more  ` FieldPath  ` objects that should be included in the request. 

  * **pagination_strategy** ( _Optional_ _[_ _Type_ _[_ [ _PaginationStrategy_ ](../subgrounds.pagination/#subgrounds.pagination.PaginationStrategy "subgrounds.pagination.PaginationStrategy") _]_ _]_ _,_ _optional_ ) -- A Class implementing the ` PaginationStrategy  ` ` Protocol  ` . If ` None  ` , then automatic pagination is disabled. Defaults to ` LegacyStrategy  ` . 

Returns  :

    

The reponse data

Return type  :

    

[ list ](https://docs.python.org/3/library/stdtypes.html#list "\(in Python
v3.11\)") [ [ dict ](https://docs.python.org/3/library/stdtypes.html#dict
"\(in Python v3.11\)") [ [ str
](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.11\)") ,
Any]]

query_json_iter  (  _ fpaths  _ , _ pagination_strategy=<class
'subgrounds.pagination.strategies.LegacyStrategy'> _ )  #

    

Same as  query_json  except an iterator over the response data pages is
returned.

Parameters  :

    

  * **fpaths** (  _FieldPath_ _|_ [ _list_ ](https://docs.python.org/3/library/stdtypes.html#list "\(in Python v3.11\)") _[_ _FieldPath_ _]_ ) -- One or more  ` FieldPath  ` objects that should be included in the request. 

  * **pagination_strategy** ( _Optional_ _[_ _Type_ _[_ [ _PaginationStrategy_ ](../subgrounds.pagination/#subgrounds.pagination.PaginationStrategy "subgrounds.pagination.PaginationStrategy") _]_ _]_ _,_ _optional_ ) -- A Class implementing the ` PaginationStrategy  ` ` Protocol  ` . If ` None  ` , then automatic pagination is disabled. Defaults to ` LegacyStrategy  ` . 

Returns  :

    

The reponse data

Return type  :

    

[ list ](https://docs.python.org/3/library/stdtypes.html#list "\(in Python
v3.11\)") [ [ dict ](https://docs.python.org/3/library/stdtypes.html#dict
"\(in Python v3.11\)") [ [ str
](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.11\)") ,
Any]]

query_df  (  _ fpaths  _ , _ columns=None  _ , _ concat=False  _ , _
pagination_strategy=<class  'subgrounds.pagination.strategies.LegacyStrategy'>
_ )  #

    

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

  * **pagination_strategy** ( _Optional_ _[_ _Type_ _[_ [ _PaginationStrategy_ ](../subgrounds.pagination/#subgrounds.pagination.PaginationStrategy "subgrounds.pagination.PaginationStrategy") _]_ _]_ _,_ _optional_ ) -- A Class implementing the ` PaginationStrategy  ` ` Protocol  ` . If ` None  ` , then automatic pagination is disabled. Defaults to ` LegacyStrategy  ` . 

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
    

query_df_iter  (  _ fpaths  _ , _ pagination_strategy=<class
'subgrounds.pagination.strategies.LegacyStrategy'> _ )  #

    

Same as  query_df  except an iterator over the response data pages is returned
:param fpaths: One or more  FieldPath  objects that

> should be included in the request

Parameters  :

    

  * **columns** ( _Optional_ _[_ [ _list_ ](https://docs.python.org/3/library/stdtypes.html#list "\(in Python v3.11\)") _[_ [ _str_ ](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.11\)") _]_ _]_ _,_ _optional_ ) -- The column labels. Defaults to None. 

  * **merge** ( [ _bool_ ](https://docs.python.org/3/library/functions.html#bool "\(in Python v3.11\)") _,_ _optional_ ) -- Whether or not to merge resulting dataframes. 

  * **pagination_strategy** ( _Optional_ _[_ _Type_ _[_ [ _PaginationStrategy_ ](../subgrounds.pagination/#subgrounds.pagination.PaginationStrategy "subgrounds.pagination.PaginationStrategy") _]_ _]_ _,_ _optional_ ) -- A Class implementing the ` PaginationStrategy  ` ` Protocol  ` . If ` None  ` , then automatic pagination is disabled. Defaults to ` LegacyStrategy  ` . 

Returns  :

    

An iterator over the response data pages, each as a DataFrame

Return type  :

    

Iterator[pd.DataFrame]

query  (  _ fpaths  _ , _ unwrap=True  _ , _ pagination_strategy=<class
'subgrounds.pagination.strategies.LegacyStrategy'> _ )  #

    

Executes one or multiple ` FieldPath  ` objects immediately and return the
data (as a tuple if multiple ` FieldPath  ` objects are provided).

Parameters  :

    

  * **fpaths** (  _FieldPath_ _|_ [ _list_ ](https://docs.python.org/3/library/stdtypes.html#list "\(in Python v3.11\)") _[_ _FieldPath_ _]_ ) -- One or more ` FieldPath  ` object(s) to query. 

  * **unwrap** ( [ _bool_ ](https://docs.python.org/3/library/functions.html#bool "\(in Python v3.11\)") _,_ _optional_ ) -- Flag indicating whether or not, in the case where the returned data is a list of one element, the element itself should be returned instead of the list. Defaults to ` True  ` . 

  * **pagination_strategy** ( _Optional_ _[_ _Type_ _[_ [ _PaginationStrategy_ ](../subgrounds.pagination/#subgrounds.pagination.PaginationStrategy "subgrounds.pagination.PaginationStrategy") _]_ _]_ _,_ _optional_ ) -- A Class implementing the ` PaginationStrategy  ` ` Protocol  ` . If ` None  ` , then automatic pagination is disabled. Defaults to ` LegacyStrategy  ` . 

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
    

query_iter  (  _ fpaths  _ , _ unwrap=True  _ , _ pagination_strategy=<class
'subgrounds.pagination.strategies.LegacyStrategy'> _ )  #

    

Same as  query  except an iterator over the resonse data pages is returned.

Parameters  :

    

  * **fpath** (  _FieldPath_ _|_ [ _list_ ](https://docs.python.org/3/library/stdtypes.html#list "\(in Python v3.11\)") _[_ _FieldPath_ _]_ ) -- One or more ` FieldPath  ` object(s) to query. 

  * **unwrap** ( [ _bool_ ](https://docs.python.org/3/library/functions.html#bool "\(in Python v3.11\)") _,_ _optional_ ) -- Flag indicating whether or not, in the case where the returned data is a list of one element, the element itself should be returned instead of the list. Defaults to ` True  ` . 

  * **pagination_strategy** ( _Optional_ _[_ _Type_ _[_ [ _PaginationStrategy_ ](../subgrounds.pagination/#subgrounds.pagination.PaginationStrategy "subgrounds.pagination.PaginationStrategy") _]_ _]_ _,_ _optional_ ) -- A Class implementing the ` PaginationStrategy  ` ` Protocol  ` . If ` None  ` , then automatic pagination is disabled. Defaults to ` LegacyStrategy  ` . 

Returns  :

    

An iterator over the ` FieldPath  ` object(s)' data pages

Return type  :

    

Iterator[ [ type ](https://docs.python.org/3/library/functions.html#type "\(in
Python v3.11\)") ]

_ class  _ subgrounds.  SyntheticField  (  _ f  :  'Callable'  _ , _ type_  :
'TypeRef.T'  _ , _ deps  :  'list[FieldPath  |  SyntheticField]  |  FieldPath
|  SyntheticField'  _ , _ default  :  'Any'  =  None  _ )  #

    

Bases: [ ` FieldOperatorMixin  `
](../subgrounds.subgraph.fieldpath/#subgrounds.subgraph.fieldpath.FieldOperatorMixin
"subgrounds.subgraph.fieldpath.FieldOperatorMixin")

STRING  _ :  ClassVar  [  [ TypeRef.Named
](../subgrounds.schema/#subgrounds.schema.TypeRef.Named
"subgrounds.schema.TypeRef.Named") ]  _ _ =  Named(name_='String',
kind='SCALAR')  _ #

    

INT  _ :  ClassVar  [  [ TypeRef.Named
](../subgrounds.schema/#subgrounds.schema.TypeRef.Named
"subgrounds.schema.TypeRef.Named") ]  _ _ =  Named(name_='Int',
kind='SCALAR')  _ #

    

FLOAT  _ :  ClassVar  [  [ TypeRef.Named
](../subgrounds.schema/#subgrounds.schema.TypeRef.Named
"subgrounds.schema.TypeRef.Named") ]  _ _ =  Named(name_='Float',
kind='SCALAR')  _ #

    

BOOL  _ :  ClassVar  [  [ TypeRef.Named
](../subgrounds.schema/#subgrounds.schema.TypeRef.Named
"subgrounds.schema.TypeRef.Named") ]  _ _ =  Named(name_='Boolean',
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

  * **type** ( [ _TypeRef.T_ ](../subgrounds.schema/#subgrounds.schema.TypeRef.T "subgrounds.schema.TypeRef.T") ) -- The type of the resulting field 

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
    

[ Next  subgrounds.pagination package  ](../subgrounds.pagination/) [ Previous
API Documentation  ](../../modules/)

Made with [ Furo ](https://github.com/pradyunsg/furo)

[ ](https://github.com/0xPlaygrounds/subgrounds) [
](https://discord.gg/v4r4zhBAh2) [ ](https://twitter.com/Playgrounds0x)

On this page

  * subgrounds package 
    * Subpackages 
    * Submodules 
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

Give us a ⭐️ on [ Github ](https://github.com/0xPlaygrounds/subgrounds) !

Toggle site navigation sidebar

_ _

[ ![Light Logo](../../../_static/assets/pg-logotype-dark.svg) ![Dark
Logo](../../../_static/assets/pg-logotype-primary.svg)
](https://playgrounds.network)

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
      * [ Merging ](../../getting_started/field_paths/merging/)
    * [ Querying ](../../getting_started/querying/)
    * [ Synthetic Fields ](../../getting_started/synthetic_fields/)
  * [ Advanced Topics ](../../advanced_topics/)

Toggle child pages in navigation

_ _

    * [ Pagination ](../../advanced_topics/pagination/)

Toggle child pages in navigation

_ _

      * [ Custom Strategies ](../../advanced_topics/pagination/custom/)
  * [ FAQ ](../../faq/)

Toggle child pages in navigation

_ _

    * [ Setup ](../../faq/setup/)

Toggle child pages in navigation

_ _

      * [ Python Versioning ](../../faq/setup/version_management/)
    * [ Contrib ](../../faq/contrib/)
  * [ Examples ](../../examples/)

Toggle child pages in navigation

_ _

    * [ Exchanges ](../../examples/exchanges/)
    * [ Bridges ](../../examples/bridges/)
    * [ Liquid Staking ](../../examples/liquid_staking/)
    * [ Governance ](../../examples/governance/)
    * [ Advanced Research ](../../examples/advanced_research/)
    * [ Vaults ](../../examples/vaults/)
  * [ Tutorials ](../../tutorials/)
  * [ Changelog ](../../changelog/)
  * [ API Reference ](../../modules/)

Toggle child pages in navigation

_ _

    * [ subgrounds package ](../subgrounds/)

Toggle child pages in navigation

_ _

      * subgrounds.pagination package 

Toggle child pages in navigation

_ _

        * [ subgrounds.pagination.pagination module ](../subgrounds.pagination.pagination/)
        * [ subgrounds.pagination.preprocess module ](../subgrounds.pagination.preprocess/)
        * [ subgrounds.pagination.strategies module ](../subgrounds.pagination.strategies/)
        * [ subgrounds.pagination.utils module ](../subgrounds.pagination.utils/)
      * [ subgrounds.subgraph package ](../subgrounds.subgraph/)

Toggle child pages in navigation

_ _

        * [ subgrounds.subgraph.fieldpath module ](../subgrounds.subgraph.fieldpath/)
        * [ subgrounds.subgraph.filter module ](../subgrounds.subgraph.filter/)
        * [ subgrounds.subgraph.object module ](../subgrounds.subgraph.object/)
        * [ subgrounds.subgraph.subgraph module ](../subgrounds.subgraph.subgraph/)
      * [ subgrounds.client module ](../subgrounds.client/)
      * [ subgrounds.dash_wrappers module ](../subgrounds.dash_wrappers/)
      * [ subgrounds.dataframe_utils module ](../subgrounds.dataframe_utils/)
      * [ subgrounds.plotly_wrappers module ](../subgrounds.plotly_wrappers/)
      * [ subgrounds.query module ](../subgrounds.query/)
      * [ subgrounds.schema module ](../subgrounds.schema/)
      * [ subgrounds.subgrounds module ](../subgrounds.subgrounds/)
      * [ subgrounds.transform module ](../subgrounds.transform/)
      * [ subgrounds.utils module ](../subgrounds.utils/)

Back to top

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

_ _

#  subgrounds.pagination package  #

##  Submodules  #

  * [ subgrounds.pagination.pagination module ](../subgrounds.pagination.pagination/)
    * [ ` PaginationError  ` ](../subgrounds.pagination.pagination/#subgrounds.pagination.pagination.PaginationError)
    * [ ` PaginationStrategy  ` ](../subgrounds.pagination.pagination/#subgrounds.pagination.pagination.PaginationStrategy)
      * [ ` PaginationStrategy.step()  ` ](../subgrounds.pagination.pagination/#subgrounds.pagination.pagination.PaginationStrategy.step)
    * [ ` paginate()  ` ](../subgrounds.pagination.pagination/#subgrounds.pagination.pagination.paginate)
    * [ ` paginate_iter()  ` ](../subgrounds.pagination.pagination/#subgrounds.pagination.pagination.paginate_iter)
  * [ subgrounds.pagination.preprocess module ](../subgrounds.pagination.preprocess/)
    * [ ` PaginationNode  ` ](../subgrounds.pagination.preprocess/#subgrounds.pagination.preprocess.PaginationNode)
      * [ ` PaginationNode.node_idx  ` ](../subgrounds.pagination.preprocess/#subgrounds.pagination.preprocess.PaginationNode.node_idx)
      * [ ` PaginationNode.filter_field  ` ](../subgrounds.pagination.preprocess/#subgrounds.pagination.preprocess.PaginationNode.filter_field)
      * [ ` PaginationNode.first_value  ` ](../subgrounds.pagination.preprocess/#subgrounds.pagination.preprocess.PaginationNode.first_value)
      * [ ` PaginationNode.skip_value  ` ](../subgrounds.pagination.preprocess/#subgrounds.pagination.preprocess.PaginationNode.skip_value)
      * [ ` PaginationNode.filter_value  ` ](../subgrounds.pagination.preprocess/#subgrounds.pagination.preprocess.PaginationNode.filter_value)
      * [ ` PaginationNode.filter_value_type  ` ](../subgrounds.pagination.preprocess/#subgrounds.pagination.preprocess.PaginationNode.filter_value_type)
      * [ ` PaginationNode.key_path  ` ](../subgrounds.pagination.preprocess/#subgrounds.pagination.preprocess.PaginationNode.key_path)
      * [ ` PaginationNode.inner  ` ](../subgrounds.pagination.preprocess/#subgrounds.pagination.preprocess.PaginationNode.inner)
      * [ ` PaginationNode.node_idx  ` ](../subgrounds.pagination.preprocess/#id0)
      * [ ` PaginationNode.filter_field  ` ](../subgrounds.pagination.preprocess/#id1)
      * [ ` PaginationNode.first_value  ` ](../subgrounds.pagination.preprocess/#id2)
      * [ ` PaginationNode.skip_value  ` ](../subgrounds.pagination.preprocess/#id3)
      * [ ` PaginationNode.filter_value  ` ](../subgrounds.pagination.preprocess/#id4)
      * [ ` PaginationNode.filter_value_type  ` ](../subgrounds.pagination.preprocess/#id5)
      * [ ` PaginationNode.key_path  ` ](../subgrounds.pagination.preprocess/#id6)
      * [ ` PaginationNode.inner  ` ](../subgrounds.pagination.preprocess/#id7)
      * [ ` PaginationNode.get_vardefs()  ` ](../subgrounds.pagination.preprocess/#subgrounds.pagination.preprocess.PaginationNode.get_vardefs)
    * [ ` is_pagination_node()  ` ](../subgrounds.pagination.preprocess/#subgrounds.pagination.preprocess.is_pagination_node)
    * [ ` get_orderBy_value()  ` ](../subgrounds.pagination.preprocess/#subgrounds.pagination.preprocess.get_orderBy_value)
    * [ ` get_orderDirection_value()  ` ](../subgrounds.pagination.preprocess/#subgrounds.pagination.preprocess.get_orderDirection_value)
    * [ ` get_filtering_args()  ` ](../subgrounds.pagination.preprocess/#subgrounds.pagination.preprocess.get_filtering_args)
    * [ ` get_filtering_value()  ` ](../subgrounds.pagination.preprocess/#subgrounds.pagination.preprocess.get_filtering_value)
    * [ ` generate_pagination_nodes()  ` ](../subgrounds.pagination.preprocess/#subgrounds.pagination.preprocess.generate_pagination_nodes)
    * [ ` normalize()  ` ](../subgrounds.pagination.preprocess/#subgrounds.pagination.preprocess.normalize)
    * [ ` prune_doc()  ` ](../subgrounds.pagination.preprocess/#subgrounds.pagination.preprocess.prune_doc)
  * [ subgrounds.pagination.strategies module ](../subgrounds.pagination.strategies/)
    * [ ` StopPagination  ` ](../subgrounds.pagination.strategies/#subgrounds.pagination.strategies.StopPagination)
    * [ ` SkipPagination  ` ](../subgrounds.pagination.strategies/#subgrounds.pagination.strategies.SkipPagination)
    * [ ` LegacyStrategyArgGenerator  ` ](../subgrounds.pagination.strategies/#subgrounds.pagination.strategies.LegacyStrategyArgGenerator)
      * [ ` LegacyStrategyArgGenerator.active_idx  ` ](../subgrounds.pagination.strategies/#subgrounds.pagination.strategies.LegacyStrategyArgGenerator.active_idx)
      * [ ` LegacyStrategyArgGenerator.Cursor  ` ](../subgrounds.pagination.strategies/#subgrounds.pagination.strategies.LegacyStrategyArgGenerator.Cursor)
        * [ ` LegacyStrategyArgGenerator.Cursor.inner_idx  ` ](../subgrounds.pagination.strategies/#subgrounds.pagination.strategies.LegacyStrategyArgGenerator.Cursor.inner_idx)
        * [ ` LegacyStrategyArgGenerator.Cursor.filter_value  ` ](../subgrounds.pagination.strategies/#subgrounds.pagination.strategies.LegacyStrategyArgGenerator.Cursor.filter_value)
        * [ ` LegacyStrategyArgGenerator.Cursor.queried_entities  ` ](../subgrounds.pagination.strategies/#subgrounds.pagination.strategies.LegacyStrategyArgGenerator.Cursor.queried_entities)
        * [ ` LegacyStrategyArgGenerator.Cursor.stop  ` ](../subgrounds.pagination.strategies/#subgrounds.pagination.strategies.LegacyStrategyArgGenerator.Cursor.stop)
        * [ ` LegacyStrategyArgGenerator.Cursor.page_count  ` ](../subgrounds.pagination.strategies/#subgrounds.pagination.strategies.LegacyStrategyArgGenerator.Cursor.page_count)
        * [ ` LegacyStrategyArgGenerator.Cursor.keys  ` ](../subgrounds.pagination.strategies/#subgrounds.pagination.strategies.LegacyStrategyArgGenerator.Cursor.keys)
        * [ ` LegacyStrategyArgGenerator.Cursor.page_node  ` ](../subgrounds.pagination.strategies/#subgrounds.pagination.strategies.LegacyStrategyArgGenerator.Cursor.page_node)
        * [ ` LegacyStrategyArgGenerator.Cursor.inner  ` ](../subgrounds.pagination.strategies/#subgrounds.pagination.strategies.LegacyStrategyArgGenerator.Cursor.inner)
        * [ ` LegacyStrategyArgGenerator.Cursor.is_leaf  ` ](../subgrounds.pagination.strategies/#subgrounds.pagination.strategies.LegacyStrategyArgGenerator.Cursor.is_leaf)
        * [ ` LegacyStrategyArgGenerator.Cursor.update()  ` ](../subgrounds.pagination.strategies/#subgrounds.pagination.strategies.LegacyStrategyArgGenerator.Cursor.update)
        * [ ` LegacyStrategyArgGenerator.Cursor.step()  ` ](../subgrounds.pagination.strategies/#subgrounds.pagination.strategies.LegacyStrategyArgGenerator.Cursor.step)
        * [ ` LegacyStrategyArgGenerator.Cursor.first_arg_value()  ` ](../subgrounds.pagination.strategies/#subgrounds.pagination.strategies.LegacyStrategyArgGenerator.Cursor.first_arg_value)
        * [ ` LegacyStrategyArgGenerator.Cursor.args()  ` ](../subgrounds.pagination.strategies/#subgrounds.pagination.strategies.LegacyStrategyArgGenerator.Cursor.args)
        * [ ` LegacyStrategyArgGenerator.Cursor.reset()  ` ](../subgrounds.pagination.strategies/#subgrounds.pagination.strategies.LegacyStrategyArgGenerator.Cursor.reset)
      * [ ` LegacyStrategyArgGenerator.cursor  ` ](../subgrounds.pagination.strategies/#subgrounds.pagination.strategies.LegacyStrategyArgGenerator.cursor)
      * [ ` LegacyStrategyArgGenerator.step()  ` ](../subgrounds.pagination.strategies/#subgrounds.pagination.strategies.LegacyStrategyArgGenerator.step)
    * [ ` LegacyStrategy  ` ](../subgrounds.pagination.strategies/#subgrounds.pagination.strategies.LegacyStrategy)
      * [ ` LegacyStrategy.schema  ` ](../subgrounds.pagination.strategies/#subgrounds.pagination.strategies.LegacyStrategy.schema)
      * [ ` LegacyStrategy.arg_generator  ` ](../subgrounds.pagination.strategies/#subgrounds.pagination.strategies.LegacyStrategy.arg_generator)
      * [ ` LegacyStrategy.normalized_doc  ` ](../subgrounds.pagination.strategies/#subgrounds.pagination.strategies.LegacyStrategy.normalized_doc)
      * [ ` LegacyStrategy.step()  ` ](../subgrounds.pagination.strategies/#subgrounds.pagination.strategies.LegacyStrategy.step)
    * [ ` ShallowStrategyArgGenerator  ` ](../subgrounds.pagination.strategies/#subgrounds.pagination.strategies.ShallowStrategyArgGenerator)
      * [ ` ShallowStrategyArgGenerator.Cursor  ` ](../subgrounds.pagination.strategies/#subgrounds.pagination.strategies.ShallowStrategyArgGenerator.Cursor)
        * [ ` ShallowStrategyArgGenerator.Cursor.page_node  ` ](../subgrounds.pagination.strategies/#subgrounds.pagination.strategies.ShallowStrategyArgGenerator.Cursor.page_node)
        * [ ` ShallowStrategyArgGenerator.Cursor.inner  ` ](../subgrounds.pagination.strategies/#subgrounds.pagination.strategies.ShallowStrategyArgGenerator.Cursor.inner)
        * [ ` ShallowStrategyArgGenerator.Cursor.inner_idx  ` ](../subgrounds.pagination.strategies/#subgrounds.pagination.strategies.ShallowStrategyArgGenerator.Cursor.inner_idx)
        * [ ` ShallowStrategyArgGenerator.Cursor.filter_value  ` ](../subgrounds.pagination.strategies/#subgrounds.pagination.strategies.ShallowStrategyArgGenerator.Cursor.filter_value)
        * [ ` ShallowStrategyArgGenerator.Cursor.queried_entities  ` ](../subgrounds.pagination.strategies/#subgrounds.pagination.strategies.ShallowStrategyArgGenerator.Cursor.queried_entities)
        * [ ` ShallowStrategyArgGenerator.Cursor.stop  ` ](../subgrounds.pagination.strategies/#subgrounds.pagination.strategies.ShallowStrategyArgGenerator.Cursor.stop)
        * [ ` ShallowStrategyArgGenerator.Cursor.page_count  ` ](../subgrounds.pagination.strategies/#subgrounds.pagination.strategies.ShallowStrategyArgGenerator.Cursor.page_count)
        * [ ` ShallowStrategyArgGenerator.Cursor.keys  ` ](../subgrounds.pagination.strategies/#subgrounds.pagination.strategies.ShallowStrategyArgGenerator.Cursor.keys)
        * [ ` ShallowStrategyArgGenerator.Cursor.page_node  ` ](../subgrounds.pagination.strategies/#id0)
        * [ ` ShallowStrategyArgGenerator.Cursor.inner  ` ](../subgrounds.pagination.strategies/#id1)
        * [ ` ShallowStrategyArgGenerator.Cursor.inner_idx  ` ](../subgrounds.pagination.strategies/#id2)
        * [ ` ShallowStrategyArgGenerator.Cursor.filter_value  ` ](../subgrounds.pagination.strategies/#id3)
        * [ ` ShallowStrategyArgGenerator.Cursor.queried_entities  ` ](../subgrounds.pagination.strategies/#id4)
        * [ ` ShallowStrategyArgGenerator.Cursor.page_count  ` ](../subgrounds.pagination.strategies/#id5)
        * [ ` ShallowStrategyArgGenerator.Cursor.from_pagination_node()  ` ](../subgrounds.pagination.strategies/#subgrounds.pagination.strategies.ShallowStrategyArgGenerator.Cursor.from_pagination_node)
        * [ ` ShallowStrategyArgGenerator.Cursor.is_leaf  ` ](../subgrounds.pagination.strategies/#subgrounds.pagination.strategies.ShallowStrategyArgGenerator.Cursor.is_leaf)
        * [ ` ShallowStrategyArgGenerator.Cursor.active_cursor  ` ](../subgrounds.pagination.strategies/#subgrounds.pagination.strategies.ShallowStrategyArgGenerator.Cursor.active_cursor)
        * [ ` ShallowStrategyArgGenerator.Cursor.iter()  ` ](../subgrounds.pagination.strategies/#subgrounds.pagination.strategies.ShallowStrategyArgGenerator.Cursor.iter)
        * [ ` ShallowStrategyArgGenerator.Cursor.mapi()  ` ](../subgrounds.pagination.strategies/#subgrounds.pagination.strategies.ShallowStrategyArgGenerator.Cursor.mapi)
      * [ ` ShallowStrategyArgGenerator.cursor  ` ](../subgrounds.pagination.strategies/#subgrounds.pagination.strategies.ShallowStrategyArgGenerator.cursor)
      * [ ` ShallowStrategyArgGenerator.iter_cursors()  ` ](../subgrounds.pagination.strategies/#subgrounds.pagination.strategies.ShallowStrategyArgGenerator.iter_cursors)
      * [ ` ShallowStrategyArgGenerator.update_cursor()  ` ](../subgrounds.pagination.strategies/#subgrounds.pagination.strategies.ShallowStrategyArgGenerator.update_cursor)
      * [ ` ShallowStrategyArgGenerator.step()  ` ](../subgrounds.pagination.strategies/#subgrounds.pagination.strategies.ShallowStrategyArgGenerator.step)
    * [ ` ShallowStrategy  ` ](../subgrounds.pagination.strategies/#subgrounds.pagination.strategies.ShallowStrategy)
      * [ ` ShallowStrategy.schema  ` ](../subgrounds.pagination.strategies/#subgrounds.pagination.strategies.ShallowStrategy.schema)
      * [ ` ShallowStrategy.arg_generator  ` ](../subgrounds.pagination.strategies/#subgrounds.pagination.strategies.ShallowStrategy.arg_generator)
      * [ ` ShallowStrategy.normalized_doc  ` ](../subgrounds.pagination.strategies/#subgrounds.pagination.strategies.ShallowStrategy.normalized_doc)
      * [ ` ShallowStrategy.step()  ` ](../subgrounds.pagination.strategies/#subgrounds.pagination.strategies.ShallowStrategy.step)
  * [ subgrounds.pagination.utils module ](../subgrounds.pagination.utils/)
    * [ ` merge()  ` ](../subgrounds.pagination.utils/#subgrounds.pagination.utils.merge)
    * [ ` merge_input_value_object_metas()  ` ](../subgrounds.pagination.utils/#subgrounds.pagination.utils.merge_input_value_object_metas)

##  Module contents  #

This module contains all code related to automatic pagination.

The ` pagination  ` module contains the pagination algorithms (both regular
and iterative) that make use of ` PaginationStrategies  ` .

The ` preprocess  ` and ` strategties  ` modules implement the currently
supported ` PaginationStrategies  ` : ` LegacyStrategy  ` and `
ShallowStrategy  ` .

The ` utils  ` module contains some generic functions that are useful in the
context of pagination.

subgrounds.pagination.  generate_pagination_nodes  (  _ schema  _ , _ document
_ )  #

    

_ class  _ subgrounds.pagination.  LegacyStrategy  (  _ schema  _ , _ document
_ )  #

    

Bases: [ ` object  ` ](https://docs.python.org/3/library/functions.html#object
"\(in Python v3.11\)")

schema  _ :  [ SchemaMeta
](../subgrounds.schema/#subgrounds.schema.SchemaMeta
"subgrounds.schema.SchemaMeta") _ #

    

arg_generator  _ :  [ LegacyStrategyArgGenerator
](../subgrounds.pagination.strategies/#subgrounds.pagination.strategies.LegacyStrategyArgGenerator
"subgrounds.pagination.strategies.LegacyStrategyArgGenerator") _ #

    

normalized_doc  _ :  [ Document
](../subgrounds.query/#subgrounds.query.Document "subgrounds.query.Document")
_ #

    

step  (  _ page_data  =  None  _ )  #

    

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

    

  * **schema** ( [ _SchemaMeta_ ](../subgrounds.schema/#subgrounds.schema.SchemaMeta "subgrounds.schema.SchemaMeta") ) -- The GraphQL schema on which the request document is based 

  * **doc** ( [ _Document_ ](../subgrounds.query/#subgrounds.query.Document "subgrounds.query.Document") ) -- The request document 

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

    

  * **schema** ( [ _SchemaMeta_ ](../subgrounds.schema/#subgrounds.schema.SchemaMeta "subgrounds.schema.SchemaMeta") ) -- The GraphQL schema on which the request document is based 

  * **doc** ( [ _Document_ ](../subgrounds.query/#subgrounds.query.Document "subgrounds.query.Document") ) -- The request document 

Returns  :

    

The response data as a JSON dictionary

Return type  :

    

[ dict ](https://docs.python.org/3/library/stdtypes.html#dict "\(in Python
v3.11\)") [ [ str ](https://docs.python.org/3/library/stdtypes.html#str "\(in
Python v3.11\)") , Any]

_ exception  _ subgrounds.pagination.  PaginationError  (  _ message  _ , _
strategy  _ )  #

    

Bases: [ ` RuntimeError  `
](https://docs.python.org/3/library/exceptions.html#RuntimeError "\(in Python
v3.11\)")

_ class  _ subgrounds.pagination.  PaginationNode  (  _ node_idx  _ , _
filter_field  _ , _ first_value  _ , _ skip_value  _ , _ filter_value  _ , _
filter_value_type  _ , _ key_path  _ , _ inner=<factory> _ )  #

    

Bases: [ ` object  ` ](https://docs.python.org/3/library/functions.html#object
"\(in Python v3.11\)")

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

    

[ TypeRef.T ](../subgrounds.schema/#subgrounds.schema.TypeRef.T
"subgrounds.schema.TypeRef.T")

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

node_idx  _ :  [ int  ](https://docs.python.org/3/library/functions.html#int
"\(in Python v3.11\)") _ #

    

filter_field  _ :  [ str
](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.11\)") _
#

    

first_value  _ :  [ int
](https://docs.python.org/3/library/functions.html#int "\(in Python v3.11\)")
_ #

    

skip_value  _ :  [ int  ](https://docs.python.org/3/library/functions.html#int
"\(in Python v3.11\)") _ #

    

filter_value  _ :  [ Any
](https://docs.python.org/3/library/typing.html#typing.Any "\(in Python
v3.11\)") _ #

    

filter_value_type  _ :  [ T
](../subgrounds.schema/#subgrounds.schema.TypeRef.T
"subgrounds.schema.TypeRef.T") _ #

    

key_path  _ :  [ list  ](https://docs.python.org/3/library/stdtypes.html#list
"\(in Python v3.11\)") [  [ str
](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.11\)") ]
_ #

    

inner  _ :  [ list  ](https://docs.python.org/3/library/stdtypes.html#list
"\(in Python v3.11\)") [  [ subgrounds.pagination.preprocess.PaginationNode
](../subgrounds.pagination.preprocess/#subgrounds.pagination.preprocess.PaginationNode
"subgrounds.pagination.preprocess.PaginationNode") ]  _ #

    

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
](../subgrounds.query/#subgrounds.query.VariableDefinition
"subgrounds.query.VariableDefinition") ]

_ class  _ subgrounds.pagination.  PaginationStrategy  (  _ *  args  _ , _ **
kwargs  _ )  #

    

Bases: [ ` Protocol  `
](https://docs.python.org/3/library/typing.html#typing.Protocol "\(in Python
v3.11\)")

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

    

Tuple[ [ Document ](../subgrounds.query/#subgrounds.query.Document
"subgrounds.query.Document") , [ dict
](https://docs.python.org/3/library/stdtypes.html#dict "\(in Python v3.11\)")
[ [ str ](https://docs.python.org/3/library/stdtypes.html#str "\(in Python
v3.11\)") , Any]]

subgrounds.pagination.  prune_doc  (  _ document  _ , _ args  _ )  #

    

_ class  _ subgrounds.pagination.  ShallowStrategy  (  _ schema  _ , _
document  _ )  #

    

Bases: [ ` object  ` ](https://docs.python.org/3/library/functions.html#object
"\(in Python v3.11\)")

schema  _ :  [ SchemaMeta
](../subgrounds.schema/#subgrounds.schema.SchemaMeta
"subgrounds.schema.SchemaMeta") _ #

    

arg_generator  _ :  [ ShallowStrategyArgGenerator
](../subgrounds.pagination.strategies/#subgrounds.pagination.strategies.ShallowStrategyArgGenerator
"subgrounds.pagination.strategies.ShallowStrategyArgGenerator") _ #

    

normalized_doc  _ :  [ Document
](../subgrounds.query/#subgrounds.query.Document "subgrounds.query.Document")
_ #

    

step  (  _ page_data  =  None  _ )  #

    

[ Next  subgrounds.pagination.pagination module
](../subgrounds.pagination.pagination/) [ Previous  subgrounds package
](../subgrounds/)

Made with [ Furo ](https://github.com/pradyunsg/furo)

[ ](https://github.com/0xPlaygrounds/subgrounds) [
](https://discord.gg/v4r4zhBAh2) [ ](https://twitter.com/Playgrounds0x)

On this page

  * subgrounds.pagination package 
    * Submodules 
    * Module contents 
      * ` generate_pagination_nodes()  `
      * ` LegacyStrategy  `
        * ` LegacyStrategy.schema  `
        * ` LegacyStrategy.arg_generator  `
        * ` LegacyStrategy.normalized_doc  `
        * ` LegacyStrategy.step()  `
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
      * ` prune_doc()  `
      * ` ShallowStrategy  `
        * ` ShallowStrategy.schema  `
        * ` ShallowStrategy.arg_generator  `
        * ` ShallowStrategy.normalized_doc  `
        * ` ShallowStrategy.step()  `



Contents  Menu  Expand  Light mode  Dark mode  Auto light/dark mode

Hide navigation sidebar

Hide table of contents sidebar

Give us a ⭐️ on [ Github ](https://github.com/0xPlaygrounds/subgrounds) !

Toggle site navigation sidebar

_ _

[ ![Light Logo](../../../_static/assets/pg-logotype-dark.svg) ![Dark
Logo](../../../_static/assets/pg-logotype-primary.svg)
](https://playgrounds.network)

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
      * [ Merging ](../../getting_started/field_paths/merging/)
    * [ Querying ](../../getting_started/querying/)
    * [ Synthetic Fields ](../../getting_started/synthetic_fields/)
  * [ Advanced Topics ](../../advanced_topics/)

Toggle child pages in navigation

_ _

    * [ Pagination ](../../advanced_topics/pagination/)

Toggle child pages in navigation

_ _

      * [ Custom Strategies ](../../advanced_topics/pagination/custom/)
  * [ FAQ ](../../faq/)

Toggle child pages in navigation

_ _

    * [ Setup ](../../faq/setup/)

Toggle child pages in navigation

_ _

      * [ Python Versioning ](../../faq/setup/version_management/)
    * [ Contrib ](../../faq/contrib/)
  * [ Examples ](../../examples/)

Toggle child pages in navigation

_ _

    * [ Exchanges ](../../examples/exchanges/)
    * [ Bridges ](../../examples/bridges/)
    * [ Liquid Staking ](../../examples/liquid_staking/)
    * [ Governance ](../../examples/governance/)
    * [ Advanced Research ](../../examples/advanced_research/)
    * [ Vaults ](../../examples/vaults/)
  * [ Tutorials ](../../tutorials/)
  * [ Changelog ](../../changelog/)
  * [ API Reference ](../../modules/)

Toggle child pages in navigation

_ _

    * [ subgrounds package ](../subgrounds/)

Toggle child pages in navigation

_ _

      * [ subgrounds.pagination package ](../subgrounds.pagination/)

Toggle child pages in navigation

_ _

        * [ subgrounds.pagination.pagination module ](../subgrounds.pagination.pagination/)
        * subgrounds.pagination.preprocess module 
        * [ subgrounds.pagination.strategies module ](../subgrounds.pagination.strategies/)
        * [ subgrounds.pagination.utils module ](../subgrounds.pagination.utils/)
      * [ subgrounds.subgraph package ](../subgrounds.subgraph/)

Toggle child pages in navigation

_ _

        * [ subgrounds.subgraph.fieldpath module ](../subgrounds.subgraph.fieldpath/)
        * [ subgrounds.subgraph.filter module ](../subgrounds.subgraph.filter/)
        * [ subgrounds.subgraph.object module ](../subgrounds.subgraph.object/)
        * [ subgrounds.subgraph.subgraph module ](../subgrounds.subgraph.subgraph/)
      * [ subgrounds.client module ](../subgrounds.client/)
      * [ subgrounds.dash_wrappers module ](../subgrounds.dash_wrappers/)
      * [ subgrounds.dataframe_utils module ](../subgrounds.dataframe_utils/)
      * [ subgrounds.plotly_wrappers module ](../subgrounds.plotly_wrappers/)
      * [ subgrounds.query module ](../subgrounds.query/)
      * [ subgrounds.schema module ](../subgrounds.schema/)
      * [ subgrounds.subgrounds module ](../subgrounds.subgrounds/)
      * [ subgrounds.transform module ](../subgrounds.transform/)
      * [ subgrounds.utils module ](../subgrounds.utils/)

Back to top

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

_ _

#  subgrounds.pagination.preprocess module  #

Helper functions and classes used by Subgrounds' own pagination strategies.

_ class  _ subgrounds.pagination.preprocess.  PaginationNode  (  _ node_idx  _
, _ filter_field  _ , _ first_value  _ , _ skip_value  _ , _ filter_value  _ ,
_ filter_value_type  _ , _ key_path  _ , _ inner=<factory> _ )  #

    

Bases: [ ` object  ` ](https://docs.python.org/3/library/functions.html#object
"\(in Python v3.11\)")

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

    

[ TypeRef.T ](../subgrounds.schema/#subgrounds.schema.TypeRef.T
"subgrounds.schema.TypeRef.T")

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

node_idx  _ :  [ int  ](https://docs.python.org/3/library/functions.html#int
"\(in Python v3.11\)") _ #

    

filter_field  _ :  [ str
](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.11\)") _
#

    

first_value  _ :  [ int
](https://docs.python.org/3/library/functions.html#int "\(in Python v3.11\)")
_ #

    

skip_value  _ :  [ int  ](https://docs.python.org/3/library/functions.html#int
"\(in Python v3.11\)") _ #

    

filter_value  _ :  [ Any
](https://docs.python.org/3/library/typing.html#typing.Any "\(in Python
v3.11\)") _ #

    

filter_value_type  _ :  [ T
](../subgrounds.schema/#subgrounds.schema.TypeRef.T
"subgrounds.schema.TypeRef.T") _ #

    

key_path  _ :  [ list  ](https://docs.python.org/3/library/stdtypes.html#list
"\(in Python v3.11\)") [  [ str
](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.11\)") ]
_ #

    

inner  _ :  [ list  ](https://docs.python.org/3/library/stdtypes.html#list
"\(in Python v3.11\)") [  subgrounds.pagination.preprocess.PaginationNode  ]
_ #

    

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
](../subgrounds.query/#subgrounds.query.VariableDefinition
"subgrounds.query.VariableDefinition") ]

subgrounds.pagination.preprocess.  is_pagination_node  (  _ schema  _ , _
selection  _ )  #

    

subgrounds.pagination.preprocess.  get_orderBy_value  (  _ selection  _ )  #

    

subgrounds.pagination.preprocess.  get_orderDirection_value  (  _ selection  _
)  #

    

subgrounds.pagination.preprocess.  get_filtering_args  (  _ selection  _ )  #

    

subgrounds.pagination.preprocess.  get_filtering_value  (  _ selection  _ )  #

    

subgrounds.pagination.preprocess.  generate_pagination_nodes  (  _ schema  _ ,
_ document  _ )  #

    

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

subgrounds.pagination.preprocess.  prune_doc  (  _ document  _ , _ args  _ )
#

    

[ Next  subgrounds.pagination.strategies module
](../subgrounds.pagination.strategies/) [ Previous
subgrounds.pagination.pagination module
](../subgrounds.pagination.pagination/)

Made with [ Furo ](https://github.com/pradyunsg/furo)

[ ](https://github.com/0xPlaygrounds/subgrounds) [
](https://discord.gg/v4r4zhBAh2) [ ](https://twitter.com/Playgrounds0x)

On this page

  * subgrounds.pagination.preprocess module 
    * ` PaginationNode  `
      * ` PaginationNode.node_idx  `
      * ` PaginationNode.filter_field  `
      * ` PaginationNode.first_value  `
      * ` PaginationNode.skip_value  `
      * ` PaginationNode.filter_value  `
      * ` PaginationNode.filter_value_type  `
      * ` PaginationNode.key_path  `
      * ` PaginationNode.inner  `
      * ` PaginationNode.node_idx  `
      * ` PaginationNode.filter_field  `
      * ` PaginationNode.first_value  `
      * ` PaginationNode.skip_value  `
      * ` PaginationNode.filter_value  `
      * ` PaginationNode.filter_value_type  `
      * ` PaginationNode.key_path  `
      * ` PaginationNode.inner  `
      * ` PaginationNode.get_vardefs()  `
    * ` is_pagination_node()  `
    * ` get_orderBy_value()  `
    * ` get_orderDirection_value()  `
    * ` get_filtering_args()  `
    * ` get_filtering_value()  `
    * ` generate_pagination_nodes()  `
    * ` normalize()  `
    * ` prune_doc()  `



Contents  Menu  Expand  Light mode  Dark mode  Auto light/dark mode

Hide navigation sidebar

Hide table of contents sidebar

Give us a ⭐️ on [ Github ](https://github.com/0xPlaygrounds/subgrounds) !

Toggle site navigation sidebar

_ _

[ ![Light Logo](../../../_static/assets/pg-logotype-dark.svg) ![Dark
Logo](../../../_static/assets/pg-logotype-primary.svg)
](https://playgrounds.network)

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
      * [ Merging ](../../getting_started/field_paths/merging/)
    * [ Querying ](../../getting_started/querying/)
    * [ Synthetic Fields ](../../getting_started/synthetic_fields/)
  * [ Advanced Topics ](../../advanced_topics/)

Toggle child pages in navigation

_ _

    * [ Pagination ](../../advanced_topics/pagination/)

Toggle child pages in navigation

_ _

      * [ Custom Strategies ](../../advanced_topics/pagination/custom/)
  * [ FAQ ](../../faq/)

Toggle child pages in navigation

_ _

    * [ Setup ](../../faq/setup/)

Toggle child pages in navigation

_ _

      * [ Python Versioning ](../../faq/setup/version_management/)
    * [ Contrib ](../../faq/contrib/)
  * [ Examples ](../../examples/)

Toggle child pages in navigation

_ _

    * [ Exchanges ](../../examples/exchanges/)
    * [ Bridges ](../../examples/bridges/)
    * [ Liquid Staking ](../../examples/liquid_staking/)
    * [ Governance ](../../examples/governance/)
    * [ Advanced Research ](../../examples/advanced_research/)
    * [ Vaults ](../../examples/vaults/)
  * [ Tutorials ](../../tutorials/)
  * [ Changelog ](../../changelog/)
  * [ API Reference ](../../modules/)

Toggle child pages in navigation

_ _

    * [ subgrounds package ](../subgrounds/)

Toggle child pages in navigation

_ _

      * [ subgrounds.pagination package ](../subgrounds.pagination/)

Toggle child pages in navigation

_ _

        * [ subgrounds.pagination.pagination module ](../subgrounds.pagination.pagination/)
        * [ subgrounds.pagination.preprocess module ](../subgrounds.pagination.preprocess/)
        * subgrounds.pagination.strategies module 
        * [ subgrounds.pagination.utils module ](../subgrounds.pagination.utils/)
      * [ subgrounds.subgraph package ](../subgrounds.subgraph/)

Toggle child pages in navigation

_ _

        * [ subgrounds.subgraph.fieldpath module ](../subgrounds.subgraph.fieldpath/)
        * [ subgrounds.subgraph.filter module ](../subgrounds.subgraph.filter/)
        * [ subgrounds.subgraph.object module ](../subgrounds.subgraph.object/)
        * [ subgrounds.subgraph.subgraph module ](../subgrounds.subgraph.subgraph/)
      * [ subgrounds.client module ](../subgrounds.client/)
      * [ subgrounds.dash_wrappers module ](../subgrounds.dash_wrappers/)
      * [ subgrounds.dataframe_utils module ](../subgrounds.dataframe_utils/)
      * [ subgrounds.plotly_wrappers module ](../subgrounds.plotly_wrappers/)
      * [ subgrounds.query module ](../subgrounds.query/)
      * [ subgrounds.schema module ](../subgrounds.schema/)
      * [ subgrounds.subgrounds module ](../subgrounds.subgrounds/)
      * [ subgrounds.transform module ](../subgrounds.transform/)
      * [ subgrounds.utils module ](../subgrounds.utils/)

Back to top

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

_ _

#  subgrounds.pagination.strategies module  #

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

    

Bases: [ ` Exception  `
](https://docs.python.org/3/library/exceptions.html#Exception "\(in Python
v3.11\)")

_ exception  _ subgrounds.pagination.strategies.  SkipPagination  (  _ *  args
_ )  #

    

Bases: [ ` Exception  `
](https://docs.python.org/3/library/exceptions.html#Exception "\(in Python
v3.11\)")

_ class  _ subgrounds.pagination.strategies.  LegacyStrategyArgGenerator  (  _
pagination_nodes  :  'list[PaginationNode]'  _ )  #

    

Bases: [ ` object  ` ](https://docs.python.org/3/library/functions.html#object
"\(in Python v3.11\)")

active_idx  _ :  [ int  ](https://docs.python.org/3/library/functions.html#int
"\(in Python v3.11\)") _ _ =  0  _ #

    

_ class  _ Cursor  (  _ page_node  :  'PaginationNode'  _ )  #

    

Bases: [ ` object  ` ](https://docs.python.org/3/library/functions.html#object
"\(in Python v3.11\)")

inner_idx  _ :  [ int  ](https://docs.python.org/3/library/functions.html#int
"\(in Python v3.11\)") _ _ =  0  _ #

    

filter_value  _ :  [ Any
](https://docs.python.org/3/library/typing.html#typing.Any "\(in Python
v3.11\)") _ _ =  None  _ #

    

queried_entities  _ :  [ int
](https://docs.python.org/3/library/functions.html#int "\(in Python v3.11\)")
_ _ =  0  _ #

    

stop  _ :  [ bool  ](https://docs.python.org/3/library/functions.html#bool
"\(in Python v3.11\)") _ _ =  False  _ #

    

page_count  _ :  [ int  ](https://docs.python.org/3/library/functions.html#int
"\(in Python v3.11\)") _ _ =  0  _ #

    

keys  _ :  [ set  ](https://docs.python.org/3/library/stdtypes.html#set "\(in
Python v3.11\)") [  [ str
](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.11\)") ]
_ #

    

page_node  _ :  [ PaginationNode
](../subgrounds.pagination.preprocess/#subgrounds.pagination.preprocess.PaginationNode
"subgrounds.pagination.preprocess.PaginationNode") _ #

    

inner  _ :  [ list  ](https://docs.python.org/3/library/stdtypes.html#list
"\(in Python v3.11\)") [
subgrounds.pagination.strategies.LegacyStrategyArgGenerator.Cursor  ]  _ #

    

_ property  _ is_leaf  #

    

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

first_arg_value  (  )  #

    

args  (  )  #

    

Returns the pagination arguments for the current state of the state machine
:returns: _description_ :rtype: dict

reset  (  )  #

    

Reset state machine

cursor  _ :  [ list  ](https://docs.python.org/3/library/stdtypes.html#list
"\(in Python v3.11\)") [  Cursor  ]  _ #

    

step  (  _ page_data  =  None  _ )  #

    

_ class  _ subgrounds.pagination.strategies.  LegacyStrategy  (  _ schema  _ ,
_ document  _ )  #

    

Bases: [ ` object  ` ](https://docs.python.org/3/library/functions.html#object
"\(in Python v3.11\)")

schema  _ :  [ SchemaMeta
](../subgrounds.schema/#subgrounds.schema.SchemaMeta
"subgrounds.schema.SchemaMeta") _ #

    

arg_generator  _ :  LegacyStrategyArgGenerator  _ #

    

normalized_doc  _ :  [ Document
](../subgrounds.query/#subgrounds.query.Document "subgrounds.query.Document")
_ #

    

step  (  _ page_data  =  None  _ )  #

    

_ class  _ subgrounds.pagination.strategies.  ShallowStrategyArgGenerator  (
_ pagination_nodes  :  'list[PaginationNode]'  _ )  #

    

Bases: [ ` object  ` ](https://docs.python.org/3/library/functions.html#object
"\(in Python v3.11\)")

_ class  _ Cursor  (  _ page_node  _ , _ inner  _ , _ inner_idx  =  0  _ , _
filter_value  =  None  _ , _ queried_entities  =  0  _ , _ page_count  =  0  _
)  #

    

Bases: [ ` object  ` ](https://docs.python.org/3/library/functions.html#object
"\(in Python v3.11\)")

Class used to generate the pagination variables for a given tree of `
PaginationNode  ` objects.

page_node  #

    

The ` PaginationNode  ` object which this cursor is iterating through.

Type  :

    

[ subgrounds.pagination.preprocess.PaginationNode
](../subgrounds.pagination.preprocess/#subgrounds.pagination.preprocess.PaginationNode
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

page_node  _ :  [ PaginationNode
](../subgrounds.pagination.preprocess/#subgrounds.pagination.preprocess.PaginationNode
"subgrounds.pagination.preprocess.PaginationNode") _ #

    

inner  _ :  [ list  ](https://docs.python.org/3/library/stdtypes.html#list
"\(in Python v3.11\)") [
subgrounds.pagination.strategies.ShallowStrategyArgGenerator.Cursor  ]  _ #

    

inner_idx  _ :  [ int  ](https://docs.python.org/3/library/functions.html#int
"\(in Python v3.11\)") _ _ =  0  _ #

    

filter_value  _ :  [ Any
](https://docs.python.org/3/library/typing.html#typing.Any "\(in Python
v3.11\)") _ _ =  None  _ #

    

queried_entities  _ :  [ int
](https://docs.python.org/3/library/functions.html#int "\(in Python v3.11\)")
_ _ =  0  _ #

    

page_count  _ :  [ int  ](https://docs.python.org/3/library/functions.html#int
"\(in Python v3.11\)") _ _ =  0  _ #

    

_ static  _ from_pagination_node  (  _ page_node  _ )  #

    

_ property  _ is_leaf  _ :  [ bool
](https://docs.python.org/3/library/functions.html#bool "\(in Python v3.11\)")
_ #

    

_ property  _ active_cursor  _ :  [ Optional
](https://docs.python.org/3/library/typing.html#typing.Optional "\(in Python
v3.11\)") [  Cursor  ]  _ #

    

iter  (  _ only_active  =  False  _ )  #

    

mapi  (  _ map_f  _ , _ priority  =  'self'  _ , _ counter  =  None  _ )  #

    

cursor  _ :  [ list  ](https://docs.python.org/3/library/stdtypes.html#list
"\(in Python v3.11\)") [  Cursor  ]  _ #

    

iter_cursors  (  )  #

    

_ static  _ update_cursor  (  _ cursor  _ , _ data  _ )  #

    

step  (  _ page_data  =  None  _ )  #

    

_ class  _ subgrounds.pagination.strategies.  ShallowStrategy  (  _ schema  _
, _ document  _ )  #

    

Bases: [ ` object  ` ](https://docs.python.org/3/library/functions.html#object
"\(in Python v3.11\)")

schema  _ :  [ SchemaMeta
](../subgrounds.schema/#subgrounds.schema.SchemaMeta
"subgrounds.schema.SchemaMeta") _ #

    

arg_generator  _ :  ShallowStrategyArgGenerator  _ #

    

normalized_doc  _ :  [ Document
](../subgrounds.query/#subgrounds.query.Document "subgrounds.query.Document")
_ #

    

step  (  _ page_data  =  None  _ )  #

    

[ Next  subgrounds.pagination.utils module  ](../subgrounds.pagination.utils/)
[ Previous  subgrounds.pagination.preprocess module
](../subgrounds.pagination.preprocess/)

Made with [ Furo ](https://github.com/pradyunsg/furo)

[ ](https://github.com/0xPlaygrounds/subgrounds) [
](https://discord.gg/v4r4zhBAh2) [ ](https://twitter.com/Playgrounds0x)

On this page

  * subgrounds.pagination.strategies module 
    * ` StopPagination  `
    * ` SkipPagination  `
    * ` LegacyStrategyArgGenerator  `
      * ` LegacyStrategyArgGenerator.active_idx  `
      * ` LegacyStrategyArgGenerator.Cursor  `
        * ` LegacyStrategyArgGenerator.Cursor.inner_idx  `
        * ` LegacyStrategyArgGenerator.Cursor.filter_value  `
        * ` LegacyStrategyArgGenerator.Cursor.queried_entities  `
        * ` LegacyStrategyArgGenerator.Cursor.stop  `
        * ` LegacyStrategyArgGenerator.Cursor.page_count  `
        * ` LegacyStrategyArgGenerator.Cursor.keys  `
        * ` LegacyStrategyArgGenerator.Cursor.page_node  `
        * ` LegacyStrategyArgGenerator.Cursor.inner  `
        * ` LegacyStrategyArgGenerator.Cursor.is_leaf  `
        * ` LegacyStrategyArgGenerator.Cursor.update()  `
        * ` LegacyStrategyArgGenerator.Cursor.step()  `
        * ` LegacyStrategyArgGenerator.Cursor.first_arg_value()  `
        * ` LegacyStrategyArgGenerator.Cursor.args()  `
        * ` LegacyStrategyArgGenerator.Cursor.reset()  `
      * ` LegacyStrategyArgGenerator.cursor  `
      * ` LegacyStrategyArgGenerator.step()  `
    * ` LegacyStrategy  `
      * ` LegacyStrategy.schema  `
      * ` LegacyStrategy.arg_generator  `
      * ` LegacyStrategy.normalized_doc  `
      * ` LegacyStrategy.step()  `
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
        * ` ShallowStrategyArgGenerator.Cursor.page_node  `
        * ` ShallowStrategyArgGenerator.Cursor.inner  `
        * ` ShallowStrategyArgGenerator.Cursor.inner_idx  `
        * ` ShallowStrategyArgGenerator.Cursor.filter_value  `
        * ` ShallowStrategyArgGenerator.Cursor.queried_entities  `
        * ` ShallowStrategyArgGenerator.Cursor.page_count  `
        * ` ShallowStrategyArgGenerator.Cursor.from_pagination_node()  `
        * ` ShallowStrategyArgGenerator.Cursor.is_leaf  `
        * ` ShallowStrategyArgGenerator.Cursor.active_cursor  `
        * ` ShallowStrategyArgGenerator.Cursor.iter()  `
        * ` ShallowStrategyArgGenerator.Cursor.mapi()  `
      * ` ShallowStrategyArgGenerator.cursor  `
      * ` ShallowStrategyArgGenerator.iter_cursors()  `
      * ` ShallowStrategyArgGenerator.update_cursor()  `
      * ` ShallowStrategyArgGenerator.step()  `
    * ` ShallowStrategy  `
      * ` ShallowStrategy.schema  `
      * ` ShallowStrategy.arg_generator  `
      * ` ShallowStrategy.normalized_doc  `
      * ` ShallowStrategy.step()  `



Contents  Menu  Expand  Light mode  Dark mode  Auto light/dark mode

Hide navigation sidebar

Hide table of contents sidebar

Give us a ⭐️ on [ Github ](https://github.com/0xPlaygrounds/subgrounds) !

Toggle site navigation sidebar

_ _

[ ![Light Logo](../../../_static/assets/pg-logotype-dark.svg) ![Dark
Logo](../../../_static/assets/pg-logotype-primary.svg)
](https://playgrounds.network)

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
      * [ Merging ](../../getting_started/field_paths/merging/)
    * [ Querying ](../../getting_started/querying/)
    * [ Synthetic Fields ](../../getting_started/synthetic_fields/)
  * [ Advanced Topics ](../../advanced_topics/)

Toggle child pages in navigation

_ _

    * [ Pagination ](../../advanced_topics/pagination/)

Toggle child pages in navigation

_ _

      * [ Custom Strategies ](../../advanced_topics/pagination/custom/)
  * [ FAQ ](../../faq/)

Toggle child pages in navigation

_ _

    * [ Setup ](../../faq/setup/)

Toggle child pages in navigation

_ _

      * [ Python Versioning ](../../faq/setup/version_management/)
    * [ Contrib ](../../faq/contrib/)
  * [ Examples ](../../examples/)

Toggle child pages in navigation

_ _

    * [ Exchanges ](../../examples/exchanges/)
    * [ Bridges ](../../examples/bridges/)
    * [ Liquid Staking ](../../examples/liquid_staking/)
    * [ Governance ](../../examples/governance/)
    * [ Advanced Research ](../../examples/advanced_research/)
    * [ Vaults ](../../examples/vaults/)
  * [ Tutorials ](../../tutorials/)
  * [ Changelog ](../../changelog/)
  * [ API Reference ](../../modules/)

Toggle child pages in navigation

_ _

    * [ subgrounds package ](../subgrounds/)

Toggle child pages in navigation

_ _

      * [ subgrounds.pagination package ](../subgrounds.pagination/)

Toggle child pages in navigation

_ _

        * [ subgrounds.pagination.pagination module ](../subgrounds.pagination.pagination/)
        * [ subgrounds.pagination.preprocess module ](../subgrounds.pagination.preprocess/)
        * [ subgrounds.pagination.strategies module ](../subgrounds.pagination.strategies/)
        * subgrounds.pagination.utils module 
      * [ subgrounds.subgraph package ](../subgrounds.subgraph/)

Toggle child pages in navigation

_ _

        * [ subgrounds.subgraph.fieldpath module ](../subgrounds.subgraph.fieldpath/)
        * [ subgrounds.subgraph.filter module ](../subgrounds.subgraph.filter/)
        * [ subgrounds.subgraph.object module ](../subgrounds.subgraph.object/)
        * [ subgrounds.subgraph.subgraph module ](../subgrounds.subgraph.subgraph/)
      * [ subgrounds.client module ](../subgrounds.client/)
      * [ subgrounds.dash_wrappers module ](../subgrounds.dash_wrappers/)
      * [ subgrounds.dataframe_utils module ](../subgrounds.dataframe_utils/)
      * [ subgrounds.plotly_wrappers module ](../subgrounds.plotly_wrappers/)
      * [ subgrounds.query module ](../subgrounds.query/)
      * [ subgrounds.schema module ](../subgrounds.schema/)
      * [ subgrounds.subgrounds module ](../subgrounds.subgrounds/)
      * [ subgrounds.transform module ](../subgrounds.transform/)
      * [ subgrounds.utils module ](../subgrounds.utils/)

Back to top

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

_ _

#  subgrounds.pagination.utils module  #

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

subgrounds.pagination.utils.  merge_input_value_object_metas  (  _ data1  :  [
Object  ](../subgrounds.query/#subgrounds.query.InputValue.Object
"subgrounds.query.InputValue.Object") _ , _ data2  :  [ Object
](../subgrounds.query/#subgrounds.query.InputValue.Object
"subgrounds.query.InputValue.Object") _ )  →  [ Object
](../subgrounds.query/#subgrounds.query.InputValue.Object
"subgrounds.query.InputValue.Object") #

subgrounds.pagination.utils.  merge_input_value_object_metas  (  _ data1  :  [
dict  ](https://docs.python.org/3/library/stdtypes.html#dict "\(in Python
v3.11\)") [  [ str  ](https://docs.python.org/3/library/stdtypes.html#str
"\(in Python v3.11\)") ,  [ subgrounds.query.InputValue.Object
](../subgrounds.query/#subgrounds.query.InputValue.Object
"subgrounds.query.InputValue.Object") ]  _ , _ data2  :  [ dict
](https://docs.python.org/3/library/stdtypes.html#dict "\(in Python v3.11\)")
[  [ str  ](https://docs.python.org/3/library/stdtypes.html#str "\(in Python
v3.11\)") ,  [ subgrounds.query.InputValue.Object
](../subgrounds.query/#subgrounds.query.InputValue.Object
"subgrounds.query.InputValue.Object") ]  _ )  →  [ dict
](https://docs.python.org/3/library/stdtypes.html#dict "\(in Python v3.11\)")
[  [ str  ](https://docs.python.org/3/library/stdtypes.html#str "\(in Python
v3.11\)") ,  [ subgrounds.query.InputValue.Object
](../subgrounds.query/#subgrounds.query.InputValue.Object
"subgrounds.query.InputValue.Object") ]

    

Merges ` data1  ` and ` data2  ` and returns the combined result.

` data1  ` and ` data2  ` must be of the same type. Either both are ` dict  `
, ` InputValue.Object  `

[ Next  subgrounds.subgraph package  ](../subgrounds.subgraph/) [ Previous
subgrounds.pagination.strategies module
](../subgrounds.pagination.strategies/)

Made with [ Furo ](https://github.com/pradyunsg/furo)

[ ](https://github.com/0xPlaygrounds/subgrounds) [
](https://discord.gg/v4r4zhBAh2) [ ](https://twitter.com/Playgrounds0x)

On this page

  * subgrounds.pagination.utils module 
    * ` merge()  `
    * ` merge_input_value_object_metas()  `



Contents  Menu  Expand  Light mode  Dark mode  Auto light/dark mode

Hide navigation sidebar

Hide table of contents sidebar

Give us a ⭐️ on [ Github ](https://github.com/0xPlaygrounds/subgrounds) !

Toggle site navigation sidebar

_ _

[ ![Light Logo](../../../_static/assets/pg-logotype-dark.svg) ![Dark
Logo](../../../_static/assets/pg-logotype-primary.svg)
](https://playgrounds.network)

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
      * [ Merging ](../../getting_started/field_paths/merging/)
    * [ Querying ](../../getting_started/querying/)
    * [ Synthetic Fields ](../../getting_started/synthetic_fields/)
  * [ Advanced Topics ](../../advanced_topics/)

Toggle child pages in navigation

_ _

    * [ Pagination ](../../advanced_topics/pagination/)

Toggle child pages in navigation

_ _

      * [ Custom Strategies ](../../advanced_topics/pagination/custom/)
  * [ FAQ ](../../faq/)

Toggle child pages in navigation

_ _

    * [ Setup ](../../faq/setup/)

Toggle child pages in navigation

_ _

      * [ Python Versioning ](../../faq/setup/version_management/)
    * [ Contrib ](../../faq/contrib/)
  * [ Examples ](../../examples/)

Toggle child pages in navigation

_ _

    * [ Exchanges ](../../examples/exchanges/)
    * [ Bridges ](../../examples/bridges/)
    * [ Liquid Staking ](../../examples/liquid_staking/)
    * [ Governance ](../../examples/governance/)
    * [ Advanced Research ](../../examples/advanced_research/)
    * [ Vaults ](../../examples/vaults/)
  * [ Tutorials ](../../tutorials/)
  * [ Changelog ](../../changelog/)
  * [ API Reference ](../../modules/)

Toggle child pages in navigation

_ _

    * [ subgrounds package ](../subgrounds/)

Toggle child pages in navigation

_ _

      * [ subgrounds.pagination package ](../subgrounds.pagination/)

Toggle child pages in navigation

_ _

        * [ subgrounds.pagination.pagination module ](../subgrounds.pagination.pagination/)
        * [ subgrounds.pagination.preprocess module ](../subgrounds.pagination.preprocess/)
        * [ subgrounds.pagination.strategies module ](../subgrounds.pagination.strategies/)
        * [ subgrounds.pagination.utils module ](../subgrounds.pagination.utils/)
      * subgrounds.subgraph package 

Toggle child pages in navigation

_ _

        * [ subgrounds.subgraph.fieldpath module ](../subgrounds.subgraph.fieldpath/)
        * [ subgrounds.subgraph.filter module ](../subgrounds.subgraph.filter/)
        * [ subgrounds.subgraph.object module ](../subgrounds.subgraph.object/)
        * [ subgrounds.subgraph.subgraph module ](../subgrounds.subgraph.subgraph/)
      * [ subgrounds.client module ](../subgrounds.client/)
      * [ subgrounds.dash_wrappers module ](../subgrounds.dash_wrappers/)
      * [ subgrounds.dataframe_utils module ](../subgrounds.dataframe_utils/)
      * [ subgrounds.plotly_wrappers module ](../subgrounds.plotly_wrappers/)
      * [ subgrounds.query module ](../subgrounds.query/)
      * [ subgrounds.schema module ](../subgrounds.schema/)
      * [ subgrounds.subgrounds module ](../subgrounds.subgrounds/)
      * [ subgrounds.transform module ](../subgrounds.transform/)
      * [ subgrounds.utils module ](../subgrounds.utils/)

Back to top

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

_ _

#  subgrounds.subgraph package  #

##  Submodules  #

  * [ subgrounds.subgraph.fieldpath module ](../subgrounds.subgraph.fieldpath/)
    * [ ` typeref_of_binary_op()  ` ](../subgrounds.subgraph.fieldpath/#subgrounds.subgraph.fieldpath.typeref_of_binary_op)
    * [ ` type_ref_of_unary_op()  ` ](../subgrounds.subgraph.fieldpath/#subgrounds.subgraph.fieldpath.type_ref_of_unary_op)
    * [ ` FieldOperatorMixin  ` ](../subgrounds.subgraph.fieldpath/#subgrounds.subgraph.fieldpath.FieldOperatorMixin)
    * [ ` fieldpaths_of_object()  ` ](../subgrounds.subgraph.fieldpath/#subgrounds.subgraph.fieldpath.fieldpaths_of_object)
    * [ ` FieldPath  ` ](../subgrounds.subgraph.fieldpath/#subgrounds.subgraph.fieldpath.FieldPath)
    * [ ` SyntheticField  ` ](../subgrounds.subgraph.fieldpath/#subgrounds.subgraph.fieldpath.SyntheticField)
      * [ ` SyntheticField.STRING  ` ](../subgrounds.subgraph.fieldpath/#subgrounds.subgraph.fieldpath.SyntheticField.STRING)
      * [ ` SyntheticField.INT  ` ](../subgrounds.subgraph.fieldpath/#subgrounds.subgraph.fieldpath.SyntheticField.INT)
      * [ ` SyntheticField.FLOAT  ` ](../subgrounds.subgraph.fieldpath/#subgrounds.subgraph.fieldpath.SyntheticField.FLOAT)
      * [ ` SyntheticField.BOOL  ` ](../subgrounds.subgraph.fieldpath/#subgrounds.subgraph.fieldpath.SyntheticField.BOOL)
      * [ ` SyntheticField.default_of_type()  ` ](../subgrounds.subgraph.fieldpath/#subgrounds.subgraph.fieldpath.SyntheticField.default_of_type)
      * [ ` SyntheticField.constant()  ` ](../subgrounds.subgraph.fieldpath/#subgrounds.subgraph.fieldpath.SyntheticField.constant)
      * [ ` SyntheticField.datetime_of_timestamp()  ` ](../subgrounds.subgraph.fieldpath/#subgrounds.subgraph.fieldpath.SyntheticField.datetime_of_timestamp)
      * [ ` SyntheticField.map()  ` ](../subgrounds.subgraph.fieldpath/#subgrounds.subgraph.fieldpath.SyntheticField.map)
  * [ subgrounds.subgraph.filter module ](../subgrounds.subgraph.filter/)
    * [ ` Filter  ` ](../subgrounds.subgraph.filter/#subgrounds.subgraph.filter.Filter)
      * [ ` Filter.field  ` ](../subgrounds.subgraph.filter/#subgrounds.subgraph.filter.Filter.field)
      * [ ` Filter.op  ` ](../subgrounds.subgraph.filter/#subgrounds.subgraph.filter.Filter.op)
      * [ ` Filter.value  ` ](../subgrounds.subgraph.filter/#subgrounds.subgraph.filter.Filter.value)
      * [ ` Filter.Operator  ` ](../subgrounds.subgraph.filter/#subgrounds.subgraph.filter.Filter.Operator)
        * [ ` Filter.Operator.EQ  ` ](../subgrounds.subgraph.filter/#subgrounds.subgraph.filter.Filter.Operator.EQ)
        * [ ` Filter.Operator.NEQ  ` ](../subgrounds.subgraph.filter/#subgrounds.subgraph.filter.Filter.Operator.NEQ)
        * [ ` Filter.Operator.LT  ` ](../subgrounds.subgraph.filter/#subgrounds.subgraph.filter.Filter.Operator.LT)
        * [ ` Filter.Operator.LTE  ` ](../subgrounds.subgraph.filter/#subgrounds.subgraph.filter.Filter.Operator.LTE)
        * [ ` Filter.Operator.GT  ` ](../subgrounds.subgraph.filter/#subgrounds.subgraph.filter.Filter.Operator.GT)
        * [ ` Filter.Operator.GTE  ` ](../subgrounds.subgraph.filter/#subgrounds.subgraph.filter.Filter.Operator.GTE)
      * [ ` Filter.mk_filter()  ` ](../subgrounds.subgraph.filter/#subgrounds.subgraph.filter.Filter.mk_filter)
      * [ ` Filter.name  ` ](../subgrounds.subgraph.filter/#subgrounds.subgraph.filter.Filter.name)
      * [ ` Filter.to_dict()  ` ](../subgrounds.subgraph.filter/#subgrounds.subgraph.filter.Filter.to_dict)
  * [ subgrounds.subgraph.object module ](../subgrounds.subgraph.object/)
    * [ ` Object  ` ](../subgrounds.subgraph.object/#subgrounds.subgraph.object.Object)
  * [ subgrounds.subgraph.subgraph module ](../subgrounds.subgraph.subgraph/)
    * [ ` Subgraph  ` ](../subgrounds.subgraph.subgraph/#subgrounds.subgraph.subgraph.Subgraph)

##  Module contents  #

_ class  _ subgrounds.subgraph.  FieldPath  (  _ subgraph  :  'Subgraph'  _ ,
_ root_type  :  'TypeRef.T'  _ , _ type_  :  'TypeRef.T'  _ , _ path  :
'list[Tuple[Optional[dict[str,  Any]],  TypeMeta.FieldMeta]]'  _ )  #

    

Bases: [ ` FieldOperatorMixin  `
](../subgrounds.subgraph.fieldpath/#subgrounds.subgraph.fieldpath.FieldOperatorMixin
"subgrounds.subgraph.fieldpath.FieldOperatorMixin")

_ class  _ subgrounds.subgraph.  Filter  (  _ field  :  'TypeMeta.FieldMeta'
_ , _ op  :  'Filter.Operator'  _ , _ value  :  'Any'  _ )  #

    

Bases: [ ` object  ` ](../subgrounds.subgraph.object/#module-
subgrounds.subgraph.object "subgrounds.subgraph.object")

field  _ :  [ FieldMeta
](../subgrounds.schema/#subgrounds.schema.TypeMeta.FieldMeta
"subgrounds.schema.TypeMeta.FieldMeta") _ #

    

op  _ :  [ Operator
](../subgrounds.subgraph.filter/#subgrounds.subgraph.filter.Filter.Operator
"subgrounds.subgraph.filter.Filter.Operator") _ #

    

value  _ :  [ Any  ](https://docs.python.org/3/library/typing.html#typing.Any
"\(in Python v3.11\)") _ #

    

_ class  _ Operator  (  _ value  _ )  #

    

Bases: [ ` Enum  ` ](https://docs.python.org/3/library/enum.html#enum.Enum
"\(in Python v3.11\)")

An enumeration.

EQ  _ =  1  _ #

    

NEQ  _ =  2  _ #

    

LT  _ =  3  _ #

    

LTE  _ =  4  _ #

    

GT  _ =  5  _ #

    

GTE  _ =  6  _ #

    

_ static  _ mk_filter  (  _ fpath  _ , _ op  _ , _ value  _ )  #

    

_ property  _ name  #

    

_ static  _ to_dict  (  _ filters  _ )  #

    

_ class  _ subgrounds.subgraph.  Object  (  _ subgraph  :  'Subgraph'  _ , _
object  :  'TypeMeta.ObjectMeta  |  TypeMeta.InterfaceMeta'  _ )  #

    

Bases: [ ` object  ` ](../subgrounds.subgraph.object/#module-
subgrounds.subgraph.object "subgrounds.subgraph.object")

_ class  _ subgrounds.subgraph.  Subgraph  (  _ url:  'str',  schema:
'SchemaMeta',  transforms:  'list[DocumentTransform]'  =
[<subgrounds.transform.TypeTransform  object  at  0x7f4e4c37f850>,
<subgrounds.transform.TypeTransform  object  at  0x7f4e4c37e5c0>],
is_subgraph:  'bool'  =  True  _ )  #

    

Bases: [ ` object  ` ](../subgrounds.subgraph.object/#module-
subgrounds.subgraph.object "subgrounds.subgraph.object")

_ class  _ subgrounds.subgraph.  SyntheticField  (  _ f  :  'Callable'  _ , _
type_  :  'TypeRef.T'  _ , _ deps  :  'list[FieldPath  |  SyntheticField]  |
FieldPath  |  SyntheticField'  _ , _ default  :  'Any'  =  None  _ )  #

    

Bases: [ ` FieldOperatorMixin  `
](../subgrounds.subgraph.fieldpath/#subgrounds.subgraph.fieldpath.FieldOperatorMixin
"subgrounds.subgraph.fieldpath.FieldOperatorMixin")

STRING  _ :  ClassVar  [  [ TypeRef.Named
](../subgrounds.schema/#subgrounds.schema.TypeRef.Named
"subgrounds.schema.TypeRef.Named") ]  _ _ =  Named(name_='String',
kind='SCALAR')  _ #

    

INT  _ :  ClassVar  [  [ TypeRef.Named
](../subgrounds.schema/#subgrounds.schema.TypeRef.Named
"subgrounds.schema.TypeRef.Named") ]  _ _ =  Named(name_='Int',
kind='SCALAR')  _ #

    

FLOAT  _ :  ClassVar  [  [ TypeRef.Named
](../subgrounds.schema/#subgrounds.schema.TypeRef.Named
"subgrounds.schema.TypeRef.Named") ]  _ _ =  Named(name_='Float',
kind='SCALAR')  _ #

    

BOOL  _ :  ClassVar  [  [ TypeRef.Named
](../subgrounds.schema/#subgrounds.schema.TypeRef.Named
"subgrounds.schema.TypeRef.Named") ]  _ _ =  Named(name_='Boolean',
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

  * **type** ( [ _TypeRef.T_ ](../subgrounds.schema/#subgrounds.schema.TypeRef.T "subgrounds.schema.TypeRef.T") ) -- The type of the resulting field 

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
    

[ Next  subgrounds.subgraph.fieldpath module
](../subgrounds.subgraph.fieldpath/) [ Previous  subgrounds.pagination.utils
module  ](../subgrounds.pagination.utils/)

Made with [ Furo ](https://github.com/pradyunsg/furo)

[ ](https://github.com/0xPlaygrounds/subgrounds) [
](https://discord.gg/v4r4zhBAh2) [ ](https://twitter.com/Playgrounds0x)

On this page

  * subgrounds.subgraph package 
    * Submodules 
    * Module contents 
      * ` FieldPath  `
      * ` Filter  `
        * ` Filter.field  `
        * ` Filter.op  `
        * ` Filter.value  `
        * ` Filter.Operator  `
          * ` Filter.Operator.EQ  `
          * ` Filter.Operator.NEQ  `
          * ` Filter.Operator.LT  `
          * ` Filter.Operator.LTE  `
          * ` Filter.Operator.GT  `
          * ` Filter.Operator.GTE  `
        * ` Filter.mk_filter()  `
        * ` Filter.name  `
        * ` Filter.to_dict()  `
      * ` Object  `
      * ` Subgraph  `
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

Give us a ⭐️ on [ Github ](https://github.com/0xPlaygrounds/subgrounds) !

Toggle site navigation sidebar

_ _

[ ![Light Logo](../../../_static/assets/pg-logotype-dark.svg) ![Dark
Logo](../../../_static/assets/pg-logotype-primary.svg)
](https://playgrounds.network)

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
      * [ Merging ](../../getting_started/field_paths/merging/)
    * [ Querying ](../../getting_started/querying/)
    * [ Synthetic Fields ](../../getting_started/synthetic_fields/)
  * [ Advanced Topics ](../../advanced_topics/)

Toggle child pages in navigation

_ _

    * [ Pagination ](../../advanced_topics/pagination/)

Toggle child pages in navigation

_ _

      * [ Custom Strategies ](../../advanced_topics/pagination/custom/)
  * [ FAQ ](../../faq/)

Toggle child pages in navigation

_ _

    * [ Setup ](../../faq/setup/)

Toggle child pages in navigation

_ _

      * [ Python Versioning ](../../faq/setup/version_management/)
    * [ Contrib ](../../faq/contrib/)
  * [ Examples ](../../examples/)

Toggle child pages in navigation

_ _

    * [ Exchanges ](../../examples/exchanges/)
    * [ Bridges ](../../examples/bridges/)
    * [ Liquid Staking ](../../examples/liquid_staking/)
    * [ Governance ](../../examples/governance/)
    * [ Advanced Research ](../../examples/advanced_research/)
    * [ Vaults ](../../examples/vaults/)
  * [ Tutorials ](../../tutorials/)
  * [ Changelog ](../../changelog/)
  * [ API Reference ](../../modules/)

Toggle child pages in navigation

_ _

    * [ subgrounds package ](../subgrounds/)

Toggle child pages in navigation

_ _

      * [ subgrounds.pagination package ](../subgrounds.pagination/)

Toggle child pages in navigation

_ _

        * [ subgrounds.pagination.pagination module ](../subgrounds.pagination.pagination/)
        * [ subgrounds.pagination.preprocess module ](../subgrounds.pagination.preprocess/)
        * [ subgrounds.pagination.strategies module ](../subgrounds.pagination.strategies/)
        * [ subgrounds.pagination.utils module ](../subgrounds.pagination.utils/)
      * [ subgrounds.subgraph package ](../subgrounds.subgraph/)

Toggle child pages in navigation

_ _

        * subgrounds.subgraph.fieldpath module 
        * [ subgrounds.subgraph.filter module ](../subgrounds.subgraph.filter/)
        * [ subgrounds.subgraph.object module ](../subgrounds.subgraph.object/)
        * [ subgrounds.subgraph.subgraph module ](../subgrounds.subgraph.subgraph/)
      * [ subgrounds.client module ](../subgrounds.client/)
      * [ subgrounds.dash_wrappers module ](../subgrounds.dash_wrappers/)
      * [ subgrounds.dataframe_utils module ](../subgrounds.dataframe_utils/)
      * [ subgrounds.plotly_wrappers module ](../subgrounds.plotly_wrappers/)
      * [ subgrounds.query module ](../subgrounds.query/)
      * [ subgrounds.schema module ](../subgrounds.schema/)
      * [ subgrounds.subgrounds module ](../subgrounds.subgrounds/)
      * [ subgrounds.transform module ](../subgrounds.transform/)
      * [ subgrounds.utils module ](../subgrounds.utils/)

Back to top

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

_ _

#  subgrounds.subgraph.fieldpath module  #

subgrounds.subgraph.fieldpath.  typeref_of_binary_op  (  _ op  _ , _ t1  _ , _
t2  _ )  #

    

subgrounds.subgraph.fieldpath.  type_ref_of_unary_op  (  _ op  _ , _ t  _ )  #

    

_ class  _ subgrounds.subgraph.fieldpath.  FieldOperatorMixin  #

    

Bases: [ ` object  ` ](https://docs.python.org/3/library/functions.html#object
"\(in Python v3.11\)")

subgrounds.subgraph.fieldpath.  fieldpaths_of_object  (  _ subgraph  _ , _
object_  _ )  #

    

Returns generator of FieldPath objects that selects all non-list fields of
GraphQL Object of Interface ` object_  ` .

Parameters  :

    

  * **schema** ( [ _SchemaMeta_ ](../subgrounds.schema/#subgrounds.schema.SchemaMeta "subgrounds.schema.SchemaMeta") ) -- _description_ 

  * **object** ( [ _TypeMeta.ObjectMeta_ ](../subgrounds.schema/#subgrounds.schema.TypeMeta.ObjectMeta "subgrounds.schema.TypeMeta.ObjectMeta") _|_ [ _TypeMeta.InterfaceMeta_ ](../subgrounds.schema/#subgrounds.schema.TypeMeta.InterfaceMeta "subgrounds.schema.TypeMeta.InterfaceMeta") ) -- _description_ 

Yields  :

    

__type__ \-- _description_

_ class  _ subgrounds.subgraph.fieldpath.  FieldPath  (  _ subgraph  :
'Subgraph'  _ , _ root_type  :  'TypeRef.T'  _ , _ type_  :  'TypeRef.T'  _ ,
_ path  :  'list[Tuple[Optional[dict[str,  Any]],  TypeMeta.FieldMeta]]'  _ )
#

    

Bases:  ` FieldOperatorMixin  `

_ class  _ subgrounds.subgraph.fieldpath.  SyntheticField  (  _ f  :
'Callable'  _ , _ type_  :  'TypeRef.T'  _ , _ deps  :  'list[FieldPath  |
SyntheticField]  |  FieldPath  |  SyntheticField'  _ , _ default  :  'Any'  =
None  _ )  #

    

Bases:  ` FieldOperatorMixin  `

STRING  _ :  ClassVar  [  [ TypeRef.Named
](../subgrounds.schema/#subgrounds.schema.TypeRef.Named
"subgrounds.schema.TypeRef.Named") ]  _ _ =  Named(name_='String',
kind='SCALAR')  _ #

    

INT  _ :  ClassVar  [  [ TypeRef.Named
](../subgrounds.schema/#subgrounds.schema.TypeRef.Named
"subgrounds.schema.TypeRef.Named") ]  _ _ =  Named(name_='Int',
kind='SCALAR')  _ #

    

FLOAT  _ :  ClassVar  [  [ TypeRef.Named
](../subgrounds.schema/#subgrounds.schema.TypeRef.Named
"subgrounds.schema.TypeRef.Named") ]  _ _ =  Named(name_='Float',
kind='SCALAR')  _ #

    

BOOL  _ :  ClassVar  [  [ TypeRef.Named
](../subgrounds.schema/#subgrounds.schema.TypeRef.Named
"subgrounds.schema.TypeRef.Named") ]  _ _ =  Named(name_='Boolean',
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

  * **type** ( [ _TypeRef.T_ ](../subgrounds.schema/#subgrounds.schema.TypeRef.T "subgrounds.schema.TypeRef.T") ) -- The type of the resulting field 

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
    

[ Next  subgrounds.subgraph.filter module  ](../subgrounds.subgraph.filter/) [
Previous  subgrounds.subgraph package  ](../subgrounds.subgraph/)

Made with [ Furo ](https://github.com/pradyunsg/furo)

[ ](https://github.com/0xPlaygrounds/subgrounds) [
](https://discord.gg/v4r4zhBAh2) [ ](https://twitter.com/Playgrounds0x)

On this page

  * subgrounds.subgraph.fieldpath module 
    * ` typeref_of_binary_op()  `
    * ` type_ref_of_unary_op()  `
    * ` FieldOperatorMixin  `
    * ` fieldpaths_of_object()  `
    * ` FieldPath  `
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

Give us a ⭐️ on [ Github ](https://github.com/0xPlaygrounds/subgrounds) !

Toggle site navigation sidebar

_ _

[ ![Light Logo](../../../_static/assets/pg-logotype-dark.svg) ![Dark
Logo](../../../_static/assets/pg-logotype-primary.svg)
](https://playgrounds.network)

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
      * [ Merging ](../../getting_started/field_paths/merging/)
    * [ Querying ](../../getting_started/querying/)
    * [ Synthetic Fields ](../../getting_started/synthetic_fields/)
  * [ Advanced Topics ](../../advanced_topics/)

Toggle child pages in navigation

_ _

    * [ Pagination ](../../advanced_topics/pagination/)

Toggle child pages in navigation

_ _

      * [ Custom Strategies ](../../advanced_topics/pagination/custom/)
  * [ FAQ ](../../faq/)

Toggle child pages in navigation

_ _

    * [ Setup ](../../faq/setup/)

Toggle child pages in navigation

_ _

      * [ Python Versioning ](../../faq/setup/version_management/)
    * [ Contrib ](../../faq/contrib/)
  * [ Examples ](../../examples/)

Toggle child pages in navigation

_ _

    * [ Exchanges ](../../examples/exchanges/)
    * [ Bridges ](../../examples/bridges/)
    * [ Liquid Staking ](../../examples/liquid_staking/)
    * [ Governance ](../../examples/governance/)
    * [ Advanced Research ](../../examples/advanced_research/)
    * [ Vaults ](../../examples/vaults/)
  * [ Tutorials ](../../tutorials/)
  * [ Changelog ](../../changelog/)
  * [ API Reference ](../../modules/)

Toggle child pages in navigation

_ _

    * [ subgrounds package ](../subgrounds/)

Toggle child pages in navigation

_ _

      * [ subgrounds.pagination package ](../subgrounds.pagination/)

Toggle child pages in navigation

_ _

        * [ subgrounds.pagination.pagination module ](../subgrounds.pagination.pagination/)
        * [ subgrounds.pagination.preprocess module ](../subgrounds.pagination.preprocess/)
        * [ subgrounds.pagination.strategies module ](../subgrounds.pagination.strategies/)
        * [ subgrounds.pagination.utils module ](../subgrounds.pagination.utils/)
      * [ subgrounds.subgraph package ](../subgrounds.subgraph/)

Toggle child pages in navigation

_ _

        * [ subgrounds.subgraph.fieldpath module ](../subgrounds.subgraph.fieldpath/)
        * subgrounds.subgraph.filter module 
        * [ subgrounds.subgraph.object module ](../subgrounds.subgraph.object/)
        * [ subgrounds.subgraph.subgraph module ](../subgrounds.subgraph.subgraph/)
      * [ subgrounds.client module ](../subgrounds.client/)
      * [ subgrounds.dash_wrappers module ](../subgrounds.dash_wrappers/)
      * [ subgrounds.dataframe_utils module ](../subgrounds.dataframe_utils/)
      * [ subgrounds.plotly_wrappers module ](../subgrounds.plotly_wrappers/)
      * [ subgrounds.query module ](../subgrounds.query/)
      * [ subgrounds.schema module ](../subgrounds.schema/)
      * [ subgrounds.subgrounds module ](../subgrounds.subgrounds/)
      * [ subgrounds.transform module ](../subgrounds.transform/)
      * [ subgrounds.utils module ](../subgrounds.utils/)

Back to top

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

_ _

#  subgrounds.subgraph.filter module  #

_ class  _ subgrounds.subgraph.filter.  Filter  (  _ field  :
'TypeMeta.FieldMeta'  _ , _ op  :  'Filter.Operator'  _ , _ value  :  'Any'  _
)  #

    

Bases: [ ` object  ` ](https://docs.python.org/3/library/functions.html#object
"\(in Python v3.11\)")

field  _ :  [ FieldMeta
](../subgrounds.schema/#subgrounds.schema.TypeMeta.FieldMeta
"subgrounds.schema.TypeMeta.FieldMeta") _ #

    

op  _ :  Operator  _ #

    

value  _ :  [ Any  ](https://docs.python.org/3/library/typing.html#typing.Any
"\(in Python v3.11\)") _ #

    

_ class  _ Operator  (  _ value  _ )  #

    

Bases: [ ` Enum  ` ](https://docs.python.org/3/library/enum.html#enum.Enum
"\(in Python v3.11\)")

An enumeration.

EQ  _ =  1  _ #

    

NEQ  _ =  2  _ #

    

LT  _ =  3  _ #

    

LTE  _ =  4  _ #

    

GT  _ =  5  _ #

    

GTE  _ =  6  _ #

    

_ static  _ mk_filter  (  _ fpath  _ , _ op  _ , _ value  _ )  #

    

_ property  _ name  #

    

_ static  _ to_dict  (  _ filters  _ )  #

    

[ Next  subgrounds.subgraph.object module  ](../subgrounds.subgraph.object/) [
Previous  subgrounds.subgraph.fieldpath module
](../subgrounds.subgraph.fieldpath/)

Made with [ Furo ](https://github.com/pradyunsg/furo)

[ ](https://github.com/0xPlaygrounds/subgrounds) [
](https://discord.gg/v4r4zhBAh2) [ ](https://twitter.com/Playgrounds0x)

On this page

  * subgrounds.subgraph.filter module 
    * ` Filter  `
      * ` Filter.field  `
      * ` Filter.op  `
      * ` Filter.value  `
      * ` Filter.Operator  `
        * ` Filter.Operator.EQ  `
        * ` Filter.Operator.NEQ  `
        * ` Filter.Operator.LT  `
        * ` Filter.Operator.LTE  `
        * ` Filter.Operator.GT  `
        * ` Filter.Operator.GTE  `
      * ` Filter.mk_filter()  `
      * ` Filter.name  `
      * ` Filter.to_dict()  `



Contents  Menu  Expand  Light mode  Dark mode  Auto light/dark mode

Hide navigation sidebar

Hide table of contents sidebar

Give us a ⭐️ on [ Github ](https://github.com/0xPlaygrounds/subgrounds) !

Toggle site navigation sidebar

_ _

[ ![Light Logo](../../../_static/assets/pg-logotype-dark.svg) ![Dark
Logo](../../../_static/assets/pg-logotype-primary.svg)
](https://playgrounds.network)

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
      * [ Merging ](../../getting_started/field_paths/merging/)
    * [ Querying ](../../getting_started/querying/)
    * [ Synthetic Fields ](../../getting_started/synthetic_fields/)
  * [ Advanced Topics ](../../advanced_topics/)

Toggle child pages in navigation

_ _

    * [ Pagination ](../../advanced_topics/pagination/)

Toggle child pages in navigation

_ _

      * [ Custom Strategies ](../../advanced_topics/pagination/custom/)
  * [ FAQ ](../../faq/)

Toggle child pages in navigation

_ _

    * [ Setup ](../../faq/setup/)

Toggle child pages in navigation

_ _

      * [ Python Versioning ](../../faq/setup/version_management/)
    * [ Contrib ](../../faq/contrib/)
  * [ Examples ](../../examples/)

Toggle child pages in navigation

_ _

    * [ Exchanges ](../../examples/exchanges/)
    * [ Bridges ](../../examples/bridges/)
    * [ Liquid Staking ](../../examples/liquid_staking/)
    * [ Governance ](../../examples/governance/)
    * [ Advanced Research ](../../examples/advanced_research/)
    * [ Vaults ](../../examples/vaults/)
  * [ Tutorials ](../../tutorials/)
  * [ Changelog ](../../changelog/)
  * [ API Reference ](../../modules/)

Toggle child pages in navigation

_ _

    * [ subgrounds package ](../subgrounds/)

Toggle child pages in navigation

_ _

      * [ subgrounds.pagination package ](../subgrounds.pagination/)

Toggle child pages in navigation

_ _

        * [ subgrounds.pagination.pagination module ](../subgrounds.pagination.pagination/)
        * [ subgrounds.pagination.preprocess module ](../subgrounds.pagination.preprocess/)
        * [ subgrounds.pagination.strategies module ](../subgrounds.pagination.strategies/)
        * [ subgrounds.pagination.utils module ](../subgrounds.pagination.utils/)
      * [ subgrounds.subgraph package ](../subgrounds.subgraph/)

Toggle child pages in navigation

_ _

        * [ subgrounds.subgraph.fieldpath module ](../subgrounds.subgraph.fieldpath/)
        * [ subgrounds.subgraph.filter module ](../subgrounds.subgraph.filter/)
        * subgrounds.subgraph.object module 
        * [ subgrounds.subgraph.subgraph module ](../subgrounds.subgraph.subgraph/)
      * [ subgrounds.client module ](../subgrounds.client/)
      * [ subgrounds.dash_wrappers module ](../subgrounds.dash_wrappers/)
      * [ subgrounds.dataframe_utils module ](../subgrounds.dataframe_utils/)
      * [ subgrounds.plotly_wrappers module ](../subgrounds.plotly_wrappers/)
      * [ subgrounds.query module ](../subgrounds.query/)
      * [ subgrounds.schema module ](../subgrounds.schema/)
      * [ subgrounds.subgrounds module ](../subgrounds.subgrounds/)
      * [ subgrounds.transform module ](../subgrounds.transform/)
      * [ subgrounds.utils module ](../subgrounds.utils/)

Back to top

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

_ _

#  subgrounds.subgraph.object module  #

_ class  _ subgrounds.subgraph.object.  Object  (  _ subgraph  :  'Subgraph'
_ , _ object  :  'TypeMeta.ObjectMeta  |  TypeMeta.InterfaceMeta'  _ )  #

    

Bases: [ ` object  ` ](https://docs.python.org/3/library/functions.html#object
"\(in Python v3.11\)")

[ Next  subgrounds.subgraph.subgraph module
](../subgrounds.subgraph.subgraph/) [ Previous  subgrounds.subgraph.filter
module  ](../subgrounds.subgraph.filter/)

Made with [ Furo ](https://github.com/pradyunsg/furo)

[ ](https://github.com/0xPlaygrounds/subgrounds) [
](https://discord.gg/v4r4zhBAh2) [ ](https://twitter.com/Playgrounds0x)

On this page

  * subgrounds.subgraph.object module 
    * ` Object  `



Contents  Menu  Expand  Light mode  Dark mode  Auto light/dark mode

Hide navigation sidebar

Hide table of contents sidebar

Give us a ⭐️ on [ Github ](https://github.com/0xPlaygrounds/subgrounds) !

Toggle site navigation sidebar

_ _

[ ![Light Logo](../../../_static/assets/pg-logotype-dark.svg) ![Dark
Logo](../../../_static/assets/pg-logotype-primary.svg)
](https://playgrounds.network)

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
      * [ Merging ](../../getting_started/field_paths/merging/)
    * [ Querying ](../../getting_started/querying/)
    * [ Synthetic Fields ](../../getting_started/synthetic_fields/)
  * [ Advanced Topics ](../../advanced_topics/)

Toggle child pages in navigation

_ _

    * [ Pagination ](../../advanced_topics/pagination/)

Toggle child pages in navigation

_ _

      * [ Custom Strategies ](../../advanced_topics/pagination/custom/)
  * [ FAQ ](../../faq/)

Toggle child pages in navigation

_ _

    * [ Setup ](../../faq/setup/)

Toggle child pages in navigation

_ _

      * [ Python Versioning ](../../faq/setup/version_management/)
    * [ Contrib ](../../faq/contrib/)
  * [ Examples ](../../examples/)

Toggle child pages in navigation

_ _

    * [ Exchanges ](../../examples/exchanges/)
    * [ Bridges ](../../examples/bridges/)
    * [ Liquid Staking ](../../examples/liquid_staking/)
    * [ Governance ](../../examples/governance/)
    * [ Advanced Research ](../../examples/advanced_research/)
    * [ Vaults ](../../examples/vaults/)
  * [ Tutorials ](../../tutorials/)
  * [ Changelog ](../../changelog/)
  * [ API Reference ](../../modules/)

Toggle child pages in navigation

_ _

    * [ subgrounds package ](../subgrounds/)

Toggle child pages in navigation

_ _

      * [ subgrounds.pagination package ](../subgrounds.pagination/)

Toggle child pages in navigation

_ _

        * [ subgrounds.pagination.pagination module ](../subgrounds.pagination.pagination/)
        * [ subgrounds.pagination.preprocess module ](../subgrounds.pagination.preprocess/)
        * [ subgrounds.pagination.strategies module ](../subgrounds.pagination.strategies/)
        * [ subgrounds.pagination.utils module ](../subgrounds.pagination.utils/)
      * [ subgrounds.subgraph package ](../subgrounds.subgraph/)

Toggle child pages in navigation

_ _

        * [ subgrounds.subgraph.fieldpath module ](../subgrounds.subgraph.fieldpath/)
        * [ subgrounds.subgraph.filter module ](../subgrounds.subgraph.filter/)
        * [ subgrounds.subgraph.object module ](../subgrounds.subgraph.object/)
        * subgrounds.subgraph.subgraph module 
      * [ subgrounds.client module ](../subgrounds.client/)
      * [ subgrounds.dash_wrappers module ](../subgrounds.dash_wrappers/)
      * [ subgrounds.dataframe_utils module ](../subgrounds.dataframe_utils/)
      * [ subgrounds.plotly_wrappers module ](../subgrounds.plotly_wrappers/)
      * [ subgrounds.query module ](../subgrounds.query/)
      * [ subgrounds.schema module ](../subgrounds.schema/)
      * [ subgrounds.subgrounds module ](../subgrounds.subgrounds/)
      * [ subgrounds.transform module ](../subgrounds.transform/)
      * [ subgrounds.utils module ](../subgrounds.utils/)

Back to top

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

_ _

#  subgrounds.subgraph.subgraph module  #

Subgraph module that defines various classes to manipulate requests and
subgraphs.

This module is the glue that connects the lower level modules (i.e.:
:module:`query`  ,  :module:`schema`  ,  :module:`transform`  ,
:module:`pagination`  ) to the higher toplevel modules (i.e.:
:module:`subgrounds`  ).

_ class  _ subgrounds.subgraph.subgraph.  Subgraph  (  _ url:  'str',  schema:
'SchemaMeta',  transforms:  'list[DocumentTransform]'  =
[<subgrounds.transform.TypeTransform  object  at  0x7f4e4c37f850>,
<subgrounds.transform.TypeTransform  object  at  0x7f4e4c37e5c0>],
is_subgraph:  'bool'  =  True  _ )  #

    

Bases: [ ` object  ` ](https://docs.python.org/3/library/functions.html#object
"\(in Python v3.11\)")

[ Next  subgrounds.client module  ](../subgrounds.client/) [ Previous
subgrounds.subgraph.object module  ](../subgrounds.subgraph.object/)

Made with [ Furo ](https://github.com/pradyunsg/furo)

[ ](https://github.com/0xPlaygrounds/subgrounds) [
](https://discord.gg/v4r4zhBAh2) [ ](https://twitter.com/Playgrounds0x)

On this page

  * subgrounds.subgraph.subgraph module 
    * ` Subgraph  `



Contents  Menu  Expand  Light mode  Dark mode  Auto light/dark mode

Hide navigation sidebar

Hide table of contents sidebar

Give us a ⭐️ on [ Github ](https://github.com/0xPlaygrounds/subgrounds) !

Toggle site navigation sidebar

_ _

[ ![Light Logo](../../../_static/assets/pg-logotype-dark.svg) ![Dark
Logo](../../../_static/assets/pg-logotype-primary.svg)
](https://playgrounds.network)

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
      * [ Merging ](../../getting_started/field_paths/merging/)
    * [ Querying ](../../getting_started/querying/)
    * [ Synthetic Fields ](../../getting_started/synthetic_fields/)
  * [ Advanced Topics ](../../advanced_topics/)

Toggle child pages in navigation

_ _

    * [ Pagination ](../../advanced_topics/pagination/)

Toggle child pages in navigation

_ _

      * [ Custom Strategies ](../../advanced_topics/pagination/custom/)
  * [ FAQ ](../../faq/)

Toggle child pages in navigation

_ _

    * [ Setup ](../../faq/setup/)

Toggle child pages in navigation

_ _

      * [ Python Versioning ](../../faq/setup/version_management/)
    * [ Contrib ](../../faq/contrib/)
  * [ Examples ](../../examples/)

Toggle child pages in navigation

_ _

    * [ Exchanges ](../../examples/exchanges/)
    * [ Bridges ](../../examples/bridges/)
    * [ Liquid Staking ](../../examples/liquid_staking/)
    * [ Governance ](../../examples/governance/)
    * [ Advanced Research ](../../examples/advanced_research/)
    * [ Vaults ](../../examples/vaults/)
  * [ Tutorials ](../../tutorials/)
  * [ Changelog ](../../changelog/)
  * [ API Reference ](../../modules/)

Toggle child pages in navigation

_ _

    * [ subgrounds package ](../subgrounds/)

Toggle child pages in navigation

_ _

      * [ subgrounds.pagination package ](../subgrounds.pagination/)

Toggle child pages in navigation

_ _

        * [ subgrounds.pagination.pagination module ](../subgrounds.pagination.pagination/)
        * [ subgrounds.pagination.preprocess module ](../subgrounds.pagination.preprocess/)
        * [ subgrounds.pagination.strategies module ](../subgrounds.pagination.strategies/)
        * [ subgrounds.pagination.utils module ](../subgrounds.pagination.utils/)
      * [ subgrounds.subgraph package ](../subgrounds.subgraph/)

Toggle child pages in navigation

_ _

        * [ subgrounds.subgraph.fieldpath module ](../subgrounds.subgraph.fieldpath/)
        * [ subgrounds.subgraph.filter module ](../subgrounds.subgraph.filter/)
        * [ subgrounds.subgraph.object module ](../subgrounds.subgraph.object/)
        * [ subgrounds.subgraph.subgraph module ](../subgrounds.subgraph.subgraph/)
      * subgrounds.client module 
      * [ subgrounds.dash_wrappers module ](../subgrounds.dash_wrappers/)
      * [ subgrounds.dataframe_utils module ](../subgrounds.dataframe_utils/)
      * [ subgrounds.plotly_wrappers module ](../subgrounds.plotly_wrappers/)
      * [ subgrounds.query module ](../subgrounds.query/)
      * [ subgrounds.schema module ](../subgrounds.schema/)
      * [ subgrounds.subgrounds module ](../subgrounds.subgrounds/)
      * [ subgrounds.transform module ](../subgrounds.transform/)
      * [ subgrounds.utils module ](../subgrounds.utils/)

Back to top

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

_ _

#  subgrounds.client module  #

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

  * **ServerError** \-- If server responds back non-json content 

  * **GraphQLError** \-- If the GraphQL query failed or other grapql server errors 

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

  * **ServerError** \-- If server responds back non-json content 

  * **GraphQLError** \-- If the GraphQL query failed or other grapql server errors 

Returns  :

    

Response data

Return type  :

    

[ dict ](https://docs.python.org/3/library/stdtypes.html#dict "\(in Python
v3.11\)") [ [ str ](https://docs.python.org/3/library/stdtypes.html#str "\(in
Python v3.11\)") , Any]

[ Next  subgrounds.dash_wrappers module  ](../subgrounds.dash_wrappers/) [
Previous  subgrounds.subgraph.subgraph module
](../subgrounds.subgraph.subgraph/)

Made with [ Furo ](https://github.com/pradyunsg/furo)

[ ](https://github.com/0xPlaygrounds/subgrounds) [
](https://discord.gg/v4r4zhBAh2) [ ](https://twitter.com/Playgrounds0x)

On this page

  * subgrounds.client module 
    * ` get_schema()  `
    * ` query()  `



Contents  Menu  Expand  Light mode  Dark mode  Auto light/dark mode

Hide navigation sidebar

Hide table of contents sidebar

Give us a ⭐️ on [ Github ](https://github.com/0xPlaygrounds/subgrounds) !

Toggle site navigation sidebar

_ _

[ ![Light Logo](../../../_static/assets/pg-logotype-dark.svg) ![Dark
Logo](../../../_static/assets/pg-logotype-primary.svg)
](https://playgrounds.network)

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
      * [ Merging ](../../getting_started/field_paths/merging/)
    * [ Querying ](../../getting_started/querying/)
    * [ Synthetic Fields ](../../getting_started/synthetic_fields/)
  * [ Advanced Topics ](../../advanced_topics/)

Toggle child pages in navigation

_ _

    * [ Pagination ](../../advanced_topics/pagination/)

Toggle child pages in navigation

_ _

      * [ Custom Strategies ](../../advanced_topics/pagination/custom/)
  * [ FAQ ](../../faq/)

Toggle child pages in navigation

_ _

    * [ Setup ](../../faq/setup/)

Toggle child pages in navigation

_ _

      * [ Python Versioning ](../../faq/setup/version_management/)
    * [ Contrib ](../../faq/contrib/)
  * [ Examples ](../../examples/)

Toggle child pages in navigation

_ _

    * [ Exchanges ](../../examples/exchanges/)
    * [ Bridges ](../../examples/bridges/)
    * [ Liquid Staking ](../../examples/liquid_staking/)
    * [ Governance ](../../examples/governance/)
    * [ Advanced Research ](../../examples/advanced_research/)
    * [ Vaults ](../../examples/vaults/)
  * [ Tutorials ](../../tutorials/)
  * [ Changelog ](../../changelog/)
  * [ API Reference ](../../modules/)

Toggle child pages in navigation

_ _

    * [ subgrounds package ](../subgrounds/)

Toggle child pages in navigation

_ _

      * [ subgrounds.pagination package ](../subgrounds.pagination/)

Toggle child pages in navigation

_ _

        * [ subgrounds.pagination.pagination module ](../subgrounds.pagination.pagination/)
        * [ subgrounds.pagination.preprocess module ](../subgrounds.pagination.preprocess/)
        * [ subgrounds.pagination.strategies module ](../subgrounds.pagination.strategies/)
        * [ subgrounds.pagination.utils module ](../subgrounds.pagination.utils/)
      * [ subgrounds.subgraph package ](../subgrounds.subgraph/)

Toggle child pages in navigation

_ _

        * [ subgrounds.subgraph.fieldpath module ](../subgrounds.subgraph.fieldpath/)
        * [ subgrounds.subgraph.filter module ](../subgrounds.subgraph.filter/)
        * [ subgrounds.subgraph.object module ](../subgrounds.subgraph.object/)
        * [ subgrounds.subgraph.subgraph module ](../subgrounds.subgraph.subgraph/)
      * [ subgrounds.client module ](../subgrounds.client/)
      * subgrounds.dash_wrappers module 
      * [ subgrounds.dataframe_utils module ](../subgrounds.dataframe_utils/)
      * [ subgrounds.plotly_wrappers module ](../subgrounds.plotly_wrappers/)
      * [ subgrounds.query module ](../subgrounds.query/)
      * [ subgrounds.schema module ](../subgrounds.schema/)
      * [ subgrounds.subgrounds module ](../subgrounds.subgrounds/)
      * [ subgrounds.transform module ](../subgrounds.transform/)
      * [ subgrounds.utils module ](../subgrounds.utils/)

Back to top

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

_ _

#  subgrounds.dash_wrappers module  #

DEPRECIATED: Use  subgrounds.contrib.dash  instead

_ class  _ subgrounds.dash_wrappers.  Refreshable  #

    

Bases: [ ` ABC  ` ](https://docs.python.org/3/library/abc.html#abc.ABC "\(in
Python v3.11\)")

_ abstract  property  _ dash_dependencies  _ :  [ list
](https://docs.python.org/3/library/stdtypes.html#list "\(in Python v3.11\)")
[  dash.dependencies.Output  ]  _ #

    

_ abstract  property  _ dash_dependencies_outputs  _ :  [ list
](https://docs.python.org/3/library/stdtypes.html#list "\(in Python v3.11\)")
[  [ Any  ](https://docs.python.org/3/library/typing.html#typing.Any "\(in
Python v3.11\)") ]  _ #

    

_ class  _ subgrounds.dash_wrappers.  Graph  (  _ fig  _ , _ **  kwargs  _ )
#

    

Bases: ` Graph  ` ,  ` Refreshable  `

counter  _ :  [ ClassVar
](https://docs.python.org/3/library/typing.html#typing.ClassVar "\(in Python
v3.11\)") [  [ int  ](https://docs.python.org/3/library/functions.html#int
"\(in Python v3.11\)") ]  _ _ =  0  _ #

    

wrapped_figure  _ :  [ Figure
](../subgrounds.plotly_wrappers/#subgrounds.plotly_wrappers.Figure
"subgrounds.contrib.plotly.figure.Figure") _ #

    

_ property  _ dash_dependencies  _ :  [ list
](https://docs.python.org/3/library/stdtypes.html#list "\(in Python v3.11\)")
[  dash.dependencies.Output  ]  _ #

    

_ property  _ dash_dependencies_outputs  _ :  [ list
](https://docs.python.org/3/library/stdtypes.html#list "\(in Python v3.11\)")
[  [ Any  ](https://docs.python.org/3/library/typing.html#typing.Any "\(in
Python v3.11\)") ]  _ #

    

_ class  _ subgrounds.dash_wrappers.  DataTable  (  _ subgrounds  _ , _ data
_ , _ columns  =  None  _ , _ concat  =  False  _ , _ append  =  False  _ , _
**  kwargs  _ )  #

    

Bases: ` DataTable  ` ,  ` Refreshable  `

counter  _ :  [ ClassVar
](https://docs.python.org/3/library/typing.html#typing.ClassVar "\(in Python
v3.11\)") [  [ int  ](https://docs.python.org/3/library/functions.html#int
"\(in Python v3.11\)") ]  _ _ =  0  _ #

    

data  _ :  [ list  ](https://docs.python.org/3/library/stdtypes.html#list
"\(in Python v3.11\)") [  [ subgrounds.subgraph.fieldpath.FieldPath
](../subgrounds.subgraph.fieldpath/#subgrounds.subgraph.fieldpath.FieldPath
"subgrounds.subgraph.fieldpath.FieldPath") ]  _ #

    

columns  _ :  [ list  ](https://docs.python.org/3/library/stdtypes.html#list
"\(in Python v3.11\)") [  [ str
](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.11\)") ]
|  [ None  ](https://docs.python.org/3/library/constants.html#None "\(in
Python v3.11\)") _ #

    

subgrounds  _ :  [ Subgrounds
](../subgrounds.subgrounds/#subgrounds.subgrounds.Subgrounds
"subgrounds.subgrounds.Subgrounds") _ #

    

concat  _ :  [ bool  ](https://docs.python.org/3/library/functions.html#bool
"\(in Python v3.11\)") _ #

    

append  _ :  [ bool  ](https://docs.python.org/3/library/functions.html#bool
"\(in Python v3.11\)") _ #

    

df  _ :  [ pandas.core.frame.DataFrame  ](http://pandas.pydata.org/pandas-
docs/dev/reference/api/pandas.DataFrame.html#pandas.DataFrame "\(in pandas
v2.1.0.dev0+1123.g866a388412\)") |  [ list
](https://docs.python.org/3/library/stdtypes.html#list "\(in Python v3.11\)")
[  [ pandas.core.frame.DataFrame  ](http://pandas.pydata.org/pandas-
docs/dev/reference/api/pandas.DataFrame.html#pandas.DataFrame "\(in pandas
v2.1.0.dev0+1123.g866a388412\)") ]  |  [ None
](https://docs.python.org/3/library/constants.html#None "\(in Python v3.11\)")
_ #

    

refresh  (  )  #

    

_ property  _ dash_dependencies  _ :  [ list
](https://docs.python.org/3/library/stdtypes.html#list "\(in Python v3.11\)")
[  dash.dependencies.Output  ]  _ #

    

_ property  _ dash_dependencies_outputs  _ :  [ list
](https://docs.python.org/3/library/stdtypes.html#list "\(in Python v3.11\)")
[  dash.dependencies.Output  ]  _ #

    

_ class  _ subgrounds.dash_wrappers.  AutoUpdate  (  _ app  _ , _ sec_interval
=  1  _ , _ children  =  []  _ , _ **  kwargs  _ )  #

    

Bases: ` Div  `

counter  _ :  [ ClassVar
](https://docs.python.org/3/library/typing.html#typing.ClassVar "\(in Python
v3.11\)") [  [ int  ](https://docs.python.org/3/library/functions.html#int
"\(in Python v3.11\)") ]  _ _ =  0  _ #

    

[ Next  subgrounds.dataframe_utils module  ](../subgrounds.dataframe_utils/) [
Previous  subgrounds.client module  ](../subgrounds.client/)

Made with [ Furo ](https://github.com/pradyunsg/furo)

[ ](https://github.com/0xPlaygrounds/subgrounds) [
](https://discord.gg/v4r4zhBAh2) [ ](https://twitter.com/Playgrounds0x)

On this page

  * subgrounds.dash_wrappers module 
    * ` Refreshable  `
      * ` Refreshable.dash_dependencies  `
      * ` Refreshable.dash_dependencies_outputs  `
    * ` Graph  `
      * ` Graph.counter  `
      * ` Graph.wrapped_figure  `
      * ` Graph.dash_dependencies  `
      * ` Graph.dash_dependencies_outputs  `
    * ` DataTable  `
      * ` DataTable.counter  `
      * ` DataTable.data  `
      * ` DataTable.columns  `
      * ` DataTable.subgrounds  `
      * ` DataTable.concat  `
      * ` DataTable.append  `
      * ` DataTable.df  `
      * ` DataTable.refresh()  `
      * ` DataTable.dash_dependencies  `
      * ` DataTable.dash_dependencies_outputs  `
    * ` AutoUpdate  `
      * ` AutoUpdate.counter  `



Contents  Menu  Expand  Light mode  Dark mode  Auto light/dark mode

Hide navigation sidebar

Hide table of contents sidebar

Give us a ⭐️ on [ Github ](https://github.com/0xPlaygrounds/subgrounds) !

Toggle site navigation sidebar

_ _

[ ![Light Logo](../../../_static/assets/pg-logotype-dark.svg) ![Dark
Logo](../../../_static/assets/pg-logotype-primary.svg)
](https://playgrounds.network)

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
      * [ Merging ](../../getting_started/field_paths/merging/)
    * [ Querying ](../../getting_started/querying/)
    * [ Synthetic Fields ](../../getting_started/synthetic_fields/)
  * [ Advanced Topics ](../../advanced_topics/)

Toggle child pages in navigation

_ _

    * [ Pagination ](../../advanced_topics/pagination/)

Toggle child pages in navigation

_ _

      * [ Custom Strategies ](../../advanced_topics/pagination/custom/)
  * [ FAQ ](../../faq/)

Toggle child pages in navigation

_ _

    * [ Setup ](../../faq/setup/)

Toggle child pages in navigation

_ _

      * [ Python Versioning ](../../faq/setup/version_management/)
    * [ Contrib ](../../faq/contrib/)
  * [ Examples ](../../examples/)

Toggle child pages in navigation

_ _

    * [ Exchanges ](../../examples/exchanges/)
    * [ Bridges ](../../examples/bridges/)
    * [ Liquid Staking ](../../examples/liquid_staking/)
    * [ Governance ](../../examples/governance/)
    * [ Advanced Research ](../../examples/advanced_research/)
    * [ Vaults ](../../examples/vaults/)
  * [ Tutorials ](../../tutorials/)
  * [ Changelog ](../../changelog/)
  * [ API Reference ](../../modules/)

Toggle child pages in navigation

_ _

    * [ subgrounds package ](../subgrounds/)

Toggle child pages in navigation

_ _

      * [ subgrounds.pagination package ](../subgrounds.pagination/)

Toggle child pages in navigation

_ _

        * [ subgrounds.pagination.pagination module ](../subgrounds.pagination.pagination/)
        * [ subgrounds.pagination.preprocess module ](../subgrounds.pagination.preprocess/)
        * [ subgrounds.pagination.strategies module ](../subgrounds.pagination.strategies/)
        * [ subgrounds.pagination.utils module ](../subgrounds.pagination.utils/)
      * [ subgrounds.subgraph package ](../subgrounds.subgraph/)

Toggle child pages in navigation

_ _

        * [ subgrounds.subgraph.fieldpath module ](../subgrounds.subgraph.fieldpath/)
        * [ subgrounds.subgraph.filter module ](../subgrounds.subgraph.filter/)
        * [ subgrounds.subgraph.object module ](../subgrounds.subgraph.object/)
        * [ subgrounds.subgraph.subgraph module ](../subgrounds.subgraph.subgraph/)
      * [ subgrounds.client module ](../subgrounds.client/)
      * [ subgrounds.dash_wrappers module ](../subgrounds.dash_wrappers/)
      * subgrounds.dataframe_utils module 
      * [ subgrounds.plotly_wrappers module ](../subgrounds.plotly_wrappers/)
      * [ subgrounds.query module ](../subgrounds.query/)
      * [ subgrounds.schema module ](../subgrounds.schema/)
      * [ subgrounds.subgrounds module ](../subgrounds.subgrounds/)
      * [ subgrounds.transform module ](../subgrounds.transform/)
      * [ subgrounds.utils module ](../subgrounds.utils/)

Back to top

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

_ _

#  subgrounds.dataframe_utils module  #

Pandas DataFrame utility module containing functions related to the formatting
of GraphQL JSON data into DataFrames.

subgrounds.dataframe_utils.  gen_columns  (  _ data  _ , _ prefix  =  ''  _ )
#

    

subgrounds.dataframe_utils.  fmt_cols  (  _ df  _ , _ col_map  _ )  #

    

_ class  _ subgrounds.dataframe_utils.  DataFrameColumns  (  _ key  _ , _
fpaths  _ )  #

    

Bases: [ ` object  ` ](https://docs.python.org/3/library/functions.html#object
"\(in Python v3.11\)")

Helper class that holds data related to the shape of a DataFrame

key  _ :  [ str  ](https://docs.python.org/3/library/stdtypes.html#str "\(in
Python v3.11\)") _ #

    

fpaths  _ :  [ list  ](https://docs.python.org/3/library/stdtypes.html#list
"\(in Python v3.11\)") [  [ str
](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.11\)") ]
_ #

    

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

  * **path_map** ( [ _dict_ ](https://docs.python.org/3/library/stdtypes.html#dict "\(in Python v3.11\)") _[_ [ _str_ ](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.11\)") _,_ [ _FieldPath_ ](../subgrounds/#subgrounds.FieldPath "subgrounds.FieldPath") _]_ ) -- A dictionary of ` (key-FieldPath)  ` pairs 

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
_[_ [ _Selection_ ](../subgrounds.query/#subgrounds.query.Selection
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

  * **fpaths** ( [ _list_ ](https://docs.python.org/3/library/stdtypes.html#list "\(in Python v3.11\)") _[_ [ _FieldPath_ ](../subgrounds/#subgrounds.FieldPath "subgrounds.FieldPath") _]_ ) -- Fieldpaths that yielded the response data 

  * **columns** ( _Optional_ _[_ [ _list_ ](https://docs.python.org/3/library/stdtypes.html#list "\(in Python v3.11\)") _[_ [ _str_ ](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.11\)") _]_ _]_ _,_ _optional_ ) -- Column names. Defaults to None. 

  * **concat** ( [ _bool_ ](https://docs.python.org/3/library/functions.html#bool "\(in Python v3.11\)") _,_ _optional_ ) -- Flag indicating whether or not to concatenate the resulting dataframes, if there are more than one. Defaults to False. 

Returns  :

    

The resulting dataframe(s)

Return type  :

    

pd.DataFrame | [ list ](https://docs.python.org/3/library/stdtypes.html#list
"\(in Python v3.11\)") [pd.DataFrame]

[ Next  subgrounds.plotly_wrappers module  ](../subgrounds.plotly_wrappers/) [
Previous  subgrounds.dash_wrappers module  ](../subgrounds.dash_wrappers/)

Made with [ Furo ](https://github.com/pradyunsg/furo)

[ ](https://github.com/0xPlaygrounds/subgrounds) [
](https://discord.gg/v4r4zhBAh2) [ ](https://twitter.com/Playgrounds0x)

On this page

  * subgrounds.dataframe_utils module 
    * ` gen_columns()  `
    * ` fmt_cols()  `
    * ` DataFrameColumns  `
      * ` DataFrameColumns.key  `
      * ` DataFrameColumns.fpaths  `
      * ` DataFrameColumns.combine()  `
      * ` DataFrameColumns.mk_df()  `
    * ` columns_of_selections()  `
    * ` df_of_json()  `



Contents  Menu  Expand  Light mode  Dark mode  Auto light/dark mode

Hide navigation sidebar

Hide table of contents sidebar

Give us a ⭐️ on [ Github ](https://github.com/0xPlaygrounds/subgrounds) !

Toggle site navigation sidebar

_ _

[ ![Light Logo](../../../_static/assets/pg-logotype-dark.svg) ![Dark
Logo](../../../_static/assets/pg-logotype-primary.svg)
](https://playgrounds.network)

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
      * [ Merging ](../../getting_started/field_paths/merging/)
    * [ Querying ](../../getting_started/querying/)
    * [ Synthetic Fields ](../../getting_started/synthetic_fields/)
  * [ Advanced Topics ](../../advanced_topics/)

Toggle child pages in navigation

_ _

    * [ Pagination ](../../advanced_topics/pagination/)

Toggle child pages in navigation

_ _

      * [ Custom Strategies ](../../advanced_topics/pagination/custom/)
  * [ FAQ ](../../faq/)

Toggle child pages in navigation

_ _

    * [ Setup ](../../faq/setup/)

Toggle child pages in navigation

_ _

      * [ Python Versioning ](../../faq/setup/version_management/)
    * [ Contrib ](../../faq/contrib/)
  * [ Examples ](../../examples/)

Toggle child pages in navigation

_ _

    * [ Exchanges ](../../examples/exchanges/)
    * [ Bridges ](../../examples/bridges/)
    * [ Liquid Staking ](../../examples/liquid_staking/)
    * [ Governance ](../../examples/governance/)
    * [ Advanced Research ](../../examples/advanced_research/)
    * [ Vaults ](../../examples/vaults/)
  * [ Tutorials ](../../tutorials/)
  * [ Changelog ](../../changelog/)
  * [ API Reference ](../../modules/)

Toggle child pages in navigation

_ _

    * [ subgrounds package ](../subgrounds/)

Toggle child pages in navigation

_ _

      * [ subgrounds.pagination package ](../subgrounds.pagination/)

Toggle child pages in navigation

_ _

        * [ subgrounds.pagination.pagination module ](../subgrounds.pagination.pagination/)
        * [ subgrounds.pagination.preprocess module ](../subgrounds.pagination.preprocess/)
        * [ subgrounds.pagination.strategies module ](../subgrounds.pagination.strategies/)
        * [ subgrounds.pagination.utils module ](../subgrounds.pagination.utils/)
      * [ subgrounds.subgraph package ](../subgrounds.subgraph/)

Toggle child pages in navigation

_ _

        * [ subgrounds.subgraph.fieldpath module ](../subgrounds.subgraph.fieldpath/)
        * [ subgrounds.subgraph.filter module ](../subgrounds.subgraph.filter/)
        * [ subgrounds.subgraph.object module ](../subgrounds.subgraph.object/)
        * [ subgrounds.subgraph.subgraph module ](../subgrounds.subgraph.subgraph/)
      * [ subgrounds.client module ](../subgrounds.client/)
      * [ subgrounds.dash_wrappers module ](../subgrounds.dash_wrappers/)
      * [ subgrounds.dataframe_utils module ](../subgrounds.dataframe_utils/)
      * subgrounds.plotly_wrappers module 
      * [ subgrounds.query module ](../subgrounds.query/)
      * [ subgrounds.schema module ](../subgrounds.schema/)
      * [ subgrounds.subgrounds module ](../subgrounds.subgrounds/)
      * [ subgrounds.transform module ](../subgrounds.transform/)
      * [ subgrounds.utils module ](../subgrounds.utils/)

Back to top

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

_ _

#  subgrounds.plotly_wrappers module  #

DEPRECIATED: Use  subgrounds.contrib.plotly  instead

_ class  _ subgrounds.plotly_wrappers.  Figure  (  _ subgrounds  _ , _ traces
_ , _ **  kwargs  _ )  #

    

Bases: [ ` object  ` ](https://docs.python.org/3/library/functions.html#object
"\(in Python v3.11\)")

figure  _ :  Figure  _ #

    

subgrounds  _ :  [ Subgrounds
](../subgrounds.subgrounds/#subgrounds.subgrounds.Subgrounds
"subgrounds.subgrounds.Subgrounds") _ #

    

traces  _ :  [ list  ](https://docs.python.org/3/library/stdtypes.html#list
"\(in Python v3.11\)") [  subgrounds.contrib.plotly.traces.TraceWrapper  ]  _
#

    

req  _ :  [ subgrounds.query.DataRequest
](../subgrounds.query/#subgrounds.query.DataRequest
"subgrounds.query.DataRequest") |  [ None
](https://docs.python.org/3/library/constants.html#None "\(in Python v3.11\)")
_ #

    

data  _ :  [ list  ](https://docs.python.org/3/library/stdtypes.html#list
"\(in Python v3.11\)") [  [ dict
](https://docs.python.org/3/library/stdtypes.html#dict "\(in Python v3.11\)")
[  [ str  ](https://docs.python.org/3/library/stdtypes.html#str "\(in Python
v3.11\)") ,  [ Any  ](https://docs.python.org/3/library/typing.html#typing.Any
"\(in Python v3.11\)") ]  ]  |  [ None
](https://docs.python.org/3/library/constants.html#None "\(in Python v3.11\)")
_ #

    

args  _ :  [ dict  ](https://docs.python.org/3/library/stdtypes.html#dict
"\(in Python v3.11\)") [  [ str
](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.11\)") ,
[ Any  ](https://docs.python.org/3/library/typing.html#typing.Any "\(in Python
v3.11\)") ]  _ #

    

refresh  (  )  #

    

_ class  _ subgrounds.plotly_wrappers.  TraceWrapper  (  _ **  kwargs  _ )  #

    

Bases: [ ` ABC  ` ](https://docs.python.org/3/library/abc.html#abc.ABC "\(in
Python v3.11\)")

graph_object  _ :  BaseTraceType  _ #

    

fpaths  _ :  [ dict  ](https://docs.python.org/3/library/stdtypes.html#dict
"\(in Python v3.11\)") [  [ str
](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.11\)") ,
[ subgrounds.subgraph.fieldpath.FieldPath
](../subgrounds.subgraph.fieldpath/#subgrounds.subgraph.fieldpath.FieldPath
"subgrounds.subgraph.fieldpath.FieldPath") ]  _ #

    

args  _ :  [ dict  ](https://docs.python.org/3/library/stdtypes.html#dict
"\(in Python v3.11\)") [  [ str
](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.11\)") ,
[ Any  ](https://docs.python.org/3/library/typing.html#typing.Any "\(in Python
v3.11\)") ]  _ #

    

mk_trace  (  _ data  _ )  #

    

_ property  _ field_paths  _ :  [ list
](https://docs.python.org/3/library/stdtypes.html#list "\(in Python v3.11\)")
[  [ subgrounds.subgraph.fieldpath.FieldPath
](../subgrounds.subgraph.fieldpath/#subgrounds.subgraph.fieldpath.FieldPath
"subgrounds.subgraph.fieldpath.FieldPath") ]  _ #

    

_ class  _ subgrounds.plotly_wrappers.  Scatter  (  _ **  kwargs  _ )  #

    

Bases:  ` TraceWrapper  `

See [ https://plotly.com/python/line-and-scatter/
](https://plotly.com/python/line-and-scatter/)

graph_object  #

    

alias of ` Scatter  `

_ class  _ subgrounds.plotly_wrappers.  Pie  (  _ **  kwargs  _ )  #

    

Bases:  ` TraceWrapper  `

See [ https://plotly.com/python/pie-charts/ ](https://plotly.com/python/pie-
charts/)

graph_object  #

    

alias of ` Pie  `

_ class  _ subgrounds.plotly_wrappers.  Bar  (  _ **  kwargs  _ )  #

    

Bases:  ` TraceWrapper  `

See [ https://plotly.com/python/bar-charts/ ](https://plotly.com/python/bar-
charts/)

graph_object  #

    

alias of ` Bar  `

_ class  _ subgrounds.plotly_wrappers.  Heatmap  (  _ **  kwargs  _ )  #

    

Bases:  ` TraceWrapper  `

See [ https://plotly.com/python/heatmaps/
](https://plotly.com/python/heatmaps/)

graph_object  #

    

alias of ` Heatmap  `

_ class  _ subgrounds.plotly_wrappers.  Contour  (  _ **  kwargs  _ )  #

    

Bases:  ` TraceWrapper  `

See [ https://plotly.com/python/contour-plots/
](https://plotly.com/python/contour-plots/)

graph_object  #

    

alias of ` Contour  `

_ class  _ subgrounds.plotly_wrappers.  Table  (  _ **  kwargs  _ )  #

    

Bases:  ` TraceWrapper  `

See [ https://plotly.com/python/contour-plots/
](https://plotly.com/python/contour-plots/)

graph_object  #

    

alias of ` Table  `

_ class  _ subgrounds.plotly_wrappers.  Box  (  _ **  kwargs  _ )  #

    

Bases:  ` TraceWrapper  `

See [ https://plotly.com/python/box-plots/ ](https://plotly.com/python/box-
plots/)

graph_object  #

    

alias of ` Box  `

_ class  _ subgrounds.plotly_wrappers.  Violin  (  _ **  kwargs  _ )  #

    

Bases:  ` TraceWrapper  `

See [ https://plotly.com/python/violin/ ](https://plotly.com/python/violin/)

graph_object  #

    

alias of ` Violin  `

_ class  _ subgrounds.plotly_wrappers.  Histogram  (  _ **  kwargs  _ )  #

    

Bases:  ` TraceWrapper  `

See [ https://plotly.com/python/histograms/
](https://plotly.com/python/histograms/)

graph_object  #

    

alias of ` Histogram  `

_ class  _ subgrounds.plotly_wrappers.  Histogram2d  (  _ **  kwargs  _ )  #

    

Bases:  ` TraceWrapper  `

See [ https://plotly.com/python/2D-Histogram/
](https://plotly.com/python/2D-Histogram/)

graph_object  #

    

alias of ` Histogram2d  `

_ class  _ subgrounds.plotly_wrappers.  Histogram2dContour  (  _ **  kwargs  _
)  #

    

Bases:  ` TraceWrapper  `

See [ https://plotly.com/python/2d-histogram-contour/
](https://plotly.com/python/2d-histogram-contour/)

graph_object  #

    

alias of ` Histogram2dContour  `

_ class  _ subgrounds.plotly_wrappers.  Ohlc  (  _ **  kwargs  _ )  #

    

Bases:  ` TraceWrapper  `

See [ https://plotly.com/python/ohlc-charts/ ](https://plotly.com/python/ohlc-
charts/)

graph_object  #

    

alias of ` Ohlc  `

_ class  _ subgrounds.plotly_wrappers.  Candlestick  (  _ **  kwargs  _ )  #

    

Bases:  ` TraceWrapper  `

See [ https://plotly.com/python/candlestick-charts/
](https://plotly.com/python/candlestick-charts/)

graph_object  #

    

alias of ` Candlestick  `

_ class  _ subgrounds.plotly_wrappers.  Waterfall  (  _ **  kwargs  _ )  #

    

Bases:  ` TraceWrapper  `

See [ https://plotly.com/python/waterfall-charts/
](https://plotly.com/python/waterfall-charts/)

graph_object  #

    

alias of ` Waterfall  `

_ class  _ subgrounds.plotly_wrappers.  Funnel  (  _ **  kwargs  _ )  #

    

Bases:  ` TraceWrapper  `

See [ https://plotly.com/python/funnel-charts/
](https://plotly.com/python/funnel-charts/)

graph_object  #

    

alias of ` Funnel  `

_ class  _ subgrounds.plotly_wrappers.  Indicator  (  _ **  kwargs  _ )  #

    

Bases:  ` TraceWrapper  `

See [ https://plotly.com/python/indicator/
](https://plotly.com/python/indicator/)

graph_object  #

    

alias of ` Indicator  `

_ class  _ subgrounds.plotly_wrappers.  Scatter3d  (  _ **  kwargs  _ )  #

    

Bases:  ` TraceWrapper  `

See [ https://plotly.com/python/3d-scatter-plots/
](https://plotly.com/python/3d-scatter-plots/)

graph_object  #

    

alias of ` Scatter3d  `

_ class  _ subgrounds.plotly_wrappers.  Surface  (  _ **  kwargs  _ )  #

    

Bases:  ` TraceWrapper  `

See [ https://plotly.com/python/3d-surface-plots/
](https://plotly.com/python/3d-surface-plots/)

graph_object  #

    

alias of ` Surface  `

_ class  _ subgrounds.plotly_wrappers.  Scattergeo  (  _ **  kwargs  _ )  #

    

Bases:  ` TraceWrapper  `

See [ https://plotly.com/python/scatter-plots-on-maps/
](https://plotly.com/python/scatter-plots-on-maps/)

graph_object  #

    

alias of ` Scattergeo  `

_ class  _ subgrounds.plotly_wrappers.  Choropleth  (  _ **  kwargs  _ )  #

    

Bases:  ` TraceWrapper  `

See [ https://plotly.com/python/choropleth-maps/
](https://plotly.com/python/choropleth-maps/)

graph_object  #

    

alias of ` Choropleth  `

_ class  _ subgrounds.plotly_wrappers.  Scattermapbox  (  _ **  kwargs  _ )  #

    

Bases:  ` TraceWrapper  `

See [ https://plotly.com/python/scattermapbox/
](https://plotly.com/python/scattermapbox/)

graph_object  #

    

alias of ` Scattermapbox  `

_ class  _ subgrounds.plotly_wrappers.  Choroplethmapbox  (  _ **  kwargs  _ )
#

    

Bases:  ` TraceWrapper  `

See [ https://plotly.com/python/mapbox-county-choropleth/
](https://plotly.com/python/mapbox-county-choropleth/)

graph_object  #

    

alias of ` Choroplethmapbox  `

_ class  _ subgrounds.plotly_wrappers.  Densitymapbox  (  _ **  kwargs  _ )  #

    

Bases:  ` TraceWrapper  `

See [ https://plotly.com/python/mapbox-density-heatmaps/
](https://plotly.com/python/mapbox-density-heatmaps/)

graph_object  #

    

alias of ` Densitymapbox  `

_ class  _ subgrounds.plotly_wrappers.  Scatterpolar  (  _ **  kwargs  _ )  #

    

Bases:  ` TraceWrapper  `

See [ https://plotly.com/python/polar-chart/
](https://plotly.com/python/polar-chart/)

graph_object  #

    

alias of ` Scatterpolar  `

_ class  _ subgrounds.plotly_wrappers.  Barpolar  (  _ **  kwargs  _ )  #

    

Bases:  ` TraceWrapper  `

See [ https://plotly.com/python/wind-rose-charts/
](https://plotly.com/python/wind-rose-charts/)

graph_object  #

    

alias of ` Barpolar  `

_ class  _ subgrounds.plotly_wrappers.  Sunburst  (  _ **  kwargs  _ )  #

    

Bases:  ` TraceWrapper  `

See [ https://plotly.com/python/sunburst-charts/
](https://plotly.com/python/sunburst-charts/)

graph_object  #

    

alias of ` Sunburst  `

_ class  _ subgrounds.plotly_wrappers.  Treemap  (  _ **  kwargs  _ )  #

    

Bases:  ` TraceWrapper  `

See [ https://plotly.com/python/treemaps/
](https://plotly.com/python/treemaps/)

graph_object  #

    

alias of ` Treemap  `

_ class  _ subgrounds.plotly_wrappers.  Icicle  (  _ **  kwargs  _ )  #

    

Bases:  ` TraceWrapper  `

See [ https://plotly.com/python/icicle-charts/
](https://plotly.com/python/icicle-charts/)

graph_object  #

    

alias of ` Icicle  `

_ class  _ subgrounds.plotly_wrappers.  Sankey  (  _ **  kwargs  _ )  #

    

Bases:  ` TraceWrapper  `

See [ https://plotly.com/python/sankey-diagram/
](https://plotly.com/python/sankey-diagram/)

graph_object  #

    

alias of ` Sankey  `

_ class  _ subgrounds.plotly_wrappers.  Parcoords  (  _ **  kwargs  _ )  #

    

Bases:  ` TraceWrapper  `

See [ https://plotly.com/python/parallel-coordinates-plot/
](https://plotly.com/python/parallel-coordinates-plot/)

graph_object  #

    

alias of ` Parcoords  `

_ class  _ subgrounds.plotly_wrappers.  Parcats  (  _ **  kwargs  _ )  #

    

Bases:  ` TraceWrapper  `

See [ https://plotly.com/python/parallel-categories-diagram/
](https://plotly.com/python/parallel-categories-diagram/)

graph_object  #

    

alias of ` Parcats  `

_ class  _ subgrounds.plotly_wrappers.  Carpet  (  _ **  kwargs  _ )  #

    

Bases:  ` TraceWrapper  `

See [ https://plotly.com/python/carpet-plot/
](https://plotly.com/python/carpet-plot/)

graph_object  #

    

alias of ` Carpet  `

_ class  _ subgrounds.plotly_wrappers.  Scattercarpet  (  _ **  kwargs  _ )  #

    

Bases:  ` TraceWrapper  `

See [ https://plotly.com/python/carpet-scatter/
](https://plotly.com/python/carpet-scatter/)

graph_object  #

    

alias of ` Scattercarpet  `

_ class  _ subgrounds.plotly_wrappers.  Contourcarpet  (  _ **  kwargs  _ )  #

    

Bases:  ` TraceWrapper  `

See [ https://plotly.com/python/carpet-contour/
](https://plotly.com/python/carpet-contour/)

graph_object  #

    

alias of ` Contourcarpet  `

[ Next  subgrounds.query module  ](../subgrounds.query/) [ Previous
subgrounds.dataframe_utils module  ](../subgrounds.dataframe_utils/)

Made with [ Furo ](https://github.com/pradyunsg/furo)

[ ](https://github.com/0xPlaygrounds/subgrounds) [
](https://discord.gg/v4r4zhBAh2) [ ](https://twitter.com/Playgrounds0x)

On this page

  * subgrounds.plotly_wrappers module 
    * ` Figure  `
      * ` Figure.figure  `
      * ` Figure.subgrounds  `
      * ` Figure.traces  `
      * ` Figure.req  `
      * ` Figure.data  `
      * ` Figure.args  `
      * ` Figure.refresh()  `
    * ` TraceWrapper  `
      * ` TraceWrapper.graph_object  `
      * ` TraceWrapper.fpaths  `
      * ` TraceWrapper.args  `
      * ` TraceWrapper.mk_trace()  `
      * ` TraceWrapper.field_paths  `
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

Give us a ⭐️ on [ Github ](https://github.com/0xPlaygrounds/subgrounds) !

Toggle site navigation sidebar

_ _

[ ![Light Logo](../../../_static/assets/pg-logotype-dark.svg) ![Dark
Logo](../../../_static/assets/pg-logotype-primary.svg)
](https://playgrounds.network)

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
      * [ Merging ](../../getting_started/field_paths/merging/)
    * [ Querying ](../../getting_started/querying/)
    * [ Synthetic Fields ](../../getting_started/synthetic_fields/)
  * [ Advanced Topics ](../../advanced_topics/)

Toggle child pages in navigation

_ _

    * [ Pagination ](../../advanced_topics/pagination/)

Toggle child pages in navigation

_ _

      * [ Custom Strategies ](../../advanced_topics/pagination/custom/)
  * [ FAQ ](../../faq/)

Toggle child pages in navigation

_ _

    * [ Setup ](../../faq/setup/)

Toggle child pages in navigation

_ _

      * [ Python Versioning ](../../faq/setup/version_management/)
    * [ Contrib ](../../faq/contrib/)
  * [ Examples ](../../examples/)

Toggle child pages in navigation

_ _

    * [ Exchanges ](../../examples/exchanges/)
    * [ Bridges ](../../examples/bridges/)
    * [ Liquid Staking ](../../examples/liquid_staking/)
    * [ Governance ](../../examples/governance/)
    * [ Advanced Research ](../../examples/advanced_research/)
    * [ Vaults ](../../examples/vaults/)
  * [ Tutorials ](../../tutorials/)
  * [ Changelog ](../../changelog/)
  * [ API Reference ](../../modules/)

Toggle child pages in navigation

_ _

    * [ subgrounds package ](../subgrounds/)

Toggle child pages in navigation

_ _

      * [ subgrounds.pagination package ](../subgrounds.pagination/)

Toggle child pages in navigation

_ _

        * [ subgrounds.pagination.pagination module ](../subgrounds.pagination.pagination/)
        * [ subgrounds.pagination.preprocess module ](../subgrounds.pagination.preprocess/)
        * [ subgrounds.pagination.strategies module ](../subgrounds.pagination.strategies/)
        * [ subgrounds.pagination.utils module ](../subgrounds.pagination.utils/)
      * [ subgrounds.subgraph package ](../subgrounds.subgraph/)

Toggle child pages in navigation

_ _

        * [ subgrounds.subgraph.fieldpath module ](../subgrounds.subgraph.fieldpath/)
        * [ subgrounds.subgraph.filter module ](../subgrounds.subgraph.filter/)
        * [ subgrounds.subgraph.object module ](../subgrounds.subgraph.object/)
        * [ subgrounds.subgraph.subgraph module ](../subgrounds.subgraph.subgraph/)
      * [ subgrounds.client module ](../subgrounds.client/)
      * [ subgrounds.dash_wrappers module ](../subgrounds.dash_wrappers/)
      * [ subgrounds.dataframe_utils module ](../subgrounds.dataframe_utils/)
      * [ subgrounds.plotly_wrappers module ](../subgrounds.plotly_wrappers/)
      * subgrounds.query module 
      * [ subgrounds.schema module ](../subgrounds.schema/)
      * [ subgrounds.subgrounds module ](../subgrounds.subgrounds/)
      * [ subgrounds.transform module ](../subgrounds.transform/)
      * [ subgrounds.utils module ](../subgrounds.utils/)

Back to top

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

_ _

#  subgrounds.query module  #

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
    

_ class  _ subgrounds.query.  InputValue  #

    

Bases: [ ` object  ` ](https://docs.python.org/3/library/functions.html#object
"\(in Python v3.11\)")

_ class  _ T  (  _ *  args  _ , _ **  kwargs  _ )  #

    

Bases: [ ` Protocol  `
](https://docs.python.org/3/library/typing.html#typing.Protocol "\(in Python
v3.11\)")

_ property  _ graphql  _ :  [ str
](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.11\)") _
#

    

Returns a GraphQL string representation of the input value

Returns  :

    

The GraphQL string representation of the input value

Return type  :

    

[ str ](https://docs.python.org/3/library/stdtypes.html#str "\(in Python
v3.11\)")

_ property  _ is_variable  _ :  [ bool
](https://docs.python.org/3/library/functions.html#bool "\(in Python v3.11\)")
_ #

    

Returns True i.f.f. the input value is of type Variable

Returns  :

    

True i.f.f. the input value is of type Variable, otherwise False

Return type  :

    

[ bool ](https://docs.python.org/3/library/functions.html#bool "\(in Python
v3.11\)")

_ property  _ is_number  _ :  [ bool
](https://docs.python.org/3/library/functions.html#bool "\(in Python v3.11\)")
_ #

    

Returns True i.f.f. the input value is of type Float or Int

Returns  :

    

True i.f.f. the input value is of type Float or Int, otherwise False

Return type  :

    

[ bool ](https://docs.python.org/3/library/functions.html#bool "\(in Python
v3.11\)")

iter  (  )  #

    

_ class  _ Null  #

    

Bases: [ ` object  ` ](https://docs.python.org/3/library/functions.html#object
"\(in Python v3.11\)")

_ property  _ graphql  _ :  [ str
](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.11\)") _
#

    

_ property  _ is_variable  _ :  [ bool
](https://docs.python.org/3/library/functions.html#bool "\(in Python v3.11\)")
_ #

    

_ property  _ is_number  _ :  [ bool
](https://docs.python.org/3/library/functions.html#bool "\(in Python v3.11\)")
_ #

    

iter  (  )  #

    

_ class  _ Int  (  _ value  :  'int'  _ )  #

    

Bases: [ ` object  ` ](https://docs.python.org/3/library/functions.html#object
"\(in Python v3.11\)")

value  _ :  [ int  ](https://docs.python.org/3/library/functions.html#int
"\(in Python v3.11\)") _ #

    

_ property  _ graphql  _ :  [ str
](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.11\)") _
#

    

_ property  _ is_variable  _ :  [ bool
](https://docs.python.org/3/library/functions.html#bool "\(in Python v3.11\)")
_ #

    

_ property  _ is_number  _ :  [ bool
](https://docs.python.org/3/library/functions.html#bool "\(in Python v3.11\)")
_ #

    

iter  (  )  #

    

_ class  _ Float  (  _ value  :  'float'  _ )  #

    

Bases: [ ` object  ` ](https://docs.python.org/3/library/functions.html#object
"\(in Python v3.11\)")

value  _ :  [ float  ](https://docs.python.org/3/library/functions.html#float
"\(in Python v3.11\)") _ #

    

_ property  _ graphql  _ :  [ str
](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.11\)") _
#

    

_ property  _ is_variable  _ :  [ bool
](https://docs.python.org/3/library/functions.html#bool "\(in Python v3.11\)")
_ #

    

_ property  _ is_number  _ :  [ bool
](https://docs.python.org/3/library/functions.html#bool "\(in Python v3.11\)")
_ #

    

iter  (  )  #

    

_ class  _ String  (  _ value  :  'str'  _ )  #

    

Bases: [ ` object  ` ](https://docs.python.org/3/library/functions.html#object
"\(in Python v3.11\)")

value  _ :  [ str  ](https://docs.python.org/3/library/stdtypes.html#str "\(in
Python v3.11\)") _ #

    

_ property  _ graphql  _ :  [ str
](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.11\)") _
#

    

_ property  _ is_variable  _ :  [ bool
](https://docs.python.org/3/library/functions.html#bool "\(in Python v3.11\)")
_ #

    

_ property  _ is_number  _ :  [ bool
](https://docs.python.org/3/library/functions.html#bool "\(in Python v3.11\)")
_ #

    

iter  (  )  #

    

_ class  _ Boolean  (  _ value  :  'bool'  _ )  #

    

Bases: [ ` object  ` ](https://docs.python.org/3/library/functions.html#object
"\(in Python v3.11\)")

value  _ :  [ bool  ](https://docs.python.org/3/library/functions.html#bool
"\(in Python v3.11\)") _ #

    

_ property  _ graphql  _ :  [ str
](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.11\)") _
#

    

_ property  _ is_variable  _ :  [ bool
](https://docs.python.org/3/library/functions.html#bool "\(in Python v3.11\)")
_ #

    

_ property  _ is_number  _ :  [ bool
](https://docs.python.org/3/library/functions.html#bool "\(in Python v3.11\)")
_ #

    

iter  (  )  #

    

_ class  _ Enum  (  _ value  :  'str'  _ )  #

    

Bases: [ ` object  ` ](https://docs.python.org/3/library/functions.html#object
"\(in Python v3.11\)")

value  _ :  [ str  ](https://docs.python.org/3/library/stdtypes.html#str "\(in
Python v3.11\)") _ #

    

_ property  _ graphql  _ :  [ str
](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.11\)") _
#

    

_ property  _ is_variable  _ :  [ bool
](https://docs.python.org/3/library/functions.html#bool "\(in Python v3.11\)")
_ #

    

_ property  _ is_number  _ :  [ bool
](https://docs.python.org/3/library/functions.html#bool "\(in Python v3.11\)")
_ #

    

iter  (  )  #

    

_ class  _ Variable  (  _ name  :  'str'  _ )  #

    

Bases: [ ` object  ` ](https://docs.python.org/3/library/functions.html#object
"\(in Python v3.11\)")

name  _ :  [ str  ](https://docs.python.org/3/library/stdtypes.html#str "\(in
Python v3.11\)") _ #

    

_ property  _ graphql  _ :  [ str
](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.11\)") _
#

    

_ property  _ is_variable  _ :  [ bool
](https://docs.python.org/3/library/functions.html#bool "\(in Python v3.11\)")
_ #

    

_ property  _ is_number  _ :  [ bool
](https://docs.python.org/3/library/functions.html#bool "\(in Python v3.11\)")
_ #

    

iter  (  )  #

    

_ class  _ List  (  _ value  :  'list[InputValue.T]'  _ )  #

    

Bases: [ ` object  ` ](https://docs.python.org/3/library/functions.html#object
"\(in Python v3.11\)")

value  _ :  [ list  ](https://docs.python.org/3/library/stdtypes.html#list
"\(in Python v3.11\)") [  subgrounds.query.InputValue.T  ]  _ #

    

_ property  _ graphql  _ :  [ str
](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.11\)") _
#

    

_ property  _ is_variable  _ :  [ bool
](https://docs.python.org/3/library/functions.html#bool "\(in Python v3.11\)")
_ #

    

_ property  _ is_number  _ :  [ bool
](https://docs.python.org/3/library/functions.html#bool "\(in Python v3.11\)")
_ #

    

iter  (  )  #

    

_ class  _ Object  (  _ value  :  'dict[str,  InputValue.T]'  _ )  #

    

Bases: [ ` object  ` ](https://docs.python.org/3/library/functions.html#object
"\(in Python v3.11\)")

value  _ :  [ dict  ](https://docs.python.org/3/library/stdtypes.html#dict
"\(in Python v3.11\)") [  [ str
](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.11\)") ,
subgrounds.query.InputValue.T  ]  _ #

    

_ property  _ graphql  _ :  [ str
](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.11\)") _
#

    

_ property  _ is_variable  _ :  [ bool
](https://docs.python.org/3/library/functions.html#bool "\(in Python v3.11\)")
_ #

    

_ property  _ is_number  _ :  [ bool
](https://docs.python.org/3/library/functions.html#bool "\(in Python v3.11\)")
_ #

    

iter  (  )  #

    

_ class  _ subgrounds.query.  VariableDefinition  (  _ name  _ , _ type_  _ ,
_ default  =  None  _ )  #

    

Bases: [ ` object  ` ](https://docs.python.org/3/library/functions.html#object
"\(in Python v3.11\)")

Representation of a GraphQL variable definition

name  #

    

Name of the argument

Type  :

    

[ str ](https://docs.python.org/3/library/stdtypes.html#str "\(in Python
v3.11\)")

type_  #

    

GraphQL type of the argument

Type  :

    

[ TypeRef.T ](../subgrounds.schema/#subgrounds.schema.TypeRef.T
"subgrounds.schema.TypeRef.T")

default  #

    

Default value of the variable. Defaults to None.

Type  :

    

InputValue.T  , optional

name  _ :  [ str  ](https://docs.python.org/3/library/stdtypes.html#str "\(in
Python v3.11\)") _ #

    

type_  _ :  [ T  ](../subgrounds.schema/#subgrounds.schema.TypeRef.T
"subgrounds.schema.TypeRef.T") _ #

    

default  _ :  [ Optional
](https://docs.python.org/3/library/typing.html#typing.Optional "\(in Python
v3.11\)") [  T  ]  _ _ =  None  _ #

    

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

    

Bases: [ ` object  ` ](https://docs.python.org/3/library/functions.html#object
"\(in Python v3.11\)")

name  _ :  [ str  ](https://docs.python.org/3/library/stdtypes.html#str "\(in
Python v3.11\)") _ #

    

value  _ :  T  _ #

    

_ property  _ graphql  _ :  [ str
](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.11\)") _
#

    

iter  (  )  #

    

iter_vars  (  )  #

    

for_all  (  _ predicate  _ )  #

    

for_all_vars  (  _ predicate  _ )  #

    

exists  (  _ predicate  _ )  #

    

exists_vars  (  _ predicate  _ )  #

    

find  (  _ predicate  _ )  #

    

find_var  (  _ predicate  _ )  #

    

all_defined  (  _ variables  _ )  #

    

_ class  _ subgrounds.query.  Selection  (  _ fmeta  _ , _ alias=None  _ , _
arguments=<factory> _ , _ selection=<factory> _ )  #

    

Bases: [ ` object  ` ](https://docs.python.org/3/library/functions.html#object
"\(in Python v3.11\)")

Represents a GraphQL field selection.

fmeta  #

    

The type definition of the field being selected.

Type  :

    

[ TypeMeta.FieldMeta
](../subgrounds.schema/#subgrounds.schema.TypeMeta.FieldMeta
"subgrounds.schema.TypeMeta.FieldMeta")

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

fmeta  _ :  [ FieldMeta
](../subgrounds.schema/#subgrounds.schema.TypeMeta.FieldMeta
"subgrounds.schema.TypeMeta.FieldMeta") _ #

    

alias  _ :  [ Optional
](https://docs.python.org/3/library/typing.html#typing.Optional "\(in Python
v3.11\)") [  [ str  ](https://docs.python.org/3/library/stdtypes.html#str
"\(in Python v3.11\)") ]  _ _ =  None  _ #

    

arguments  _ :  [ list  ](https://docs.python.org/3/library/stdtypes.html#list
"\(in Python v3.11\)") [  subgrounds.query.Argument  ]  _ #

    

selection  _ :  [ list  ](https://docs.python.org/3/library/stdtypes.html#list
"\(in Python v3.11\)") [  subgrounds.query.Selection  ]  _ #

    

_ property  _ key  #

    

_ property  _ args_graphql  _ :  [ str
](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.11\)") _
#

    

graphql  (  _ level  =  0  _ )  #

    

_ property  _ data_path  _ :  [ list
](https://docs.python.org/3/library/stdtypes.html#list "\(in Python v3.11\)")
[  [ str  ](https://docs.python.org/3/library/stdtypes.html#str "\(in Python
v3.11\)") ]  _ #

    

_ property  _ data_paths  _ :  [ list
](https://docs.python.org/3/library/stdtypes.html#list "\(in Python v3.11\)")
[  [ list  ](https://docs.python.org/3/library/stdtypes.html#list "\(in Python
v3.11\)") [  [ str  ](https://docs.python.org/3/library/stdtypes.html#str
"\(in Python v3.11\)") ]  ]  _ #

    

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

filter_map  (  _ map_f  _ )  #

    

filter_map_args  (  _ map_f  _ , _ recurse  =  True  _ )  #

    

for_all  (  _ predicate  _ )  #

    

for_all_args  (  _ predicate  _ , _ recurse  =  True  _ )  #

    

exists  (  _ predicate  _ )  #

    

exists_args  (  _ predicate  _ , _ recurse  =  True  _ )  #

    

find  (  _ predicate  _ )  #

    

find_args  (  _ predicate  _ , _ recurse  =  True  _ )  #

    

find_all  (  _ predicate  _ )  #

    

find_all_args  (  _ predicate  _ , _ recurse  =  True  _ )  #

    

T  #

    

alias of TypeVar('T')

fold  (  _ fold_f  _ , _ parents  =  []  _ )  #

    

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

extract_data  (  _ data  _ )  #

    

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

infer_variable_definitions  (  )  #

    

combine  (  _ other  _ )  #

    

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
object  ` select  ` with name ` argname  ` . If  ` select  ` does not contain
such an argument and ` recurse  ` is True, then the function is called
recursively on  ` select  ` 's inner selections. If no such argument is found
in  ` select  ` or its inner selections, then the function raises an
exception.

Parameters  :

    

  * **select** (  _Selection_ ) -- The selection to scan 

  * **argname** ( [ _str_ ](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.11\)") ) -- The name of the argument to find 

  * **recurse** ( [ _bool_ ](https://docs.python.org/3/library/functions.html#bool "\(in Python v3.11\)") _,_ _optional_ ) -- Flag indicating whether or not the method should be run recursively on nested selections. Defaults to True. 

Raises  :

    

[ **KeyError** ](https://docs.python.org/3/library/exceptions.html#KeyError
"\(in Python v3.11\)") \-- If no argument named ` argname  ` exists in the
selection ` self  ` .

Returns  :

    

The argument in  ` select  ` with name ` argname  ` (if any).

Return type  :

    

Argument

get_argument_by_variable  (  _ varname  _ , _ recurse  =  True  _ )  #

    

Returns an Argument object corresponding to the argument in the Selection
object  ` select  ` whose value is a variable named ` varname  ` . If  `
select  ` does not contain such an argument and ` recurse  ` is True, then the
function is called recursively on  ` select  ` 's inner selections. If no such
argument is found in  ` select  ` or its inner selections, then the function
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

    

The argument in  ` select  ` with variable value named

    

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

select  (  _ other  _ )  #

    

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

    

Bases: [ ` object  ` ](https://docs.python.org/3/library/functions.html#object
"\(in Python v3.11\)")

name  _ :  [ Optional
](https://docs.python.org/3/library/typing.html#typing.Optional "\(in Python
v3.11\)") [  [ str  ](https://docs.python.org/3/library/stdtypes.html#str
"\(in Python v3.11\)") ]  _ _ =  None  _ #

    

selection  _ :  [ list  ](https://docs.python.org/3/library/stdtypes.html#list
"\(in Python v3.11\)") [  subgrounds.query.Selection  ]  _ #

    

variables  _ :  [ list  ](https://docs.python.org/3/library/stdtypes.html#list
"\(in Python v3.11\)") [  subgrounds.query.VariableDefinition  ]  _ #

    

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

filter_vardefs  (  _ predicate  _ )  #

    

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

map_vardefs  (  _ map_f  _ )  #

    

filter_map  (  _ map_f  _ )  #

    

filter_map_args  (  _ map_f  _ )  #

    

filter_map_vardefs  (  _ map_f  _ )  #

    

for_all  (  _ predicate  _ )  #

    

for_all_args  (  _ predicate  _ )  #

    

for_all_vardefs  (  _ predicate  _ )  #

    

exists  (  _ predicate  _ )  #

    

exists_args  (  _ predicate  _ )  #

    

exists_vardefs  (  _ predicate  _ )  #

    

find  (  _ predicate  _ )  #

    

find_args  (  _ predicate  _ )  #

    

find_vardefs  (  _ predicate  _ )  #

    

T  #

    

alias of TypeVar('T')

fold  (  _ fold_f  _ )  #

    

infer_variable_definitions  (  )  #

    

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

add_vardefs  (  _ vardefs  _ )  #

    

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

_ static  _ transform  (  _ query  _ , _ variable_f=<function  identity> _ , _
selection_f=<function  identity> _ )  #

    

contains_selection  (  _ selection  _ )  #

    

Returns True i.f.f. the selection tree  ` selection  ` is present in ` query
` .

Parameters  :

    

  * **query** (  _Query_ ) -- A query object 

  * **selection** (  _Selection_ ) -- The selection to be found (or not) in ` query  `

Returns  :

    

True if the  ` selection  ` is present in ` query  ` , False

    

otherwise.

Return type  :

    

[ bool ](https://docs.python.org/3/library/functions.html#bool "\(in Python
v3.11\)")

contains_argument  (  _ argname  _ )  #

    

get_argument  (  _ argname  _ )  #

    

_ static  _ substitute_arg  (  _ query  _ , _ arg_name  _ , _ replacement  _ )
#

    

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

prune_undefined  (  _ variables  _ )  #

    

_ class  _ subgrounds.query.  Fragment  (  _ name:  'str'  _ , _ type_:
'TypeRef.T'  _ , _ selection:  'list[Selection]'  =  <factory> _ , _
variables:  'list[VariableDefinition]'  =  <factory> _ )  #

    

Bases: [ ` object  ` ](https://docs.python.org/3/library/functions.html#object
"\(in Python v3.11\)")

name  _ :  [ str  ](https://docs.python.org/3/library/stdtypes.html#str "\(in
Python v3.11\)") _ #

    

type_  _ :  [ T  ](../subgrounds.schema/#subgrounds.schema.TypeRef.T
"subgrounds.schema.TypeRef.T") _ #

    

selection  _ :  [ list  ](https://docs.python.org/3/library/stdtypes.html#list
"\(in Python v3.11\)") [  subgrounds.query.Selection  ]  _ #

    

variables  _ :  [ list  ](https://docs.python.org/3/library/stdtypes.html#list
"\(in Python v3.11\)") [  subgrounds.query.VariableDefinition  ]  _ #

    

_ property  _ graphql  #

    

_ static  _ combine  (  _ frag  _ , _ other  _ )  #

    

_ static  _ transform  (  _ frag  _ , _ f  _ )  #

    

_ class  _ subgrounds.query.  Document  (  _ url:  'str'  _ , _ query:
'Query'  _ , _ fragments:  'list[Fragment]'  =  <factory> _ , _ variables:
'dict[str  _ , _ Any]'  =  <factory> _ )  #

    

Bases: [ ` object  ` ](https://docs.python.org/3/library/functions.html#object
"\(in Python v3.11\)")

url  _ :  [ str  ](https://docs.python.org/3/library/stdtypes.html#str "\(in
Python v3.11\)") _ #

    

query  _ :  Query  _ #

    

fragments  _ :  [ list  ](https://docs.python.org/3/library/stdtypes.html#list
"\(in Python v3.11\)") [  subgrounds.query.Fragment  ]  _ #

    

variables  _ :  [ dict  ](https://docs.python.org/3/library/stdtypes.html#dict
"\(in Python v3.11\)") [  [ str
](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.11\)") ,
[ Any  ](https://docs.python.org/3/library/typing.html#typing.Any "\(in Python
v3.11\)") ]  _ #

    

_ property  _ graphql  #

    

_ static  _ mk_single_query  (  _ url  _ , _ query  _ )  #

    

filter  (  _ predicate  _ )  #

    

filter_args  (  _ predicate  _ )  #

    

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

filter_map  (  _ map_f  _ )  #

    

_ static  _ combine  (  _ doc  _ , _ other  _ )  #

    

_ static  _ transform  (  _ doc  _ , _ query_f=<function  identity> _ , _
fragment_f=<function  identity> _ )  #

    

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

    

Bases: [ ` object  ` ](https://docs.python.org/3/library/functions.html#object
"\(in Python v3.11\)")

documents  _ :  [ list  ](https://docs.python.org/3/library/stdtypes.html#list
"\(in Python v3.11\)") [  subgrounds.query.Document  ]  _ #

    

_ property  _ graphql  #

    

_ static  _ combine  (  _ req  _ , _ other  _ )  #

    

_ static  _ transform  (  _ req  _ , _ f  _ )  #

    

_ static  _ single_query  (  _ url  _ , _ query  _ )  #

    

_ static  _ single_document  (  _ doc  _ )  #

    

_ static  _ add_documents  (  _ self  _ , _ docs  _ )  #

    

subgrounds.query.  selections_of_object  (  _ schema  _ , _ object_  _ )  #

    

Returns generator of Selection objects that selects all non-list fields of
GraphQL Object of Interface ` object_  ` .

Parameters  :

    

  * **schema** ( [ _SchemaMeta_ ](../subgrounds.schema/#subgrounds.schema.SchemaMeta "subgrounds.schema.SchemaMeta") ) -- _description_ 

  * **object** ( [ _TypeMeta.ObjectMeta_ ](../subgrounds.schema/#subgrounds.schema.TypeMeta.ObjectMeta "subgrounds.schema.TypeMeta.ObjectMeta") _|_ [ _TypeMeta.InterfaceMeta_ ](../subgrounds.schema/#subgrounds.schema.TypeMeta.InterfaceMeta "subgrounds.schema.TypeMeta.InterfaceMeta") ) -- _description_ 

Yields  :

    

__type__ \-- _description_

subgrounds.query.  input_value_of_argument  (  _ schema  _ , _ argmeta  _ , _
value  _ )  #

    

subgrounds.query.  arguments_of_field_args  (  _ schema  _ , _ field  _ , _
args  _ )  #

    

[ Next  subgrounds.schema module  ](../subgrounds.schema/) [ Previous
subgrounds.plotly_wrappers module  ](../subgrounds.plotly_wrappers/)

Made with [ Furo ](https://github.com/pradyunsg/furo)

[ ](https://github.com/0xPlaygrounds/subgrounds) [
](https://discord.gg/v4r4zhBAh2) [ ](https://twitter.com/Playgrounds0x)

On this page

  * subgrounds.query module 
    * ` InputValue  `
      * ` InputValue.T  `
        * ` InputValue.T.graphql  `
        * ` InputValue.T.is_variable  `
        * ` InputValue.T.is_number  `
        * ` InputValue.T.iter()  `
      * ` InputValue.Null  `
        * ` InputValue.Null.graphql  `
        * ` InputValue.Null.is_variable  `
        * ` InputValue.Null.is_number  `
        * ` InputValue.Null.iter()  `
      * ` InputValue.Int  `
        * ` InputValue.Int.value  `
        * ` InputValue.Int.graphql  `
        * ` InputValue.Int.is_variable  `
        * ` InputValue.Int.is_number  `
        * ` InputValue.Int.iter()  `
      * ` InputValue.Float  `
        * ` InputValue.Float.value  `
        * ` InputValue.Float.graphql  `
        * ` InputValue.Float.is_variable  `
        * ` InputValue.Float.is_number  `
        * ` InputValue.Float.iter()  `
      * ` InputValue.String  `
        * ` InputValue.String.value  `
        * ` InputValue.String.graphql  `
        * ` InputValue.String.is_variable  `
        * ` InputValue.String.is_number  `
        * ` InputValue.String.iter()  `
      * ` InputValue.Boolean  `
        * ` InputValue.Boolean.value  `
        * ` InputValue.Boolean.graphql  `
        * ` InputValue.Boolean.is_variable  `
        * ` InputValue.Boolean.is_number  `
        * ` InputValue.Boolean.iter()  `
      * ` InputValue.Enum  `
        * ` InputValue.Enum.value  `
        * ` InputValue.Enum.graphql  `
        * ` InputValue.Enum.is_variable  `
        * ` InputValue.Enum.is_number  `
        * ` InputValue.Enum.iter()  `
      * ` InputValue.Variable  `
        * ` InputValue.Variable.name  `
        * ` InputValue.Variable.graphql  `
        * ` InputValue.Variable.is_variable  `
        * ` InputValue.Variable.is_number  `
        * ` InputValue.Variable.iter()  `
      * ` InputValue.List  `
        * ` InputValue.List.value  `
        * ` InputValue.List.graphql  `
        * ` InputValue.List.is_variable  `
        * ` InputValue.List.is_number  `
        * ` InputValue.List.iter()  `
      * ` InputValue.Object  `
        * ` InputValue.Object.value  `
        * ` InputValue.Object.graphql  `
        * ` InputValue.Object.is_variable  `
        * ` InputValue.Object.is_number  `
        * ` InputValue.Object.iter()  `
    * ` VariableDefinition  `
      * ` VariableDefinition.name  `
      * ` VariableDefinition.type_  `
      * ` VariableDefinition.default  `
      * ` VariableDefinition.name  `
      * ` VariableDefinition.type_  `
      * ` VariableDefinition.default  `
      * ` VariableDefinition.graphql  `
    * ` Argument  `
      * ` Argument.name  `
      * ` Argument.value  `
      * ` Argument.graphql  `
      * ` Argument.iter()  `
      * ` Argument.iter_vars()  `
      * ` Argument.for_all()  `
      * ` Argument.for_all_vars()  `
      * ` Argument.exists()  `
      * ` Argument.exists_vars()  `
      * ` Argument.find()  `
      * ` Argument.find_var()  `
      * ` Argument.all_defined()  `
    * ` Selection  `
      * ` Selection.fmeta  `
      * ` Selection.alias  `
      * ` Selection.arguments  `
      * ` Selection.selection  `
      * ` Selection.fmeta  `
      * ` Selection.alias  `
      * ` Selection.arguments  `
      * ` Selection.selection  `
      * ` Selection.key  `
      * ` Selection.args_graphql  `
      * ` Selection.graphql()  `
      * ` Selection.data_path  `
      * ` Selection.data_paths  `
      * ` Selection.iter()  `
      * ` Selection.iter_args()  `
      * ` Selection.filter()  `
      * ` Selection.filter_args()  `
      * ` Selection.map()  `
      * ` Selection.map_args()  `
      * ` Selection.filter_map()  `
      * ` Selection.filter_map_args()  `
      * ` Selection.for_all()  `
      * ` Selection.for_all_args()  `
      * ` Selection.exists()  `
      * ` Selection.exists_args()  `
      * ` Selection.find()  `
      * ` Selection.find_args()  `
      * ` Selection.find_all()  `
      * ` Selection.find_all_args()  `
      * ` Selection.T  `
      * ` Selection.fold()  `
      * ` Selection.contains_list()  `
      * ` Selection.split()  `
      * ` Selection.extract_data()  `
      * ` Selection.add()  `
      * ` Selection.remove()  `
      * ` Selection.variable_args()  `
      * ` Selection.infer_variable_definitions()  `
      * ` Selection.combine()  `
      * ` Selection.merge()  `
      * ` Selection.contains()  `
      * ` Selection.contains_argument()  `
      * ` Selection.get_argument()  `
      * ` Selection.get_argument_by_variable()  `
      * ` Selection.substitute_arg()  `
      * ` Selection.select()  `
      * ` Selection.prune_undefined()  `
    * ` Query  `
      * ` Query.name  `
      * ` Query.selection  `
      * ` Query.variables  `
      * ` Query.graphql  `
      * ` Query.iter()  `
      * ` Query.iter_args()  `
      * ` Query.iter_vardefs()  `
      * ` Query.filter()  `
      * ` Query.filter_args()  `
      * ` Query.filter_vardefs()  `
      * ` Query.map()  `
      * ` Query.map_args()  `
      * ` Query.map_vardefs()  `
      * ` Query.filter_map()  `
      * ` Query.filter_map_args()  `
      * ` Query.filter_map_vardefs()  `
      * ` Query.for_all()  `
      * ` Query.for_all_args()  `
      * ` Query.for_all_vardefs()  `
      * ` Query.exists()  `
      * ` Query.exists_args()  `
      * ` Query.exists_vardefs()  `
      * ` Query.find()  `
      * ` Query.find_args()  `
      * ` Query.find_vardefs()  `
      * ` Query.T  `
      * ` Query.fold()  `
      * ` Query.infer_variable_definitions()  `
      * ` Query.add()  `
      * ` Query.add_vardefs()  `
      * ` Query.remove()  `
      * ` Query.transform()  `
      * ` Query.contains_selection()  `
      * ` Query.contains_argument()  `
      * ` Query.get_argument()  `
      * ` Query.substitute_arg()  `
      * ` Query.contains()  `
      * ` Query.select()  `
      * ` Query.prune_undefined()  `
    * ` Fragment  `
      * ` Fragment.name  `
      * ` Fragment.type_  `
      * ` Fragment.selection  `
      * ` Fragment.variables  `
      * ` Fragment.graphql  `
      * ` Fragment.combine()  `
      * ` Fragment.transform()  `
    * ` Document  `
      * ` Document.url  `
      * ` Document.query  `
      * ` Document.fragments  `
      * ` Document.variables  `
      * ` Document.graphql  `
      * ` Document.mk_single_query()  `
      * ` Document.filter()  `
      * ` Document.filter_args()  `
      * ` Document.map()  `
      * ` Document.map_args()  `
      * ` Document.filter_map()  `
      * ` Document.combine()  `
      * ` Document.transform()  `
      * ` Document.prune_undefined()  `
    * ` DataRequest  `
      * ` DataRequest.documents  `
      * ` DataRequest.graphql  `
      * ` DataRequest.combine()  `
      * ` DataRequest.transform()  `
      * ` DataRequest.single_query()  `
      * ` DataRequest.single_document()  `
      * ` DataRequest.add_documents()  `
    * ` selections_of_object()  `
    * ` input_value_of_argument()  `
    * ` arguments_of_field_args()  `



Contents  Menu  Expand  Light mode  Dark mode  Auto light/dark mode

Hide navigation sidebar

Hide table of contents sidebar

Give us a ⭐️ on [ Github ](https://github.com/0xPlaygrounds/subgrounds) !

Toggle site navigation sidebar

_ _

[ ![Light Logo](../../../_static/assets/pg-logotype-dark.svg) ![Dark
Logo](../../../_static/assets/pg-logotype-primary.svg)
](https://playgrounds.network)

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
      * [ Merging ](../../getting_started/field_paths/merging/)
    * [ Querying ](../../getting_started/querying/)
    * [ Synthetic Fields ](../../getting_started/synthetic_fields/)
  * [ Advanced Topics ](../../advanced_topics/)

Toggle child pages in navigation

_ _

    * [ Pagination ](../../advanced_topics/pagination/)

Toggle child pages in navigation

_ _

      * [ Custom Strategies ](../../advanced_topics/pagination/custom/)
  * [ FAQ ](../../faq/)

Toggle child pages in navigation

_ _

    * [ Setup ](../../faq/setup/)

Toggle child pages in navigation

_ _

      * [ Python Versioning ](../../faq/setup/version_management/)
    * [ Contrib ](../../faq/contrib/)
  * [ Examples ](../../examples/)

Toggle child pages in navigation

_ _

    * [ Exchanges ](../../examples/exchanges/)
    * [ Bridges ](../../examples/bridges/)
    * [ Liquid Staking ](../../examples/liquid_staking/)
    * [ Governance ](../../examples/governance/)
    * [ Advanced Research ](../../examples/advanced_research/)
    * [ Vaults ](../../examples/vaults/)
  * [ Tutorials ](../../tutorials/)
  * [ Changelog ](../../changelog/)
  * [ API Reference ](../../modules/)

Toggle child pages in navigation

_ _

    * [ subgrounds package ](../subgrounds/)

Toggle child pages in navigation

_ _

      * [ subgrounds.pagination package ](../subgrounds.pagination/)

Toggle child pages in navigation

_ _

        * [ subgrounds.pagination.pagination module ](../subgrounds.pagination.pagination/)
        * [ subgrounds.pagination.preprocess module ](../subgrounds.pagination.preprocess/)
        * [ subgrounds.pagination.strategies module ](../subgrounds.pagination.strategies/)
        * [ subgrounds.pagination.utils module ](../subgrounds.pagination.utils/)
      * [ subgrounds.subgraph package ](../subgrounds.subgraph/)

Toggle child pages in navigation

_ _

        * [ subgrounds.subgraph.fieldpath module ](../subgrounds.subgraph.fieldpath/)
        * [ subgrounds.subgraph.filter module ](../subgrounds.subgraph.filter/)
        * [ subgrounds.subgraph.object module ](../subgrounds.subgraph.object/)
        * [ subgrounds.subgraph.subgraph module ](../subgrounds.subgraph.subgraph/)
      * [ subgrounds.client module ](../subgrounds.client/)
      * [ subgrounds.dash_wrappers module ](../subgrounds.dash_wrappers/)
      * [ subgrounds.dataframe_utils module ](../subgrounds.dataframe_utils/)
      * [ subgrounds.plotly_wrappers module ](../subgrounds.plotly_wrappers/)
      * [ subgrounds.query module ](../subgrounds.query/)
      * subgrounds.schema module 
      * [ subgrounds.subgrounds module ](../subgrounds.subgrounds/)
      * [ subgrounds.transform module ](../subgrounds.transform/)
      * [ subgrounds.utils module ](../subgrounds.utils/)

Back to top

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

_ _

#  subgrounds.schema module  #

Schema data structure module

This module contains various data structures in the form of dataclasses that
are used to represent GraphQL schemas in Subgrounds using an AST-like
approach.

_ class  _ subgrounds.schema.  BaseModel  #

    

Bases: ` BaseModel  `

_ class  _ Config  #

    

Bases: [ ` object  ` ](https://docs.python.org/3/library/functions.html#object
"\(in Python v3.11\)")

allow_population_by_field_name  _ =  True  _ #

    

_ class  _ subgrounds.schema.  TypeRef  #

    

Bases: [ ` object  ` ](https://docs.python.org/3/library/functions.html#object
"\(in Python v3.11\)")

_ class  _ T  #

    

Bases:  ` BaseModel  `

Base class of all types of type references.

_ property  _ name  _ :  [ str
](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.11\)") _
#

    

_ property  _ is_list  _ :  [ bool
](https://docs.python.org/3/library/functions.html#bool "\(in Python v3.11\)")
_ #

    

_ property  _ is_non_null  _ :  [ bool
](https://docs.python.org/3/library/functions.html#bool "\(in Python v3.11\)")
_ #

    

_ class  _ Named  (  _ *  _ , _ name  _ , _ kind  _ )  #

    

Bases:  ` T  `

name_  _ :  [ str  ](https://docs.python.org/3/library/stdtypes.html#str "\(in
Python v3.11\)") _ #

    

kind  _ :  [ str  ](https://docs.python.org/3/library/stdtypes.html#str "\(in
Python v3.11\)") _ #

    

_ property  _ name  _ :  [ str
](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.11\)") _
#

    

_ class  _ NonNull  (  _ *  _ , _ ofType  _ , _ kind  =  'NON_NULL'  _ )  #

    

Bases:  ` T  `

inner  _ :  [ Union
](https://docs.python.org/3/library/typing.html#typing.Union "\(in Python
v3.11\)") [  List  ,  NonNull  ,  Named  ]  _ #

    

kind  _ :  [ Literal
](https://docs.python.org/3/library/typing.html#typing.Literal "\(in Python
v3.11\)") [  'NON_NULL'  ]  _ #

    

_ property  _ name  _ :  [ str
](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.11\)") _
#

    

_ property  _ is_list  _ :  [ bool
](https://docs.python.org/3/library/functions.html#bool "\(in Python v3.11\)")
_ #

    

_ property  _ is_non_null  _ :  [ bool
](https://docs.python.org/3/library/functions.html#bool "\(in Python v3.11\)")
_ #

    

_ class  _ List  (  _ *  _ , _ ofType  _ , _ kind  =  'LIST'  _ )  #

    

Bases:  ` T  `

inner  _ :  [ Union
](https://docs.python.org/3/library/typing.html#typing.Union "\(in Python
v3.11\)") [  List  ,  NonNull  ,  Named  ]  _ #

    

kind  _ :  [ Literal
](https://docs.python.org/3/library/typing.html#typing.Literal "\(in Python
v3.11\)") [  'LIST'  ]  _ #

    

_ property  _ name  _ :  [ str
](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.11\)") _
#

    

_ property  _ is_list  _ :  [ bool
](https://docs.python.org/3/library/functions.html#bool "\(in Python v3.11\)")
_ #

    

_ property  _ is_non_null  _ :  [ bool
](https://docs.python.org/3/library/functions.html#bool "\(in Python v3.11\)")
_ #

    

_ static  _ non_null  (  _ name  _ , _ kind  =  'SCALAR'  _ )  #

    

_ static  _ non_null_list  (  _ name  _ , _ kind  =  'SCALAR'  _ )  #

    

_ static  _ root_type_name  (  _ type_  _ )  #

    

_ static  _ is_non_null  (  _ type_  _ )  #

    

_ static  _ is_list  (  _ type_  _ )  #

    

_ static  _ graphql  (  _ type_  _ )  #

    

_ class  _ subgrounds.schema.  TypeMeta  #

    

Bases: [ ` object  ` ](https://docs.python.org/3/library/functions.html#object
"\(in Python v3.11\)")

_ class  _ T  (  _ *  _ , _ name  _ , _ description  =  None  _ )  #

    

Bases:  ` BaseModel  `

Base class of all GraphQL schema types.

name  _ :  [ str  ](https://docs.python.org/3/library/stdtypes.html#str "\(in
Python v3.11\)") _ #

    

description  _ :  [ str  ](https://docs.python.org/3/library/stdtypes.html#str
"\(in Python v3.11\)") |  [ None
](https://docs.python.org/3/library/constants.html#None "\(in Python v3.11\)")
_ #

    

_ property  _ is_object  _ :  [ bool
](https://docs.python.org/3/library/functions.html#bool "\(in Python v3.11\)")
_ #

    

_ class  _ ArgumentMeta  (  _ *  _ , _ name  _ , _ description  =  None  _ , _
type  _ , _ defaultValue  =  None  _ )  #

    

Bases:  ` T  `

Class representing a field argument definition.

type_  _ :  [ Union
](https://docs.python.org/3/library/typing.html#typing.Union "\(in Python
v3.11\)") [  List  ,  NonNull  ,  Named  ]  _ #

    

default_value  _ :  [ str
](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.11\)") |
[ None  ](https://docs.python.org/3/library/constants.html#None "\(in Python
v3.11\)") _ #

    

_ class  _ FieldMeta  (  _ *  _ , _ name  _ , _ description  =  None  _ , _
args  _ , _ type  _ )  #

    

Bases:  ` T  `

Class representing an object field definition.

arguments  _ :  [ list  ](https://docs.python.org/3/library/stdtypes.html#list
"\(in Python v3.11\)") [  subgrounds.schema.TypeMeta.ArgumentMeta  ]  _ #

    

type_  _ :  [ Union
](https://docs.python.org/3/library/typing.html#typing.Union "\(in Python
v3.11\)") [  List  ,  NonNull  ,  Named  ]  _ #

    

has_arg  (  _ argname  _ )  #

    

type_of_arg  (  _ argname  _ )  #

    

_ class  _ ScalarMeta  (  _ *  _ , _ name  _ , _ description  =  None  _ , _
kind  =  'SCALAR'  _ )  #

    

Bases:  ` T  `

kind  _ :  [ Literal
](https://docs.python.org/3/library/typing.html#typing.Literal "\(in Python
v3.11\)") [  'SCALAR'  ]  _ #

    

Class representing an scalar definition.

_ class  _ ObjectMeta  (  _ *  _ , _ name  _ , _ description  =  None  _ , _
kind  =  'OBJECT'  _ , _ fields  _ , _ interfaces  =  None  _ )  #

    

Bases:  ` T  `

Class representing an object definition.

kind  _ :  [ Literal
](https://docs.python.org/3/library/typing.html#typing.Literal "\(in Python
v3.11\)") [  'OBJECT'  ]  _ #

    

fields  _ :  [ list  ](https://docs.python.org/3/library/stdtypes.html#list
"\(in Python v3.11\)") [  subgrounds.schema.TypeMeta.FieldMeta  ]  _ #

    

interfaces_  _ :  [ list
](https://docs.python.org/3/library/stdtypes.html#list "\(in Python v3.11\)")
[  [ dict  ](https://docs.python.org/3/library/stdtypes.html#dict "\(in Python
v3.11\)") ]  _ #

    

_ property  _ interfaces  _ :  [ list
](https://docs.python.org/3/library/stdtypes.html#list "\(in Python v3.11\)")
[  [ str  ](https://docs.python.org/3/library/stdtypes.html#str "\(in Python
v3.11\)") ]  _ #

    

_ property  _ is_object  _ :  [ bool
](https://docs.python.org/3/library/functions.html#bool "\(in Python v3.11\)")
_ #

    

field  (  _ fname  _ )  #

    

Returns the field definition of object ` self  ` with name ` fname  ` , if
any.

Parameters  :

    

  * **self** (  _TypeMeta.ObjectMeta_ ) -- The object type 

  * **fname** ( [ _str_ ](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.11\)") ) -- The name of the desired field definition 

Raises  :

    

[ **KeyError** ](https://docs.python.org/3/library/exceptions.html#KeyError
"\(in Python v3.11\)") \-- If no field named ` fname  ` is defined for object
` self  ` .

Returns  :

    

The field definition

Return type  :

    

TypeMeta.FieldMeta

type_of_field  (  _ fname  _ )  #

    

Returns the type reference of the field of object ` self  ` with name ` fname
` , if any.

Parameters  :

    

  * **self** (  _TypeMeta.ObjectMeta_ ) -- The object type 

  * **fname** ( [ _str_ ](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.11\)") ) -- The name of the desired field type 

Raises  :

    

[ **KeyError** ](https://docs.python.org/3/library/exceptions.html#KeyError
"\(in Python v3.11\)") \-- If no field named ` fname  ` is defined for object
` self  ` .

Returns  :

    

The field type reference

Return type  :

    

TypeRef.T

_ class  _ EnumValueMeta  (  _ *  _ , _ name  _ , _ description  =  None  _ )
#

    

Bases:  ` T  `

Class representing an enum value definition.

_ class  _ EnumMeta  (  _ *  _ , _ name  _ , _ description  =  None  _ , _
kind  =  'ENUM'  _ , _ enumValues  _ )  #

    

Bases:  ` T  `

Class representing an enum definition.

kind  _ :  [ Literal
](https://docs.python.org/3/library/typing.html#typing.Literal "\(in Python
v3.11\)") [  'ENUM'  ]  _ #

    

values  _ :  [ list  ](https://docs.python.org/3/library/stdtypes.html#list
"\(in Python v3.11\)") [  subgrounds.schema.TypeMeta.EnumValueMeta  ]  _ #

    

_ class  _ InterfaceMeta  (  _ *  _ , _ name  _ , _ description  =  None  _ ,
_ kind  =  'INTERFACE'  _ , _ fields  _ )  #

    

Bases:  ` T  `

Class representing an interface definition.

kind  _ :  [ Literal
](https://docs.python.org/3/library/typing.html#typing.Literal "\(in Python
v3.11\)") [  'INTERFACE'  ]  _ #

    

fields  _ :  [ list  ](https://docs.python.org/3/library/stdtypes.html#list
"\(in Python v3.11\)") [  subgrounds.schema.TypeMeta.FieldMeta  ]  _ #

    

_ property  _ is_object  _ :  [ bool
](https://docs.python.org/3/library/functions.html#bool "\(in Python v3.11\)")
_ #

    

field  (  _ fname  _ )  #

    

Returns the field definition of interface  self  with name  fname  , if any.

Parameters  :

    

  * **self** (  _TypeMeta.InterfaceMeta_ ) -- The interface type 

  * **fname** ( [ _str_ ](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.11\)") ) -- The name of the desired field definition 

Raises  :

    

[ **KeyError** ](https://docs.python.org/3/library/exceptions.html#KeyError
"\(in Python v3.11\)") \-- If no field named ` fname  ` is defined for
interface ` self  ` .

Returns  :

    

The field definition

Return type  :

    

TypeMeta.FieldMeta

_ class  _ UnionMeta  (  _ *  _ , _ name  _ , _ description  =  None  _ , _
kind  =  'UNION'  _ , _ possibleTypes  _ )  #

    

Bases:  ` T  `

Class representing an union definition.

kind  _ :  [ Literal
](https://docs.python.org/3/library/typing.html#typing.Literal "\(in Python
v3.11\)") [  'UNION'  ]  _ #

    

types  _ :  [ list  ](https://docs.python.org/3/library/stdtypes.html#list
"\(in Python v3.11\)") [  [ str
](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.11\)") ]
_ #

    

_ class  _ InputObjectMeta  (  _ *  _ , _ name  _ , _ description  =  None  _
, _ kind  =  'INPUT_OBJECT'  _ , _ inputFields  _ )  #

    

Bases:  ` T  `

Class representing an input object definition.

kind  _ :  [ Literal
](https://docs.python.org/3/library/typing.html#typing.Literal "\(in Python
v3.11\)") [  'INPUT_OBJECT'  ]  _ #

    

input_fields  _ :  [ list
](https://docs.python.org/3/library/stdtypes.html#list "\(in Python v3.11\)")
[  subgrounds.schema.TypeMeta.ArgumentMeta  ]  _ #

    

type_of_input_field  (  _ fname  _ )  #

    

Returns the type reference of the input field named  fname  in the input
object  self  , if any.

Parameters  :

    

  * **self** (  _TypeMeta.InputObjectMeta_ ) -- The input object 

  * **fname** ( [ _str_ ](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.11\)") ) -- The name of the input field 

Raises  :

    

[ **KeyError** ](https://docs.python.org/3/library/exceptions.html#KeyError
"\(in Python v3.11\)") \-- If  fname  is not an input field of input object
self

Returns  :

    

The type reference for input field  fname

Return type  :

    

TypeRef.T

_ class  _ subgrounds.schema.  SchemaMeta  (  _ *  _ , _ queryType  _ , _
types  _ , _ type_map  =  None  _ , _ mutationType  =  None  _ , _
subscriptionType  =  None  _ )  #

    

Bases:  ` BaseModel  `

Class representing a GraphQL schema.

Contains all type definitions.

query_type_  _ :  [ dict
](https://docs.python.org/3/library/stdtypes.html#dict "\(in Python v3.11\)")
[  [ str  ](https://docs.python.org/3/library/stdtypes.html#str "\(in Python
v3.11\)") ,  [ str  ](https://docs.python.org/3/library/stdtypes.html#str
"\(in Python v3.11\)") ]  _ #

    

types  _ :  [ list  ](https://docs.python.org/3/library/stdtypes.html#list
"\(in Python v3.11\)") [  subgrounds.schema.TypeMeta.ScalarMeta  |
subgrounds.schema.TypeMeta.ObjectMeta  |  subgrounds.schema.TypeMeta.EnumMeta
|  subgrounds.schema.TypeMeta.InterfaceMeta  |
subgrounds.schema.TypeMeta.UnionMeta  |
subgrounds.schema.TypeMeta.InputObjectMeta  ]  _ #

    

type_map  _ :  [ dict  ](https://docs.python.org/3/library/stdtypes.html#dict
"\(in Python v3.11\)") [  [ str
](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.11\)") ,
subgrounds.schema.TypeMeta.ScalarMeta  |
subgrounds.schema.TypeMeta.ObjectMeta  |  subgrounds.schema.TypeMeta.EnumMeta
|  subgrounds.schema.TypeMeta.InterfaceMeta  |
subgrounds.schema.TypeMeta.UnionMeta  |
subgrounds.schema.TypeMeta.InputObjectMeta  ]  _ #

    

mutation_type_  _ :  [ dict
](https://docs.python.org/3/library/stdtypes.html#dict "\(in Python v3.11\)")
[  [ str  ](https://docs.python.org/3/library/stdtypes.html#str "\(in Python
v3.11\)") ,  [ str  ](https://docs.python.org/3/library/stdtypes.html#str
"\(in Python v3.11\)") ]  |  [ None
](https://docs.python.org/3/library/constants.html#None "\(in Python v3.11\)")
_ #

    

subscription_type_  _ :  [ dict
](https://docs.python.org/3/library/stdtypes.html#dict "\(in Python v3.11\)")
[  [ str  ](https://docs.python.org/3/library/stdtypes.html#str "\(in Python
v3.11\)") ,  [ str  ](https://docs.python.org/3/library/stdtypes.html#str
"\(in Python v3.11\)") ]  |  [ None
](https://docs.python.org/3/library/constants.html#None "\(in Python v3.11\)")
_ #

    

_ property  _ query_type  _ :  [ str
](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.11\)") _
#

    

_ property  _ mutation_type  _ :  [ str
](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.11\)") |
[ None  ](https://docs.python.org/3/library/constants.html#None "\(in Python
v3.11\)") _ #

    

_ property  _ subscription_type  _ :  [ str
](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.11\)") |
[ None  ](https://docs.python.org/3/library/constants.html#None "\(in Python
v3.11\)") _ #

    

_ classmethod  _ type_map_generator  (  _ values  _ )  #

    

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

[ Next  subgrounds.subgrounds module  ](../subgrounds.subgrounds/) [ Previous
subgrounds.query module  ](../subgrounds.query/)

Made with [ Furo ](https://github.com/pradyunsg/furo)

[ ](https://github.com/0xPlaygrounds/subgrounds) [
](https://discord.gg/v4r4zhBAh2) [ ](https://twitter.com/Playgrounds0x)

On this page

  * subgrounds.schema module 
    * ` BaseModel  `
      * ` BaseModel.Config  `
        * ` BaseModel.Config.allow_population_by_field_name  `
    * ` TypeRef  `
      * ` TypeRef.T  `
        * ` TypeRef.T.name  `
        * ` TypeRef.T.is_list  `
        * ` TypeRef.T.is_non_null  `
      * ` TypeRef.Named  `
        * ` TypeRef.Named.name_  `
        * ` TypeRef.Named.kind  `
        * ` TypeRef.Named.name  `
      * ` TypeRef.NonNull  `
        * ` TypeRef.NonNull.inner  `
        * ` TypeRef.NonNull.kind  `
        * ` TypeRef.NonNull.name  `
        * ` TypeRef.NonNull.is_list  `
        * ` TypeRef.NonNull.is_non_null  `
      * ` TypeRef.List  `
        * ` TypeRef.List.inner  `
        * ` TypeRef.List.kind  `
        * ` TypeRef.List.name  `
        * ` TypeRef.List.is_list  `
        * ` TypeRef.List.is_non_null  `
      * ` TypeRef.non_null()  `
      * ` TypeRef.non_null_list()  `
      * ` TypeRef.root_type_name()  `
      * ` TypeRef.is_non_null()  `
      * ` TypeRef.is_list()  `
      * ` TypeRef.graphql()  `
    * ` TypeMeta  `
      * ` TypeMeta.T  `
        * ` TypeMeta.T.name  `
        * ` TypeMeta.T.description  `
        * ` TypeMeta.T.is_object  `
      * ` TypeMeta.ArgumentMeta  `
        * ` TypeMeta.ArgumentMeta.type_  `
        * ` TypeMeta.ArgumentMeta.default_value  `
      * ` TypeMeta.FieldMeta  `
        * ` TypeMeta.FieldMeta.arguments  `
        * ` TypeMeta.FieldMeta.type_  `
        * ` TypeMeta.FieldMeta.has_arg()  `
        * ` TypeMeta.FieldMeta.type_of_arg()  `
      * ` TypeMeta.ScalarMeta  `
        * ` TypeMeta.ScalarMeta.kind  `
      * ` TypeMeta.ObjectMeta  `
        * ` TypeMeta.ObjectMeta.kind  `
        * ` TypeMeta.ObjectMeta.fields  `
        * ` TypeMeta.ObjectMeta.interfaces_  `
        * ` TypeMeta.ObjectMeta.interfaces  `
        * ` TypeMeta.ObjectMeta.is_object  `
        * ` TypeMeta.ObjectMeta.field()  `
        * ` TypeMeta.ObjectMeta.type_of_field()  `
      * ` TypeMeta.EnumValueMeta  `
      * ` TypeMeta.EnumMeta  `
        * ` TypeMeta.EnumMeta.kind  `
        * ` TypeMeta.EnumMeta.values  `
      * ` TypeMeta.InterfaceMeta  `
        * ` TypeMeta.InterfaceMeta.kind  `
        * ` TypeMeta.InterfaceMeta.fields  `
        * ` TypeMeta.InterfaceMeta.is_object  `
        * ` TypeMeta.InterfaceMeta.field()  `
      * ` TypeMeta.UnionMeta  `
        * ` TypeMeta.UnionMeta.kind  `
        * ` TypeMeta.UnionMeta.types  `
      * ` TypeMeta.InputObjectMeta  `
        * ` TypeMeta.InputObjectMeta.kind  `
        * ` TypeMeta.InputObjectMeta.input_fields  `
        * ` TypeMeta.InputObjectMeta.type_of_input_field()  `
    * ` SchemaMeta  `
      * ` SchemaMeta.query_type_  `
      * ` SchemaMeta.types  `
      * ` SchemaMeta.type_map  `
      * ` SchemaMeta.mutation_type_  `
      * ` SchemaMeta.subscription_type_  `
      * ` SchemaMeta.query_type  `
      * ` SchemaMeta.mutation_type  `
      * ` SchemaMeta.subscription_type  `
      * ` SchemaMeta.type_map_generator()  `
      * ` SchemaMeta.type_of_typeref()  `
      * ` SchemaMeta.type_of()  `
      * ` SchemaMeta.type_of_input_object_meta()  `



Contents  Menu  Expand  Light mode  Dark mode  Auto light/dark mode

Hide navigation sidebar

Hide table of contents sidebar

Give us a ⭐️ on [ Github ](https://github.com/0xPlaygrounds/subgrounds) !

Toggle site navigation sidebar

_ _

[ ![Light Logo](../../../_static/assets/pg-logotype-dark.svg) ![Dark
Logo](../../../_static/assets/pg-logotype-primary.svg)
](https://playgrounds.network)

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
      * [ Merging ](../../getting_started/field_paths/merging/)
    * [ Querying ](../../getting_started/querying/)
    * [ Synthetic Fields ](../../getting_started/synthetic_fields/)
  * [ Advanced Topics ](../../advanced_topics/)

Toggle child pages in navigation

_ _

    * [ Pagination ](../../advanced_topics/pagination/)

Toggle child pages in navigation

_ _

      * [ Custom Strategies ](../../advanced_topics/pagination/custom/)
  * [ FAQ ](../../faq/)

Toggle child pages in navigation

_ _

    * [ Setup ](../../faq/setup/)

Toggle child pages in navigation

_ _

      * [ Python Versioning ](../../faq/setup/version_management/)
    * [ Contrib ](../../faq/contrib/)
  * [ Examples ](../../examples/)

Toggle child pages in navigation

_ _

    * [ Exchanges ](../../examples/exchanges/)
    * [ Bridges ](../../examples/bridges/)
    * [ Liquid Staking ](../../examples/liquid_staking/)
    * [ Governance ](../../examples/governance/)
    * [ Advanced Research ](../../examples/advanced_research/)
    * [ Vaults ](../../examples/vaults/)
  * [ Tutorials ](../../tutorials/)
  * [ Changelog ](../../changelog/)
  * [ API Reference ](../../modules/)

Toggle child pages in navigation

_ _

    * [ subgrounds package ](../subgrounds/)

Toggle child pages in navigation

_ _

      * [ subgrounds.pagination package ](../subgrounds.pagination/)

Toggle child pages in navigation

_ _

        * [ subgrounds.pagination.pagination module ](../subgrounds.pagination.pagination/)
        * [ subgrounds.pagination.preprocess module ](../subgrounds.pagination.preprocess/)
        * [ subgrounds.pagination.strategies module ](../subgrounds.pagination.strategies/)
        * [ subgrounds.pagination.utils module ](../subgrounds.pagination.utils/)
      * [ subgrounds.subgraph package ](../subgrounds.subgraph/)

Toggle child pages in navigation

_ _

        * [ subgrounds.subgraph.fieldpath module ](../subgrounds.subgraph.fieldpath/)
        * [ subgrounds.subgraph.filter module ](../subgrounds.subgraph.filter/)
        * [ subgrounds.subgraph.object module ](../subgrounds.subgraph.object/)
        * [ subgrounds.subgraph.subgraph module ](../subgrounds.subgraph.subgraph/)
      * [ subgrounds.client module ](../subgrounds.client/)
      * [ subgrounds.dash_wrappers module ](../subgrounds.dash_wrappers/)
      * [ subgrounds.dataframe_utils module ](../subgrounds.dataframe_utils/)
      * [ subgrounds.plotly_wrappers module ](../subgrounds.plotly_wrappers/)
      * [ subgrounds.query module ](../subgrounds.query/)
      * [ subgrounds.schema module ](../subgrounds.schema/)
      * subgrounds.subgrounds module 
      * [ subgrounds.transform module ](../subgrounds.transform/)
      * [ subgrounds.utils module ](../subgrounds.utils/)

Back to top

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

_ _

#  subgrounds.subgrounds module  #

Toplevel Subgrounds module

This module implements the toplevel API that most developers will be using
when querying The Graph with Subgrounds.

subgrounds.subgrounds.  store_schema  (  _ schema  _ , _ path  _ )  #

    

subgrounds.subgrounds.  load_schema  (  _ path  _ )  #

    

subgrounds.subgrounds.  subgraph_slug  (  _ url  _ )  #

    

_ class  _ subgrounds.subgrounds.  Subgrounds  (  _ headers:  dict[str  _ , _
typing.Any]  =  <factory> _ , _ global_transforms:
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
](../subgrounds.transform/#subgrounds.transform.RequestTransform
"subgrounds.transform.RequestTransform") ]  _ #

    

subgraphs  _ :  [ dict  ](https://docs.python.org/3/library/stdtypes.html#dict
"\(in Python v3.11\)") [  [ str
](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.11\)") ,
[ subgrounds.subgraph.subgraph.Subgraph
](../subgrounds.subgraph.subgraph/#subgrounds.subgraph.subgraph.Subgraph
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

    

[ Subgraph ](../subgrounds/#subgrounds.Subgraph "subgrounds.Subgraph")

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

    

[ Subgraph ](../subgrounds/#subgrounds.Subgraph "subgrounds.Subgraph")

mk_request  (  _ fpaths  _ )  #

    

Creates a ` DataRequest  ` object by combining one or more ` FieldPath  `
objects.

Parameters  :

    

**fpaths** ( [ _FieldPath_ ](../subgrounds/#subgrounds.FieldPath
"subgrounds.FieldPath") _|_ [ _list_
](https://docs.python.org/3/library/stdtypes.html#list "\(in Python v3.11\)")
_[_ [ _FieldPath_ ](../subgrounds/#subgrounds.FieldPath
"subgrounds.FieldPath") _]_ ) -- One or more ` FieldPath  ` objects that
should be included in the request

Returns  :

    

A new ` DataRequest  ` object

Return type  :

    

[ DataRequest ](../subgrounds.query/#subgrounds.query.DataRequest
"subgrounds.query.DataRequest")

execute  (  _ req  _ , _ pagination_strategy=<class
'subgrounds.pagination.strategies.LegacyStrategy'> _ )  #

    

Executes a ` DataRequest  ` object, sending the underlying query(ies) to the
server and returning a data blob (list of Python dictionaries, one per actual
query).

Parameters  :

    

  * **req** ( [ _DataRequest_ ](../subgrounds.query/#subgrounds.query.DataRequest "subgrounds.query.DataRequest") ) -- The ` DataRequest  ` object to be executed 

  * **pagination_strategy** ( _Optional_ _[_ _Type_ _[_ [ _PaginationStrategy_ ](../subgrounds.pagination/#subgrounds.pagination.PaginationStrategy "subgrounds.pagination.PaginationStrategy") _]_ _]_ _,_ _optional_ ) -- A Class implementing the ` PaginationStrategy  ` ` Protocol  ` . If ` None  ` , then automatic pagination is disabled. Defaults to ` LegacyStrategy  ` . 

Returns  :

    

The reponse data

Return type  :

    

[ list ](https://docs.python.org/3/library/stdtypes.html#list "\(in Python
v3.11\)") [ [ dict ](https://docs.python.org/3/library/stdtypes.html#dict
"\(in Python v3.11\)") ]

execute_iter  (  _ req  _ , _ pagination_strategy=<class
'subgrounds.pagination.strategies.LegacyStrategy'> _ )  #

    

Same as  execute  , except that an iterator is returned which will iterate the
data pages.

Parameters  :

    

  * **req** ( [ _DataRequest_ ](../subgrounds.query/#subgrounds.query.DataRequest "subgrounds.query.DataRequest") ) -- The ` DataRequest  ` object to be executed 

  * **pagination_strategy** ( _Optional_ _[_ _Type_ _[_ [ _PaginationStrategy_ ](../subgrounds.pagination/#subgrounds.pagination.PaginationStrategy "subgrounds.pagination.PaginationStrategy") _]_ _]_ _,_ _optional_ ) -- A Class implementing the ` PaginationStrategy  ` ` Protocol  ` . If ` None  ` , then automatic pagination is disabled. Defaults to ` LegacyStrategy  ` . 

Returns  :

    

An iterator over the reponse data pages

Return type  :

    

Iterator[ [ dict ](https://docs.python.org/3/library/stdtypes.html#dict "\(in
Python v3.11\)") ]

query_json  (  _ fpaths  _ , _ pagination_strategy=<class
'subgrounds.pagination.strategies.LegacyStrategy'> _ )  #

    

Equivalent to ` Subgrounds.execute(Subgrounds.mk_request(fpaths),
pagination_strategy)  ` .

Parameters  :

    

  * **fpaths** ( [ _FieldPath_ ](../subgrounds/#subgrounds.FieldPath "subgrounds.FieldPath") _|_ [ _list_ ](https://docs.python.org/3/library/stdtypes.html#list "\(in Python v3.11\)") _[_ [ _FieldPath_ ](../subgrounds/#subgrounds.FieldPath "subgrounds.FieldPath") _]_ ) -- One or more ` FieldPath  ` objects that should be included in the request. 

  * **pagination_strategy** ( _Optional_ _[_ _Type_ _[_ [ _PaginationStrategy_ ](../subgrounds.pagination/#subgrounds.pagination.PaginationStrategy "subgrounds.pagination.PaginationStrategy") _]_ _]_ _,_ _optional_ ) -- A Class implementing the ` PaginationStrategy  ` ` Protocol  ` . If ` None  ` , then automatic pagination is disabled. Defaults to ` LegacyStrategy  ` . 

Returns  :

    

The reponse data

Return type  :

    

[ list ](https://docs.python.org/3/library/stdtypes.html#list "\(in Python
v3.11\)") [ [ dict ](https://docs.python.org/3/library/stdtypes.html#dict
"\(in Python v3.11\)") [ [ str
](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.11\)") ,
Any]]

query_json_iter  (  _ fpaths  _ , _ pagination_strategy=<class
'subgrounds.pagination.strategies.LegacyStrategy'> _ )  #

    

Same as  query_json  except an iterator over the response data pages is
returned.

Parameters  :

    

  * **fpaths** ( [ _FieldPath_ ](../subgrounds/#subgrounds.FieldPath "subgrounds.FieldPath") _|_ [ _list_ ](https://docs.python.org/3/library/stdtypes.html#list "\(in Python v3.11\)") _[_ [ _FieldPath_ ](../subgrounds/#subgrounds.FieldPath "subgrounds.FieldPath") _]_ ) -- One or more ` FieldPath  ` objects that should be included in the request. 

  * **pagination_strategy** ( _Optional_ _[_ _Type_ _[_ [ _PaginationStrategy_ ](../subgrounds.pagination/#subgrounds.pagination.PaginationStrategy "subgrounds.pagination.PaginationStrategy") _]_ _]_ _,_ _optional_ ) -- A Class implementing the ` PaginationStrategy  ` ` Protocol  ` . If ` None  ` , then automatic pagination is disabled. Defaults to ` LegacyStrategy  ` . 

Returns  :

    

The reponse data

Return type  :

    

[ list ](https://docs.python.org/3/library/stdtypes.html#list "\(in Python
v3.11\)") [ [ dict ](https://docs.python.org/3/library/stdtypes.html#dict
"\(in Python v3.11\)") [ [ str
](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.11\)") ,
Any]]

query_df  (  _ fpaths  _ , _ columns=None  _ , _ concat=False  _ , _
pagination_strategy=<class  'subgrounds.pagination.strategies.LegacyStrategy'>
_ )  #

    

Same as  ` Subgrounds.query()  ` but formats the response data into a Pandas
DataFrame. If the response data cannot be flattened to a single query (e.g.:
when querying multiple list fields that return different entities), then
multiple dataframes are returned

` fpaths  ` is a list of ` FieldPath  ` objects that indicate which data must
be queried.

` columns  ` is an optional argument used to rename the dataframes(s) columns.
The length of ` columns  ` must be the same as the number of columns of _all_
returned dataframes.

` concat  ` indicates whether or not the resulting dataframes should be
concatenated together. The dataframes must have the same number of columns, as
well as the same column names and types (the names can be set using the `
columns  ` argument).

Parameters  :

    

  * **fpaths** ( [ _FieldPath_ ](../subgrounds/#subgrounds.FieldPath "subgrounds.FieldPath") _|_ [ _list_ ](https://docs.python.org/3/library/stdtypes.html#list "\(in Python v3.11\)") _[_ [ _FieldPath_ ](../subgrounds/#subgrounds.FieldPath "subgrounds.FieldPath") _]_ ) -- One or more  FieldPath  objects that should be included in the request. 

  * **columns** ( _Optional_ _[_ [ _list_ ](https://docs.python.org/3/library/stdtypes.html#list "\(in Python v3.11\)") _[_ [ _str_ ](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.11\)") _]_ _]_ _,_ _optional_ ) -- The column labels. Defaults to None. 

  * **merge** ( [ _bool_ ](https://docs.python.org/3/library/functions.html#bool "\(in Python v3.11\)") _,_ _optional_ ) -- Whether or not to merge resulting dataframes. 

  * **pagination_strategy** ( _Optional_ _[_ _Type_ _[_ [ _PaginationStrategy_ ](../subgrounds.pagination/#subgrounds.pagination.PaginationStrategy "subgrounds.pagination.PaginationStrategy") _]_ _]_ _,_ _optional_ ) -- A Class implementing the ` PaginationStrategy  ` ` Protocol  ` . If ` None  ` , then automatic pagination is disabled. Defaults to ` LegacyStrategy  ` . 

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
    

query_df_iter  (  _ fpaths  _ , _ pagination_strategy=<class
'subgrounds.pagination.strategies.LegacyStrategy'> _ )  #

    

Same as  query_df  except an iterator over the response data pages is returned
:param fpaths: One or more  FieldPath  objects that

> should be included in the request

Parameters  :

    

  * **columns** ( _Optional_ _[_ [ _list_ ](https://docs.python.org/3/library/stdtypes.html#list "\(in Python v3.11\)") _[_ [ _str_ ](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.11\)") _]_ _]_ _,_ _optional_ ) -- The column labels. Defaults to None. 

  * **merge** ( [ _bool_ ](https://docs.python.org/3/library/functions.html#bool "\(in Python v3.11\)") _,_ _optional_ ) -- Whether or not to merge resulting dataframes. 

  * **pagination_strategy** ( _Optional_ _[_ _Type_ _[_ [ _PaginationStrategy_ ](../subgrounds.pagination/#subgrounds.pagination.PaginationStrategy "subgrounds.pagination.PaginationStrategy") _]_ _]_ _,_ _optional_ ) -- A Class implementing the ` PaginationStrategy  ` ` Protocol  ` . If ` None  ` , then automatic pagination is disabled. Defaults to ` LegacyStrategy  ` . 

Returns  :

    

An iterator over the response data pages, each as a DataFrame

Return type  :

    

Iterator[pd.DataFrame]

query  (  _ fpaths  _ , _ unwrap=True  _ , _ pagination_strategy=<class
'subgrounds.pagination.strategies.LegacyStrategy'> _ )  #

    

Executes one or multiple ` FieldPath  ` objects immediately and return the
data (as a tuple if multiple ` FieldPath  ` objects are provided).

Parameters  :

    

  * **fpaths** ( [ _FieldPath_ ](../subgrounds/#subgrounds.FieldPath "subgrounds.FieldPath") _|_ [ _list_ ](https://docs.python.org/3/library/stdtypes.html#list "\(in Python v3.11\)") _[_ [ _FieldPath_ ](../subgrounds/#subgrounds.FieldPath "subgrounds.FieldPath") _]_ ) -- One or more ` FieldPath  ` object(s) to query. 

  * **unwrap** ( [ _bool_ ](https://docs.python.org/3/library/functions.html#bool "\(in Python v3.11\)") _,_ _optional_ ) -- Flag indicating whether or not, in the case where the returned data is a list of one element, the element itself should be returned instead of the list. Defaults to ` True  ` . 

  * **pagination_strategy** ( _Optional_ _[_ _Type_ _[_ [ _PaginationStrategy_ ](../subgrounds.pagination/#subgrounds.pagination.PaginationStrategy "subgrounds.pagination.PaginationStrategy") _]_ _]_ _,_ _optional_ ) -- A Class implementing the ` PaginationStrategy  ` ` Protocol  ` . If ` None  ` , then automatic pagination is disabled. Defaults to ` LegacyStrategy  ` . 

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
    

query_iter  (  _ fpaths  _ , _ unwrap=True  _ , _ pagination_strategy=<class
'subgrounds.pagination.strategies.LegacyStrategy'> _ )  #

    

Same as  query  except an iterator over the resonse data pages is returned.

Parameters  :

    

  * **fpath** ( [ _FieldPath_ ](../subgrounds/#subgrounds.FieldPath "subgrounds.FieldPath") _|_ [ _list_ ](https://docs.python.org/3/library/stdtypes.html#list "\(in Python v3.11\)") _[_ [ _FieldPath_ ](../subgrounds/#subgrounds.FieldPath "subgrounds.FieldPath") _]_ ) -- One or more ` FieldPath  ` object(s) to query. 

  * **unwrap** ( [ _bool_ ](https://docs.python.org/3/library/functions.html#bool "\(in Python v3.11\)") _,_ _optional_ ) -- Flag indicating whether or not, in the case where the returned data is a list of one element, the element itself should be returned instead of the list. Defaults to ` True  ` . 

  * **pagination_strategy** ( _Optional_ _[_ _Type_ _[_ [ _PaginationStrategy_ ](../subgrounds.pagination/#subgrounds.pagination.PaginationStrategy "subgrounds.pagination.PaginationStrategy") _]_ _]_ _,_ _optional_ ) -- A Class implementing the ` PaginationStrategy  ` ` Protocol  ` . If ` None  ` , then automatic pagination is disabled. Defaults to ` LegacyStrategy  ` . 

Returns  :

    

An iterator over the ` FieldPath  ` object(s)' data pages

Return type  :

    

Iterator[ [ type ](https://docs.python.org/3/library/functions.html#type "\(in
Python v3.11\)") ]

[ Next  subgrounds.transform module  ](../subgrounds.transform/) [ Previous
subgrounds.schema module  ](../subgrounds.schema/)

Made with [ Furo ](https://github.com/pradyunsg/furo)

[ ](https://github.com/0xPlaygrounds/subgrounds) [
](https://discord.gg/v4r4zhBAh2) [ ](https://twitter.com/Playgrounds0x)

On this page

  * subgrounds.subgrounds module 
    * ` store_schema()  `
    * ` load_schema()  `
    * ` subgraph_slug()  `
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



Contents  Menu  Expand  Light mode  Dark mode  Auto light/dark mode

Hide navigation sidebar

Hide table of contents sidebar

Give us a ⭐️ on [ Github ](https://github.com/0xPlaygrounds/subgrounds) !

Toggle site navigation sidebar

_ _

[ ![Light Logo](../../../_static/assets/pg-logotype-dark.svg) ![Dark
Logo](../../../_static/assets/pg-logotype-primary.svg)
](https://playgrounds.network)

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
      * [ Merging ](../../getting_started/field_paths/merging/)
    * [ Querying ](../../getting_started/querying/)
    * [ Synthetic Fields ](../../getting_started/synthetic_fields/)
  * [ Advanced Topics ](../../advanced_topics/)

Toggle child pages in navigation

_ _

    * [ Pagination ](../../advanced_topics/pagination/)

Toggle child pages in navigation

_ _

      * [ Custom Strategies ](../../advanced_topics/pagination/custom/)
  * [ FAQ ](../../faq/)

Toggle child pages in navigation

_ _

    * [ Setup ](../../faq/setup/)

Toggle child pages in navigation

_ _

      * [ Python Versioning ](../../faq/setup/version_management/)
    * [ Contrib ](../../faq/contrib/)
  * [ Examples ](../../examples/)

Toggle child pages in navigation

_ _

    * [ Exchanges ](../../examples/exchanges/)
    * [ Bridges ](../../examples/bridges/)
    * [ Liquid Staking ](../../examples/liquid_staking/)
    * [ Governance ](../../examples/governance/)
    * [ Advanced Research ](../../examples/advanced_research/)
    * [ Vaults ](../../examples/vaults/)
  * [ Tutorials ](../../tutorials/)
  * [ Changelog ](../../changelog/)
  * [ API Reference ](../../modules/)

Toggle child pages in navigation

_ _

    * [ subgrounds package ](../subgrounds/)

Toggle child pages in navigation

_ _

      * [ subgrounds.pagination package ](../subgrounds.pagination/)

Toggle child pages in navigation

_ _

        * [ subgrounds.pagination.pagination module ](../subgrounds.pagination.pagination/)
        * [ subgrounds.pagination.preprocess module ](../subgrounds.pagination.preprocess/)
        * [ subgrounds.pagination.strategies module ](../subgrounds.pagination.strategies/)
        * [ subgrounds.pagination.utils module ](../subgrounds.pagination.utils/)
      * [ subgrounds.subgraph package ](../subgrounds.subgraph/)

Toggle child pages in navigation

_ _

        * [ subgrounds.subgraph.fieldpath module ](../subgrounds.subgraph.fieldpath/)
        * [ subgrounds.subgraph.filter module ](../subgrounds.subgraph.filter/)
        * [ subgrounds.subgraph.object module ](../subgrounds.subgraph.object/)
        * [ subgrounds.subgraph.subgraph module ](../subgrounds.subgraph.subgraph/)
      * [ subgrounds.client module ](../subgrounds.client/)
      * [ subgrounds.dash_wrappers module ](../subgrounds.dash_wrappers/)
      * [ subgrounds.dataframe_utils module ](../subgrounds.dataframe_utils/)
      * [ subgrounds.plotly_wrappers module ](../subgrounds.plotly_wrappers/)
      * [ subgrounds.query module ](../subgrounds.query/)
      * [ subgrounds.schema module ](../subgrounds.schema/)
      * [ subgrounds.subgrounds module ](../subgrounds.subgrounds/)
      * subgrounds.transform module 
      * [ subgrounds.utils module ](../subgrounds.utils/)

Back to top

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

_ _

#  subgrounds.transform module  #

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

subgrounds.transform.  select_data  (  _ select  _ , _ data  _ )  #

    

_ class  _ subgrounds.transform.  RequestTransform  #

    

Bases: [ ` ABC  ` ](https://docs.python.org/3/library/abc.html#abc.ABC "\(in
Python v3.11\)")

Abstract class representing a transformation layer to be applied to entire `
DataRequest  ` objects.

_ abstract  _ transform_request  (  _ req  _ )  #

    

Method that will be applied to all ` DataRequest  ` objects that pass through
the transformation layer.

Parameters  :

    

**req** ( [ _DataRequest_ ](../subgrounds.query/#subgrounds.query.DataRequest
"subgrounds.query.DataRequest") ) -- The initial request object

Returns  :

    

The transformed request object

Return type  :

    

[ DataRequest ](../subgrounds.query/#subgrounds.query.DataRequest
"subgrounds.query.DataRequest")

_ abstract  _ transform_response  (  _ req  _ , _ data  _ )  #

    

Method to be applied to all response data ` data  ` of requests that pass
through the transformation layer.

` req  ` is the initial ` DataRequest  ` object that yielded the resulting
JSON data ` data  ` .

Parameters  :

    

  * **req** ( [ _DataRequest_ ](../subgrounds.query/#subgrounds.query.DataRequest "subgrounds.query.DataRequest") ) -- Initial data request object 

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

    

Bases: [ ` ABC  ` ](https://docs.python.org/3/library/abc.html#abc.ABC "\(in
Python v3.11\)")

Abstract class representing a transformation layer to be applied to ` Document
` objects.

_ abstract  _ transform_document  (  _ doc  _ )  #

    

Method that will be applied to all ` Document  ` objects that pass through the
transformation layer.

Parameters  :

    

**doc** ( [ _Document_ ](../subgrounds.query/#subgrounds.query.Document
"subgrounds.query.Document") ) -- The initial document

Returns  :

    

The transformed document

Return type  :

    

[ Document ](../subgrounds.query/#subgrounds.query.Document
"subgrounds.query.Document")

_ abstract  _ transform_response  (  _ req  _ , _ data  _ )  #

    

Method to be applied to all response data ` data  ` of requests that pass
through the transformation layer.

` doc  ` is the initial ` Document  ` object that yielded the resulting JSON
data ` data  ` .

Parameters  :

    

  * **doc** ( [ _Document_ ](../subgrounds.query/#subgrounds.query.Document "subgrounds.query.Document") ) -- Initial document 

  * **data** ( [ _dict_ ](https://docs.python.org/3/library/stdtypes.html#dict "\(in Python v3.11\)") _[_ [ _str_ ](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.11\)") _,_ _Any_ _]_ ) -- JSON data blob resulting from the execution of the transformed document. 

Returns  :

    

The transformed response data

Return type  :

    

[ dict ](https://docs.python.org/3/library/stdtypes.html#dict "\(in Python
v3.11\)") [ [ str ](https://docs.python.org/3/library/stdtypes.html#str "\(in
Python v3.11\)") , Any]

_ class  _ subgrounds.transform.  TypeTransform  (  _ type_  _ , _ f  _ )  #

    

Bases:  ` DocumentTransform  `

Transform to be applied to scalar fields on a per-type basis.

type_  #

    

Type indicating which scalar values (i.e.: values of that type) should be
transformed using the function ` f  `

Type  :

    

[ TypeRef.T ](../subgrounds.schema/#subgrounds.schema.TypeRef.T
"subgrounds.schema.TypeRef.T")

f  #

    

Function to be applied to scalar values of type ` type_  ` in the response
data.

Type  :

    

Callable[[Any], Any]

type_  _ :  [ T  ](../subgrounds.schema/#subgrounds.schema.TypeRef.T
"subgrounds.schema.TypeRef.T") _ #

    

f  _ :  [ Callable
](https://docs.python.org/3/library/typing.html#typing.Callable "\(in Python
v3.11\)") [  [  [ Any
](https://docs.python.org/3/library/typing.html#typing.Any "\(in Python
v3.11\)") ]  ,  [ Any
](https://docs.python.org/3/library/typing.html#typing.Any "\(in Python
v3.11\)") ]  _ #

    

transform_document  (  _ doc  _ )  #

    

Method that will be applied to all ` Document  ` objects that pass through the
transformation layer.

Parameters  :

    

**doc** ( [ _Document_ ](../subgrounds.query/#subgrounds.query.Document
"subgrounds.query.Document") ) -- The initial document

Returns  :

    

The transformed document

Return type  :

    

[ Document ](../subgrounds.query/#subgrounds.query.Document
"subgrounds.query.Document")

transform_response  (  _ doc  _ , _ data  _ )  #

    

Method to be applied to all response data ` data  ` of requests that pass
through the transformation layer.

` doc  ` is the initial ` Document  ` object that yielded the resulting JSON
data ` data  ` .

Parameters  :

    

  * **doc** ( [ _Document_ ](../subgrounds.query/#subgrounds.query.Document "subgrounds.query.Document") ) -- Initial document 

  * **data** ( [ _dict_ ](https://docs.python.org/3/library/stdtypes.html#dict "\(in Python v3.11\)") _[_ [ _str_ ](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.11\)") _,_ _Any_ _]_ ) -- JSON data blob resulting from the execution of the transformed document. 

Returns  :

    

The transformed response data

Return type  :

    

[ dict ](https://docs.python.org/3/library/stdtypes.html#dict "\(in Python
v3.11\)") [ [ str ](https://docs.python.org/3/library/stdtypes.html#str "\(in
Python v3.11\)") , Any]

_ class  _ subgrounds.transform.  LocalSyntheticField  (  _ subgraph  _ , _
fmeta  _ , _ type_  _ , _ f  _ , _ default  _ , _ args  _ )  #

    

Bases:  ` DocumentTransform  `

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

    

[ Subgraph ](../subgrounds/#subgrounds.Subgraph "subgrounds.Subgraph")

fmeta  #

    

The synthetic field

Type  :

    

[ TypeMeta.FieldMeta
](../subgrounds.schema/#subgrounds.schema.TypeMeta.FieldMeta
"subgrounds.schema.TypeMeta.FieldMeta")

type_  #

    

The object for which the synthetic field is defined

Type  :

    

[ TypeMeta.ObjectMeta
](../subgrounds.schema/#subgrounds.schema.TypeMeta.ObjectMeta
"subgrounds.schema.TypeMeta.ObjectMeta") | [ TypeMeta.InterfaceMeta
](../subgrounds.schema/#subgrounds.schema.TypeMeta.InterfaceMeta
"subgrounds.schema.TypeMeta.InterfaceMeta")

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
v3.11\)") [ [ Selection ](../subgrounds.query/#subgrounds.query.Selection
"subgrounds.query.Selection") ]

subgraph  _ :  [ Subgraph  ](../subgrounds/#subgrounds.Subgraph
"subgrounds.Subgraph") _ #

    

fmeta  _ :  [ TypeMeta.FieldMeta
](../subgrounds.schema/#subgrounds.schema.TypeMeta.FieldMeta
"subgrounds.schema.TypeMeta.FieldMeta") _ #

    

type_  _ :  [ TypeMeta.ObjectMeta
](../subgrounds.schema/#subgrounds.schema.TypeMeta.ObjectMeta
"subgrounds.schema.TypeMeta.ObjectMeta") |  [ TypeMeta.InterfaceMeta
](../subgrounds.schema/#subgrounds.schema.TypeMeta.InterfaceMeta
"subgrounds.schema.TypeMeta.InterfaceMeta") _ #

    

f  _ :  Callable  _ #

    

default  _ :  Any  _ #

    

args  _ :  [ list  ](https://docs.python.org/3/library/stdtypes.html#list
"\(in Python v3.11\)") [  [ Selection
](../subgrounds.query/#subgrounds.query.Selection
"subgrounds.query.Selection") ]  _ #

    

transform_document  (  _ doc  _ )  #

    

Method that will be applied to all ` Document  ` objects that pass through the
transformation layer.

Parameters  :

    

**doc** ( [ _Document_ ](../subgrounds.query/#subgrounds.query.Document
"subgrounds.query.Document") ) -- The initial document

Returns  :

    

The transformed document

Return type  :

    

[ Document ](../subgrounds.query/#subgrounds.query.Document
"subgrounds.query.Document")

transform_response  (  _ doc  _ , _ data  _ )  #

    

Method to be applied to all response data ` data  ` of requests that pass
through the transformation layer.

` doc  ` is the initial ` Document  ` object that yielded the resulting JSON
data ` data  ` .

Parameters  :

    

  * **doc** ( [ _Document_ ](../subgrounds.query/#subgrounds.query.Document "subgrounds.query.Document") ) -- Initial document 

  * **data** ( [ _dict_ ](https://docs.python.org/3/library/stdtypes.html#dict "\(in Python v3.11\)") _[_ [ _str_ ](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.11\)") _,_ _Any_ _]_ ) -- JSON data blob resulting from the execution of the transformed document. 

Returns  :

    

The transformed response data

Return type  :

    

[ dict ](https://docs.python.org/3/library/stdtypes.html#dict "\(in Python
v3.11\)") [ [ str ](https://docs.python.org/3/library/stdtypes.html#str "\(in
Python v3.11\)") , Any]

_ class  _ subgrounds.transform.  SplitTransform  (  _ query  _ )  #

    

Bases:  ` RequestTransform  `

transform_request  (  _ req  _ )  #

    

Method that will be applied to all ` DataRequest  ` objects that pass through
the transformation layer.

Parameters  :

    

**req** ( [ _DataRequest_ ](../subgrounds.query/#subgrounds.query.DataRequest
"subgrounds.query.DataRequest") ) -- The initial request object

Returns  :

    

The transformed request object

Return type  :

    

[ DataRequest ](../subgrounds.query/#subgrounds.query.DataRequest
"subgrounds.query.DataRequest")

transform_response  (  _ req  _ , _ data  _ )  #

    

Method to be applied to all response data ` data  ` of requests that pass
through the transformation layer.

` req  ` is the initial ` DataRequest  ` object that yielded the resulting
JSON data ` data  ` .

Parameters  :

    

  * **req** ( [ _DataRequest_ ](../subgrounds.query/#subgrounds.query.DataRequest "subgrounds.query.DataRequest") ) -- Initial data request object 

  * **data** ( [ _list_ ](https://docs.python.org/3/library/stdtypes.html#list "\(in Python v3.11\)") _[_ [ _dict_ ](https://docs.python.org/3/library/stdtypes.html#dict "\(in Python v3.11\)") _[_ [ _str_ ](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.11\)") _,_ _Any_ _]_ _]_ ) -- JSON data blob resulting from the execution of the transformed data request. 

Returns  :

    

The transformed response data

Return type  :

    

[ list ](https://docs.python.org/3/library/stdtypes.html#list "\(in Python
v3.11\)") [ [ dict ](https://docs.python.org/3/library/stdtypes.html#dict
"\(in Python v3.11\)") [ [ str
](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.11\)") ,
Any]]

[ Next  subgrounds.utils module  ](../subgrounds.utils/) [ Previous
subgrounds.subgrounds module  ](../subgrounds.subgrounds/)

Made with [ Furo ](https://github.com/pradyunsg/furo)

[ ](https://github.com/0xPlaygrounds/subgrounds) [
](https://discord.gg/v4r4zhBAh2) [ ](https://twitter.com/Playgrounds0x)

On this page

  * subgrounds.transform module 
    * ` select_data()  `
    * ` RequestTransform  `
      * ` RequestTransform.transform_request()  `
      * ` RequestTransform.transform_response()  `
    * ` DocumentTransform  `
      * ` DocumentTransform.transform_document()  `
      * ` DocumentTransform.transform_response()  `
    * ` TypeTransform  `
      * ` TypeTransform.type_  `
      * ` TypeTransform.f  `
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

Give us a ⭐️ on [ Github ](https://github.com/0xPlaygrounds/subgrounds) !

Toggle site navigation sidebar

_ _

[ ![Light Logo](../../../_static/assets/pg-logotype-dark.svg) ![Dark
Logo](../../../_static/assets/pg-logotype-primary.svg)
](https://playgrounds.network)

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
      * [ Merging ](../../getting_started/field_paths/merging/)
    * [ Querying ](../../getting_started/querying/)
    * [ Synthetic Fields ](../../getting_started/synthetic_fields/)
  * [ Advanced Topics ](../../advanced_topics/)

Toggle child pages in navigation

_ _

    * [ Pagination ](../../advanced_topics/pagination/)

Toggle child pages in navigation

_ _

      * [ Custom Strategies ](../../advanced_topics/pagination/custom/)
  * [ FAQ ](../../faq/)

Toggle child pages in navigation

_ _

    * [ Setup ](../../faq/setup/)

Toggle child pages in navigation

_ _

      * [ Python Versioning ](../../faq/setup/version_management/)
    * [ Contrib ](../../faq/contrib/)
  * [ Examples ](../../examples/)

Toggle child pages in navigation

_ _

    * [ Exchanges ](../../examples/exchanges/)
    * [ Bridges ](../../examples/bridges/)
    * [ Liquid Staking ](../../examples/liquid_staking/)
    * [ Governance ](../../examples/governance/)
    * [ Advanced Research ](../../examples/advanced_research/)
    * [ Vaults ](../../examples/vaults/)
  * [ Tutorials ](../../tutorials/)
  * [ Changelog ](../../changelog/)
  * [ API Reference ](../../modules/)

Toggle child pages in navigation

_ _

    * [ subgrounds package ](../subgrounds/)

Toggle child pages in navigation

_ _

      * [ subgrounds.pagination package ](../subgrounds.pagination/)

Toggle child pages in navigation

_ _

        * [ subgrounds.pagination.pagination module ](../subgrounds.pagination.pagination/)
        * [ subgrounds.pagination.preprocess module ](../subgrounds.pagination.preprocess/)
        * [ subgrounds.pagination.strategies module ](../subgrounds.pagination.strategies/)
        * [ subgrounds.pagination.utils module ](../subgrounds.pagination.utils/)
      * [ subgrounds.subgraph package ](../subgrounds.subgraph/)

Toggle child pages in navigation

_ _

        * [ subgrounds.subgraph.fieldpath module ](../subgrounds.subgraph.fieldpath/)
        * [ subgrounds.subgraph.filter module ](../subgrounds.subgraph.filter/)
        * [ subgrounds.subgraph.object module ](../subgrounds.subgraph.object/)
        * [ subgrounds.subgraph.subgraph module ](../subgrounds.subgraph.subgraph/)
      * [ subgrounds.client module ](../subgrounds.client/)
      * [ subgrounds.dash_wrappers module ](../subgrounds.dash_wrappers/)
      * [ subgrounds.dataframe_utils module ](../subgrounds.dataframe_utils/)
      * [ subgrounds.plotly_wrappers module ](../subgrounds.plotly_wrappers/)
      * [ subgrounds.query module ](../subgrounds.query/)
      * [ subgrounds.schema module ](../subgrounds.schema/)
      * [ subgrounds.subgrounds module ](../subgrounds.subgrounds/)
      * [ subgrounds.transform module ](../subgrounds.transform/)
      * subgrounds.utils module 

Back to top

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

_ _

#  subgrounds.utils module  #

Utility module for Subgrounds

subgrounds.utils.  flatten  (  _ t  _ )  #

    

subgrounds.utils.  identity  (  _ x  _ )  #

    

subgrounds.utils.  fst  (  _ tup  _ )  #

    

subgrounds.utils.  snd  (  _ tup  _ )  #

    

subgrounds.utils.  intersection  (  _ l1  _ , _ l2  _ , _ key=<function
identity> _ , _ combine=<function  <lambda>> _ )  #

    

subgrounds.utils.  rel_complement  (  _ l1  _ , _ l2  _ , _ key=<function
identity> _ )  #

    

subgrounds.utils.  sym_diff  (  _ l1  _ , _ l2  _ , _ key=<function  identity>
_ )  #

    

subgrounds.utils.  union  (  _ l1  _ , _ l2  _ , _ key=<function  identity> _
, _ combine=<function  <lambda>> _ )  #

    

subgrounds.utils.  filter_none  (  _ items  _ )  #

    

subgrounds.utils.  loop_generator  (  _ items  _ )  #

    

subgrounds.utils.  repeat  (  _ value  _ , _ n  _ )  #

    

subgrounds.utils.  extract_data  (  _ keys  _ , _ data  _ )  #

    

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
](../subgrounds/#subgrounds.Subgrounds "subgrounds.Subgrounds") with a headers

    

parameter with a dictionary containing an empty "User-Agent" key-value
pairing.

[ Previous  subgrounds.transform module  ](../subgrounds.transform/)

Made with [ Furo ](https://github.com/pradyunsg/furo)

[ ](https://github.com/0xPlaygrounds/subgrounds) [
](https://discord.gg/v4r4zhBAh2) [ ](https://twitter.com/Playgrounds0x)

On this page

  * subgrounds.utils module 
    * ` flatten()  `
    * ` identity()  `
    * ` fst()  `
    * ` snd()  `
    * ` intersection()  `
    * ` rel_complement()  `
    * ` sym_diff()  `
    * ` union()  `
    * ` filter_none()  `
    * ` loop_generator()  `
    * ` repeat()  `
    * ` extract_data()  `
    * ` flatten_dict()  `
    * ` contains_list()  `
    * ` default_header()  `
    * ` user_agent()  `



Contents  Menu  Expand  Light mode  Dark mode  Auto light/dark mode

Hide navigation sidebar

Hide table of contents sidebar

Give us a ⭐️ on [ Github ](https://github.com/0xPlaygrounds/subgrounds) !

Toggle site navigation sidebar

_ _

[ ![Light Logo](../../_static/assets/pg-logotype-dark.svg) ![Dark
Logo](../../_static/assets/pg-logotype-primary.svg)
](https://playgrounds.network)

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
      * [ Merging ](../../subgrounds/getting_started/field_paths/merging/)
    * [ Querying ](../../subgrounds/getting_started/querying/)
    * [ Synthetic Fields ](../../subgrounds/getting_started/synthetic_fields/)
  * [ Advanced Topics ](../../subgrounds/advanced_topics/)

Toggle child pages in navigation

_ _

    * [ Pagination ](../../subgrounds/advanced_topics/pagination/)

Toggle child pages in navigation

_ _

      * [ Custom Strategies ](../../subgrounds/advanced_topics/pagination/custom/)
  * [ FAQ ](../../subgrounds/faq/)

Toggle child pages in navigation

_ _

    * [ Setup ](../../subgrounds/faq/setup/)

Toggle child pages in navigation

_ _

      * [ Python Versioning ](../../subgrounds/faq/setup/version_management/)
    * [ Contrib ](../../subgrounds/faq/contrib/)
  * [ Examples ](../../subgrounds/examples/)

Toggle child pages in navigation

_ _

    * [ Exchanges ](../../subgrounds/examples/exchanges/)
    * [ Bridges ](../../subgrounds/examples/bridges/)
    * [ Liquid Staking ](../../subgrounds/examples/liquid_staking/)
    * [ Governance ](../../subgrounds/examples/governance/)
    * [ Advanced Research ](../../subgrounds/examples/advanced_research/)
    * [ Vaults ](../../subgrounds/examples/vaults/)
  * [ Tutorials ](../../subgrounds/tutorials/)
  * [ Changelog ](../../subgrounds/changelog/)
  * [ API Reference ](../../subgrounds/modules/)

Toggle child pages in navigation

_ _

    * [ subgrounds package ](../../subgrounds/api/subgrounds/)

Toggle child pages in navigation

_ _

      * [ subgrounds.pagination package ](../../subgrounds/api/subgrounds.pagination/)

Toggle child pages in navigation

_ _

        * [ subgrounds.pagination.pagination module ](../../subgrounds/api/subgrounds.pagination.pagination/)
        * [ subgrounds.pagination.preprocess module ](../../subgrounds/api/subgrounds.pagination.preprocess/)
        * [ subgrounds.pagination.strategies module ](../../subgrounds/api/subgrounds.pagination.strategies/)
        * [ subgrounds.pagination.utils module ](../../subgrounds/api/subgrounds.pagination.utils/)
      * [ subgrounds.subgraph package ](../../subgrounds/api/subgrounds.subgraph/)

Toggle child pages in navigation

_ _

        * [ subgrounds.subgraph.fieldpath module ](../../subgrounds/api/subgrounds.subgraph.fieldpath/)
        * [ subgrounds.subgraph.filter module ](../../subgrounds/api/subgrounds.subgraph.filter/)
        * [ subgrounds.subgraph.object module ](../../subgrounds/api/subgrounds.subgraph.object/)
        * [ subgrounds.subgraph.subgraph module ](../../subgrounds/api/subgrounds.subgraph.subgraph/)
      * [ subgrounds.client module ](../../subgrounds/api/subgrounds.client/)
      * [ subgrounds.dash_wrappers module ](../../subgrounds/api/subgrounds.dash_wrappers/)
      * [ subgrounds.dataframe_utils module ](../../subgrounds/api/subgrounds.dataframe_utils/)
      * [ subgrounds.plotly_wrappers module ](../../subgrounds/api/subgrounds.plotly_wrappers/)
      * [ subgrounds.query module ](../../subgrounds/api/subgrounds.query/)
      * [ subgrounds.schema module ](../../subgrounds/api/subgrounds.schema/)
      * [ subgrounds.subgrounds module ](../../subgrounds/api/subgrounds.subgrounds/)
      * [ subgrounds.transform module ](../../subgrounds/api/subgrounds.transform/)
      * [ subgrounds.utils module ](../../subgrounds/api/subgrounds.utils/)

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
following into the header of your request (replacing ` PG_API_KEY  ` with your
own)!

    
    
    Playgrounds-Api-Key: PG_API_KEY
    

Note

In ` subgrounds  ` , you can set the ` $PLAYGROUNDS_API_KEY  ` environment
variable to your API key and use our endpoints — the library will handle all
of the authentication on your behalf!

##  Endpoints  #

We currently only host a _single_ endpoint.

###  Subgraph Proxy

/v1/proxy

[ ](../reference/proxy/)

[ Next  Subgraph Proxy  ](../reference/proxy/) [ Previous  Subgrounds
Integration  ](../subgrounds/)

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

Give us a ⭐️ on [ Github ](https://github.com/0xPlaygrounds/subgrounds) !

Toggle site navigation sidebar

_ _

[ ![Light Logo](../../../_static/assets/pg-logotype-dark.svg) ![Dark
Logo](../../../_static/assets/pg-logotype-primary.svg)
](https://playgrounds.network)

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
      * [ Merging ](../../../subgrounds/getting_started/field_paths/merging/)
    * [ Querying ](../../../subgrounds/getting_started/querying/)
    * [ Synthetic Fields ](../../../subgrounds/getting_started/synthetic_fields/)
  * [ Advanced Topics ](../../../subgrounds/advanced_topics/)

Toggle child pages in navigation

_ _

    * [ Pagination ](../../../subgrounds/advanced_topics/pagination/)

Toggle child pages in navigation

_ _

      * [ Custom Strategies ](../../../subgrounds/advanced_topics/pagination/custom/)
  * [ FAQ ](../../../subgrounds/faq/)

Toggle child pages in navigation

_ _

    * [ Setup ](../../../subgrounds/faq/setup/)

Toggle child pages in navigation

_ _

      * [ Python Versioning ](../../../subgrounds/faq/setup/version_management/)
    * [ Contrib ](../../../subgrounds/faq/contrib/)
  * [ Examples ](../../../subgrounds/examples/)

Toggle child pages in navigation

_ _

    * [ Exchanges ](../../../subgrounds/examples/exchanges/)
    * [ Bridges ](../../../subgrounds/examples/bridges/)
    * [ Liquid Staking ](../../../subgrounds/examples/liquid_staking/)
    * [ Governance ](../../../subgrounds/examples/governance/)
    * [ Advanced Research ](../../../subgrounds/examples/advanced_research/)
    * [ Vaults ](../../../subgrounds/examples/vaults/)
  * [ Tutorials ](../../../subgrounds/tutorials/)
  * [ Changelog ](../../../subgrounds/changelog/)
  * [ API Reference ](../../../subgrounds/modules/)

Toggle child pages in navigation

_ _

    * [ subgrounds package ](../../../subgrounds/api/subgrounds/)

Toggle child pages in navigation

_ _

      * [ subgrounds.pagination package ](../../../subgrounds/api/subgrounds.pagination/)

Toggle child pages in navigation

_ _

        * [ subgrounds.pagination.pagination module ](../../../subgrounds/api/subgrounds.pagination.pagination/)
        * [ subgrounds.pagination.preprocess module ](../../../subgrounds/api/subgrounds.pagination.preprocess/)
        * [ subgrounds.pagination.strategies module ](../../../subgrounds/api/subgrounds.pagination.strategies/)
        * [ subgrounds.pagination.utils module ](../../../subgrounds/api/subgrounds.pagination.utils/)
      * [ subgrounds.subgraph package ](../../../subgrounds/api/subgrounds.subgraph/)

Toggle child pages in navigation

_ _

        * [ subgrounds.subgraph.fieldpath module ](../../../subgrounds/api/subgrounds.subgraph.fieldpath/)
        * [ subgrounds.subgraph.filter module ](../../../subgrounds/api/subgrounds.subgraph.filter/)
        * [ subgrounds.subgraph.object module ](../../../subgrounds/api/subgrounds.subgraph.object/)
        * [ subgrounds.subgraph.subgraph module ](../../../subgrounds/api/subgrounds.subgraph.subgraph/)
      * [ subgrounds.client module ](../../../subgrounds/api/subgrounds.client/)
      * [ subgrounds.dash_wrappers module ](../../../subgrounds/api/subgrounds.dash_wrappers/)
      * [ subgrounds.dataframe_utils module ](../../../subgrounds/api/subgrounds.dataframe_utils/)
      * [ subgrounds.plotly_wrappers module ](../../../subgrounds/api/subgrounds.plotly_wrappers/)
      * [ subgrounds.query module ](../../../subgrounds/api/subgrounds.query/)
      * [ subgrounds.schema module ](../../../subgrounds/api/subgrounds.schema/)
      * [ subgrounds.subgrounds module ](../../../subgrounds/api/subgrounds.subgrounds/)
      * [ subgrounds.transform module ](../../../subgrounds/api/subgrounds.transform/)
      * [ subgrounds.utils module ](../../../subgrounds/api/subgrounds.utils/)

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

Give us a ⭐️ on [ Github ](https://github.com/0xPlaygrounds/subgrounds) !

Toggle site navigation sidebar

_ _

[ ![Light Logo](../../../../_static/assets/pg-logotype-dark.svg) ![Dark
Logo](../../../../_static/assets/pg-logotype-primary.svg)
](https://playgrounds.network)

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
      * [ Merging ](../../../../subgrounds/getting_started/field_paths/merging/)
    * [ Querying ](../../../../subgrounds/getting_started/querying/)
    * [ Synthetic Fields ](../../../../subgrounds/getting_started/synthetic_fields/)
  * [ Advanced Topics ](../../../../subgrounds/advanced_topics/)

Toggle child pages in navigation

_ _

    * [ Pagination ](../../../../subgrounds/advanced_topics/pagination/)

Toggle child pages in navigation

_ _

      * [ Custom Strategies ](../../../../subgrounds/advanced_topics/pagination/custom/)
  * [ FAQ ](../../../../subgrounds/faq/)

Toggle child pages in navigation

_ _

    * [ Setup ](../../../../subgrounds/faq/setup/)

Toggle child pages in navigation

_ _

      * [ Python Versioning ](../../../../subgrounds/faq/setup/version_management/)
    * [ Contrib ](../../../../subgrounds/faq/contrib/)
  * [ Examples ](../../../../subgrounds/examples/)

Toggle child pages in navigation

_ _

    * [ Exchanges ](../../../../subgrounds/examples/exchanges/)
    * [ Bridges ](../../../../subgrounds/examples/bridges/)
    * [ Liquid Staking ](../../../../subgrounds/examples/liquid_staking/)
    * [ Governance ](../../../../subgrounds/examples/governance/)
    * [ Advanced Research ](../../../../subgrounds/examples/advanced_research/)
    * [ Vaults ](../../../../subgrounds/examples/vaults/)
  * [ Tutorials ](../../../../subgrounds/tutorials/)
  * [ Changelog ](../../../../subgrounds/changelog/)
  * [ API Reference ](../../../../subgrounds/modules/)

Toggle child pages in navigation

_ _

    * [ subgrounds package ](../../../../subgrounds/api/subgrounds/)

Toggle child pages in navigation

_ _

      * [ subgrounds.pagination package ](../../../../subgrounds/api/subgrounds.pagination/)

Toggle child pages in navigation

_ _

        * [ subgrounds.pagination.pagination module ](../../../../subgrounds/api/subgrounds.pagination.pagination/)
        * [ subgrounds.pagination.preprocess module ](../../../../subgrounds/api/subgrounds.pagination.preprocess/)
        * [ subgrounds.pagination.strategies module ](../../../../subgrounds/api/subgrounds.pagination.strategies/)
        * [ subgrounds.pagination.utils module ](../../../../subgrounds/api/subgrounds.pagination.utils/)
      * [ subgrounds.subgraph package ](../../../../subgrounds/api/subgrounds.subgraph/)

Toggle child pages in navigation

_ _

        * [ subgrounds.subgraph.fieldpath module ](../../../../subgrounds/api/subgrounds.subgraph.fieldpath/)
        * [ subgrounds.subgraph.filter module ](../../../../subgrounds/api/subgrounds.subgraph.filter/)
        * [ subgrounds.subgraph.object module ](../../../../subgrounds/api/subgrounds.subgraph.object/)
        * [ subgrounds.subgraph.subgraph module ](../../../../subgrounds/api/subgrounds.subgraph.subgraph/)
      * [ subgrounds.client module ](../../../../subgrounds/api/subgrounds.client/)
      * [ subgrounds.dash_wrappers module ](../../../../subgrounds/api/subgrounds.dash_wrappers/)
      * [ subgrounds.dataframe_utils module ](../../../../subgrounds/api/subgrounds.dataframe_utils/)
      * [ subgrounds.plotly_wrappers module ](../../../../subgrounds/api/subgrounds.plotly_wrappers/)
      * [ subgrounds.query module ](../../../../subgrounds/api/subgrounds.query/)
      * [ subgrounds.schema module ](../../../../subgrounds/api/subgrounds.schema/)
      * [ subgrounds.subgrounds module ](../../../../subgrounds/api/subgrounds.subgrounds/)
      * [ subgrounds.transform module ](../../../../subgrounds/api/subgrounds.transform/)
      * [ subgrounds.utils module ](../../../../subgrounds/api/subgrounds.utils/)

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
    

##  ` subgraphs/id/:subgraph_id/:toplevel_field  ` #

###  GET  #

  

####  URL Parameters  #

  

####  Request Body (JSON)  #

  

####  Example  #

    
    
    

Response:

    
    
    {}
    

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
    * ` subgraphs/id/:subgraph_id/:toplevel_field  `
      * GET 
        * URL Parameters 
        * Request Body (JSON) 
        * Example 



Contents  Menu  Expand  Light mode  Dark mode  Auto light/dark mode

Hide navigation sidebar

Hide table of contents sidebar

Give us a ⭐️ on [ Github ](https://github.com/0xPlaygrounds/subgrounds) !

Toggle site navigation sidebar

_ _

[ ![Light Logo](../../../../_static/assets/pg-logotype-dark.svg) ![Dark
Logo](../../../../_static/assets/pg-logotype-primary.svg)
](https://playgrounds.network)

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
      * [ Merging ](../../../../subgrounds/getting_started/field_paths/merging/)
    * [ Querying ](../../../../subgrounds/getting_started/querying/)
    * [ Synthetic Fields ](../../../../subgrounds/getting_started/synthetic_fields/)
  * [ Advanced Topics ](../../../../subgrounds/advanced_topics/)

Toggle child pages in navigation

_ _

    * [ Pagination ](../../../../subgrounds/advanced_topics/pagination/)

Toggle child pages in navigation

_ _

      * [ Custom Strategies ](../../../../subgrounds/advanced_topics/pagination/custom/)
  * [ FAQ ](../../../../subgrounds/faq/)

Toggle child pages in navigation

_ _

    * [ Setup ](../../../../subgrounds/faq/setup/)

Toggle child pages in navigation

_ _

      * [ Python Versioning ](../../../../subgrounds/faq/setup/version_management/)
    * [ Contrib ](../../../../subgrounds/faq/contrib/)
  * [ Examples ](../../../../subgrounds/examples/)

Toggle child pages in navigation

_ _

    * [ Exchanges ](../../../../subgrounds/examples/exchanges/)
    * [ Bridges ](../../../../subgrounds/examples/bridges/)
    * [ Liquid Staking ](../../../../subgrounds/examples/liquid_staking/)
    * [ Governance ](../../../../subgrounds/examples/governance/)
    * [ Advanced Research ](../../../../subgrounds/examples/advanced_research/)
    * [ Vaults ](../../../../subgrounds/examples/vaults/)
  * [ Tutorials ](../../../../subgrounds/tutorials/)
  * [ Changelog ](../../../../subgrounds/changelog/)
  * [ API Reference ](../../../../subgrounds/modules/)

Toggle child pages in navigation

_ _

    * [ subgrounds package ](../../../../subgrounds/api/subgrounds/)

Toggle child pages in navigation

_ _

      * [ subgrounds.pagination package ](../../../../subgrounds/api/subgrounds.pagination/)

Toggle child pages in navigation

_ _

        * [ subgrounds.pagination.pagination module ](../../../../subgrounds/api/subgrounds.pagination.pagination/)
        * [ subgrounds.pagination.preprocess module ](../../../../subgrounds/api/subgrounds.pagination.preprocess/)
        * [ subgrounds.pagination.strategies module ](../../../../subgrounds/api/subgrounds.pagination.strategies/)
        * [ subgrounds.pagination.utils module ](../../../../subgrounds/api/subgrounds.pagination.utils/)
      * [ subgrounds.subgraph package ](../../../../subgrounds/api/subgrounds.subgraph/)

Toggle child pages in navigation

_ _

        * [ subgrounds.subgraph.fieldpath module ](../../../../subgrounds/api/subgrounds.subgraph.fieldpath/)
        * [ subgrounds.subgraph.filter module ](../../../../subgrounds/api/subgrounds.subgraph.filter/)
        * [ subgrounds.subgraph.object module ](../../../../subgrounds/api/subgrounds.subgraph.object/)
        * [ subgrounds.subgraph.subgraph module ](../../../../subgrounds/api/subgrounds.subgraph.subgraph/)
      * [ subgrounds.client module ](../../../../subgrounds/api/subgrounds.client/)
      * [ subgrounds.dash_wrappers module ](../../../../subgrounds/api/subgrounds.dash_wrappers/)
      * [ subgrounds.dataframe_utils module ](../../../../subgrounds/api/subgrounds.dataframe_utils/)
      * [ subgrounds.plotly_wrappers module ](../../../../subgrounds/api/subgrounds.plotly_wrappers/)
      * [ subgrounds.query module ](../../../../subgrounds/api/subgrounds.query/)
      * [ subgrounds.schema module ](../../../../subgrounds/api/subgrounds.schema/)
      * [ subgrounds.subgrounds module ](../../../../subgrounds/api/subgrounds.subgrounds/)
      * [ subgrounds.transform module ](../../../../subgrounds/api/subgrounds.transform/)
      * [ subgrounds.utils module ](../../../../subgrounds/api/subgrounds.utils/)

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
    

##  ` deployments/id/:deployment_id/:toplevel_field  ` #

###  GET  #

  

####  URL Parameters  #

  

####  Request Body (JSON)  #

  

####  Example  #

    
    
    

Response:

    
    
    {}
    

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
    * ` deployments/id/:deployment_id/:toplevel_field  `
      * GET 
        * URL Parameters 
        * Request Body (JSON) 
        * Example 





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