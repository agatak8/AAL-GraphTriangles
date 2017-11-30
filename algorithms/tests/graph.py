import unittest
from algorithms.graph import AdjacencyList

vertices = {1, 2, 3, 4, 5, 6}
edges = ((1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4), (4, 5))


class TestAdjacencyList(unittest.TestCase):
    def test_init_empty(self):
        graph = AdjacencyList()
        self.assertEqual(graph.get_vertex_count(), 0)
        self.assertEqual(graph.get_edge_count(), 0)

    def test_init_nonempty(self):
        graph = AdjacencyList(vertices, edges)
        self.assertEqual(graph.get_vertex_count(), len(vertices))
        self.assertEqual(graph.get_edge_count(), len(edges))
        for v in vertices:
            self.assertTrue(graph.has_vertex(v))
        for e in edges:
            self.assertTrue(graph.has_edge(e[0], e[1]))

    def test_init_only_vertices(self):
        graph = AdjacencyList(vertices, set())
        self.assertEqual(graph.get_vertex_count(), len(vertices))
        self.assertEqual(graph.get_edge_count(), 0)
        for v in vertices:
            self.assertEqual(graph.degree(v), 0)

    def test_degree(self):
        graph = AdjacencyList(vertices, edges)
        for v in vertices:
            self.assertEqual(graph.degree(v), sum(1 for edge in edges if v in edge))

    def test_add_edge(self):
        graph = AdjacencyList(vertices, edges)
        self.assertFalse(graph.has_edge(5, 6))
        graph.add_edge(5, 6)
        self.assertTrue(graph.has_edge(5, 6))

    def test_complement_of_empty(self):
        graph = AdjacencyList(vertices, set())
        complement = graph.get_complement()
        for v in vertices:
            for u in vertices:
                if (v != u):
                    self.assertTrue(complement.has_edge(v, u))

    def test_complement_inverse(self):
        graph = AdjacencyList(vertices, edges)
        complement = graph.get_complement()
        graph2 = complement.get_complement()
        for v in vertices:
            for u in vertices:
                self.assertEqual(graph.has_edge(v, u), graph2.has_edge(v, u))

    def test_subgraph_with_one_vertex(self):
        graph = AdjacencyList(vertices, edges)
        subgraph = graph.get_subgraph_with_vertices({1})
        self.assertEqual(subgraph.get_edge_count(), 0)
        self.assertEqual(subgraph.get_vertex_count(), 1)

    def test_subgraph_with_all_vertices(self):
        graph = AdjacencyList(vertices, edges)
        subgraph = graph.get_subgraph_with_vertices(vertices)
        self.assertEqual(graph.get_vertex_count(), subgraph.get_vertex_count())
        self.assertEqual(graph.get_edge_count(), subgraph.get_edge_count())
        for e in edges:
            self.assertTrue(subgraph.has_edge(e[0], e[1]))

    def test_subgraph_with_some_vertices(self):
        graph = AdjacencyList(vertices, edges)
        subset = {1, 2, 4}
        subgraph = graph.get_subgraph_with_vertices(subset)
        for v in vertices:
            self.assertEqual(v in subset, subgraph.has_vertex(v))
        subedges = [edge for edge in edges if (edge[0] in subset and edge[1] in subset)]
        self.assertEqual(subgraph.get_edge_count(), len(subedges))
        for e in subedges:
            self.assertTrue(subgraph.has_edge(e[0], e[1]))

    def test_subgraph_without_some_vertices(self):
        graph = AdjacencyList(vertices, edges)
        subset = {1, 2, 4}
        subgraph = graph.get_subgraph_without_vertices(subset)
        for v in vertices:
            self.assertNotEqual(v in subset, subgraph.has_vertex(v))
        for e in subgraph.edges():
            self.assertEqual(subset.intersection(e), set())
