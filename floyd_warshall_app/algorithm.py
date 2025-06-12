# Campus Navigator -Project of Floyd-Warshall
# According to Project Structure: algorithm.py

import math

# Define building names in a fixed order
NODES = [
    "Refectory",
    "Library",
    "Faculty of Technology",
    "Faculty of Education",
    "Murad Camii",
    "Sok Market",
    "30th Year Cafe"
]

# Algorithm of Floyd-Warshall

def floyd_warshall(graph):
    n = len(graph)
    dist = [[graph[i][j] for j in range(n)] for i in range(n)]
    next_node = [[j if graph[i][j] != math.inf else None for j in range(n)] for i in range(n)]

    steps = []  # Stores the dist matrix at each step

    for k in range(n):
        step = [[dist[i][j] for j in range(n)] for i in range(n)]  # Copy
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    next_node[i][j] = next_node[i][k]
                    step[i][j] = dist[i][j]  # Update in steps

        steps.append(step)

    return dist, next_node, steps

# Function that solves the shortest path in nodes
def reconstruct_path(u, v, next_node):
    if next_node[u][v] is None:
        return []
    path = [u]
    while u != v:
        u = next_node[u][v]
        path.append(u)
    return path

# Initial graph (distances), ready for processing
def create_initial_graph():
    size = len(NODES)
    INF = math.inf
    graph = [[INF] * size for _ in range(size)]

    for i in range(size):
        graph[i][i] = 0  # Distance from itself 0

    # Fixed distances (added one by one)
    distances = [
        (0, 1, 200),
        (0, 6, 150),
        (1, 2, 300),
        (2, 3, 180),
        (3, 4, 350),
        (4, 5, 120),
        (5, 6, 220),
        (2, 5, 270),
        (1, 4, 500),
    ]

    for u, v, d in distances:
        graph[u][v] = d
        graph[v][u] = d  # bidirectional

    return graph