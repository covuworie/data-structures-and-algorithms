# 33. DLL: Append

From the code, we can see that the DoublyLinkedList append method first creates a new node using the Node constructor. First the code deals with the edge case where the list is empty by pointing both head and tail to the new node. 

![Doubly Linked List Append Empty](./images/doubly-linked-list-append-empty.jpg?raw=true "Doubly Linked List Append Empty")

Then it points the last node to the the new node, the new node to the previous and points tail to the new node.

![Doubly Linked List Append](./images/doubly-linked-list-append.jpg?raw=true "Doubly Linked List Append")

Finally the code increments the length of the list by 1.
