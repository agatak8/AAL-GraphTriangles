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
    radius = width//2
    angle = 0
    for i in vertices:
        x = int(radius*cos(-angle*pi/180))
        y = int(radius*sin(-angle*pi/180))
        point_dict[i] = (x,y)
        angle += 360/n_vertices
    return point_dict


def full_graph(n_vertices):
    vertices = list(range(n_vertices))
    all_edges = [(i, j) for i in range(0, n_vertices - 1) for j in range(i + 1, n_vertices)]
    return (vertices, all_edges)


def k_regular(n_vertices, k):
    vertices = range(n_vertices)
    m = k // 2
    edges = set()
    for i in range(0, n_vertices - 1):
        cnt = 0
        for j in range(1, m + 1):
            edges.add(frozenset({i, (i + j) % n_vertices}))
            edges.add(frozenset({i, (i - j) % n_vertices}))
    if (k % 2 == 1):
        if (n_vertices % 2 != 0):
            print("If n_vertices is odd, k must be even!")
            return
        else:
            for i in range(0, n_vertices - 1):
                edges.update(frozenset((i, i + n_vertices / 2)))
    edges2 = [list(edge) for edge in edges]
    return (vertices, edges2)


def binary_tree(n_vertices):
    vertices = range(n_vertices)
    edges = []
    for i in range(1, n_vertices):
        edges.append((i, int(log2(i+1)-1)))
    return (vertices, edges)


def full_bipartite_graph(n_vertices):
    n2 = n_vertices // 2
    vertices_1 = list(range(0, n2))
    vertices_2 = list(range(n2, n_vertices))
    all_edges = [(i, j) for i in vertices_1 for j in vertices_2]
    return (vertices_1 + vertices_2, all_edges)


def bipartite_graph(n_vertices, n_edges):
    vertices, all_edges = full_bipartite_graph(n_vertices)
    edges = []
    for i in range(n_edges):
        edges.append(all_edges.pop(randint(0, len(all_edges))))


def random_graph(n_vertices, n_edges):
    vertices, all_edges = full_graph(n_vertices)
    edges = []
    for i in range(n_edges):
        edges.append(all_edges.pop(randint(0, len(all_edges) - 1)))
    return (vertices, edges)
