# 67. Graph: Big O

Let's compare and contrast the *space and time complexity* of the *adjacency matrix* and *adjacency list* representations of a graph by looking at the same bidirectional graph we have seen previously.

![Graph](./images/graph.jpg?raw=true "Graph")

As we saw previously, it can be represented by the following adjacency matrix and adjacency list.

![Graph Adjacency Matrix and List](./images/graph-adjacency-matrix-and-list.jpg?raw=true "Graph Adjacency Matrix and List")


## Space Complexity

An adjacency list stores each vertex and *only* the edges this vertex has with other vertices. On the other hand, an adjacency matrix stores each vertex and *all* relationships it has to others vertices (including itself).

![Graph Adjacency Matrix and List A](./images/graph-adjacency-matrix-and-list-a.jpg?raw=true "Graph Adjacency Matrix and List A")

The adjacency list has space complexity O(|V| + |E|) where |V| is the *number of vertices* and |E| is the *number of edges*. On the other hand, the adjacency matrix has space complexity O(|V|<sup>2</sup>). So we can see that the adjacency list is more efficient in terms of space complexity.

![Graph Space Complexity](./images/graph-space-complexity.jpg?raw=true "Graph Space Complexity")

## Time Complexity

Now let's look at the Big O time complexity for the common operations for a graph.

### Add Vertex

Let's add a new vertex **F**. For an adjacency list, to add a vertex we simply have to insert a new key with an empty value. This is O(1). For an adjacency matrix it is much more complex as we have to insert a new column and a new row both full of zeros. Essentially the matrix has to be rewritten so this is O(|V|<sup>2</sup>). This is a huge efficiency advantage for an adjacency list.

![Graph Add Vertex Time Complexity](./images/graph-add-vertex-time-complexity.jpg?raw=true "Graph Add Vertex Time Complexity")

### Add Edge

Let's add a new edge **B-F**. For an adjacency list, to add an edge we simply have to append the value to the end of the list for the two vertex keys. This is O(1). For an adjacency matrix we simply have to set a<sub>ij</sub> = a<sub>ji</sub> = 1 at the appropriate (i,j) cell. This is also O(1). There is no clear winner in this scenario.

![Graph Add Edge Time Complexity](./images/graph-add-edge-time-complexity.jpg?raw=true "Graph Add Edge Time Complexity")

### Remove Edge

Let's now remove the edge **B-F**. For an adjacency list, to remove an edge we have to loop through the values in the list for the two vertex keys. When we find the vertex then we will delete it. This is O(|E|). For an adjacency matrix we simply have to set a<sub>ij</sub> = a<sub>ji</sub> = 0 at the appropriate (i,j) cell. This is O(1). This is an efficiency advantage for an adjacency matrix.

![Graph Remove Edge Time Complexity](./images/graph-remove-edge-time-complexity.jpg?raw=true "Graph Remove Edge Time Complexity")

### Remove Vertex

Let's now remove the vertex **F**. For an adjacency list, to remove a vertex we have to delete its key and we also have to remove all of it's edges. So we have to loop through the values of every other vertex key and delete it from those locations. This is O(|V| + O|E|). However, there are bidirectional connections and we will see there is a way to make this more efficient. For an adjacency matrix we delete the corresponding row and column. Again this is basically rewriting the entire matrix. This is O(|V|<sup>2</sup>). This is an efficiency advantage for the adjacency list.

![Graph Remove Node Time Complexity](./images/graph-remove-node-time-complexity.jpg?raw=true "Graph Remove Node Time Complexity")

## Adjacency Matrix Sparsity

We mentioned before that in an adjacency matrix we are storing a lot of redundant information as we store the zeros. This is not a big deal in small matrices like this.

![Graph Adjacency Matrix Sparse](./images/graph-adjacency-matrix-sparse.jpg?raw=true "Graph Adjacency Matrix Sparse")

However, if the matrix gets large then that's a lot of wasted memory. Imagine if it was Facebook who has a billion users and the matrix was storing the friendship relationship. That would be a billion by billion matrix! Let's say at most a person has 1000 friends then you would be storing 1 million zeros for every one. So it's incredibly inefficient from a storage perspective. 

Whereas with an adjacency list we don't have to store all those zeros. So this is what we are going to use in this course. It is much simpler and it is much more efficient.

**Note**: There is another approach not mentioned in the course. We actually don't need to store all those zeros if we use a [sparse matrix](https://en.wikipedia.org/wiki/Sparse_matrix) instead! This can actually give you the best of both worlds as [adjacency matrices can make some problems easier](https://stackoverflow.com/a/22598035). 
