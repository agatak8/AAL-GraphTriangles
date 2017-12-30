def n_choose_3(n):
    return n * (n - 1) * (n - 2) / 6


class SolverTest(object):
    def __init__(self, alg, only_count=False):
        self.alg = alg
        self.only_count = only_count

    def count_assert(self, vertices, edges, count):
        count2 = self.alg(vertices, edges, True)
        self.assertEqual(count, count2)

        if not self.only_count:
            triangles = self.alg(vertices, edges)
            self.assertEqual(count, len(triangles))

    def test_empty(self):
        vertices = range(50)
        edges = ()
        self.count_assert(vertices, edges, n_choose_3(50))

    def test_full_3(self):
        vertices = (1, 2, 3)
        edges = ((1, 2), (1, 3), (2, 3))
        self.count_assert(vertices, edges, 1)

    def test_full_50(self):
        vertices = range(50)
        edges = ((i, j) for i in vertices for j in range(i + 1, len(vertices)))
        self.count_assert(vertices, edges, n_choose_3(50))

    def test_1_regular(self):
        vertices = (1, 2, 3, 4, 5)
        edges = ((1, 2), (2, 3), (3, 4), (4, 5), (5, 1))
        self.count_assert(vertices, edges, 0)
