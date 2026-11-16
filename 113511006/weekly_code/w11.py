"""Week 11 | Graphs: find the fewest steps through an unweighted maze."""

from collections import deque


def shortest_path(grid, start, goal):
    """Return a path of (row, col) cells, or [] if unreachable.

    '.' is walkable and '#' is blocked. Movement is four-directional.
    """
    if not grid or not grid[0] or any(len(row) != len(grid[0]) for row in grid):
        return []
    rows, cols = len(grid), len(grid[0])

    def open_cell(cell):
        r, c = cell
        return 0 <= r < rows and 0 <= c < cols and grid[r][c] != "#"

    if not open_cell(start) or not open_cell(goal):
        return []

    parents = {start: None}
    queue = deque([start])
    while queue:
        current = queue.popleft()
        if current == goal:
            path = []
            while current is not None:
                path.append(current)
                current = parents[current]
            return path[::-1]
        r, c = current
        for neighbor in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
            if open_cell(neighbor) and neighbor not in parents:
                parents[neighbor] = current
                queue.append(neighbor)
    return []


if __name__ == "__main__":
    maze = ["...", "##.", "..."]
    assert shortest_path(maze, (0, 0), (2, 0)) == [
        (0, 0), (0, 1), (0, 2), (1, 2), (2, 2), (2, 1), (2, 0)]
    assert shortest_path([".#", "#."], (0, 0), (1, 1)) == []
    assert shortest_path(["."], (0, 0), (0, 0)) == [(0, 0)]
    assert shortest_path(["#"], (0, 0), (0, 0)) == []
    print("Week 11: 4 tests passed")
