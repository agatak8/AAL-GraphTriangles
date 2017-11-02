def brute_force(graph):
    results = set()
    for v in graph.vertices():
        for w in graph.vertices():
            for u in graph.vertices():
                if graph.has_edge(v, w) and graph.has_edge(v, u) and graph.has_edge(w, u):
                    results.update({v, w, u})
    return results


def smarter_brute_force(graph):
    graph_copy = graph.copy()
    # todo - iterate by sorted vertices, update degrees on the go?
    # sorted_vertices = sorted(graph_copy.vertices, key=lambda vertex: graph_copy.degree(vertex))
    results = set()
    for v in graph_copy.vertices():
        for w in graph_copy.vertices():
            for u in graph_copy.vertices():
                if graph_copy.has_edge(v, w) and graph_copy.has_edge(v, u) and graph_copy.has_edge(w, u):
                    results.update({v, w, u})
        graph_copy.remove_vertex(v)
    return results
