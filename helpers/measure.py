# Agata Kłoss
# znalezienie liczby trójkątów w grafie

from algorithms.solvers import solve
from time import process_time as timer

def measure(vertices, edges, algorithm):
    t1 = timer()
    solution = solve(vertices, edges, algorithm, True)
    t2 = timer()
    return t2-t1