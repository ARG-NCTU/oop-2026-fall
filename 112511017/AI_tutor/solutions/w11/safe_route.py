def shortest_safe_route(graph, start, goal, closed):
    """Find a minimum-edge directed route that avoids every closed node."""
    blocked = dict.fromkeys(closed)
    if start in blocked or goal in blocked:
        return None

    parents = {start: None}
    queue = [start]
    head = 0
    while head < len(queue):
        node = queue[head]
        head += 1
        if node == goal:
            path = []
            while node is not None:
                path.append(node)
                node = parents[node]
            path.reverse()
            return path

        for neighbor in graph[node]:
            if neighbor not in blocked and neighbor not in parents:
                parents[neighbor] = node
                queue.append(neighbor)
    return None
