from copy import deepcopy
from itertools import permutations

import pytest

from safe_route import shortest_safe_route


@pytest.mark.parametrize(
    "graph,start,goal,closed,expected",
    [
        ({"A": ["B", "C"], "B": ["D"], "C": ["D"], "D": []},
         "A", "D", ["B"], ["A", "C", "D"]),
        ({"A": ["B"], "B": []}, "B", "A", [], None),
        ({"A": []}, "A", "A", [], ["A"]),
        ({"A": []}, "A", "A", ["A"], None),
        ({"A": ["B"], "B": []}, "A", "B", ["A"], None),
        ({"A": ["B"], "B": []}, "A", "B", ["B"], None),
        ({"A": ["A", "B", "B"], "B": ["A"]},
         "A", "B", [], ["A", "B"]),
        ({"A": ["B"], "B": ["A"], "C": []}, "A", "C", [], None),
        ({"A": ["B", "D"], "B": ["C"], "C": ["D"], "D": []},
         "A", "D", [], ["A", "D"]),
        ({"A": ["C", "B"], "B": ["D"], "C": ["D"], "D": []},
         "A", "D", [], ["A", "C", "D"]),
    ],
)
def test_shortest_directed_route_respects_closures_and_neighbor_order(
    graph, start, goal, closed, expected
):
    before = deepcopy(graph)
    closed_before = closed.copy()
    assert shortest_safe_route(graph, start, goal, closed) == expected
    assert graph == before
    assert closed == closed_before


def test_every_three_node_digraph_against_simple_path_enumeration():
    nodes = ["A", "B", "C"]
    edges = list(permutations(nodes, 2))
    for mask in range(1 << len(edges)):
        graph = {node: [] for node in nodes}
        for bit, (source, target) in enumerate(edges):
            if mask & (1 << bit):
                graph[source].append(target)
        for closed_mask in range(8):
            closed = [node for i, node in enumerate(nodes) if closed_mask & (1 << i)]
            for start in nodes:
                for goal in nodes:
                    candidates = []
                    for size in range(1, 4):
                        for path in permutations(nodes, size):
                            if path[0] != start or path[-1] != goal:
                                continue
                            if any(node in closed for node in path):
                                continue
                            if all(b in graph[a] for a, b in zip(path, path[1:])):
                                candidates.append(path)
                    result = shortest_safe_route(graph, start, goal, closed)
                    if not candidates:
                        assert result is None
                    else:
                        assert tuple(result) in candidates
                        assert len(result) == min(map(len, candidates))


def test_ten_thousand_node_route_without_recursion():
    nodes = [str(i) for i in range(10_000)]
    graph = {node: nodes[i + 1:i + 2] for i, node in enumerate(nodes)}
    assert shortest_safe_route(graph, nodes[0], nodes[-1], []) == nodes
    assert shortest_safe_route(graph, nodes[0], nodes[-1], [nodes[5000]]) is None
