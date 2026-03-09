# Graph structure - given from the 2nd example
graph = {
    "Sinamar 2 St": {"Sunrise":2, "USM Avenue":5},
    "Sunrise": {"USM Main Gate":1},
    "USM Avenue": {"USM Main Gate":6},
    "USM Main Gate": {"CBDEM":2, "DDC":4},
    "CBDEM": {"KEPLRC":2, "CED Lobby":4},
    "CED Lobby": {"ICT Building":4},
    "KEPLRC": {"ICT Building":3},
    "DDC": {"CVM Hospital":3},
    "CVM Hospital": {"ICT Building":2},
    "ICT Building": {}
}

# Heuristic values h(n)
h = {
    "Sinamar 2 St":7,
    "USM Avenue":5,
    "Sunrise":2,
    "USM Main Gate":1,
    "DDC":6,
    "CBDEM":3,
    "CED Lobby":4,
    "CVM Hospital":7,
    "KEPLRC":2,
    "ICT Building":0
}

print("====================================")
print("EXAMPLE 2 : USM CAMPUS NAVIGATION")
print("====================================")

# Display graph
print("\nGRAPH STRUCTURE:")
print("----------------")

for node in graph: # loop through every node
    for neighbor in graph[node]: # show its connected nodes
        print(node, "->", neighbor, "cost =", graph[node][neighbor])

print("\nHeuristic Values:")
print("----------------")

for node in h: # loop through every node in the heuristic dictionary
    print(node, "=", h[node])

print("\nPATH COMPARISON: (f(n) = g(n) + h(n))")
print("------------------------------------")


# Pairwise path comparisons (like the first example)
comparisons = [

    # Step 1
    ("Sinamar 2 St -> Sunrise -> USM Main Gate",
     "Sinamar 2 St -> USM Avenue -> USM Main Gate"),

    # Step 2
    ("Sinamar 2 St -> Sunrise -> USM Main Gate -> DDC",
     "Sinamar 2 St -> Sunrise -> USM Main Gate -> CBDEM"),

    # Step 3
    ("Sinamar 2 St -> Sunrise -> USM Main Gate -> CBDEM -> CED Lobby",
    "Sinamar 2 St -> Sunrise -> USM Main Gate -> CBDEM -> KEPLRC"),

    # Step 4
    ("Sinamar 2 St -> Sunrise -> USM Main Gate -> CBDEM -> CED Lobby -> ICT Building",
    "Sinamar 2 St -> Sunrise -> USM Main Gate -> CBDEM -> KEPLRC -> ICT Building")
]

# Variables to store the best path to the goal
best_goal_path = None 
best_goal_cost = float('inf')

# Function to compute g(n)
def compute_g(path):
    nodes = path.split(" -> ") # split path into nodes
    cost = 0

    for i in range(len(nodes)-1):
        src = nodes[i]
        dst = nodes[i+1]
        cost += graph[src][dst]

    return cost

# Loop through comparison pairs
for path1, path2 in comparisons:

    # Calculate g(n), h(n), f(n) for path 1
    g1 = compute_g(path1)
    h1 = h[path1.split(" -> ")[-1]]
    f1 = g1 + h1

    # Calculate g(n), h(n), f(n) for path 2
    g2 = compute_g(path2)
    h2 = h[path2.split(" -> ")[-1]]
    f2 = g2 + h2

    # Print first path
    print(path1)
    print("g(n) =", g1, "| h(n) =", h1, "| f(n) =", f1)
    print()

    # Print second path
    print(path2)
    print("g(n) =", g2, "| h(n) =", h2, "| f(n) =", f2)

    # Determine shorter path
    if f1 < f2:
        short_path = path1
    else:
        short_path = path2

    print("\nShort Path:", short_path)
    print("------------------------------------")

    # Track best path reaching ICT Building
    for path, g in [(path1, g1), (path2, g2)]:
        if path.endswith("ICT Building") and g < best_goal_cost:
            best_goal_cost = g
            best_goal_path = path

# Final result
print("\nSHORTEST PATH FOUND:")
print(best_goal_path)
print("Total Cost =", best_goal_cost)


# =====================================================
# MINI CAMPUS-MAP STYLE VISUALIZATION (UPDATED STYLE)
# =====================================================

import networkx as nx
import matplotlib.pyplot as plt

# Create graph
G = nx.DiGraph()

for node in graph:
    for neighbor in graph[node]:
        G.add_edge(node, neighbor, weight=graph[node][neighbor])

# Map-style layout
pos = {
    "Sinamar 2 St": (0,5),
    "Sunrise": (-2,4),
    "USM Avenue": (2,4),
    "USM Main Gate": (0,3),
    "CBDEM": (-1,2),
    "DDC": (1,2),
    "CED Lobby": (-2,1),
    "KEPLRC": (0,1),
    "CVM Hospital": (2,1),
    "ICT Building": (0,0)
}

plt.figure(figsize=(10,7))

# Draw all roads first
nx.draw_networkx_edges(
    G,
    pos,
    edge_color="gray",
    width=2,
    arrows=False
)

# Highlight shortest route (MAGENTA)
path_nodes = best_goal_path.split(" -> ")
path_edges = [(path_nodes[i], path_nodes[i+1]) for i in range(len(path_nodes)-1)]

nx.draw_networkx_edges(
    G,
    pos,
    edgelist=path_edges,
    width=6,
    edge_color="magenta",
    arrows=False
)

# Nodes on the shortest path (except start and goal)
short_nodes = {"Sunrise", "USM Main Gate", "CBDEM", "KEPLRC"}

# Node colors
node_colors=[]
for node in G.nodes():
    if node in ["Sinamar 2 St","ICT Building"]:
        node_colors.append("yellow")  # start and goal
    elif node in short_nodes:
        node_colors.append("magenta")  # nodes on shortest path
    else:
        node_colors.append("white")

# Draw nodes (bigger circles)
nx.draw_networkx_nodes(
    G,
    pos,
    node_color=node_colors,
    node_size=3200,
    edgecolors="black"
)

# Labels
nx.draw_networkx_labels(
    G,
    pos,
    font_size=10,
    font_weight="bold"
)

# Edge weights
edge_labels={(u,v):d['weight'] for u,v,d in G.edges(data=True)}
nx.draw_networkx_edge_labels(
    G,
    pos,
    edge_labels=edge_labels,
    font_color="blue",
    font_size=11,
    bbox=dict(facecolor="white", edgecolor="none", alpha=0.7)
)

plt.title("USM Campus Route Map (A* Shortest Path)",fontsize=16)
plt.axis("off")
plt.show()