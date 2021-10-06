# 35. DLL: Prepend

From the code, we can see that the DoublyLinkedList prepend method first creates a new node using the Node constructor. First the code deals with the edge case where the list is empty by pointing both head and tail to the new node. 

![Doubly Linked List Prepend Empty](./images/doubly-linked-list-prepend-empty.jpg?raw=true "Doubly Linked List Prepend Empty")

Then it points the new node to the first node and points the first node to the new node. The code then points head to the new node.

![Doubly Linked List Prepend](./images/doubly-linked-list-prepend.jpg?raw=true "Doubly Linked List Prepend")

Finally the code increments the length of the list by 1.

