# 22. LL: Append

From the code, we can see that the LinkedList append method first creates a new node using the Node constructor. First the code deals with the edge case where the list is empty by pointing both head and tail to the new node. 

![Linked List Append Empty](./images/linked-list-append-empty.jpg?raw=true "Linked List Append Empty")

Then it points the last node to the the new node and points tail to the new node.

![Linked List Append](./images/linked-list-append.jpg?raw=true "Linked List Append")

Finally the code increments the length of the list by 1.
