# Agata Kłoss
# znalezienie liczby trójkątów w grafie

import algorithms.graph as graph
import numpy as np


# avg O(n^3), worst O(n^4)
def naive(vertices, edges, only_count=False):
    def sub_solve(graph):
        v = list(vertices)  # O(N)
        results = []
        count = 0
        for i in range(0, len(v)):
            for j in range(i + 1, len(v)):
                for k in range(j + 1, len(v)):
                    # avg O(1), worst case O(n)
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


# best O(n^2.3727), worst O(n^3)
def matrix(vertices, edges, dummy_arg=None):
    vertex_dict = {}
    i = 0
    for v in vertices:
        vertex_dict[v] = i
        i += 1
    m1 = np.matrix(np.zeros((i, i), dtype=np.int))
    for edge in edges:
        v1 = edge[0]
        v2 = edge[1]
        m1[vertex_dict[v1], vertex_dict[v2]] = m1[vertex_dict[v2], vertex_dict[v1]] = 1
    m2 = m1 ^ 1
    for i in range(len(vertices)):
        m2[i, i] = 0
    return int(((m1 ** 3).trace() / 6 + (m2 ** 3).trace() / 6)[0, 0])


# avg O(n^3), worst O(n^4)
def adj_list(vertices, edges, only_count=False):
    def sub_solve(graph):
        results = []
        for v1 in vertices:
            n = list(graph.neighbors(v1))
            for v2 in range(0, len(n) - 1):
                for v3 in range(v2 + 1, len(n)):
                    # avg O(1) worst O(n)
                    if graph.has_edge(n[v2], n[v3]):
                        results.append((v1, n[v2], n[v3]))
            graph.remove_vertex(v1)
        return results

    g1 = graph.AdjacencyList(vertices, edges)
    g2 = g1.get_complement()
    s1 = sub_solve(g1)
    s2 = sub_solve(g2)
    if only_count:
        return len(s1) + len(s2)
    else:
        return s1 + s2


# avg O(n^3), worst O(n^4)
def degree(vertices, edges, only_count=False):
    def sub_solve(graph):
        # O(1)
        def update_neighbor(v):
            v[0][1] -= 1
            index = v[1]
            if index > 0 and vd_list[index - 1][1] > v[0][1]:
                vd_list[index], vd_list[index - 1] = vd_list[index - 1], vd_list[index]

        results = set()
        # O(n)
        vd_list = [[v, graph.degree(v)] for v in graph.vertices()]
        # O(nlgn)
        vd_list.sort(key=lambda x: x[1])
        vd_count = len(vd_list)
        # avg O(n^3), worst O(n^4)
        for i in range(vd_count):
            vd = vd_list.pop(0)
            # O(n)
            neighbors = [(vd_list[i], i) for i in range(0, len(vd_list)) if graph.has_edge(vd[0], vd_list[i][0])]
            if vd[1] >= 2:
                # avg O(n^2), worst O(n^3)
                for v2 in neighbors:
                    if v2[0][1] == 1:
                        continue
                    # avg O(min(deg v1, deg v2)) ~= O(n), worst O(deg v1 * deg v2) ~= O(n^2)
                    common_neighbors = graph.neighbors(vd[0]) & graph.neighbors(v2[0][0])
                    # avg O(n), worst O(n^2)
                    for v3 in common_neighbors:
                        results.add(frozenset((vd[0], v2[0][0], v3)))
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
