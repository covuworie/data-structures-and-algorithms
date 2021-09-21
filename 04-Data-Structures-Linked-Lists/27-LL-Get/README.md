# 27. LL: Get

The LinkedList get method takes an index as its parameter and returns the node at that index. 

From the code, we can see that we must first test that we have a valid index within the bounds of the length of the list and return None if this is not the case.

![Linked List Get Invalid](./images/linked-list-get-invalid.jpg?raw=true "Linked List Get Invalid")

Then the code deals with the valid case where the index is within the bounds of the list. It points temp to the first node and then loops through the list using a for loop with the index as its range.

![Linked List Get](./images/linked-list-get.jpg?raw=true "Linked List Get")
