from matplotlib import pyplot as plt
from matplotlib import cm
import networkx as nx
import pandas as pd
import numpy as np
import folium
import community
import uuid


def process_nodes():
    nodes = []
    df = pd.read_excel(r'./nodelist.xlsx')

    for index, row in df.iterrows():
        node = {'ID': row['ID'],
                'LABEL': row['LABEL'], 'LAT': row['LAT'], 'LNG': row['LNG']}
        nodes.append(node)
    node_array = np.array(nodes)

    return node_array


def process_edges():
    edges = []
    df = pd.read_excel(r'./edgelist.xlsx')

    for index, row in df.iterrows():
        edge = {'source': row['source'],
                'target': row['target'], 'weight': row['weight']}
        edges.append(edge)
    edge_array = np.array(edges)

    return edge_array


def construct_network():
    nodes = process_nodes()
    edges = process_edges()

    [G.add_node(node['ID'], pos=(node['LAT'], node['LNG'])) for node in nodes]
    [G.add_edge(edge['source'], edge['target'], weight=edge['weight'])
     for edge in edges]


def draw_graph(graph):
    layout = nx.spring_layout(graph)
    nx.draw(graph, layout, font_size=16, with_labels=False, node_color="red")
    labels = nx.get_edge_attributes(graph, 'weight')
    nx.draw_networkx_edge_labels(graph, layout, edge_labels=labels)
    nx.draw_networkx_labels(graph, layout)
    plt.savefig('./images/' + str(uuid.uuid4()) + '.png')
    plt.show()


def shorthest_path_source():
    routes = nx.single_source_dijkstra(G, 'P78')
    merged_dictionary = {}
    for k in routes[0]:
        merged_dictionary[k] = [d[k] for d in routes]
    df = pd.DataFrame.from_dict(
        merged_dictionary, orient='index', columns=['Težina rute', 'Najkraća ruta'])
    columns_titles = ["Najkraća ruta", "Težina rute"]
    df = df.reindex(columns=columns_titles)

    map = folium.Map(location=[48.714162, 18.008848], zoom_start=4)
    weights = list(routes[0].values())
    values = list(routes[1].values())

    trail_coordinates = []
    existing_markers = []
    for index, value in enumerate(values):
        for port in value:
            trail_coordinates.append(G.nodes[port]['pos'])
            if port not in existing_markers:
                folium.Marker((G.nodes[port]['pos']), popup=port).add_to(map)
            existing_markers.append(port)
        print(weights[index])
        folium.PolyLine(trail_coordinates, tooltip=weights[index]).add_to(map)
    map.save('./map2.html')


def critical_nodes():
    degree_centrality = nx.degree_centrality(G)
    betweenness_centrality = nx.betweenness_centrality(G)
    df1 = pd.DataFrame.from_dict(degree_centrality,
                                 orient='index', columns=['Stupanj centralnosti']).sort_values(by=['Stupanj centralnosti'], ascending=False)
    df2 = pd.DataFrame.from_dict(betweenness_centrality, orient='index', columns=[
                                 'Stupanj međupoloženosti']).sort_values(by=['Stupanj međupoloženosti'], ascending=False)
    print(pd.DataFrame.to_markdown(df1))
    print(pd.DataFrame.to_markdown(df2))
    for node in ['P45', 'P67', 'P97', 'P7', 'P40', 'P50']:
        ego = nx.ego_graph(G, n=node)
        nx.draw(ego, with_labels=True)
        plt.show()


def communities():
    communities = {}
    partition = community.best_partition(G.to_undirected())
    for community_id in set(partition.values()):
        nodes = [node for node in partition.keys() if partition[node]
                 == community_id]
        subgraph = G.subgraph(nodes)
        draw_graph(subgraph)
        communities[community_id] = (nodes, nx.density(subgraph))
    df = pd.DataFrame.from_dict(
        communities, orient='index', columns=['Čvorovi', 'Gustoća'])
    print(pd.DataFrame.to_markdown(df))

    pos = nx.spring_layout(G)
    cmap = cm.get_cmap('viridis', max(partition.values()) + 1)
    nx.draw_networkx_nodes(G, pos, partition.keys(), node_size=40,
                           cmap=cmap, node_color=list(partition.values()))
    nx.draw_networkx_edges(G, pos, alpha=0.5)
    plt.show()


G = nx.DiGraph()
construct_network()
shorthest_path_source_target()
shorthest_path_source()
critical_nodes()
communities()
