# AAL-GraphTriangles
WIP project

### Given problem
There are n 2D points chosen in a way that no 3 points lay on the same line. Every pair of points is assigned either 0 or 1. Find and list all sets of three points where all the pairs are assigned the same number.
### Core problem
Find the number of / list all triangles (cliques/cycles of size 3) in a given n vertex graph and its complement (inverse) graph.
### Tested algorithms
#### Matrix
Let A be the adjacency matrix of the graph. The number of triangles is then trace(A^3)/3!.
#### Naive
For each 3 vertices check if they're all connected with each other.
#### Adjacency list
For each vertex, create a list of its neighbors. For each vertex check each pair of its neighbors - if they have an edge, the vertex and the pair form a triangle.

It might be beneficial to remove the vertex after checking its list.
#### Degree-oriented adjacency list
For each vertex, create a list of its neighbors.
Make a list of pairs (vertex, degree(vertex)) sorted by the degrees.
Take the vertex with the smallest degree.
If its degree is >= 2, follow the same steps as in the plain Adjacency list method to find its triangles.
Then, or if its degree is < 2, remove it from the graph and update its neighbors' data and positions in the sorted list.
Repeat until no vertices are left.
