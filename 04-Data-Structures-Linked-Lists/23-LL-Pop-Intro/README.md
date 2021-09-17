# 23. LL: Pop Intro

Now we will look at what is required to pop an item off the end of a Linked List. It is a more complicated operation so let's look at it in stages. Our aim is to remove the last item from the list and return it and point tail to the previous item and its value to None. 

![Linked List Pop End](./images/linked-list-pop-end.jpg?raw=true "Linked List Pop End")

We have the following two edge cases:

1. Empty Linked List

![Linked List Empty](./images/linked-list-empty.jpg?raw=true "Linked List Empty")

2. One Item in the Linked List

![Linked List One Item](./images/linked-list-one-item.jpg?raw=true "Linked List One Item")

which are simple enough. 

However, the main case is more complicated as we need to point tail at the previous node. The only way to get to that node is by iterating through the nodes. We will need two variables, `pre` and `temp`. We will initalize both to the first node. Then we will iterate through the nodes asking if temp.next is None. If it isn't then we move temp to the next node and set temp to pre. Eventually we will get to the end of the list where temp.next is None and pre will be pointing at the previous node. 

![Linked List Iteration](./images/linked-list-iteration.jpg?raw=true "Linked List Iteration")

We will set tail to pre and we will return the node that temp is pointing at.

![Linked List Pop End Temp](./images/linked-list-pop-end-temp.jpg?raw=true "Linked List Pop End Temp")
