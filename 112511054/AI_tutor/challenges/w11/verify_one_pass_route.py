"""Run the examples, edge cases, and exhaustive three-node comparisons."""

import unittest
from itertools import product
from math import inf

from one_pass_route import shortest_with_pass


def reference_distance(graph, start, goal):
    # Compute all-pairs distances using normal edges only, then try each pass.
    size = len(graph)
    distances = [[inf] * size for _ in range(size)]
    express_edges = []
    for node, neighbors in enumerate(graph):
        distances[node][node] = 0
        for neighbor, express in neighbors:
            if express:
                express_edges.append((node, neighbor))
            else:
                distances[node][neighbor] = min(distances[node][neighbor], 1)

    for via, source, target in product(range(size), repeat=3):
        distances[source][target] = min(
            distances[source][target], distances[source][via] + distances[via][target]
        )

    best = distances[start][goal]
    for source, target in express_edges:
        best = min(best, distances[start][source] + 1 + distances[target][goal])
    return -1 if best == inf else best


class OnePassRouteTests(unittest.TestCase):
    def test_examples_and_edges(self):
        cases = [
            ("express shortcut", [[(1, False), (3, True)], [(2, False)], [(3, False)], []], 0, 3, 1),
            ("save pass for later", [[(2, True), (1, False)], [(2, False)], [(3, True)], []], 0, 3, 3),
            ("two express edges", [[(1, True)], [(2, True)], []], 0, 2, -1),
            ("same endpoint", [[]], 0, 0, 0),
            ("directed edge", [[(1, False)], []], 1, 0, -1),
            ("normal route", [[(1, False)], [(2, False)], []], 0, 2, 2),
            ("parallel edges and loops", [[(0, False), (1, True), (1, False), (1, False)], [(0, False), (2, True)], []], 0, 2, 2),
            ("express seen after normal", [[(1, False), (1, True)], [(2, True)], []], 0, 2, 2),
        ]
        for name, graph, start, goal, expected in cases:
            with self.subTest(name=name):
                original = [neighbors.copy() for neighbors in graph]
                self.assertEqual(shortest_with_pass(graph, start, goal), expected)
                self.assertEqual(graph, original)

    def test_all_three_node_graphs(self):
        vertices = range(3)
        edges = [(u, v) for u, v in product(vertices, repeat=2) if u != v]
        for kinds in product(range(3), repeat=len(edges)):
            graph = [[] for _ in vertices]
            for (u, v), kind in zip(edges, kinds):
                if kind:
                    graph[u].append((v, kind == 2))
            for start, goal in product(vertices, repeat=2):
                with self.subTest(kinds=kinds, start=start, goal=goal):
                    actual = shortest_with_pass(graph, start, goal)
                    self.assertEqual(actual, reference_distance(graph, start, goal))

    def test_maximum_graph_size(self):
        size = 10_000
        graph = [[(node + 1, False)] * 5 for node in range(size - 1)] + [[]]
        graph[0].extend([(0, True)] * 5)
        self.assertEqual(shortest_with_pass(graph, 0, size - 1), size - 1)
        self.assertEqual(shortest_with_pass(graph, size - 1, 0), -1)


if __name__ == "__main__":
    unittest.main(verbosity=2)
