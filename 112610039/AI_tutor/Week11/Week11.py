class Node():
    def __init__(self, name):
        if not isinstance(name, str):
            raise TypeError
        self.name = name
    def get_name(self):
        return self.name
    def __str__(self):
        return f"Node name: {self.name}\n"

class Edge():
    def __init__(self, src, dest):
        if not isinstance(src, Node) or not isinstance(dest, Node):
            raise TypeError
        self.src = src
        self.dest = dest
    def get_source(self):
        return self.src
    def get_destination(self):
        return self.dest
    def __str__(self):
        return f"Edge: from Node <{self.src.get_name()}> to Node <{self.dest.get_name()}>\n"

class Digraph():
    def __init__(self):
        self.edges = {}
    def add_node(self, node):
        if not isinstance(node, Node):
            raise TypeError
        if node in self.edges:
            raise ValueError("Duplicate node")
        self.edges[node] = []
    def add_edge(self, edge):
        if not isinstance(edge, Edge):
            raise TypeError
        if (edge.get_source() not in self.edges) or (edge.get_destination() not in self.edges):
            raise ValueError("Node not in graph")
        self.edges[edge.get_source()].append(edge.get_destination())
    def children(self, node):
        if not isinstance(node, Node):
            raise TypeError
        for N in self.edges[node]:
            print(N)
    def has_node(self, node):
        if not isinstance(node, Node):
            raise TypeError
        return node in self.edges
    def get_node(self, name):
        if not isinstance(name, str):
            raise TypeError
        for N in self.edges:
            if N.get_name() == name:
                return N
        raise NameError(name)

class Graph(Digraph):
    def add_edge(self, edge):
        if not isinstance(edge, Edge):
            raise TypeError
        if (edge.get_source() not in self.edges) or (edge.get_destination() not in self.edges):
            raise ValueError("Node not in graph")
        self.edges[edge.get_source()].append(edge.get_destination())
        self.edges[edge.get_destination()].append(edge.get_source())


def shortest_path_bfs(graph, start, end):
    if not isinstance(graph, Digraph):
        raise TypeError
    if not isinstance(start, Node) or not isinstance(end, Node):
        raise TypeError
    if not graph.has_node(start) or not graph.has_node(end):
        raise ValueError("Node not in graph")

    path_queue = [[start]]
    while len(path_queue) != 0:
        tmp_path = path_queue.pop(0)

        if tmp_path[-1] == end:
            return tmp_path

        for neighbor in graph.edges[tmp_path[-1]]:
            if neighbor not in tmp_path:
                new_path = tmp_path.copy()
                new_path.append(neighbor)
                path_queue.append(new_path)

    return None


def main():
    g = Digraph()
    for name in ('Boston', 'Providence', 'New York', 'Chicago', 'Denver', 'Phoenix', 'Los Angeles'):
        g.add_node(Node(name))

    edges = [
        ('Boston', 'Providence'), ('Boston', 'New York'),
        ('Providence', 'Boston'), ('Providence', 'New York'),
        ('New York', 'Chicago'), ('Chicago', 'Denver'),
        ('Chicago', 'Phoenix'), ('Denver', 'Phoenix'),
        ('Denver', 'New York'), ('Los Angeles', 'Boston')
    ]
    for src, dest in edges:
        g.add_edge(Edge(g.get_node(src), g.get_node(dest)))

    path1 = shortest_path_bfs(g, g.get_node('Boston'), g.get_node('Phoenix'))
    print([n.get_name() for n in path1])
    # [n.get_name() for n in path1] -> ['Boston', 'New York', 'Chicago', 'Phoenix']

    path2 = shortest_path_bfs(g, g.get_node('Chicago'), g.get_node('Boston'))
    print([n.get_name() for n in path2])
    # path2 -> None

if __name__ == "__main__":
    main()