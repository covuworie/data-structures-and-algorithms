# 43. Stack: Push

From the code, we can see that the Stack push method first creates a new node using the Node constructor. First the code deals with the edge case where the stack is empty by pointing top to the new node. 

![Stack Push Empty](./images/stack-push-empty.jpg?raw=true "Stack Push Empty")

Then it points the new node to the top node and points top to the new node.

![Stack Push](./images/stack-push.jpg?raw=true "Stack")

Finally the code increments the height of the list by 1.

