# AAL-GraphTriangles
WIP project

### Given problem
There are n 2D points chosen in a way that no 3 points lay on the same line. Every pair of points is assigned either 0 or 1. Find and list all sets of three points where all the pairs are assigned the same number.
### Core problem
Find and list all triangles (cliques/cycles of size 3) in a given n vertex graph and its complement (inverse) graph.
### Tested algorithms
#### Brute force
Create all possible sets of 3 vertices, for each of them check if they form a triangle in the graph.
#### Divide and conquer
If the graph has 3 vertices, check if they form a triangle. If so, return a set containing the 3 vertices. If not, or if the graph has less vertices, return an empty set.

If the graph has more than 3 vertices, divide the set of vertices in two halves. Consider three graphs - two graphs induced by each of the two halves and a third graph created by taking all of the edges that join the first two graphs (and vertices in these edges).
Perform the algorithm on each of these three graphs, recursively dividing them in the same way.

It's possible that the third graph we get is actually the whole graph, meaning the division didn't simplify the problem at all. In this case, a fallback algorithm must be used.
#### Choose Two
Assume the graph is represented as an adjacency list (each vertex has a list of adjacent vertices).
For each vertex, pick two vertices from its list of neighbors and check if they're connected with each other.

It might be beneficial to remove the vertex after checking its list.
### Speed up strategies
We might be able to speed up each algorithm by first disregarding vertices of degree 1 or 0. This could also be done in multiple iterations as after removing a vertex we might get new vertices of degree 1 or 0.
