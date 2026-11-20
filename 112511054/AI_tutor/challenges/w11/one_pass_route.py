"""Find the minimum number of hops when at most one express edge is allowed."""

from collections import deque
from collections.abc import Sequence


def shortest_with_pass(
    graph: Sequence[Sequence[tuple[int, bool]]], start: int, goal: int
) -> int:
    """Return the hop count, or -1 if the goal is unreachable."""
    distances = [[-1, -1] for _ in graph]
    distances[start][0] = 0
    queue = deque([(start, 0)])

    while queue:
        node, used_pass = queue.popleft()
        distance = distances[node][used_pass]
        if node == goal:
            return distance

        for neighbor, express in graph[node]:
            next_used_pass = used_pass + express
            if next_used_pass > 1 or distances[neighbor][next_used_pass] != -1:
                continue
            distances[neighbor][next_used_pass] = distance + 1
            queue.append((neighbor, next_used_pass))

    return -1
