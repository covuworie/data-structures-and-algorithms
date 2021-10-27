# 54. BST: Insert - Code

Now it's time to implement the code of the `insert` method based on the pseduocode we wrote last time.

We can see that first we create the new node. Then we deal with the first edge case where we have an empty tree by setting `root` to the new node and returning True:

![Binary Search Tree Insert Empty](./images/binary-search-tree-insert-empty.jpg?raw=true "Binary Search Tree Insert Empty")

We then set `temp` equal to the `root` and initiate the while loop. The way we will break out of the loop is by returning True or False depending on whether we were able to add the node or not. 

Immediately inside the loop, we deal with the second edge case where the new node has a value equal to a node in the tree. In this situation we simply return False: 

![Binary Search Tree Insert Duplicate](./images/binary-search-tree-insert-duplicate.jpg?raw=true "Binary Search Tree Insert Duplicate")

Next we write the code to compare the new node value to the temp node value. If it less then we go left. If the spot to the left is available then we insert the node and return True.

![Binary Search Tree Insert Left Empty](./images/binary-search-tree-insert-left-empty.jpg?raw=true "Binary Search Tree Insert Left Empty")

Otherwise, if the spot is occupied, then we move the temp variable down to that node and repeat the process (run through the loop again). Eventually we will get to a node with a slot available on the left.

![Binary Search Tree Insert Left Filled](./images/binary-search-tree-insert-left-filled.jpg?raw=true "Binary Search Tree Insert Left Filled")

The logic that we write for the right side is similar:

![Binary Search Tree Insert Right](./images/binary-search-tree-insert-right.jpg?raw=true "Binary Search Tree Insert Right")
