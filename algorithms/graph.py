class Graph(object):
    def __init__(self, vertices=set(), edges=set()):
        self.vertices = vertices
        self.edges = edges

    def vertices(self):
        return self.vertices

    def get_vertex_count(self):
        return len(self.vertices)

    def get_edge_count(self):
        return len(self.edges)

    def add_edge(self, v1, v2):
        self.edges.add({v1, v2})

    def add_vertex(self, v1):
        self.vertices.add(v1)

    def remove_vertex(self, v1):
        self.vertices.remove(v1)
        self.edges.remove(edge for edge in self.edges if v1 in edge)

    def remove_edge(self, v1, v2):
        self.edges.remove({v1, v2})

    def has_edge(self, v1, v2):
        return {v1, v2} in self.edges

    def has_vertex(self, v1):
        return v1 in self.vertices

    def degree(self, v1):
        return sum(1 for edge in self.edges if v1 in edge)

    def get_subgraph_with_vertices(self, vertices):
        return Graph(vertices, set(edge for edge in self.edges if edge.issubset(vertices)))

    def get_subgraph_with_vertices_in_edges(self, edges):
        vertices = set()
        for edge in edges:
            vertices.update(edge)
        return self.get_subgraph_with_vertices(vertices)

    def get_subgraph_without_vertices(self, vertices):
        return self.get_subgraph_with_vertices(self.vertices - vertices)

    def get_subgraph_without_vertices_in_edges(self, edges):
        vertices_to_remove = set()
        for edge in edges:
            vertices_to_remove.update(edge)
        return self.get_subgraph_without_vertices(vertices_to_remove)

    def get_complement(self):
        edges = set({v, w} for v in self.vertices for w in self.vertices if {v, w} not in self.edges and v != w)
        return Graph(self.vertices, edges)


class AdjacencyList(object):
    def __init__(self, vertices=set(), edges=set()):
        self.data = dict.fromkeys(vertices, set())
        for edge in edges:
            vs = list(edge)
            self.data[vs[0]].update(vs[1])
            self.data[vs[1]].update(vs[0])

    def vertices(self):
        return self.data.keys()

    def get_vertex_count(self):
        return len(self.data)

    def get_edge_count(self):
        return sum(len(self.data[v]) for v in self.data) / 2

    def add_edge(self, v1, v2):
        self.data[v1].update(v2)
        self.data[v2].update(v1)

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
            new_graph.data[v] = self.data[v]
        return new_graph

    def get_subgraph_with_vertices_in_edges(self, edges):
        vertices = set()
        for edge in edges:
            vertices.update(edge)
        return self.get_subgraph_with_vertices(vertices)

    def get_subgraph_without_vertices(self, vertices):
        new_data = self.data.copy()
        for v in vertices:
            del new_data[v]
            for u in new_data:
                new_data[u].discard(v)
        new_graph = AdjacencyList()
        new_graph.data = new_data
        return new_graph

    def get_subgraph_without_vertices_in_edges(self, edges):
        vertices = set()
        for edge in edges:
            vertices.update(edge)
        return self.get_subgraph_without_vertices(vertices)

    def get_complement(self):
        vertices = set(self.data.keys())
        new_graph = AdjacencyList(vertices)
        for v in self.data:
            new_graph.data[v] = vertices - self.data[v]
        return new_graph
