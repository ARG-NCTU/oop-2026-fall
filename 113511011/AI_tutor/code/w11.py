"""Lecture 3 transfer: shortest open routes on directed or undirected graphs."""


class Node:
    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name

    def __str__(self):
        return self.name


class Edge:
    def __init__(self, src, dest):
        self.src, self.dest = src, dest

    def getSource(self):
        return self.src

    def getDestination(self):
        return self.dest

    def __str__(self):
        return f'{self.src}->{self.dest}'


class Digraph:
    def __init__(self):
        self.edges = {}

    def addNode(self, node):
        if self.hasNode(node):
            raise ValueError('Duplicate node')
        self.edges[node] = []

    def addEdge(self, edge):
        src, dest = edge.getSource(), edge.getDestination()
        if not self.hasNode(src) or not self.hasNode(dest):
            raise ValueError('Endpoint not in graph')
        self.edges[src].append(dest)

    def hasNode(self, node):
        return node in self.edges

    def childrenOf(self, node):
        return self.edges[node]


class Graph(Digraph):
    def addEdge(self, edge):
        super().addEdge(edge)
        super().addEdge(Edge(edge.getDestination(), edge.getSource()))


def query_allowed(graph, start, end, closed):
    if not graph.hasNode(start) or not graph.hasNode(end):
        raise ValueError('Endpoint not in graph')
    return start not in closed and end not in closed


def DFS(graph, start, end, closed=(), trace=None):
    """Compare simple paths, pruning prefixes unable to improve the best."""
    closed = set(closed)
    if not query_allowed(graph, start, end, closed):
        return None
    best = None

    def visit(node, path):
        nonlocal best
        path = path + [node]
        if trace is not None:
            trace.append(tuple(str(n) for n in path))
        if node is end:
            if best is None or len(path) < len(best):
                best = path
            return
        if best is not None and len(path) >= len(best):
            return
        for child in graph.childrenOf(node):
            if child not in closed and child not in path:
                visit(child, path)

    visit(start, [])
    return best


def BFS(graph, start, end, closed=(), trace=None):
    """Discover each vertex once; reconstruct a minimum-hop open route."""
    closed = set(closed)
    if not query_allowed(graph, start, end, closed):
        return None
    queue, head = [start], 0
    parent = {start: None}
    while head < len(queue):
        node = queue[head]
        head += 1
        if trace is not None:
            trace.append(str(node))
        if node is end:
            path = []
            while node is not None:
                path.append(node)
                node = parent[node]
            return path[::-1]
        for child in graph.childrenOf(node):
            if child not in closed and child not in parent:
                parent[child] = node
                queue.append(child)
    return None


def route_names(path):
    return None if path is None else [str(node) for node in path]


def build_graph(graph_type, names, links):
    graph = graph_type()
    nodes = {name: Node(name) for name in names}
    for node in nodes.values():
        graph.addNode(node)
    for src, dest in links:
        graph.addEdge(Edge(nodes[src], nodes[dest]))
    return graph, nodes


def distance_oracle(names, links, closed, undirected=False):
    """Test-only all-pairs matrix relaxation, independent of DFS and BFS."""
    size, infinity = len(names), len(names) + 1
    index = {name: i for i, name in enumerate(names)}
    distances = [[infinity] * size for _ in names]
    for name in names:
        if name not in closed:
            distances[index[name]][index[name]] = 0
    for src, dest in links:
        if src not in closed and dest not in closed:
            distances[index[src]][index[dest]] = 1
            if undirected:
                distances[index[dest]][index[src]] = 1
    for k in range(size):
        for i in range(size):
            for j in range(size):
                distances[i][j] = min(distances[i][j], distances[i][k] + distances[k][j])
    return distances


