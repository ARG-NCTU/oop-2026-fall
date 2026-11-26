"""AOOP Week 11: Minimum Transfers Between Campus Buildings.
Original educational exercise inspired by the course OCW topic.
This file is a worked-example solution; run it to execute its tests.
"""

from collections import deque


def min_transfers(n, edges, start, goal):
    adjacency = [[] for _ in range(n)]
    for a, b in edges:
        adjacency[a].append(b)
        adjacency[b].append(a)
    queue = deque([start])
    distance = [-1] * n
    distance[start] = 0
    while queue:
        node = queue.popleft()
        if node == goal:
            return distance[node]
        for neighbor in adjacency[node]:
            if distance[neighbor] == -1:
                distance[neighbor] = distance[node] + 1
                queue.append(neighbor)
    return -1


def _run_self_tests():
    """Execute provided examples and additional edge cases."""
    import copy
    cases = [
        ((5, [(0, 1), (1, 2), (0, 3), (3, 2)], 0, 2), 2),
        ((4, [(0, 1), (2, 3)], 0, 3), -1),
        ((3, [], 2, 2), 0),
        ((3, [(0, 1), (1, 2), (2, 0)], 0, 2), 1),
        ((4, [(0, 1), (1, 2), (2, 3), (0, 3)], 0, 3), 1),
    ]
    for number, (args, expected) in enumerate(cases, 1):
        given = copy.deepcopy(args)
        actual = min_transfers(*given)
        assert actual == expected, (number, actual, expected)
    print("Week 11: PASS ({} test cases)".format(len(cases)))


if __name__ == "__main__":
    _run_self_tests()
