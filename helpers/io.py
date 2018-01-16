# Agata Kłoss
# znalezienie liczby trójkątów w grafie

# this library allows converting graphs and triangles to/from their string formats
#
# graph - is a list/tuple with 3 items:
# item 1 - a list/tuple of vertices
# item 2 - a dict that maps vertices to points
# item 3 - a list/tuple of edges
#
# vertex is an int
# point is a tuple of two floats
# edge is a list/tuple of two vertices
#
# triangles - is a list/tuple of triangles where
# a single triangle is a list/tuple of 3 vertices
#
# graph string format:
# n_vertices            (1)
# vertex_nr;x;y         (n_vertices)
# vertex_nr1;vertex_nr2   (0..*)
#
# triangles string format:
# vertex_n1r;vertex_nr2;vertex_nr3 (0..*)
#
# " " is the default separator but any other character/string can be used as well
io_separator = " "


# generate graph out of string
def input_to_graph(input, separator=io_separator):
    # first line - number of vertices
    n_vertices = int(input.readline().strip())
    vertices = range(n_vertices)

    # exactly as many lines as vertices - each line specifies a vertex's coordinates in xy space
    split_coordinate_lines = (line.strip().split(separator) for _, line in
                              zip(range(n_vertices), input))  # generates lists of 3 strings
    vertex_points = tuple((int(list[0]), (float(list[1]), float(list[2]))) for list in
                          split_coordinate_lines)  # tuples with vertex and its coordinates
    if len(vertex_points) != n_vertices:
        raise (ValueError("Amount of vertex coordinate lines doesn't match amount of vertices"))

    # varied amount of lines - each line specifies a unique edge
    split_edge_lines = (line.strip().split(separator) for line in input)  # generates lists of 2 strings
    edges = tuple((int(list[0]), int(list[1])) for list in split_edge_lines)  # vertex pairs
    return vertices, vertex_points, edges


# generate string out of a graph
def graph_to_output(vertices, vertex_points, edges, separator=io_separator):
    v_gen = (separator.join((str(v), str(vertex_points[v][0]), str(vertex_points[v][1]))) for v in vertex_points)
    v = "\n".join(v_gen)
    e_gen = (separator.join((str(edge[0]), str(edge[1]))) for edge in edges)
    e = "\n".join(e_gen)
    return "\n".join((str(len(vertices)), v, e))


# generate triangle list out of string
def input_to_triangles(input, separator=io_separator):
    split_lines = (line.strip().split(separator) for line in input)
    triangles = tuple((int(line[0]), int(line[1]), int(line[2])) for line in split_lines)
    return triangles


# generate string out of triangles
def triangles_to_output(triangles, separator=io_separator):
    result = [tuple(t) for t in triangles]
    return "\n".join(separator.join((str(t[0]), str(t[1]), str(t[2]))) for t in result)
