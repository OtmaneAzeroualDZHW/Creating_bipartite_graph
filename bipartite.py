# Python3 program to create a bipartite graph

# Imports
import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd
from networkx.algorithms import bipartite

# Add dataframe with two columns
data = pd.DataFrame(
    {'domain': ["C", "B", "A"],
     'subdomain': ["F", "E", "D"]})
     
# Initialize graph
B = nx.Graph()

# Add nodes with the node attribute "bipartite"
B.add_nodes_from(data['subdomain'], bipartite=0)
B.add_nodes_from(data['domain'], bipartite=1)

# Add edges with weights between nodes of opposite node sets
B.add_edge("A", "F", weight=10) 
B.add_edge("A", "E", weight=4) 
B.add_edge("B", "D", weight=27) 
B.add_edge("B", "F", weight=12) 
B.add_edge("C", "D", weight=33) 
B.add_edge("C", "E", weight=67) 

# Get edge weights based on the count of edges
edge_to_count = dict()
for edge in B.edges():
    try:
        edge_to_count[edge] += 1
    except KeyError:
        edge_to_count[edge] = 1
        
# Positions for all nodes
pos = nx.spring_layout(B) 
for edge in B.edges(data=True): print(edge)
pos = {node:[0, i] for i,node in enumerate(data['domain'])}
pos.update({node:[1, i] for i,node in enumerate(data['subdomain'])})

# Categorize weights according to their size
elarge = [(u, v) for (u, v, d) in B.edges(data=True) 
if d["weight"] <= 12]
exlarge = [(u, v) for (u, v, d) in B.edges(data=True) 
if d["weight"] == 27]
esmall = [(u, v) for (u, v, d) in B.edges(data=True) 
if d["weight"] >= 33]

# Drawing the graph with options for node positions, labeling, titles, and many other drawing features
nx.draw_networkx_edge_labels(B, pos, edge_to_count, label_pos=1)
nx.draw_networkx_nodes(B, pos, node_size=1500, node_color="royalblue", with_labels=False)
nx.draw_networkx_edges(B, pos, edgelist=elarge, width=6)
nx.draw_networkx_edges(B, pos, edgelist=exlarge, width=6, edge_color="r", style="solid")
nx.draw_networkx_edges(B, pos, edgelist=esmall, width=6, edge_color="g", style="solid") 
nx.draw_networkx_labels(B, pos, font_size=20, font_family="sans-serif")

ax = plt.gca()
ax.margins(0.10) # These can be used to set the margins
plt.axis("off")
plt.tight_layout()
plt.show()
