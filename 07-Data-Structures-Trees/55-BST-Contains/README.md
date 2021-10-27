# 55. BST: Contains

The `contains` method takes a *value* as its parameter and returns a boolean indicating whether the value is in the tree or not. For instance, given the tree below, if we were looking for the number 27 then the method would return True. If we were looking for the number 17 then that would return False.

![Binary Search Tree](../50-Binary-Search-Trees-Example/images/binary-search-tree.jpg?raw=true "Binary Search Tree")

The psuedocode for the contains method looks like this:

![Binary Search Tree Contains Pseudocode](./images/binary-search-tree-contains-pseudocode.jpg?raw=true "Binary Search Tree Contains Pseudocode")

We can see that the code for the `contains` method first deals with the edge case of an empty tree by returning False:

![Binary Search Tree Contains Empty](./images/binary-search-tree-contains-empty.jpg?raw=true "Binary Search Tree Contains Empty")

We then set `temp` equal to the `root` and initiate the while loop. The way we will break out of the loop is by returning True or False depending on whether we find the value or not. 

Next we write the code to compare the value we are looking for to the temp node value. If it less than we go left. If its greater than we go right. If it's equal to then we have found our value and we return True.

![Binary Search Tree Contains](./images/binary-search-tree-contains.jpg?raw=true "Binary Search Contains")

If the value is not in the tree then that breaks us out of the loop and we return False. Note that the edge case of an empty tree skips the while loop entirely and returns False.
