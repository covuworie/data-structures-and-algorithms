# 80. Insertion Sort: Intro

Now we are going to look at our third sorting algorithm - **insertion sort**. In the next lesson we will actually code it.

## How does Insertion Sort Work?

Let's assume we need to sort the following unsorted list in ascending order.

| 4 | 2 | 6 | 5 | 1 | 3 |
|---|---|---|---|---|---|
|   |   |   |   |   |   |

In insertion sort we always start with the *second* item in the list and then what we do is compare it to the item before it like this.

![Insertion Sort Compare Start](./images/insertion-sort-compare-start.jpg?raw=true "Insertion Sort Compare Start")

If the item is smaller than the previous item (which in this case it is) then we insert it before the item like this.

![Insertion Sort Insert Start](./images/insertion-sort-insert-start.jpg?raw=true "Insertion Sort Insert Start")

We then go to the third item and we do the same thing, we compare it to the item before it. In this case the 6 is not smaller than the 4 so we don't move it. 

We continue in this manner through the entire list. Note that a special case is when we get to the 1. We have to compare it to all the items before it and it has to go all the way to the beginning like this.

![Insertion Sort Insert Beginning](./images/insertion-sort-insert-beginning.jpg?raw=true "Insertion Sort Insert Beginning")

Eventually when we have done this for the entire list it will be sorted like this.

![Insertion Sort Sorted](./images/insertion-sort-sorted.jpg?raw=true "Insertion Sort Sorted")
