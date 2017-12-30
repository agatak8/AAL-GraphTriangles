#!/usr/bin/python3

import argparse

import sys

import algorithms.solvers as solvers

import helpers.io


def stdio(args):
    try:
        io_graph = helpers.io.input_to_graph(sys.stdin)
    except ValueError as e:
        print("Invalid graph data provided")
        print(e.args)
        return
    triangles = solvers.solve(io_graph[0], io_graph[2], args.a)
    result = helpers.io.triangles_to_output(triangles)
    sys.stdout.write(result)


def gen(args):
    pass


def test(args):
    pass


def main():
    main_parser = argparse.ArgumentParser(description="Graph triangle finder")
    main_parser.add_argument("-a", type=str, choices=solvers.algs.keys(),
                             required=True)
    subparsers = main_parser.add_subparsers(dest="mode", help="program mode")
    subparsers.required = True

    # mode 1
    m1_parser = subparsers.add_parser("stdio", help="take graph data from stdin and put solution in stdout")
    m1_parser.set_defaults(func=stdio)

    # mode 2
    m2_parser = subparsers.add_parser("gen", help="generate graph data and put solution in stdout")
    m2_parser.add_argument("-n", type=int, required=True, help="graph size")
    m2_parser.set_defaults(func=gen)

    # mode 3
    m3_parser = subparsers.add_parser("test", help="perform testing process",
                                      description="measure time for increasing n\n"
                                                  "and compare with the theoretical complexity")
    m3_parser.add_argument("-n", type=int, required=True, help="initial graph size")
    m3_parser.add_argument("-k", type=int, required=True, help="number of graph sizes to check")
    m3_parser.add_argument("-step", type=int, required=True, help="amount to increment graph size each step")
    m3_parser.add_argument("-r", type=int, required=True, help="number of random graphs generated per size")
    m3_parser.set_defaults(func=test)

    args = main_parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
