import algorithms.graph


# file - must be in the following format:
# n_vertices            (1)
# vertex_nr;x;y         (n_vertices)
# vertex_nr;vertex_nr   (0..n_vertices choose 2)
#
# separator - allows to optionally use a different character
# than ; to separate values in the file
#
# returns 3 generators:
# vertices - numbers 0 to n_vertices - 1
# vertex_points - tuples of form (int, tuple(float, float)) meaning (vertex, (x, y))
# edges - tuples (int,int) meaning (vertex1, vertex2)
def parse_file(file, separator=';'):
    # first line - number of vertices
    n_vertices = int(file.readline().strip())
    vertices = range(n_vertices)

    # exactly as many lines as vertices - each line specifies a vertex's coordinates in xy space
    split_coordinate_lines = (line.strip().split(separator) for _, line in
                              zip(range(n_vertices), file))  # generates lists of 3 strings
    vertex_points = ((int(list[0]), (float(list[1]), float(list[2]))) for list in
                     split_coordinate_lines)  # generates tuple with vertex and its coordinates

    # varied amount of lines - each line specifies a unique edge
    split_edge_lines = (line.strip().split(separator) for line in file)  # generates lists of 2 strings
    edges = ((int(list[0]), int(list[1])) for list in split_edge_lines)  # generates vertex pairs
    return vertices, vertex_points, edges
