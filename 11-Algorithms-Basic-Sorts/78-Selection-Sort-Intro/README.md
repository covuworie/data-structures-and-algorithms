# 78. Selection Sort: Intro

Now we are going to look at our second sorting algorithm - **selection sort**. In the next lesson we will actually code it.

## How does Selection Sort Work?

Let's assume we need to sort the following unsorted list in ascending order.

| 4 | 2 | 6 | 5 | 1 | 3 |
|---|---|---|---|---|---|
| 0 | 1 | 2 | 3 | 4 | 5 |

This is the same list we saw for the bubble sort. The only difference is we have added the indices to the bottom of each list element as we will also need these.

It is convenient to view the values in a bar chart instead to compare the relative sizes. In selection sort we always start with the first item in the list and we keep track of the *index* where the *minimum value* is. 

![Selection Sort Min Index](./images/selection-sort-min-index.jpg?raw=true "Selection Sort Min Index")

We will then have a for loop which starts at the next item over and we will compare the value of this item to the value of the item at the minimum index. If it is less than that value then we will assign its index as the minimum index like this.

![Selection Sort Min Index 1](./images/selection-sort-min-index-1.jpg?raw=true "Selection Sort Min Index 1")

We are then just going to move across the list doing the same comparison. In this case we will have a `min_index = 4` (corresponding the value of 1). We will then swap this value with the first value so that value of 1 at the index of 0 is now sorted like this.

![Selection Sort Compare Swap](./images/selection-sort-compare-swap.jpg?raw=true "Selection Sort Compare Swap")

We then go to the next item in the list (i.e the 2) and store its index (i.e. 1) as the min_index. We will repeat the same process to find the min_index as we did before. In this case nothing is less than the value of 2 that we started with so this value is already sorted and there is nothing to swap.

We repeat this procedure for the remaining items in the list until the entire list has been sorted like this.

![Selection Sort Sorted](./images/selection-sort-sorted.jpg?raw=true "Selection Sort Sorted")

It is worth noting that we don't have to do this for a 6th time at the index of 5. We only had to do this for the indexes of 0 through 4.
