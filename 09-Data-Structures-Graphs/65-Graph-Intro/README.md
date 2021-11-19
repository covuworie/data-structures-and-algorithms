# 64. Graph: Intro

Now let's take a look at graphs and the terminology associated with them. A graph consists of a *vertices* (or *nodes*) and and *edges* (or *connections*).

### Vertex or Node

A *vertex* contains a value. The proper word is vertex but you will also hear the word *node*.

![Graph Vertex](./images/graph-vertex.jpg?raw=true "Graph Vertex")

### Edge or Connection

An *edge* can connect two vertices. The proper word is edge but you will also hear the word *connection*.

![Graph Edge](./images/graph-edge.jpg?raw=true "Graph Edge")

There is no limit to how many vertices a vertex can connect with.

![Graph Connected](./images/graph-connected.jpg?raw=true "Graph Connected")

### Weighted Edges

In the previous example, if you want to traverse from the 76 vertex to the 82 vertex then it would seem to make more sense to use the edge that directly connects them rather than take two hops via the 44 vertex. However, graphs can have also have *weighted edges*.

![Graph Weighted Edges](./images/graph-weighted-edges.jpg?raw=true "Graph Weighted Edges")

An example of weighted edges would be in a maps app. If the road between 76 and 82 had a lot of traffic you would be better off going the other direction because it has a total cost of 3 + 2 = 5 versus 15. 

### Bidirectional Graph

In Facebook, you are friends with a friend and they are friends with you. This is a bidirectional relationship. In a graph in which all the edges are *bidirectional* you will often see the edges connected like this without arrows.

![Graph Bidirectional Edges](./images/graph-bidirectional-edges.jpg?raw=true "Graph Bidirectional Edges")

### Directectional Graph

In Twitter, when you follow a celebrity, you are following the celebrity but they do not follow you. This is a directional relationship. In a graph in which all the edges are *directional* you will see the edges connected like this with an arrow.

![Graph Directional Edges](./images/graph-directional-edges.jpg?raw=true "Graph Directional Edges")

So to summarize, in a graph the edges can be weighted or unweighted and they can be directional or bidirectional.

## Many Types of Graph

We have already seen a few graphs in this course. A binary tree is a directed graph with the limitation that each node can only point to two other nodes.

![Graph Binary Tree](./images/graph-binary-tree.jpg?raw=true "Graph Binary Tree")

Also when we looked at trees, we mentioned that we had seen a tree before, which was a linked list. Therefore, a linked list is also a directed graph with the limitation that each node can only point to one other node.

![Graph Linked List](./images/graph-linked-list.jpg?raw=true "Graph Linked List")

However, when we think of graphs we typically think of something that looks like this.

![Graph](./images/graph.jpg?raw=true "Graph")


## What is a graph?

A **graph** is a data structure consisting of finite set of *vertices* (also called *nodes*) together with a set of unordered pairs of these vertices for an undirected graph or a set of ordered pairs for a directed graph. These pairs are known as *edges* (also called *connections*).
