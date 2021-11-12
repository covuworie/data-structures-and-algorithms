# 70. Graph: Remove Edge

The job of the `remove_edge` method is to remove an edge between two vertices like this by deleting the appropriate edge from the adjacency list.

![Graph Edge](./images/graph-remove-edge.jpg?raw=true "Graph Edge")

The method takes the two vertex values as its parameters and returns a boolean indicating whether it was successful in removing the edge. The method first deals with the edge case where one of the vertices is not in the graph by returning False. 

Then the code deals with the main case by removing each vertex in the set of edges of the other vertex. Finally the code returns True to indicate success.

Note that the set `discard` method is used instead of the `remove` method as it does not throw an exception when the item does not exist in the set. From the test code you can see from the last two `remove_edge` calls that we are returning True when the edge does not exist.
