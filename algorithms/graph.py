def get_vertices_in_edges(edges):
    vertices = set()
    for edge in edges:
        vertices.update(edge)
    return vertices


class AdjacencyList(object):
    def __init__(self, vertices=set(), edges=set()):
        self.data = dict()
        for v in vertices:
            self.data[v] = set()
        for edge in edges:
            vs = list(edge)
            self.add_edge(vs[0], vs[1])

    def vertices(self):
        return self.data.keys()

    def edges(self):
        edge_set = set()
        for v in self.data:
            for u in self.data[v]:
                edge_set.update({v, u})
        return edge_set

    def get_vertex_count(self):
        return len(self.data)

    def get_edge_count(self):
        return sum(len(self.data[v]) for v in self.data) / 2

    def add_edge(self, v1, v2):
        (self.data[v1]).add(v2)
        (self.data[v2]).add(v1)

    def add_vertex(self, v1):
        self.data[v1] = set()

    def remove_vertex(self, v1):
        del self.data[v1]
        for v in self.data:
            self.data[v].discard(v1)

    def remove_edge(self, v1, v2):
        self.data[v1].remove(v2)
        self.data[v2].remove(v1)

    def has_edge(self, v1, v2):
        return v2 in self.data[v1]

    def has_vertex(self, v1):
        return v1 in self.data

    def degree(self, v1):
        return len(self.data[v1])

    def get_subgraph_with_vertices(self, vertices):
        new_graph = AdjacencyList(vertices)
        for v in vertices:
            new_graph.data[v] = self.data[v].intersection(vertices)
        return new_graph

    def get_subgraph_without_vertices(self, vertices):
        new_data = self.data.copy()
        for v in vertices:
            del new_data[v]
            for u in new_data:
                new_data[u].discard(v)
        new_graph = AdjacencyList()
        new_graph.data = new_data
        return new_graph

    def get_complement(self):
        vertices = set(self.data.keys())
        new_graph = AdjacencyList(vertices)
        for v in self.data:
            new_graph.data[v] = vertices - self.data[v]
        return new_graph
