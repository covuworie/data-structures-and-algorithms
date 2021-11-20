# 76. Bubble Sort: Intro

Now we are going to look at our first sorting algorithm - **bubble sort**. In the next lesson we will actually code it.

## How does Bubble Sort Work?

Let's assume we need to sort the following unsorted list in ascending order.

| 4 | 2 | 6 | 5 | 1 | 3 |
|---|---|---|---|---|---|
|   |   |   |   |   |   |

It is convenient to view the values in a bar chart instead to compare the relative sizes. In bubble sort we always start with the first item in the list and compare it to the second item like this.

![Bubble Sort Compare](./images/bubble-sort-compare.jpg?raw=true "Bubble Sort Compare")

If the first item is larger than the second item (which in this case it is) then we swap them like this.

![Bubble Sort Compare Swap](./images/bubble-sort-compare-swap.jpg?raw=true "Bubble Sort Compare Swap")

We then go to the second item and compare it to the third item and do the same comparison. In this case it's not larger so we don't do the swap and continue to compare the third item to the fourth item. We continue in this manner until we have *bubbled up* the largest item to the end of the list like this. 

![Bubble Sort Largest Item Sorted](./images/bubble-sort-largest-sorted.jpg?raw=true "Bubble Sort Largest Item Sorted")

Note that we had 6 items in the list and it took 5 comparisons to do this. Now we only have 5 items left to sort. So in this round we will only have 4 comparisons to do. So we will start back at the beginning of the list and repeat the procedure until we have sorted the second largest item in the list.

We repeat this procedure for the remaining items in the list until the entire list has been sorted like this.

![Bubble Sort Sorted](./images/bubble-sort-sorted.jpg?raw=true "Bubble Sort Sorted")
