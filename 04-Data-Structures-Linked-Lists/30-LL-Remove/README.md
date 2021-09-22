# 30. LL: Remove

The LinkedList remove method takes an index as its parameters and removes the node that index.

From the code, we can see that we must first test that we have a valid index within the bounds of the length of the list and return None if this is not the case. The reason we return None here rather than False (as we did for the insert method) is because if we are successful we will return the node.

![Linked List Remove Invalid](./images/linked-list-remove-invalid.jpg?raw=true "Linked List Remove Invalid")

Then the code deals with the edge case of removing a node at the start of the list by calling the pop first method. 

![Linked List Remove Pop First](./images/linked-list-remove-pop-first.jpg?raw=true "Linked List Remove Pop First")

Then the code deals with the edge case of removing a node at the end of the list by calling the pop method. 

![Linked List Remove Pop](./images/linked-list-remove-pop.jpg?raw=true "Linked List Remove Pop")

Then the code deals with the main case of removal of a node in the middle of the list. The code first creates two variables - a temp variable that points at the node we want to remove and a prev variable that points at the previous node. 

![Linked List Remove Prev Temp](./images/linked-list-remove-prev-temp.jpg?raw=true "Linked List Remove Prev Temp")

We need the prev variable so that we can point the previous node at the node after the one we want to remove. We then break the connection between the node at the index and the next node.

![Linked List Remove Middle](./images/linked-list-remove-middle.jpg?raw=true "Linked List Remove Middle")

Finally the code decrements the length of the list by 1 and returns the node.
