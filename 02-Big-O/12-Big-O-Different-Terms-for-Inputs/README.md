# 11. Big O: Different Terms for Inputs

## What is Different Terms for Inputs?

#### Example

In previous sections the `print_items` function ran over two for loops with an input of size n. We determined that the complexity was O(n + n) = 2n and we dropped the constant to get O(n).

Now the `print_items` function takes two input parameters a and b. The first for loop runs for a operations and the second for loop for b operations. So the complexity is O(a) + O(b) = O(a + b). This cannot be simplified further as a and b are two different input sizes.

Similarly if the for loops were instead nested then the complexity would be O(a) * O(b) = O(a * b) which also cannot be simplified further.
