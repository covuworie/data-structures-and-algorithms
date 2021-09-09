# 9. Big O: Drop Non-Dominants

## Rule 2: Drop Non-Dominants

The second rule to simplify Big O notation tells us to drop non-dominant terms.

The main thing we are concerned with is what happens as n grows large. As a proportion of the total number of operations, non-dominant (i.e. lower order) terms become insignificant.


#### Example

The `print_items` function ran *n * n = n<sup>2</sup>* operations for the nested loops indexed by i and j and then another n operations for the loop indexed by k. Technically the function is O(n<sup>2</sup> + n) since we passed the function an integer input n and it ran *n<sup>2</sup> + n* operations.  However, we simplify this by dropping the non-dominant term n and simply write this as O(n<sup>2</sup>).
