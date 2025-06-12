import math
import pytest
from algorithm import create_initial_graph, floyd_warshall, reconstruct_path, NODES

def test_graph_structure():
    graph = create_initial_graph()
    assert len(graph) == len(NODES)
    for row in graph:
        assert len(row) == len(NODES)

def test_no_self_loops():
    graph = create_initial_graph()
    for i in range(len(NODES)):
        assert graph[i][i] == 0

def test_algorithm_correctness():
    graph = create_initial_graph()
    dist, next_node, _ = floyd_warshall(graph)
    
    # Refectory (0) -> Faculty of Education (3)
    path = reconstruct_path(0, 3, next_node)
    path_names = [NODES[i] for i in path]
    
    # Expected path: Refectory -> Library -> Faculty of Technology -> Faculty of Education
    expected = ["Refectory", "Library", "Faculty of Technology", "Faculty of Education"]
    assert path_names == expected
    
    # Total Distance: 200 + 300 + 180 = 680
    assert dist[0][3] == 680

def test_disconnected_nodes():
    # Let us add a disconnected node for testing purposes
    size = len(NODES)
    graph = create_initial_graph()
    for row in graph:
        row.append(math.inf)
    graph.append([math.inf] * (size + 1))
    graph[-1][-1] = 0

    dist, next_node, _ = floyd_warshall(graph)
    assert dist[0][-1] == math.inf
    assert reconstruct_path(0, size, next_node) == []