# 10. Big O: O(1)

## What is O(1)?

The efficiency of code is **O(1)** if we get the constant graph *O(n) = 1* when we plot the size of the input n versus O(n). The complexity is said to be constant with the input size n. In other words, as the size of the input n increases the number of operations remains constant.

![Graph of n versus O(1)](./images/graph.jpg?raw=true "n versus O(1)")

From the graph we can see that the line for **O(1)** is completely flat. It is the most efficient Big O possible from a complexity standpoint. Any time code is O(1) that is as optimal as it gets.

#### Example

The `print_items` function ran for 2 operations as there are two additions in it. Technically, the complexity of this function is O(2) since we passed the function an integer input n and it ran 2 operations. However, we simplify and write this as O(1).
