import algorithms.graph as graph
import numpy as np


def naive(vertices, edges, only_count=False):
    def sub_solve(graph):
        v = list(vertices)
        results = []
        count = 0
        for i in range(0, len(v)):
            for j in range(i, len(v)):
                for k in range(i, len(v)):
                    if graph.has_edge(v[i], v[j]) and graph.has_edge(v[i], v[k]) and graph.has_edge(v[j], v[k]):
                        if only_count:
                            count += 1
                        else:
                            results.append({v[i], v[j], v[k]})
        if only_count:
            return count
        else:
            return results

    g1 = graph.AdjacencyList(vertices, edges)
    g2 = g1.get_complement()
    return sub_solve(g1) + sub_solve(g2)


def matrix(vertices, edges, dummy_arg=None):
    m1 = np.zeros(len(vertices), len(vertices))
    for edge in edges:
        v1 = edge[0]
        v2 = edge[1]
        m1[v1][v2] = m1[v2][v1] = 1
    m2 = m1 ^ 1
    return (m1 ** 3).trace() / 6 + (m2 ** 3).trace() / 6


def adj_list(vertices, edges, only_count=False):
    def sub_solve(graph):
        results = set()
        for v1 in graph.vertices():
            n = graph.neighbors(v1)
            for v2 in n:
                for v3 in n:
                    if graph.has_edge(v2, v3):
                        results.add({v1, v2, v3})
        return results

    g1 = graph.AdjacencyList(vertices, edges)
    g2 = g1.get_complement()
    s1 = sub_solve(g1)
    s2 = sub_solve(g2)
    if only_count:
        return len(s1) + len(s2)
    else:
        return s1 | s2


def degree(vertices, edges, only_count=False):
    def sub_solve(graph):
        def update_neighbor(v):
            v[0][1] -= 1
            index = v[1]
            if index > 0 and vd_list[index - 1][1] > v[0][1]:
                vd_list[index], vd_list[index - 1] = vd_list[index - 1], vd_list[index]

        results = set()
        vd_list = [[v, graph.degree(v)] for v in graph.vertices()]
        vd_list.sort(key=lambda x: x[1])
        vd_count = len(vd_list)
        for i in range(vd_count):
            vd = vd_list.pop(0)
            neighbors = [(vd_list[i], i) for i in range(0, len(vd_list)) if graph.has_edge(vd[0], vd_list[i][0])]
            if vd[1] >= 2:
                for v2 in neighbors:
                    if v2[0][1] == 1:
                        continue
                    common_neighbors = graph.neighbors(vd[0]) & graph.neighbors(v2[0][0])
                    for v3 in common_neighbors:
                        results.add({vd[0], v2[0][0], v3})
                    update_neighbor(v2)
            else:
                for v in neighbors:
                    update_neighbor(v)
            graph.remove_vertex(vd[0])
        return results

    g1 = graph.AdjacencyList(vertices, edges)
    g2 = g1.get_complement()
    s1 = sub_solve(g1)
    s2 = sub_solve(g2)
    if only_count:
        return len(s1) + len(s2)
    else:
        return s1 | s2


algs = {"naive": naive, "matrix": matrix, "list": adj_list, "degree": degree}


def solve(vertices, edges, alg_choice, only_count=False):
    return algs[alg_choice](vertices, edges, only_count)
