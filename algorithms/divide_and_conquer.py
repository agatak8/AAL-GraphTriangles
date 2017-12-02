import algorithms.solvers
from algorithms.graph import get_vertices_in_edges


def divide_and_conquer(graph, fallback=algorithms.solvers.brute_force):
    n_vertices = graph.get_vertex_count()
    n_edges = graph.get_edge_count()

    if n_vertices < 3:
        return set()
    if n_vertices == 3:
        if n_edges == 3:
            return {graph.vertices}
        return set()

    # divide vertices into two and create two disjoint subgraphs
    first_half = graph.vertices.copy()
    second_half = set()
    for i in range(0, n_vertices / 2):
        second_half.add(first_half.pop())
    graph1 = graph.get_subgraph_with_vertices(first_half)
    graph2 = graph.get_subgraph_with_vertices(second_half)

    # create third subgraph by taking the edges that are not part
    # of either of the previously created 2 subgraphs
    # and taking the vertices that are part of these edges
    remaining_edges = graph.edges - graph1.edges - graph2.edges
    graph3 = graph.get_subgraph_with_vertices(get_vertices_in_edges(remaining_edges))

    # division failed
    if graph3.get_vertex_count() == n_vertices:
        return fallback(graph)

    # join results for all 3 subgraphs
    return divide_and_conquer(graph1) | divide_and_conquer(graph2) | divide_and_conquer(graph3)
