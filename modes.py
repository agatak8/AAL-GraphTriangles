import helpers.io as io
import helpers.generator as generator
import algorithms.solvers as solvers
import sys

generate_types = {"random": generator.random_graph,
                  "regular": generator.k_regular,
                  "bipartite": generator.bipartite_graph,
                  "full": generator.full_graph,
                  "full_bipartite": generator.full_bipartite_graph,
                  "tree": generator.binary_tree}


def stdio(algorithm):
    try:
        io_graph = io.input_to_graph(sys.stdin)
    except ValueError as e:
        print("Invalid graph data provided")
        print(e.args)
        return
    triangles = solvers.solve(io_graph[0], io_graph[2], algorithm)
    result = io.triangles_to_output(triangles)
    return result


def generate(algorithm, n_vertices, n_edges, type="random"):
    graph = generate_types[type](n_vertices, n_edges)
    triangles = solvers.solve(graph[0], graph[1], algorithm)
    if (type == "tree"):
        points = generator.tree_points(graph[0], n_vertices * 20, n_vertices * 10)
    elif (type in ["regular", "bipartite", "full_bipartite"]):
        points = generator.circular_points(graph[0], n_vertices * 30)
    else:
        points = generator.random_points(graph[0], n_vertices * 15)
    if (algorithm == "matrix"):
        result = str(triangles)
    else:
        result = io.triangles_to_output(triangles)
    return (io.graph_to_output(graph[0], points, graph[1]), result)
