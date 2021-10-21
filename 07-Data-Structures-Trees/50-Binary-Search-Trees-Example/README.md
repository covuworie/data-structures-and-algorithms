# 50. Binary Search Trees: Example

## Example

In order for a binary tree to be a **Binary Search Tree** then its nodes must be laid out in a very particular way. Let's look at an example now.

Suppose we have one node in our tree and we wish to add a second node. With a binary search tree, if the number is greater than the node then it goes to the right, if it is less than then it goes to the left of the node.

![Binary Search Tree Greater Node](./images/binary-search-tree-greater-node.jpg?raw=true "Binary Search Tree Greater Node")

Now let's take a look at another node. We are always going to start by comparing it to the root node. The 52 is greater than 47 so it's going to go to the right. However, there is already a node there. So now we are going to compare the 52 to the 76 node. Beacause it's less than 76 it will go to the left of that node.

![Binary Search Tree Greater Lesser Node](./images/binary-search-tree-greater-lesser-node.jpg?raw=true "Binary Search Tree Greater Lesser Node")

Now let's look at another node. The 21 node is less than the 47 and because the spot to the left of the 47 is open, it will go there.

![Binary Search Tree Lesser Node](./images/binary-search-tree-lesser-node.jpg?raw=true "Binary Search Tree Lesser Node")

We can continue like this building out our binary search tree until we get something like this.

![Binary Search Tree](./images/binary-search-tree.jpg?raw=true "Binary Search Tree")


## What is a Binary Search Tree?

A **Binary Search Tree** is a *binary tree* where if you take any node in the tree, all nodes below it to the right are greater than it 

![Binary Search Tree Right](./images/binary-search-tree-right.jpg?raw=true "Binary Search Tree Right")

and all nodes to the left are smaller than it.

![Binary Search Tree Left](./images/binary-search-tree-left.jpg?raw=true "Binary Search Tree Left")
