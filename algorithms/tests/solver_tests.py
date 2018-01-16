import unittest
from algorithms.solvers import *
from algorithms.tests import base_test


class TestNaiveMethod(unittest.TestCase, base_test.SolverTest):
    def __init__(self, *args, **kwargs):
        unittest.TestCase.__init__(self, *args, **kwargs)
        base_test.SolverTest.__init__(self, naive)


# class TestMatrixMethod(unittest.TestCase, base_test.SolverTest):
#     def __init__(self, *args, **kwargs):
#         unittest.TestCase.__init__(self, *args, **kwargs)
#         base_test.SolverTest.__init__(self, matrix, True)


class TestListMethod(unittest.TestCase, base_test.SolverTest):
    def __init__(self, *args, **kwargs):
        unittest.TestCase.__init__(self, *args, **kwargs)
        base_test.SolverTest.__init__(self, adj_list)


class TestDegreeMethod(unittest.TestCase, base_test.SolverTest):
    def __init__(self, *args, **kwargs):
        unittest.TestCase.__init__(self, *args, **kwargs)
        base_test.SolverTest.__init__(self, degree)


if __name__ == '__main__':
    unittest.main()
