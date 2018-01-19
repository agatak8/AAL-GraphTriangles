#!/usr/bin/python3

# Agata Kłoss
# znalezienie liczby trójkątów w grafie

import argparse
import sys
import algorithms.solvers as solvers
import modes


def stdio(args):
    sys.stdout.write(modes.stdio(args.a))
    sys.stdout.write("\n")


def gen(args):
    sys.stdout.write(
        "Algorithm: %s\nGraph type: %s\nVertices: %s\nEdges/regularity: %s\n"
        % (args.a, args.t, args.E, args.V))
    graph, result = modes.generate(args.a, args.V, args.E, args.t)
    with open(args.f1, "w") as f1, open(args.f2, "w") as f2:
        f1.write(graph)
        f2.write(result)
    sys.stdout.write("Generated graph written to %s\n" % args.f1)
    sys.stdout.write("Result written to %s\n" % args.f2)


def test(args):
    sys.stdout.write("Algorithm: %s\nGraph type: %s\nDensity: %f\n"
                     % (args.a, args.t, args.d))
    sys.stdout.write("Initial size: %d\nIterations: %d\nRepetitions: %d\nStep: %d\n"
                     % (args.n, args.k, args.r, args.step))
    sys.stdout.write("=======================\n")
    result = modes.test(args.a, args.n, args.d, args.step, args.k, args.t, args.r)
    sys.stdout.write("n\tt(n)\tq(n)\n")

    for it in result:
        sys.stdout.write("%d\t%.4f\t%.2f\n"
                         % (it[0], it[1], it[2]))

    if args.f:
        with open(args.f, "w") as file:
            file.write("n\tt(n)\tq(n)\n")
            for it in result:
                file.write("%d\t%.4f\t%.2f\n"
                                 % (it[0], it[1], it[2]))


# must subclass ArgumentParser to make it print help on error
class DefaultHelpParser(argparse.ArgumentParser):
    def error(self, message):
        sys.stderr.write('error: %s\n' % message)
        self.print_help()
        sys.exit(2)


def main():
    main_parser = DefaultHelpParser(description="Graph triangle finder")
    subparsers = main_parser.add_subparsers(dest="mode", help="program mode")
    subparsers.required = True

    # mode 1 - standard input/output
    m1_parser = subparsers.add_parser("stdio", help="take graph data from stdin and put solution in stdout")
    m1_parser.add_argument("-a", type=str, choices=solvers.algs.keys(),
                           required=True, help="solving algorithm")
    m1_parser.set_defaults(func=stdio)

    # mode 2 - generate and output graph and result to two files
    m2_parser = subparsers.add_parser("gen",
                                      help="generate graph data and write graph and solution to file1 and file 2 respectively")
    m2_parser.add_argument("-a", type=str, choices=solvers.algs.keys(),
                           required=True, help="solving algorithm")
    m2_parser.add_argument("-t", type=str, choices=modes.generate_types.keys(), required=True,
                           help="type of graphs to generate")
    m2_parser.add_argument("-V", type=int, required=True, help="vertex count",
                           metavar="vertices")
    m2_parser.add_argument("-E", type=int, required=False, help="edge count/regularity",
                           metavar="edges")
    m2_parser.add_argument("-f1", type=str, required=True, help="output file for graph",
                           metavar="output_graph_file")
    m2_parser.add_argument("-f2", type=str, required=True, help="output file for solution",
                           metavar="output_solution_file")
    m2_parser.set_defaults(func=gen)

    # mode 3 - time measurement testing process
    m3_parser = subparsers.add_parser("test", help="perform testing process for chosen algorithm",
                                      description="measure time for increasing n\n"
                                                  "and compare with the theoretical complexity")
    m3_parser.add_argument("-a", type=str, choices=solvers.algs.keys(),
                           required=True, help="solving algorithm")
    m3_parser.add_argument("-t", type=str, choices=modes.test_types.keys(), required=True,
                           help="type of graphs to generate")
    m3_parser.add_argument("-k", type=int, required=True, help="how many graphs to test against",
                           metavar="iterations")
    m3_parser.add_argument("-n", type=int, required=True, help="initial graph size (vertex count)",
                           metavar="size")
    m3_parser.add_argument("-d", type=float, required=True, help="graph density [0-1]",
                           metavar="density")
    m3_parser.add_argument("-step", type=int, required=True, help="amount to increment size each step",)
    m3_parser.add_argument("-r", type=int, required=True, help="how many repetitions per size",
                           metavar="repetitions")
    m3_parser.add_argument("-f", type=str, required=False, help="output file")
    m3_parser.set_defaults(func=test)

    args = main_parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
