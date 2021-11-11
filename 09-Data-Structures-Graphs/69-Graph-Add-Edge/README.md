# 69. Graph: Add Edge

The job of the `add_edge` method is to create an edge between two vertices like this by adding the appropriate edge to the adjacency list.

![Graph Edge](./images/graph-edge.jpg?raw=true "Graph Edge")

The method takes the two vertex values as its parameters and returns a boolean indicating whether it was successful in adding the edge. The method first deals with the edge case where one of the vertices is not in the graph by returning False. 

Then the code deals with the main case by inserting each vertex in the set of edges of the other vertex. Finally the code returns True to indicate success.
