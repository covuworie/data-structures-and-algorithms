# 37. DLL: Get

The DoublyLinkedList get method takes an index as its parameter and returns the node at that index. 

The code that we wrote previously for the LinkedList would also work in this case. 

![Linked List Get](./images/linked-list-get.jpg?raw=true "Linked List Get")

However, we can make it more efficient for a doubly linked list by taking advantage of the fact that we have arrows pointing in both directions. If the node we are looking for is in the first half of the list then we start iterating from the head. 

![Doubly Linked List Get First Half](./images/doubly-linked-list-get-first-half.jpg?raw=true "Doubly Linked List Get First Half")

The code looks like this.

![Doubly Linked List Get First Half Code](./images/doubly-linked-list-get-first-half-code.jpg?raw=true "Doubly Linked List Get First Half Code")

Otherwise we start iterating from the tail until we reach the node at the specified index.

![Doubly Linked List Get Second Half](./images/doubly-linked-list-get-second-half.jpg?raw=true "Doubly Linked List Get Second Half")

The code looks like this.

![Doubly Linked List Get Second Half Code](./images/doubly-linked-list-get-second-half-code.jpg?raw=true "Doubly Linked List Get Second Half Code")

Notice the difference in the arguments passed to the range function.
