# 71. Graph: Remove Vertex

The job of the `remove_vertex` method is to remove a vertex. However, before the vertex can be removed, all its edges to other vertexes *must* be removed first. Let's say we want to remove vertex D from the following graph. Then we must remove its connections with vertices A, B and C before we remove vertex D itself from the graph.

![Graph](./images/graph.jpg?raw=true "Graph")

We mentioned previously that there is an efficiency that we can use in graphs that have bidirectional connections. The efficiency is contained the the list of edges of the vertex that we wish to remove. For instance, we know if D has an edge with A, then A also has an edge with D. The symmetry also holds true for B and C.

![Graph Remove Vertex Efficiency](./images/graph-remove-vertex-efficiency.jpg?raw=true "Graph Remove Vertex Efficiency")

So in the code you will see a loop over the edge vertices of the vertex that we wish to remove. In each iteration of the loop we remove the edge that this specific edge vertex has with the vertex that we ultimately wish to remove. Finally, we are then able to remove our edge. The result will an adjacency list that looks like this.

![Graph Remove Vertex](./images/graph-remove-vertex.jpg?raw=true "Graph Remove Vertex")

Suppose we had a graph that had a thousand vertices, then we would only have to go through these three to remove edges with D! That is a huge efficiency gain.

The `remove_vertex` method takes the vertex value as its parameter and returns a boolean indicating whether it was successful in removing the vertex. The method first deals with the edge case where the vertex is not in the graph by returning False. 

Then the code deals with the main case by removing the vertex and its edges using the approach described above. Finally the code returns True to indicate success.
