# Agata Kłoss
# znalezienie liczby trójkątów w grafie

import helpers.io as io
import helpers.generator as generator
from helpers.measure import measure
import algorithms.solvers as solvers
import numpy as np
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
    if type == "tree":
        points = generator.tree_points(graph[0], n_vertices * 20, n_vertices * 10)
    elif type in ["regular", "bipartite", "full_bipartite"]:
        points = generator.circular_points(graph[0], n_vertices * 30)
    else:
        points = generator.random_points(graph[0], n_vertices * 15)
    if algorithm == "matrix":
        result = str(triangles)
    else:
        result = io.triangles_to_output(triangles)
    return io.graph_to_output(graph[0], points, graph[1]), result


def test(algorithm, initial_size, density, step, count, type):
    tested_sizes = []
    times = []
    theoretical_times = []
    result = []
    n = initial_size  # vertex count

    for i in range(count):
        graph = generate_types[type](n, int(n * (n - 1) // 2 * density))
        time = measure(graph[0], graph[1], algorithm)
        tested_sizes.append(n)
        times.append(time)
        theoretical_times.append((n ** 3)*0.001)
        n += step

    median_t = np.median(times)
    median_T = np.median(theoretical_times)
    print(median_t, median_T)
    for i in range(len(times)):
        t = times[i]
        T = theoretical_times[i]
        q = (t * median_T) / (T * median_t)
        result.append((tested_sizes[i], t, q))
    return result
