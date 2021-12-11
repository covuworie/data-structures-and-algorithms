# 90. Pivot: Intro

## Purpose

Let's talk about the `pivot` function that we are going to code. It is a *helper function* that does a portion of the task that we wish to do. The job of the `pivot` function is two-fold:

1. It will get us to the point that we discussed before where the chosen pivot is in the spot where it will be when the list is sorted like this.

![Quick Sort Iteration 1 Swap](./images/quick-sort-iteration-1-swap.jpg?raw=true "Quick Sort Iteration Swap")

2. It will return the index of the spot where the pivot is. We will talk about why we return the index and not the value in a moment.

## Algorithm

So how is the `pivot` function going to achieve what we have disussed? We will choose a pivot point (colored red) and have a variable *pivot* that points at its index. We will also have a variable *swap* that is initialized to this index. Then we will have a for loop indexed by *i* that starts at the next variable over like so.

![Pivot Start Indices](./images/pivot-start.jpg?raw=true "Pivot Start Indices")

Then we will start running through the for loop. The first value (6) is greater than the pivot (colored grey) (4). We simply move *i* to the next index. Now this value (1) is less than the pivot (colored yellow) so we will move *swap* over one and swap the values at the indices *swap* and *i* like this.  

![Pivot Start Swap i](./images/pivot-start-swap-i.jpg?raw=true "Pivot Start Swap i")

Then *i* will move forward again to the 7. This value is greater than the pivot. Then *i* will move forward again to the 3. This value is less than the pivot. So we move *swap* over one again and swap the values at *swap* and *i* like so.

![Pivot Swap i](./images/pivot-swap-i.jpg?raw=true "Pivot Swap i")

We continue iterating through the items until we are done with the *i* variable and reach the point where all the less than items are first and all the greater than items are last like this.

![Pivot Iteration End](./images/pivot-iteration-end.jpg?raw=true "Pivot Iteration End")

Then in the next step we swap the items at the *pivot* and the *swap* index like this.

![Pivot Swap](./images/pivot-swap.jpg?raw=true "Pivot Swap")

That puts the initial pivot (4) at the correct sorted position and all that's left to do is to return the *swap* index that is pointing at it. This is everything that the `pivot` function is going to do. The reason we return the index is because we will run quicksort again on the items:

1. From the beginning up to and not including the swap index
2. From the item one more than the swap index to the end

![Pivot Swap Lower Upper](./images/pivot-swap-lower-upper.jpg?raw=true "Pivot Swap Lower Upper")
