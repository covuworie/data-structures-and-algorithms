# 47. Queue: Dequeue

From the code, we can see that the Queue dequeue first deals with the first edge case where the queue is empty by returning None. 

![Queue Dequeue Empty](./images/queue-dequeue-empty.jpg?raw=true "Queue Dequeue Empty")

Then the code deals with the second edge case where the queue has one item by pointing first and last to None. 

![Queue Dequeue One](./images/queue-dequeue-one.jpg?raw=true "Queue Dequeue One")

Then the code deals with the main case where there are one or more items in the queue. The code points first at the next node and then breaks the link between the first node and the next.

![Queue Dequeue](./images/queue-dequeue.jpg?raw=true "Queue Dequeue")

Finally the code decrements the length of the list by 1 and returns the node.