def run_tests():
    from itertools import combinations, permutations

    links = [('S', 'A'), ('A', 'B'), ('B', 'T'), ('S', 'T'), ('B', 'S')]
    graph, nodes = build_graph(Digraph, ['S', 'A', 'B', 'T', 'X'], links)
    original = {node: children[:] for node, children in graph.edges.items()}
    fixed = [
        ('S', 'T', (), ['S', 'T']),
        ('S', 'B', ('A',), None),
        ('S', 'S', (), ['S']),
        ('S', 'T', ('S',), None),
        ('S', 'T', ('T',), None),
        ('S', 'X', (), None),
        ('T', 'S', (), None),
        ('S', 'B', (), ['S', 'A', 'B']),
        ('X', 'X', (), ['X']),
        ('B', 'A', (), ['B', 'S', 'A']),
    ]
    for src, dest, closed, expected in fixed:
        for solver in (DFS, BFS):
            assert route_names(solver(graph, nodes[src], nodes[dest],
                                      [nodes[n] for n in closed])) == expected
            assert graph.edges == original
    dfs_trace, bfs_trace = [], []
    assert route_names(DFS(graph, nodes['S'], nodes['T'], trace=dfs_trace)) == ['S', 'T']
    assert route_names(BFS(graph, nodes['S'], nodes['T'], trace=bfs_trace)) == ['S', 'T']
    assert dfs_trace == [('S',), ('S', 'A'), ('S', 'A', 'B'), ('S', 'A', 'B', 'T'), ('S', 'T')]
    assert bfs_trace == ['S', 'A', 'T']

    # All labeled 3-vertex simple graphs, every closure set, all endpoint pairs.
    audits = 0
    names = ['A', 'B', 'C']
    for graph_type in (Digraph, Graph):
        possible = list(permutations(names, 2) if graph_type is Digraph else combinations(names, 2))
        for mask in range(1 << len(possible)):
            links_small = [edge for bit, edge in enumerate(possible) if mask & (1 << bit)]
            g, ns = build_graph(graph_type, names, links_small)
            before = {node: children[:] for node, children in g.edges.items()}
            for closed_mask in range(1 << len(names)):
                closed = {name for bit, name in enumerate(names) if closed_mask & (1 << bit)}
                distances = distance_oracle(names, links_small, closed, graph_type is Graph)
                for i, src in enumerate(names):
                    for j, dest in enumerate(names):
                        for solver in (DFS, BFS):
                            path = solver(g, ns[src], ns[dest], [ns[name] for name in closed])
                            expected_distance = distances[i][j]
                            if expected_distance > len(names):
                                assert path is None
                            else:
                                assert path is not None and len(path) - 1 == expected_distance
                                assert path[0] is ns[src] and path[-1] is ns[dest]
                                assert len(set(path)) == len(path)
                                assert all(str(node) not in closed for node in path)
                                assert all(b in g.childrenOf(a) for a, b in zip(path, path[1:]))
                            assert g.edges == before
                        audits += 1

    def raises_value_error(action):
        try:
            action()
        except ValueError:
            return
        raise AssertionError('Expected ValueError')

    raises_value_error(lambda: graph.addNode(nodes['S']))
    outsider = Node('S')  # Same name, different identity.
    raises_value_error(lambda: graph.addEdge(Edge(nodes['S'], outsider)))
    for solver in (DFS, BFS):
        raises_value_error(lambda: solver(graph, outsider, nodes['T']))
        raises_value_error(lambda: solver(graph, nodes['S'], outsider))
    assert graph.edges == original
    assert str(Edge(nodes['S'], nodes['T'])) == 'S->T'
    assert nodes['S'].getName() == 'S'
    undirected, un = build_graph(Graph, ['A', 'B'], [('A', 'B')])
    assert isinstance(undirected, Digraph)
    assert undirected.childrenOf(un['A']) == [un['B']]
    assert undirected.childrenOf(un['B']) == [un['A']]
    raises_value_error(lambda: undirected.addEdge(Edge(un['A'], outsider)))
    assert undirected.childrenOf(un['A']) == [un['B']]

    # Revisiting X through a shorter prefix must remain possible in DFS.
    g, ns = build_graph(Digraph, ['S', 'A', 'B', 'X', 'T'],
                        [('S', 'A'), ('A', 'B'), ('B', 'X'), ('X', 'T'), ('S', 'X')])
    for solver in (DFS, BFS):
        assert route_names(solver(g, ns['S'], ns['T'])) == ['S', 'X', 'T']
    # Equal-length alternatives keep adjacency order and repeat deterministically.
    g, ns = build_graph(Digraph, ['S', 'A', 'B', 'T'],
                        [('S', 'B'), ('S', 'A'), ('A', 'T'), ('B', 'T')])
    for solver in (DFS, BFS):
        for _ in range(2):
            assert route_names(solver(g, ns['S'], ns['T'])) == ['S', 'B', 'T']
    large_names = [str(i) for i in range(2000)]
    g, ns = build_graph(Digraph, large_names, list(zip(large_names, large_names[1:])))
    assert route_names(BFS(g, ns['0'], ns['1999'])) == large_names
    print(f'W11 PASS: {len(fixed)} fixed, {audits} exhaustive route queries, class contracts, revisit/tie regressions, 1 large BFS.')
    print('DFS paths:', dfs_trace)
    print('BFS expansions:', bfs_trace)
    print("Both shortest routes: ['S', 'T']")


if __name__ == '__main__':
    run_tests()
