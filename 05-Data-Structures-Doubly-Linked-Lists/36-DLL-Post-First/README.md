# 36. DLL: Pop First

From the code, we can see that the DoublyLinkedList pop first code deals with the edge case where the list is empty by returning None. 

![Doubly Linked List Pop First Empty](./images/doubly-linked-list-pop-first-empty.jpg?raw=true "Doubly Linked List Pop First Empty")

Then the code deals with the edge case where there is one node in the list by pointing head and tail to None and returning the node through a temp variable that points to it.

![Doubly Linked List Pop First One](./images/doubly-linked-list-pop-first-empty.jpg?raw=true "Doubly Linked List Pop First One")

Then the code deals with the main case where there are at least 2 items in the list. It first points head at the next node. Then breaks both links between the first and second nodes.

![Doubly Linked List Pop First](./images/doubly-linked-list-pop-first.jpg?raw=true "Doubly Linked List Pop First")

Finally the code decrements the length of the list by 1 and returns the node.
