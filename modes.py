# Agata Kłoss
# znalezienie liczby trójkątów w grafie

import helpers.io as io
import helpers.generator as generator
from helpers.measure import measure
import algorithms.solvers as solvers
from statistics import median_low
import sys

# types of graphs available for generate mode
generate_types = {"random": generator.random_graph,
                  "regular": generator.k_regular,
                  "bipartite": generator.bipartite_graph,
                  "full": generator.full_graph,
                  "full_bipartite": generator.full_bipartite_graph,
                  "tree": generator.binary_tree}

# types of graphs available for test mode
test_types = {"random": generator.random_graph,
              "regular": generator.k_regular,
              "bipartite": generator.bipartite_graph,
              "tree": generator.binary_tree}

# maximum amount of edges/regularity for test mode types
test_types_max = {"random": lambda n: n * (n - 1) // 2,
                  "regular": lambda n: n,
                  "bipartite": lambda n: n ** 2 // 4,
                  "tree": lambda n: None}  # doesn't matter for trees


# get graph string from stdin, convert to graph, solve with algorithm, write result string to stdout
def stdio(algorithm):
    try:
        vertices, points, edges = io.input_to_graph(sys.stdin)
    except ValueError as e:
        print("Invalid graph data provided")
        print(e.args)
        return
    triangles = solvers.solve(vertices, edges, algorithm)
    if(algorithm == "matrix"):
        result = str(triangles)
    else:
        result = io.triangles_to_output(triangles)
    return result


# generate graph of given type and solve it with algorithm, return graph and solution
def generate(algorithm, n_vertices, n_edges, type="random"):
    # generate graph
    vertices, edges = generate_types[type](n_vertices, n_edges)
    # get solution
    triangles = solvers.solve(vertices, edges, algorithm)
    # generate 2D coordinates for graph vertices according to type
    if type == "tree":
        points = generator.tree_points(vertices, n_vertices * 20, n_vertices * 10)
    elif type in ["regular", "bipartite", "full_bipartite"]:
        points = generator.circular_points(vertices, n_vertices * 30)
    else:
        points = generator.random_points(vertices, n_vertices * 15)
    if algorithm == "matrix":
        result = str(triangles)
    else:
        result = io.triangles_to_output(triangles)
    # return graph string and result string
    return io.graph_to_output(vertices, points, edges), result


# perform parametrized testing process and return n, t(n), q(n) table
def test(algorithm, initial_size, density, step, count, type="random", repetitions=1):
    tested_sizes = []  # n
    times = []  # t(n)
    theoretical_times = []  # T(n)
    result = []  # n, t(n), q(n) table
    n = initial_size  # vertex count

    if repetitions < 1:
        return tuple()

    # calculate t(n)'s
    for i in range(count):
        sys.stdout.write("\rIteration: %d" % i)
        tested_sizes.append(n)
        iteration_times = []
        # r repetitions
        for j in range(repetitions):
            # generate graph with n vertices
            # and edges/regularity calculated as density * maximum edges/regularity for type
            vertices, edges = test_types[type](n, int(test_types_max[type](n) * density))
            time = measure(vertices, edges, algorithm)
            iteration_times.append(time)
        average_time = sum(iteration_times) / len(iteration_times)
        times.append(average_time)
        n += step
    sys.stdout.write("\r                       \r")

    # calculate T(n)'s
    for i in range(count):
        n = tested_sizes[i]
        # scaled by 0.001 to account for huge values of n**3
        theoretical_times.append((solvers.complexities[algorithm](n)) * 0.001)

    # calculate q(n)'s and create full result table
    median_n = median_low(tested_sizes)  # use median low to ensure median_n exists in data set
    mn_i = tested_sizes.index(median_n)  # median_n's index is the same as median_t and median_T's index
    median_t = times[mn_i]
    median_T = theoretical_times[mn_i]

    for i in range(len(times)):
        t = times[i]
        T = theoretical_times[i]
        q = (t * median_T) / (T * median_t)
        result.append((tested_sizes[i], t, q))
    return result
