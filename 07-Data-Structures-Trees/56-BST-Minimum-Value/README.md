# 56. BST: Minimum Value

The `min_value_node` method takes a *node* as its parameter and returns the node with the minimum value in any *subtree* of the tree. For instance, given the tree below,

![Binary Search Tree](../50-Binary-Search-Trees-Example/images/binary-search-tree.jpg?raw=true "Binary Search Tree")

if we pass it the root node then the method would return the 18 node. However, if we pass it the 76 node then the method would return the 52 node.

Note that in both cases we start from the `current_node` that is passed and we keep visiting the node on the left until we reach a node that does not point at any other node. We then return that leaf node as it's the minimum value node in the subtree. In the case of the root node we have,

![Binary Search Tree Min Value Node](./images/bst-min-value-node.jpg?raw=true "Binary Search Tree Min Value Node")

and in the case of the 76 node we have

![Binary Search Tree Min Value Node 76 Subtree](./images/bst-min-value-node-76.jpg?raw=true "Binary Search Tree Min Value Node 76 Subtree")

We can also see that the code for the `min_value_node` method first deals with the edge case of an empty tree by returning None.
