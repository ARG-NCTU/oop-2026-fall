# W11 AI Tutor Part B: Fewest Stops (MIT 6.0002 Lec 3: Graph-theoretic Models)
#
# Digraph: add_node(name), add_edge(src, dest), children_of(name)
# Graph(Digraph): add_edge also adds the reverse edge
# fewest_stops(graph, start, end) -> list of station names with the fewest edges, None if unreachable
#                                    BFS + parent dict, O(V + E)
# reachable(graph, start, end)    -> True/False with DFS, keeps a visited set so cycles are safe

from collections import deque


class Digraph(object):
    def __init__(self):
        self.edges = {}                      # name -> list of children

    def add_node(self, name):
        if name in self.edges:
            raise ValueError("Duplicate node: " + name)
        self.edges[name] = []

    def add_edge(self, src, dest):
        if src not in self.edges or dest not in self.edges:
            raise ValueError("Node not in graph")
        self.edges[src].append(dest)

    def children_of(self, name):
        return self.edges[name]

    def has_node(self, name):
        return name in self.edges


class Graph(Digraph):
    def add_edge(self, src, dest):
        Digraph.add_edge(self, src, dest)
        Digraph.add_edge(self, dest, src)


def fewest_stops(graph, start, end):
    if not graph.has_node(start) or not graph.has_node(end):
        return None
    parent = {start: None}                   # also works as the visited set
    queue = deque([start])                   # popleft() is O(1), list.pop(0) is O(n)
    while queue:
        node = queue.popleft()
        if node == end:
            path = []
            while node is not None:          # walk back through parents
                path.append(node)
                node = parent[node]
            return path[::-1]
        for nxt in graph.children_of(node):
            if nxt not in parent:
                parent[nxt] = node
                queue.append(nxt)
    return None


def reachable(graph, start, end, visited=None):
    if visited is None:
        visited = set()
    if start == end:
        return True
    visited.add(start)
    for nxt in graph.children_of(start):
        if nxt not in visited and reachable(graph, nxt, end, visited):
            return True
    return False


if __name__ == "__main__":
    # provided example: a small metro map (undirected)
    g = Graph()
    for s in ["Taipei", "Zhongshan", "Shuanglian", "Minquan", "Ximen", "Songshan", "Island"]:
        g.add_node(s)
    for a, b in [("Taipei", "Zhongshan"), ("Zhongshan", "Shuanglian"), ("Shuanglian", "Minquan"),
                 ("Taipei", "Ximen"), ("Zhongshan", "Songshan"), ("Songshan", "Minquan")]:
        g.add_edge(a, b)
    assert fewest_stops(g, "Taipei", "Minquan") in (
        ["Taipei", "Zhongshan", "Shuanglian", "Minquan"],
        ["Taipei", "Zhongshan", "Songshan", "Minquan"])
    assert len(fewest_stops(g, "Ximen", "Minquan")) == 5

    # edge cases
    assert fewest_stops(g, "Taipei", "Taipei") == ["Taipei"]
    assert fewest_stops(g, "Taipei", "Island") is None          # no edge to Island
    assert fewest_stops(g, "Taipei", "Nowhere") is None         # not a station
    assert reachable(g, "Ximen", "Songshan") is True            # graph has a cycle
    assert reachable(g, "Island", "Taipei") is False

    # directed graph: one-way edges
    d = Digraph()
    for s in "ABC":
        d.add_node(s)
    d.add_edge("A", "B")
    d.add_edge("B", "C")
    d.add_edge("C", "A")                                        # cycle A -> B -> C -> A
    assert fewest_stops(d, "A", "C") == ["A", "B", "C"]
    assert fewest_stops(d, "C", "B") == ["C", "A", "B"]         # cannot go C -> B directly
    assert reachable(d, "A", "C") and reachable(d, "C", "B")

    try:
        g.add_node("Taipei")
    except ValueError:
        pass
    else:
        assert False, "expected ValueError"

    print("all tests passed")
