# 82. Insertion Sort: Big O

Now let's look at the Big O for insertion sort. In the code we had a loop within a loop, so obviously the time complexity is O(n<sup>2</sup>), as the worse possible scenario.

However, the best possible scenario is when we have *sorted* or *almost sorted* data like this.

| 1 | 2 | 4 | 3 | 5 | 6 |
|---|---|---|---|---|---|
|   |   |   |   |   |   |

Let's look at the number of operations required to sort this. We can see that the 2, 4, 5 and 6 will be *left in place* as they are already greater than the item before them. So these items will not run the inner loop that compares the item to all the items before it. The 3 is the only item that will run that loop and it will immediately being swapped with the 2 in order to sort the list like this.

| 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|
|   |   |   |   |   |   |

So we can see that in this best case scenario the time complexity is O(n) as we only have to go linearly through each item in the list. 
