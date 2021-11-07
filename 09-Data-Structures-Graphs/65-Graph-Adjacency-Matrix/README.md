# 65. Graph: Adjacency Matrix

There are two ways we are going to look at representing a graph. The first one will be an **adjacency matrix**. In an adjacency matrix we take each vertex in turn. The row axis represents the actual vertex we are looking at and the column axis represents the vertices that it has an edge with.

## Adjacency Matrix of a Bidirectional Graph

Below we see the adjacency matrix for the following bidirectional graph. We take each vertex in turn and put a one whenever that vertex has an edge with another vertex and a zero otherwise (e.g. A has an edge with B and E).

![Graph Adjacency Matrix Bidirectional](./images/graph-adjacency-matrix-bidirectional.jpg?raw=true "Graph Adjacency Matrix Bidirectional")

Note that the matrix has the following properties:

- It is a *binary* matrix
- The matrix has *zeros on the main diagonal* (as a vertex cannot have an edge with itself)
- It is *symmetric* (as the relationship is bidirectional)

## Adjacency Matrix of a Directional Graph

Let's change the above graph to make it directional by removing the edge that points from B to A. Then the adjacency matrix is now no longer symmetric and now looks like this. 

![Graph Adjacency Matrix Directional](./images/graph-adjacency-matrix-directional.jpg?raw=true "Graph Adjacency Matrix Directional")

## Adjacency Matrix of a Weighted Graph

Below we see the adjacency matrix for the following weighted bidirectional graph. We take each vertex in turn and put the associated weight whenever that vertex has an edge with another vertex and a zero otherwise (e.g. A has an edge with B of weight 2 and E of weight 10).

![Graph Adjacency Matrix Weighted](./images/graph-adjacency-matrix-weighted.jpg?raw=true "Graph Adjacency Matrix Weighted")

