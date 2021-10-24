# 53. BST: Insert - Intro

Let's look at the steps (pseudo-code) we need to create the `insert` method by looking at how we insert the 27 node into this binary search tree.

![Binary Search Tree Insert](./images/binary-search-tree-insert.jpg?raw=true "Binary Search Tree Insert")

- Create `new_node`
- Compare `new_node` to the root node. If it's less than this value we will go left, if it's greater than we will go right.

![Binary Search Tree Insert Left Right](./images/binary-search-tree-insert-left-right.jpg?raw=true "Binary Search Tree Insert Left Right")

Obviously we will go left in this situation. 

- There are two possibilities. If there isn't a node in that position we just insert the node. But if there is a node then we need to move down to the next node and do the whole process of comparison again.

![Binary Search Tree Insert Next](./images/binary-search-tree-insert-next.jpg?raw=true "Binary Search Tree Insert Next")

Obviously in doing this comparison we will go to the right and find that there is no node in this position and insert it.

- As we repeated the two lines of code that are doing the comparison for both the 47 and 21 node we can see that they need to be inside of a loop. And because we do not know how many times we will be iterating through the tree this must be a `while` loop. Note that we also had a variable that was pointing to the node that we were comparing the new node to, we will call this *temp*. This must be initialized to the *root* variable before we even enter the loop.

![Binary Search Tree Insert Loop](./images/binary-search-tree-insert-loop.jpg?raw=true "Binary Search Tree Insert Loop")

These steps cover most of our situations, however we have the following two edge cases

1. An empty tree. If this happens then we will just set root equal to the new node. Note that we do not need to go through the loop in this situation and we do not need the temp variable.

![Binary Search Tree Insert Empty](./images/binary-search-tree-insert-empty.jpg?raw=true "Binary Search Tree Insert Empty")

2. A tree that has one of its node values equal to the new node. 

![Binary Search Tree Insert Duplicate](./images/binary-search-tree-insert-duplicate.jpg?raw=true "Binary Search Tree Insert Duplicate")

We cannot have duplicate values as the code only goes left or right depending on the new node value being lower or higher than the comparison node. In this case we will just return False.

![Binary Search Tree Insert Duplicate Code](./images/binary-search-tree-insert-duplicate-code.jpg?raw=true "Binary Search Tree Insert Duplicate Code")
