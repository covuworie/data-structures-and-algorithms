# 8. Big O: O(n<sup>2</sup>)

## What is O(n<sup>2</sup>)?

The efficiency of code is **O(n<sup>2</sup>)** if we get the quadratic graph *O(n) = n<sup>2</sup>* when we plot the size of the input n versus O(n). The complexity is said to vary quadratically with the input size n.

![Graph of n versus O(n^2)](./images/graph.jpg?raw=true "n versus O(n^2)")

From the graph we can see that the line for **O(n<sup>2</sup>)** is much steeper than for **O(n)**. This means that it is a lot less efficient from a complexity standpoint.

#### Example

The `print_items` function ran for *n * n = n<sup>2</sup>* operations as there are two loops of size n and one is nested inside the other. The complexity of this function is O(n<sup>2</sup>) since we passed the function an integer input n and it ran n<sup>2</sup> operations.

If we took this one level further and nested another for loop with index k &isin; [0,n) inside the other two loops then the function would run for *n * n * n = n<sup>3</sup>* operations. Technically the complexity of function is O(n<sup>3</sup>) since we passed the function an integer input n and it ran n<sup>3</sup> operations. Taking this further, for any integer m where m &ge; 2 if we nest m loops, then technically the complexity would be O(n<sup>m</sup>) However, we simplify and write all of these as O(n<sup>2</sup>).
