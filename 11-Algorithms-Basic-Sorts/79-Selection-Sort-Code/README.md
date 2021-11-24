# 79. Selection Sort: Code

Now we are going to look at the code for **selection sort**. There will be two approaches, the first is the conventional iterative approach which was covered in the course. However, I've also implemented a recursive version for comparison. Both functions do the same thing, they take a list as a parameter and they sort in the list *in-place* in ascending order.

In the iterative approach we can clearly see the two loops described in the last lesson along with the index of the minimum value. The indices look like this.

![Selection Sort Indices](./images/selection-sort-indices.jpg?raw=true "Selection Sort Indices")

From the code we see that the i loop runs from the start of the list to the penultimate value and that the `min_index` is initialized to i. We also observe that the j index loops through all the items in the list except for the i-th one. We can see that a comparison is done between the value at the j index and the `min_index`. The `min_index` is set to the value at the j index if its value is less than the previously `min_index` value. In the first iteration this value will look like this.

![Selection Sort Min Index](./images/selection-sort-min-index.jpg?raw=true "Selection Sort Min Index")

If the `min_index` is not equal to the value at the i index (i.e. the value at the i index is already sorted!) then we can see that the code swaps the value at the `min_index` with the value at the i index. For the first iteration this looks like this, which is very similar to what we did with bubble sort. Now the first item is sorted.

![Selection Sort Swap](./images/selection-sort-swap.jpg?raw=true "Selection Sort Swap")

In the recursive approach we can clearly see that the `min_index` is set to 0. Then similar to the iterative case we see that the j index loops through all the items in the list except for the first one. Again the comparison and swapping of values is similar to the iterative case. The only difference is that the swapping is always done between the value at index 0 and the value at `min_index` (as long as they are not equal). 

 At the end of the code we see how the code calls itself with a smaller list, concatenating the result with the rest of the list in the recursive case. We can also see the base case where the length of the list is one and the code simply returns the list.
