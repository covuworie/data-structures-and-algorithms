# 39. DLL: Insert

The DoublyLinkedList insert method takes an index and a value as its parameters and inserts a node with the value at that index.

From the code, we can see that we must first test that we have a valid index within the bounds of the length of the list and return None if this is not the case.

![Doubly Linked List Insert Invalid](./images/doubly-linked-list-insert-invalid.jpg?raw=true "Doubly Linked List Insert Invalid")

Then the code deals with the edge case of insertion at the start of the list by calling the prepend method. 

![Doubly Linked List Insert Prepend](./images/doubly-linked-list-insert-prepend.jpg?raw=true "Dobly Linked List Insert Prepend")

Then the code deals with the edge case of insertion at the end of the list by calling the append method. 

![Doubly Linked List Insert Append](./images/doubly-linked-list-insert-append.jpg?raw=true "Doubly Linked List Insert Append")

Then the code deals with the main case of insertion in the middle of the list. The code first creates the new node. Then a before variable is created that points to the node before the index where we are inserting the node. And an after variable is created that points to next node. 

![Doubly Linked List Insert Before Atfer](./images/doubly-linked-list-insert-before-after.jpg?raw=true "Doubly Linked List Insert Before After")

We need variables before and after so we can redirect the 4 arrows to insert the new node.

![Doubly Linked List Insert Redirect](./images/doubly-linked-list-insert-redirect.jpg?raw=true "Doubly Linked List Insert Redirect")

We do the redirection of the 4 arrows with the following code.

![Doubly Linked List Insert Middle](./images/doubly-linked-list-insert-middle.jpg?raw=true "Doubly Linked List Insert Middle")

Finally the code increments the length of the list by 1 and returns True.
