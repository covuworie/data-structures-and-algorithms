# 102. DFS: InOrder - Code

Now let's look at the code for **Depth First Search (DFS) InOrder**. It's important to point out that this is a method in the `BinarySearchTree` class and therefore it takes the `self` keyword as its only parameter.

From the code we can see that it's almost identical to the **PreOrder** and **PostOrder** methods that we wrote previously. With **PreOrder** first we wrote the node value to the `results` list and then we visited the left node and then the right node. With **PostOrder**, first we visit the left node, then we visit the right node and then we write the node value to the `results` list. However, for **InOrder** first we visit the left node, then we write the node value to the `results` list and then we visit the right node. So we have all the same code, it's just in a different order.
