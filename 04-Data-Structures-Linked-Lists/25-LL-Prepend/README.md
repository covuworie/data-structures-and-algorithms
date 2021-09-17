# 25. LL: Prepend

From the code, we can see that the LinkedList prepend method first creates a new node using the Node constructor. First the code deals with the edge case where the list is empty by pointing both head and tail to the new node. 

![Linked List Prepend Empty](../22-LL-Append/images/linked-list-append-empty.jpg?raw=true "Linked List Prepend Empty")

Then it points the new node to the first node and points head to the new node.

![Linked List Prepend](./images/linked-list-prepend.jpg?raw=true "Linked List Prepend")

Finally the code increments the length of the list by 1.

