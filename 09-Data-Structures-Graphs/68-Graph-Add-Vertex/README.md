# 68. Graph: Add Vertex

The adjacency list is initialized to an empty dictionary in the constructor.

![Graph Constructor](./images/graph-constructor.jpg?raw=true "Graph Constructor")

The job of the `add_vertex` method is to create a vertex like this by adding it to the adjacency list.

![Graph Vertex](./images/graph-vertex.jpg?raw=true "Graph Vertex")

The method takes the vertex value as it parameter and returns a boolean indicating whether it was successful in adding the vertex. The method first deals with the edge case where the vertex is already in the graph by returning False. Then the code deals with the main case by inserting the vertex in the adjacency list with an empty set of edges. Finally the code returns True to indicate success.

![Graph Add Vertex](./images/graph-add-vertex.jpg?raw=true "Graph Add Vertex")
