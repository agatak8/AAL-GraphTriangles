from algorithms.brute_force import *
from algorithms.divide_and_conquer import *

algorithms = {"brute_force": brute_force, "divide": divide_and_conquer}


def solve(graph, alg_choice):
    algorithm = algorithms[alg_choice]
    return algorithm(graph) | algorithm(graph.get_complement())
