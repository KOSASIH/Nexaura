import networkx as nx
import pandas as pd
import numpy as np
from sklearn.metrics import pairwise_distances
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
from scipy.spatial.distance import cosine

class GraphOperations:
    def __init__(self, graph_data):
        self.graph = nx.Graph()
        self.load_graph(graph_data)

    def load_graph(self, graph_data):
        nodes = graph_data['nodes']
        edges = graph_data['edges']
        for node in nodes:
            self.graph.add_node(node['id'], label=node['label'], type=node['type'])
        for edge in edges:
            self.graph.add_edge(edge['source'], edge['target'], type=edge['type'])

    def get_node_embeddings(self, method='deepwalk'):
        if method == 'deepwalk':
            return self.deepwalk_embeddings()
        elif method == 'node2vec':
            return self.node2vec_embeddings()
        else:
            raise ValueError('Invalid method')

    def deepwalk_embeddings(self):
        from deepwalk import DeepWalk
        model = DeepWalk(self.graph, num_walks=10, walk_length=30, workers=1)
        embeddings = model.get_embeddings()
        return pd.DataFrame(embeddings, index=self.graph.nodes())

    def node2vec_embeddings(self):
        from node2vec import Node2Vec
        model = Node2Vec(self.graph, dimensions=128, walk_length=30, num_walks=10, workers=1)
        embeddings = model.fit_transform()
        return pd.DataFrame(embeddings, index=self.graph.nodes())

    def get_edge_weights(self):
        edge_weights = {}
        for u, v in self.graph.edges():
            edge_weights[(u, v)] = self.calculate_edge_weight(u, v)
        return edge_weights

    def calculate_edge_weight(self, u, v):
        node_u = self.graph.nodes[u]
        node_v = self.graph.nodes[v]
        if node_u['type'] == 'entity' and node_v['type'] == 'entity':
            return self.calculate_entity_similarity(node_u, node_v)
        elif node_u['type'] == 'relation' and node_v['type'] == 'relation':
            return self.calculate_relation_similarity(node_u, node_v)
        else:
            return 0.5

    def calculate_entity_similarity(self, node_u, node_v):
        embeddings_u = self.get_node_embeddings(method='deepwalk').loc[node_u['id']]
        embeddings_v = self.get_node_embeddings(method='deepwalk').loc[node_v['id']]
        return 1 - cosine(embeddings_u, embeddings_v)

    def calculate_relation_similarity(self, node_u, node_v):
        embeddings_u = self.get_node_embeddings(method='node2vec').loc[node_u['id']]
        embeddings_v = self.get_node_embeddings(method='node2vec').loc[node_v['id']]
        return 1 - cosine(embeddings_u, embeddings_v)

    def get_shortest_path(self, source, target):
        return nx.shortest_path(self.graph, source, target)

    def get_subgraph(self, nodes):
        return self.graph.subgraph(nodes)

    def visualize_graph(self):
        import matplotlib.pyplot as plt
        pos = nx.spring_layout(self.graph)
        nx.draw_networkx(self.graph, pos, with_labels=True, node_color='lightblue', edge_color='gray')
        plt.show()

# Example usage:
graph_data = {
    'nodes': [
        {'id': 'Node 1', 'label': 'Node 1', 'type': 'entity'},
        {'id': 'Node 2', 'label': 'Node 2', 'type': 'entity'},
        {'id': 'Node 3', 'label': 'Node 3', 'type': 'entity'},
        {'id': 'Relation 1', 'label': 'Relation 1', 'type': 'relation'}
    ],
    'edges': [
        {'source': 'Node 1', 'target': 'Node 2', 'type': 'relation'},
        {'source': 'Node 2', 'target': 'Node 3', 'type': 'relation'},
        {'source': 'Node 1', 'target': 'Relation 1', 'type': 'entity_relation'}
    ]
}

graph_ops = GraphOperations(graph_data)
print(graph_ops.get_node_embeddings(method='deepwalk'))
print(graph_ops.get_edge_weights())
print(graph_ops.get_shortest_path('Node 1', 'Node 3'))
graph_ops.visualize_graph()
