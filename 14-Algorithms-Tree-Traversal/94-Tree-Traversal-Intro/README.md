# 94. Tree Traversal: Intro

## What is Tree Traversal?

Let's look at an overview of tree traversal. So what exactly is tree traversal? A **tree traversal** algorithm visits *every* node in the tree, puts the values in a list and returns that list.

Tree traversal is a little more complicated than traversing a data structure like a *linked list* where the traversal is *linear* since you simply start at the head and iterate through each node until you reach the tail. Tree traversal is *non-linear* as there are multiple ways to visit each node.

### Breadth First Search (BFS)

We could start at the root node like this,

![Tree Traversal BFS Root](./images/tree-traversal-bfs-root.jpg?raw=true "Tree Traversal BFS Root")

and then visit the next row starting at the leftmost node like this,

![Tree Traversal BFS First Row](./images/tree-traversal-bfs-row-1.jpg?raw=true "Tree Traversal BFS First Row")

and then the next row starting at the leftmost node like this.

![Tree Traversal BFS Done](./images/tree-traversal-done.jpg?raw=true "Tree Traversal BFS Done")

This is called **Breadth First Search (BFS)**.

### Depth First Search (DFS)

Another approach is top start all the way at the leftmost leaf node like this,

![Tree Traversal DFS Leaf Left](./images/tree-traversal-dfs-leaf-left.jpg?raw=true "Tree Traversal DFS Leaf Left")

and then move up to the parent node and then come down to the right child node like this,

![Tree Traversal DFS Row 2](./images/tree-traversal-dfs-row-2.jpg?raw=true "Tree Traversal DFS Row 2")

and then come up to the root node like this,

![Tree Traversal DFS Root](./images/tree-traversal-dfs-root.jpg?raw=true "Tree Traversal DFS Root")

and then go all the way to the leftmost leaf node of the nodes remaining like this,

![Tree Traversal DFS Leaf Right](./images/tree-traversal-dfs-leaf-right.jpg?raw=true "Tree Traversal DFS Leaf Right")

and then move up to the parent node and then come down to the right child node like this,

![Tree Traversal DFS Done](./images/tree-traversal-done.jpg?raw=true "Tree Traversal DFS Done")

This is called **Depth First Search (DFS)**. We will look at 3 different ways of doing depth first search.
