import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np  

Ns = {('S'), 'A', 'B', 'C', 'D', 'G'}
Es = [
    ('S','A', {'weight': 3, 'label': 3}), 
    ('S','B', {'weight': 1, 'label': 1}), 
    ('A','C', {'weight': 1, 'label': 1}), 
    ('B', 'C', {'weight': 4, 'label': 4}), 
    ('A', 'D', {'weight': 3, 'label': 3}), 
    ('A', 'G', {'weight': 4, 'label': 4}), 
    ('C', 'G', {'weight': 3, 'label': 3}), 
    ('D', 'G', {'weight': 2, 'label': 2}),
]

G = nx.DiGraph()
G.add_nodes_from(Ns)
G.add_edges_from(Es)

fixed_positions = {
    'S': (0, 0),
    'G': (3, -1)
}
fixed_nodes = fixed_positions.keys()

variable_nodes = Ns - fixed_nodes
variables_positions = nx.shell_layout(G, nlist=[list(variable_nodes)])

pos = {**fixed_positions, **variables_positions}

nx.draw(G, pos, with_labels=True, node_size = 1000, node_color = 'w', edge_color = 'b')

edge_labels = {(u, v): d['label'] for u, v, d in G.edges(data=True)}
nx.set_edge_attributes(G, edge_labels, 'label')

nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
plt.show()