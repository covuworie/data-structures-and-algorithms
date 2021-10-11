# 26. LL: Pop First

From the code, we can see that the LinkedList pop first code deals with the edge case where the list is empty by returning None. 

![Linked List Pop First Empty](./images/linked-list-pop-first-empty.jpg?raw=true "Linked List Pop First Empty")

Then the code deals with the main case where there are at least 2 items in the list. It points temp to the first node, move the head to the second node and then breaks the link between the first and second nodes.

![Linked List Pop First](./images/linked-list-pop-first.jpg?raw=true "Linked List Pop First")

Finally the code increments the length of the list by 1 and deals with the edge case where we have 1 item in the list. head is already pointing at None so we just have to point tail at None.

![Linked List Pop First One](./images/linked-list-pop-first-one.jpg?raw=true "Linked List Pop First One")
