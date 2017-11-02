import algorithms.graph


# file format:
# n
# vi,vj
# vk,vl
# ..... .....
# etc. etc.
def edge_file_to_tuple(file, separator=' '):
    return int(file.readline().strip()), [edge.strip().split(separator) for edge in file]


def tuple_to_graph(t):
    vertices = range(0, t[0])
    edges = set(t[1])
    return algorithms.graph.Graph(vertices, edges)
