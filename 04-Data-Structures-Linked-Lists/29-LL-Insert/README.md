# 29. LL: Insert

The LinkedList insert method takes an index and a value as its parameters and inserts a node with the value at that index.

From the code, we can see that we must first test that we have a valid index within the bounds of the length of the list and return None if this is not the case.

![Linked List Insert Invalid](./images/linked-list-insert-invalid.jpg?raw=true "Linked List Insert Invalid")

Then the code deals with the edge case of insertion at the start of the list by calling the prepend method. 

![Linked List Insert Prepend](./images/linked-list-insert-prepend.jpg?raw=true "Linked List Insert Prepend")

Then the code deals with the edge case of insertion at the end of the list by calling the append method. 

![Linked List Insert Append](./images/linked-list-insert-append.jpg?raw=true "Linked List Insert Append")

Then the code deals with the main case of insertion in the middle of the list. The code first creates the new node. Then a temp variable is created that points to the node before the index where we are inserting the node. 

![Linked List Insert Temp](./images/linked-list-insert-temp.jpg?raw=true "Linked List Insert Temp")

It needs to be the previous node as we need the next pointer from that node to point to the new node. Before we point the previous node at the new node we first point the new node at the next node in the list.

![Linked List Insert Middle](./images/linked-list-insert-middle.jpg?raw=true "Linked List Insert Middle")

Finally the code increments the length of the list by 1 and returns True.
