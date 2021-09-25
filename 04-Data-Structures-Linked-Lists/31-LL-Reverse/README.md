# 31. LL: Reverse

At a high-level the reversed LinkedList swaps head and tail and reverses the direction of every link in the list so it looks like this.

![Linked List Reverse](./images/linked-list-reverse.jpg?raw=true "Linked List Reverse")

From the code, we can see that we must first test if the list has zero or one item and do nothing in this case. Then the next three lines of code point a temp variable at the head and swap the head and tail of the list. 

![Linked List Swap Head Tail](./images/linked-list-swap-head-tail.jpg?raw=true "Linked List Swap Head Tail")

Then the code introduces two more variables, after that points at the node after temp and before that points at the node before temp. Before is required so that we can point the node that temp points to at it. Before is initialzed to None as the first node needs to point at None. After is required so that we can access the next node in the list. The aim is to iterate through the linked list with these three variables as we reverse the links. 

![Linked List Before After](./images/linked-list-before-after.jpg?raw=true "Linked List Before After")

The code then iterates through the entire length of the linked list, pointing after at the next node and flipping the direction of the node arrow by pointing temp.next at before.  

![Linked List Reverse Traverse](./images/linked-list-reverse-traverse.jpg?raw=true "Linked List Reverse Traverse")

You can see that there is now a gap between the 11 and the 3 nodes. So you have to make sure that the linked list never breaks in such a way that you can't get to a node across that gap. That is what the after variable is there for.

Finally inside the loop we move before up one node by pointing it at temp and move temp up one node by pointing it at after.

![Linked List Before Temp](./images/linked-list-before-temp.jpg?raw=true "Linked List Before Temp")

All four lines inside the loop have to be in exactly that order. After has to be moved over before the gap is created when the direction of the node is flipped. Then before must be moved up to temp before temp is moved across the gap.
