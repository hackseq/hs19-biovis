import ast
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_cytoscape as cyto
import dash_html_components as html
import dash_table
from dash.dependencies import Input, Output
import networkx as nx
import pandas as pd

import graph_converter as gc

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Link", href="#")),
        dbc.DropdownMenu(
            nav=True,
            in_navbar=True,
            label="Menu",
            children=[
                dbc.DropdownMenuItem("Entry 1"),
                dbc.DropdownMenuItem("Entry 2"),
                dbc.DropdownMenuItem(divider=True),
                dbc.DropdownMenuItem("Entry 3"),
            ],
        ),
    ],
    brand="RefSeq Genome Browser",
    brand_href="#",
    sticky="top",
)

cluster_buttons = dbc.FormGroup(
    [
        dbc.Label("Clustering Method"),
        dbc.RadioItems(
            options=[
                {"label": "Connectivity", "value": "connectivity"},
                {"label": "Option 2", "value": 2},
                {"label": "Disabled option", "value": 3, "disabled": True},
            ],
            value=1,
            id="radioitems-input",
        ),
    ]
)

graph = nx.read_graphml("smaller_subgraph.graphml")
subgraph_nodes = ['n{}'.format(n) for n in range(0, 100)]
subgraph = graph.subgraph(subgraph_nodes)

#def serialize_graph(network):
#    json_dict = nx.node_link_data()
#    json_str =


def assign_clusters(subgraph):
    for node in subgraph.nodes():
        node_n = int(list(node)[1])
        if node_n < 3:
            subgraph.nodes[node]['subcluster'] = 1
        elif node_n < 5:
            subgraph.nodes[node]['subcluster'] = 2
        else:
            subgraph.nodes[node]['subcluster'] = 3
    return subgraph


def make_clustered_network(graph):
    """Takes a network of genomes and returns a network of clusters with genomes as node attributes."""
    g = assign_clusters(graph)
    cluster_dict = gc.make_cluster_dict(g)
    cluster_network = gc.make_cluster_network(cluster_dict)
    return cluster_network

cluster_graph = make_clustered_network(subgraph)
cyto_elements = gc.make_cyto_elements(cluster_graph)

graph = cyto.Cytoscape(
    id='network',
    layout={'name': 'cose'},
    style={'width': '100%', 'height': '400px'},
    elements=cyto_elements
)

app.layout = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H4("Filter"),
                        html.Br(),
                        dbc.Input(id="input", placeholder="Find a genome...", type="text"),
                        html.Br(),
                        cluster_buttons
                    ],
                    width=2
                ),
                dbc.Col(
                    [
                        html.H4("Network Explorer"),
                        graph
                    ],
                    width=7
                ),
                dbc.Col([html.H4("Subcluster Details"),
                         html.Div(id='node_genomes')],
                width=3)
            ]
        )
    ],
    className="mt-4",
)

def make_genome_table(network, node):
    """Takes a network node and returns a table with its genomes."""
    genomes = network.nodes[node]['genomes'].split(', ')
    table_df = pd.DatafFrame(genomes)
    data_table = dash_table.DataTable(
        data=table_df.to_dict('records'),
        columns=[{'name': i, 'id': i} for i in table_df.columns]
    )
    return data_table


@app.callback(
    Output('node_genomes', 'children'),
    [Input('network', 'tapNodeData')])
def get_node_genomes(node_data):
    graph = nx.read_graphml("smaller_subgraph.graphml")
    subgraph_nodes = ['n{}'.format(n) for n in range(0, 100)]
    subgraph = graph.subgraph(subgraph_nodes)
    table = make_genome_table(subgraph, node_data['id'])
    return table

if __name__ == "__main__":
    app.run_server(debug=True)