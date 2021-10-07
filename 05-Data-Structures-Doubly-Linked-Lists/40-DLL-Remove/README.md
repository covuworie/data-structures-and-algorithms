# 40. DLL: Remove

The DoublyLinkedList remove method takes an index as its parameters and removes the node at that index.

From the code, we can see that we must first test that we have a valid index within the bounds of the length of the list and return None if this is not the case. The reason we return None here rather than False (as we did for the insert method) is because if we are successful we will return the node.

![Doubly Linked List Remove Invalid](./images/doubly-linked-list-remove-invalid.jpg?raw=true "Doubly Linked List Remove Invalid")

Then the code deals with the edge case of removing a node at the start of the list by calling the pop first method. 

![Doubly Linked List Remove Pop First](./images/doubly-linked-list-remove-pop-first.jpg?raw=true "Doubly Linked List Remove Pop First")

Then the code deals with the edge case of removing a node at the end of the list by calling the pop method. 

![Doubly Linked List Remove Pop](./images/doubly-linked-list-remove-pop.jpg?raw=true "Doubly Linked List Remove Pop")

Then the code deals with the main case of removal of a node in the middle of the list. The code first creates a temp variable that points at the node we want to remove. Then similarly to the insert method you could create before and after variables and redirect the two nodes to point before and after at one another. This way is actually easier to read and the recommended way of doing it.

![Doubly Linked List Remove Before After](./images/doubly-linked-list-remove-before-after.jpg?raw=true "Doubly Linked List Remove Before After")

However, this can also be done in a different way by using only the temp variable. 

![Doubly Linked List Remove Redirect](./images/doubly-linked-list-remove-redirect.jpg?raw=true "Doubly Linked List Remove Redirect")

The code then breaks the links between the node we wish to remove and the nodes before and after it.

![Doubly Linked List Remove Redirect None](./images/doubly-linked-list-remove-redirect-none.jpg?raw=true "Doubly Linked List Remove Redirect None")


Finally the code decrements the length of the list by 1 and returns the node.
