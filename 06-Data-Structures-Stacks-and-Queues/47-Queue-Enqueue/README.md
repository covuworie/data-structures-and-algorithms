# 47. Queue: Enqueue

From the code, we can see that the Queue enqueue method first creates a new node using the Node constructor. First the code deals with the edge case where the queue is empty by pointing both first and last to the new node. 

![Queue Enqueue Empty](./images/queue-enqueue-empty.jpg?raw=true "Queue Enqueue Empty")

Then the code deals with the main case where there are one or more items in the queue. The code points the last node at the new node and then points last at the new node.

![Queue Enqueue](./images/queue-enqueue.jpg?raw=true "Queue Enqueue")

Finally the code increments the length of the list by 1.

