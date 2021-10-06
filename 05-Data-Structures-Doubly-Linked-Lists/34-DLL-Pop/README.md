# 34. DLL: Pop

Now we will look at what is required to pop a node off the end of a Doubly Linked List. Let's look at it in stages. Our aim is to remove the node item from the list. To do this we will have to break both of its connections with the previous node. We will also have to point tail at the previous node. In order to return the node we will first need a temp variable pointing at it.

![Doubly Linked List Pop End](./images/doubly-linked-list-pop-end.jpg?raw=true "Doubly Linked List Pop End")

Finally the code decrements the length by one and returns the node.

We have the following two edge cases:

1. Empty Linked List

In this case the code returns None.
![Doubly Linked List Empty](./images/doubly-linked-list-pop-end-empty.jpg?raw=true "Doubly Linked List Empty")

2. One Item in the Linked List

In this case the code sets head and tail to None.
![Doubly Linked List One Item](./images/doubly-linked-list-one-item.jpg?raw=true "Doubly Linked List One Item")

