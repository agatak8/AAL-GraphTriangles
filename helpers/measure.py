# Agata Kłoss
# znalezienie liczby trójkątów w grafie

from algorithms.solvers import solve
from time import process_time as timer # use process time to exclude sleep time


# returns time taken by algorithm to solve given graph
def measure(vertices, edges, algorithm):
    t1 = timer()
    solution = solve(vertices, edges, algorithm, True) # only calculate how many triangles, not what they are
    t2 = timer()
    return t2-t1