# 18. LL: Big O

## What is Big O for the Different Linked List Operations?

Given the linked list below.

![Linked List](./images/linked-list.jpg?raw=true "Linked List")

### Append is 0(1) at the end of a linked list

`append` at the end of a linked list is a simple operation. We point both the last node and tail at the new node.

![Linked List Append End](./images/linked-list-append-end.jpg?raw=true "Linked List Append End")

### Remove or pop at the end of a linked list is 0(n)

`remove` or `pop` requires tail to point to the previous node. The only way to find this node is by starting at head and iterating through the linked list. 

![Linked List](./images/linked-list.jpg?raw=true "Linked List")

### Prepend is 0(1)

`prepend` is a simple operation. We point the new node at the first node and we point head at the new node.

![Linked List Prepend](./images/linked-list-prepend.jpg?raw=true "Linked List Prepend")

### Remove from the start of a linked list is 0(1)

`remove` from the start of a linked list is a simple operation. We point head at the next node and remove the first node.

![Linked List](./images/linked-list.jpg?raw=true "Linked List")

### Insert somewhere in the middle of a linked list is 0(n)

`insert` first requires the new node to point to the next node. The only way to find this node is by starting at head and iterating through the linked list. Then the previous node is also pointed to the new node.

![Linked List Insert](./images/linked-list-insert.jpg?raw=true "Linked List Insert")

### Remove or pop somewhere in the middle of a linked list is 0(n)

`remove` or `pop` first requires the previous node to point to the node to the right of the one to be removed. The only way to find this node is by starting at head and iterating through the linked list. We then remove the node.

![Linked List](./images/linked-list.jpg?raw=true "Linked List")

### Lookup an item by value or by index in the linked list is 0(n)

Looking for an item by value or by index requires starting from head and iteration through the items or their indexes until it is found.  The lookup by index is different from a list which is O(1).

![Linked List Lookup](./images/linked-list-lookup.jpg?raw=true "Linked List Lookup")

#### Linked Lists vs Lists

A Big O comparison table of Linked Lists vs Lists for the different operations can be found in the resources folder. We can make the following observations from the table:

- The performance for most operations is identical.
- *Pop* an item off the end of a list and *Lookup by Index* are better for *Lists*.
- *Prepend* (add) or *Pop First* (remove) an item from the beginning of a list is better for *Linked Lists*. 
