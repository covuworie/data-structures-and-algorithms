# 89. Quick Sort: Intro

Let's look at an overview of **quicksort**. We start out with a list like this,

| 4 | 6 | 1 | 7 | 3 | 2 | 5 |
|---|---|---|---|---|---|---|

except we will represent it as a chart for easier visual comparison. The way quicksort works is we start with a *pivot point*. That's going to be the first item colored in red. Then we are going to compare each of the items after the pivot point to it to see if they are *less than* (colored in yellow) or *greater than* (colored in grey) it like so. 

![Quick Sort Pivot Compare](./images/quick-sort-pivot-compare.jpg?raw=true "Quick Sort Pivot Compare")

What we then do is swap the first item that was less than (i.e. the 1) with the first item that was greater than (i.e. the 6) like this.

![Quick Sort Compare Swap](./images/quick-sort-compare-swap.jpg?raw=true "Quick Sort Compare Swap")

Then we move to the 7 which is grey as it's greater than the pivot. The 3 is less than the pivot so it's yellow and we have this situation.

![Quick Sort Pivot Compare 2](./images/quick-sort-pivot-compare-2.jpg?raw=true "Quick Sort Pivot Compare 2")

What we then do is swap the 3 with the first item that was greater than (i.e. the 6) like this.

![Quick Sort Compare Swap 2](./images/quick-sort-compare-swap-2.jpg?raw=true "Quick Sort Compare Swap 2")

Then we move to the 2 which is yellow as its less than the pivot. We then swap it with the 7. So we have reached the end of the first iteration since  we now have all the items that are less than the pivot together and all the items that are greater than the pivot together like this.

![Quick Sort Iteration 1](./images/quick-sort-iteration-1.jpg?raw=true "Quick Sort Iteration 1")

Then in the next step we swap the pivot (i.e. the 4) with the last of the less than items (i.e. the 2) like this. 

![Quick Sort Iteration 1 Swap](./images/quick-sort-iteration-1-swap.jpg?raw=true "Quick Sort Iteration Swap")

There is an important point to make here. First the pivot (i.e. the 4) is now sorted and it's colored in green. Every item less than the 4 is to the left of it and every item greater than the 4 is to the right of it.

What we are then going to do is run quicksort again on the unsorted items below the pivot and the unsorted items above the pivot like so.

![Quick Sort Again](./images/quick-sort-again.jpg?raw=true "Quick Sort Again")

Starting with the lower items, the pivot is the 2, the 1 is yellow as it's less than and the 3 is grey as its greater than. Note that in this scenario there is no item greater than to the left of the 2 so we cannot swap it with anything. Therefore we are already at the end of the iteration and so we then swap the 1 (i.e. the pivot) and the 2 (i.e. the least of the less than items) and now the 2 is sorted like this.

![Quick Sort Lower 1](./images/quick-sort-lower-1.jpg?raw=true "Quick Sort Lower 1")

We then run quicksort again on the items below and above the pivot (i.e. the 2), in this case on the 1 and the 3. Since they only contain one item then we know by definition that they are already sorted. So now we have sorted the first half of the list like this.

![Quick Sort Lower Sorted](./images/quick-sort-lower-sorted.jpg?raw=true "Quick Sort Lower Sorted")

We repeatedly run quicksort in the same way on the upper part of the list starting with the 6 as the pivot until we have sorted that part and the entire list is sorted like this.

![Quick Sort Sorted](./images/quick-sort-sorted.jpg?raw=true "Quick Sort Sorted")
