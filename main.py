#!/usr/bin/python3

import argparse


def main():
    main_parser = argparse.ArgumentParser(description="Graph triangle finder")
    subparsers = main_parser.add_subparsers(dest="mode", help="program mode")
    subparsers.required = True

    # mode 1
    m1_parser = subparsers.add_parser("stdio", help="take graph data from stdin and put solution in stdout")

    # mode 2
    m2_parser = subparsers.add_parser("gen", help="generate graph data and put solution in stdout")
    m2_parser.add_argument("-n", type=int, required=True, help="graph size")

    # mode 3
    m3_parser = subparsers.add_parser("test", help="perform testing process",
                                      description="measure time for increasing n\n"
                                                  "and compare with the theoretical complexity")
    m3_parser.add_argument("-n", type=int, required=True, help="initial graph size")
    m3_parser.add_argument("-k", type=int, required=True, help="number of graph sizes to check")
    m3_parser.add_argument("-step", type=int, required=True, help="amount to increment graph size each step")
    m3_parser.add_argument("-r", type=int, required=True, help="number of random graphs generated per size")

    namespace = main_parser.parse_args()
    print(namespace)


if __name__ == "__main__":
    main()
