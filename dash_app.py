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
import numpy as np

import graph_converter as gc

path = "../graphs/smaller_subgraph.graphml"
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

graph = nx.read_graphml(path)
subgraph_nodes = ['n{}'.format(n) for n in range(0, 100)]
subgraph = graph.subgraph(subgraph_nodes)

#def serialize_graph(network):
#    json_dict = nx.node_link_data()
#    json_str =


def assign_clusters(subgraph, n_subcluser):
    for node in subgraph.nodes():
        subgraph.nodes[node]['subcluster'] = np.random.randint(n_subcluser)
    return subgraph


def make_clustered_network(graph):
    """Takes a network of genomes and returns a network of clusters with genomes as node attributes."""
    g = assign_clusters(graph, 10)
    cluster_dict = gc.make_cluster_dict(g)
    cluster_network = gc.make_cluster_network(cluster_dict)
    return cluster_network

def add_edges(graph, n_max_connections = 5) :
    """
    Add edges to the graph
    :param graph:
    :return:
    """
    for i in range(1, graph.number_of_nodes()):
        for n in range(1, n_max_connections):
            ni = np.random.randint(1, graph.number_of_nodes())
            if i != ni : cluster_graph.add_edge(i,ni)
    return graph

cluster_graph = make_clustered_network(subgraph)
cluster_graph = add_edges(cluster_graph)
cyto_elements = gc.make_cyto_elements(cluster_graph)

graph = cyto.Cytoscape(
    id='network',
    layout={'name': 'cose'},
    style={'width': '100%', 'height': '400px', 'line-color':'red'},
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
    print(network.nodes[node])
    genomes = network.nodes[node]['genomes'].split(', ')
    table_df = pd.DataFrame(genomes)
    table_df.rename(columns={table_df.columns[0]: "Genome"}, inplace=True)
    data_table = dash_table.DataTable(
        data=table_df.to_dict('records'),
        columns=[{'name': i, 'id': i} for i in table_df.columns]
    )
    return data_table


@app.callback(
    Output('node_genomes', 'children'),
    [Input('network', 'tapNodeData')])
def get_node_genomes(node_data):
    if node_data:
        print(node_data['id'])
        cluster_graph = make_clustered_network(subgraph)
        table = make_genome_table(cluster_graph, int(node_data['id']))
        return table

if __name__ == "__main__":
    app.run_server(debug=True)