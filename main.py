#!/usr/bin/python3

import argparse
import sys
import algorithms.solvers as solvers
import modes


def stdio(args):
    sys.stdout.write(modes.stdio(args.a))


def gen(args):
    graph, result = modes.generate(args.a, args.V, args.E, args.t)
    with open(args.f1, "w") as f1, open(args.f2, "w") as f2:
        f1.write(graph)
        f2.write(result)


def test(args):
    pass


def main():
    main_parser = argparse.ArgumentParser(description="Graph triangle finder")
    # main_parser.add_argument("-a", type=str, choices=solvers.algs.keys(),
    #                         required=True)
    subparsers = main_parser.add_subparsers(dest="mode", help="program mode")
    subparsers.required = True

    # mode 1
    m1_parser = subparsers.add_parser("stdio", help="take graph data from stdin and put solution in stdout")
    m1_parser.add_argument("-a", type=str, choices=solvers.algs.keys(),
                           required=True, help="solving algorithm")
    m1_parser.set_defaults(func=stdio)

    # mode 2
    m2_parser = subparsers.add_parser("gen",
                                      help="generate graph data and write graph and solution to file1 and file 2 respectively")
    m2_parser.add_argument("-a", type=str, choices=solvers.algs.keys(),
                           required=True, help="solving algorithm")
    m2_parser.add_argument("-t", type=str, choices=modes.generate_types.keys(), required=True,
                           help="type of graphs to generate")
    m2_parser.add_argument("-V", type=int, required=True, help="vertex count")
    m2_parser.add_argument("-E", type=int, required=False, help="edge count/regularity")
    m2_parser.add_argument("-f1", type=str, required=True, help="output file for graph")
    m2_parser.add_argument("-f2", type=str, required=True, help="output file for solution")
    m2_parser.set_defaults(func=gen)

    # mode 3
    # m3_parser = subparsers.add_parser("test", help="perform testing process",
    #                                   description="measure time for increasing n\n"
    #                                               "and compare with the theoretical complexity")
    # m3_parser.add_argument("-n", type=int, required=True, help="initial graph size")
    # m3_parser.add_argument("-k", type=int, required=True, help="number of graph sizes to check")
    # m3_parser.add_argument("-step", type=int, required=True, help="amount to increment graph size each step")
    # m3_parser.add_argument("-r", type=int, required=True, help="number of random graphs generated per size")
    # m3_parser.set_defaults(func=test)

    args = main_parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
