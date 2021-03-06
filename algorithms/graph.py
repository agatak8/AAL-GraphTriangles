# Agata Kłoss
# znalezienie liczby trójkątów w grafie

class AdjacencyList(object):
    # O(n) n = len(vertices)
    def __init__(self, vertices=set(), edges=set()):
        self.data = dict()
        for v in vertices:
            self.data[v] = set()
        for edge in edges:
            self.add_edge(edge[0], edge[1])

    def vertices(self):
        return self.data.keys()

    def edges(self):
        edge_set = set()
        for v in self.data:
            for u in self.data[v]:
                edge_set.update({v, u})
        return edge_set

    def neighbors(self, v1):
        return self.data[v1]

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
        # average O(n), worst O(n^2)
        for v in self.data:
            # average O(1), worst O(n)
            self.data[v].discard(v1)

    def remove_edge(self, v1, v2):
        # average O(1), worst O(n)
        self.data[v1].remove(v2)
        self.data[v2].remove(v1)

    def has_edge(self, v1, v2):
        return v2 in self.data[v1]

    def has_vertex(self, v1):
        return v1 in self.data

    def degree(self, v1):
        return len(self.data[v1])

    # O(n^2)
    def get_complement(self):
        vertices = set(self.data.keys())
        new_graph = AdjacencyList(vertices)
        for v in self.data:
            new_graph.data[v] = vertices - self.data[v] - {v} # O(len(vertices)) + O(len(v.edges))
        return new_graph
