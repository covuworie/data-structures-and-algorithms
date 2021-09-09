# 7. Big O: Drop Constants

## Rule 1: Drop Constants

The first rule to simplify Big O notation tells us to drop constants such that O(kn) where k is an integer constant is O(n).

#### Example

The `print_items` function ran *n + n = 2n* times as there are two identical for loops of size n. Technically the function is O(2n) since we passed the function an integer input n and it ran 2n operations.  However, we simplify this by dropping the constant 2 and simply write this as O(n).
