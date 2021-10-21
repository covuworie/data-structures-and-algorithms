# 51. BST: Big O

## How Many Nodes are in the BST?

The number of nodes in a Binary Search Tree is 2<sup>n</sup> - 1 where n is the depth (number of levels) of the tree. 

![Binary Search Tree Number of Nodes](./images/binary-search-tree-num-nodes.jpg?raw=true "Binary Search Tree Number of Nodes")

An n grows large the constant 1 becomes insignificant we can approximately say that the size of the tree is 2<sup>n</sup>.

## How Many Operations Does it Take to Find a Node in the BST?

It takes n operations (i.e. steps) to find an item in the BST where n is the depth of the tree.

![Binary Search Tree Number of Operations](./images/binary-search-tree-num-ops.jpg?raw=true "Binary Search Tree Number of Operations")


## What is O(n) for a BST?

We had 2<sup>n</sup> nodes in the tree and it took n operations to *find* a node by value. It's also n operations to *insert* or *remove* a node. In all these cases we have to iterate through each of these steps in the tree. So **O(n) = log(n)** for each of the operations in a BST. The BST operations are very efficient.

![Binary Search Tree O(n)](./images/binary-search-tree-O(n).jpg?raw=true "Binary Search Tree O(n)")


## Divide and Conquer for a BST

Recall that a time complexity of O(n) is achieved by doing *divide and conquer*. Let's see how this is achieved by looking for the 49 node again. We start at the root node, then we go right. In doing this we never have to look at any of the nodes on the left side of the tree. We are effectively removing them from the search.

![Binary Search Tree Divide and Conquer First](./images/binary-search-tree-divide-first.jpg?raw=true "Binary Search Tree Divide and Conquer First")

From here we go left and now we have made it where half of the nodes on the right of the 76 we don't have to look at in the search.

![Binary Search Tree Divide and Conquer Second](./images/binary-search-tree-divide-second.jpg?raw=true "Binary Search Tree Divide and Conquer Second")

We continue doing this until we find the node we are looking for.

## What is best, average and worst case for different BSTs?

So far we have used a *perfect tree* for our Big O time complexity examples. A perfect tree will give the best possible scenario. Remember we measured this with $\Omega$. However, we are more likely to see a tree that looks like this.

![Binary Search Tree Not Perfect](./images/binary-search-tree-not-perfect.jpg?raw=true "Binary Search Tree Not Perfect")

Even in this case we would still say the time complexity is roughly O(n).

Let's look at the worst case scenario now. This is the scenario where the tree never forks and continues in a straight line.

![Binary Search Tree Straight](./images/binary-search-tree-straight.jpg?raw=true "Binary Search Tree Straight")

The complexity is O(n) and this is essentially equivalent to a linked list! Technically this is the time complexity of a binary search tree as its the worst case scenario. However, we assume that the tree always forks and we treat it as an O(log n) data structure.

## BST vs Linked List O(n)

Recall that remove and lookup are O(n) for a linked list. However, insert is O(1) as the node is just appended to the end (we do not care about the sorting of the data in this scenario). So we can see that a BST is better than a linked list for lookup and remove but not for insert.

![Binary Search Tree vs Linked List O(n)](./images/binary-search-tree-vs-linked-list.jpg?raw=true "Binary Search vs Linked List O(n)")

The same is true for a list versus a BST. The only difference that would arise is if instead we wanted to lookup by index where a list is O(1).
