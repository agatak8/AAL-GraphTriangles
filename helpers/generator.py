# Agata Kłoss
# znalezienie liczby trójkątów w grafie

from random import randint
from math import log2
from math import cos, sin, pi


def random_points(vertices, width):
    point_dict = {}
    for v in vertices:
        point_dict[v] = (randint(-width, width), randint(-width, width))
    return point_dict


def circular_points(vertices, width):
    n_vertices = len(vertices)
    point_dict = {}
    radius = width // 2
    angle = 0
    for i in vertices:
        x = int(radius * cos(-angle * pi / 180))
        y = int(radius * sin(-angle * pi / 180))
        point_dict[i] = (x, y)
        angle += 360 / n_vertices
    return point_dict


def tree_points(vertices, width, height):
    n_vertices = len(vertices)
    n_levels = int(log2(n_vertices)) + 1
    dy = height // n_levels
    point_dict = {}
    for i in vertices:
        level = int(log2(i + 1))
        n_leaves = 2 ** level
        dx = width // n_leaves
        offset = i - n_leaves + 1
        point_dict[i] = (-width // 2 + dx * offset, -height // 2 + dy * level)
    return point_dict


def full_graph(n_vertices, n_edges=None):
    vertices = list(range(n_vertices))
    all_edges = [(i, j) for i in range(0, n_vertices - 1) for j in range(i + 1, n_vertices)]
    return vertices, all_edges


def k_regular(n_vertices, k):
    vertices = range(n_vertices)
    if k > n_vertices:
        return None, None
    m = k // 2
    edges = set()
    for i in range(0, n_vertices - 1):
        for j in range(1, m + 1):
            edges.add(frozenset({i, (i + j) % n_vertices}))
            edges.add(frozenset({i, (i - j) % n_vertices}))
    if k % 2 == 1:
        if n_vertices % 2 != 0:
            print("If n_vertices is odd, k must be even!")
            return
        else:
            for i in range(0, n_vertices - 1):
                edges.add(frozenset((i, (i + n_vertices // 2) % n_vertices)))
    edges2 = [list(edge) for edge in edges]
    return vertices, edges2


def binary_tree(n_vertices, n_edges=None):
    vertices = range(n_vertices)
    edges = []
    for i in range(1, n_vertices):
        edges.append((i, (i - 1) // 2))
    return vertices, edges


def full_bipartite_graph(n_vertices, n_edges=None):
    n2 = n_vertices // 2
    vertices_1 = list(range(0, n2))
    vertices_2 = list(range(n2, n_vertices))
    all_edges = [(i, j) for i in vertices_1 for j in vertices_2]
    return vertices_1 + vertices_2, all_edges


def bipartite_graph(n_vertices, n_edges):
    vertices, all_edges = full_bipartite_graph(n_vertices)
    if n_edges > len(all_edges):
        return None, None
    edges = []
    for i in range(n_edges):
        edges.append(all_edges.pop(randint(0, len(all_edges) - 1)))
    return vertices, edges


def random_graph(n_vertices, n_edges):
    vertices, all_edges = full_graph(n_vertices)
    if n_edges > len(all_edges):
        return None, None
    edges = []
    for i in range(n_edges):
        edges.append(all_edges.pop(randint(0, len(all_edges) - 1)))
    return vertices, edges
