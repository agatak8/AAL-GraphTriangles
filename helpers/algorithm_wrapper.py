def get_results(graph, algorithm):
    return algorithm(graph) | algorithm(graph.get_complement())
