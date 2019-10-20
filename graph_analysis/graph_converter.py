from collections import defaultdict

import networkx as nx


def make_cyto_elements(graph):
    cytoscape_elements = []

    for node in graph.nodes():
        # node_info = graph.nodes(data=True)[node] # for genome graphs (not clusters)
        cyto_node = {'data': {'id': node,
                              'label': node}}
                              # 'label': node_info['name']}} # for genome graphs (not clusters)
        cytoscape_elements.append(cyto_node)

    for edge in nx.generate_edgelist(graph):
        node1, node2, name = edge.split(' ')
        cyto_edge = {'data': {'source': node1,
                              'target': node2,
                              'label': '{} to {}'.format(node1, node2)}}
        cytoscape_elements.append(cyto_edge)

    return cytoscape_elements


def make_cluster_dict(network):
    cluster_dict = defaultdict(list)
    unique_clusters = set(nx.get_node_attributes(network, 'subcluster').values())
    for node in network.nodes():
        for cluster in range(1, len(unique_clusters)+1):
            if network._node[node]['subcluster'] == cluster:
                cluster_dict[cluster].append(network._node[node]['name'])
    return cluster_dict


def make_cluster_network(cluster_dict):
    cluster_nw = nx.Graph()
    for cluster, genome in cluster_dict.items():
        cluster_nw.add_node(cluster, genomes=', '.join(genome))
    return cluster_nw

