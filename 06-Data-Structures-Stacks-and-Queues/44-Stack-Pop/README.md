# 44. Stack: Pop

From the code, we can see that the Stack pop method first deals with the edge case where the stack is empty by returning None. 

![Stack Pop Empty](./images/stack-pop-empty.jpg?raw=true "Stack Pop Empty")

Then the code deals with the main case where there are one or more items in the stack. First the code points the temp variable to the top. Then it moves top to the next node. Then the code breaks the link between the node that we want to return and the next node.

![Stack Push](./images/stack-pop.jpg?raw=true "Stack")

Finally the code decrements the height of the list by 1 and returns the node.
