# Graph structure - given na ito sa problem na nasa yellow paper
graph = {
    'S': {'A':1, 'Z':15},
    'A': {'B':2, 'C':1},
    'B': {'D':5},
    'C': {'D':3, 'Z':3},
    'D': {'Z':2},
    'Z': {}
}

# Heuristic values h(n) - given din ito
h = {
    'S':7,
    'A':3,
    'B':4,
    'C':1,
    'D':5,
    'Z':0
}

print("====================================")
print("EXAMPLE 1 : A* GRAPH SEARCH")
print("====================================")

# Display graph
print("\nGRAPH STRUCTURE:")
print("----------------")

for node in graph: # Loops through each node in graph
    for neighbor in graph[node]: # Loops through each neighbor or katabi niya of the current node
        print(node, "->", neighbor, "cost =", graph[node][neighbor])

print("\nHeuristic Values:")
print("----------------")

for node in h: # Loops through each node in the heuristic dictionary
    print(node, "=", h[node])

print("\nPATH COMPARISON: (f(n) = g(n) + h(n))")
print("------------------------------------")

# Pairwise comparisons based on the example in the problem
comparisons = [

    # Step 1 comparison
    (("S -> A", 1, h['A']),
     ("S -> Z", 15, h['Z'])),

    # Step 2 comparison
    (("S -> A -> B", 3, h['B']),
     ("S -> A -> C", 2, h['C'])),

    # Step 3 comparison
    (("S -> A -> C -> D", 5, h['D']),
     ("S -> A -> C -> Z", 5, h['Z']))
]

# Variables to store the best path to the goal
best_goal_path = None
best_goal_cost = float('inf')

# Loop through each comparison pair
for path1, path2 in comparisons:

    p1, g1, h1 = path1
    p2, g2, h2 = path2

    f1 = g1 + h1  # Calculate f(n) for first path
    f2 = g2 + h2  # Calculate f(n) for second path

    # Print first path
    print(p1)
    print("g(n) =", g1, "| h(n) =", h1, "| f(n) =", f1)
    print()

    # Print second path
    print(p2)
    print("g(n) =", g2, "| h(n) =", h2, "| f(n) =", f2)

    # Determine the shorter path based on f(n)
    if f1 < f2:
        short_path = p1
    else:
        short_path = p2

    print("\nShort Path:", short_path)
    print("------------------------------------")

    # Track the best path that reaches goal Z using actual cost g(n)
    for path, g in [(p1, g1), (p2, g2)]:
        if path.endswith("Z") and g < best_goal_cost:
            best_goal_cost = g
            best_goal_path = path


# Final result
print("\nSHORTEST PATH FOUND:")
if best_goal_path:
    print(best_goal_path)
    print("Total Cost =", best_goal_cost)
else:
    print("No path to Z found.")


# =====================================================
# VISUALIZATION PART
# =====================================================

import networkx as nx
import matplotlib.pyplot as plt

# Create directed graph
G = nx.DiGraph()

# Edges with weights
edges = [
    ('S','A',1),
    ('S','Z',15),
    ('A','B',2),
    ('A','C',1),
    ('B','D',5),
    ('C','D',3),
    ('C','Z',3),
    ('D','Z',2)
]

G.add_weighted_edges_from(edges)

# Manually set node positions to match diagram
pos = {
    'S': (0,4),
    'A': (-1,3),
    'B': (-2,2),
    'C': (0,2),
    'D': (-1,1),
    'Z': (1,1)
}

plt.figure(figsize=(6,6))

# Node colors
node_colors = []
for node in G.nodes():
    if node in ['S','Z']:
        node_colors.append('yellow')
    elif node in ['A','C']:
        node_colors.append('magenta')
    else:
        node_colors.append('white')

# Draw nodes
nx.draw_networkx_nodes(
    G,pos,
    node_size=2000,
    node_color=node_colors,
    edgecolors='black'
)

# Draw labels
nx.draw_networkx_labels(G,pos,font_size=14,font_weight='bold')

# Draw edges
nx.draw_networkx_edges(G,pos,arrows=True,edge_color='gray')

# Highlight shortest path using the computed result
path_nodes = best_goal_path.split(" -> ")
path_edges = [(path_nodes[i], path_nodes[i+1]) for i in range(len(path_nodes)-1)]

nx.draw_networkx_edges(
    G,pos,
    edgelist=path_edges,
    width=4,
    edge_color='magenta',
    arrows=True
)

# Draw edge weights
edge_labels={(u,v):d['weight'] for u,v,d in G.edges(data=True)}
nx.draw_networkx_edge_labels(G,pos,edge_labels=edge_labels,font_color='blue')

plt.title("A* Graph Visualization (Example 1)", fontsize=16)
plt.axis('off')
plt.show()