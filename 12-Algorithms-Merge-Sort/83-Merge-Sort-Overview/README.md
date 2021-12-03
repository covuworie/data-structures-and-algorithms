# 83. Merge Sort: Overview

Now let's look at **merge sort**. The idea behind merge sort is this. If you have two *sorted lists* like this,

![Merge Sort 2 Lists](./images/merge-sort-2.jpg?raw=true "Merge Sort 2 Lists")

then it is very easy to combine them into a new sorted list like this.

![Merge Sort Sorted](./images/merge-sort-sorted.jpg?raw=true "Merge Sort Sorted")

## Example

Let's suppose we started off with a list of 8 unsorted items like this.

![Merge Sort Unsorted](./images/merge-sort-unsorted.jpg?raw=true "Merge Sort Unsorted")

Merge sort is first going to break this list in half, and then break it in half again and then break it in half again until we have 8 lists that contain only one item in them like this. By definition a list with 1 item in it is already sorted.

![Merge Sort Unsorted](./images/merge-sort-unsorted-broken.jpg?raw=true "Merge Sort Unsorted Broken")

Now we can take each pair of side-by-side items and create a new list that is sorted like this.

![Merge Sort Sorted Pairs](./images/merge-sort-sorted-pairs.jpg?raw=true "Merge Sort Sorted Pairs")

We can now combine these sorted pairs to create two sorted quads like this.  

![Merge Sort Sorted Quads](./images/merge-sort-sorted-quads.jpg?raw=true "Merge Sort Sorted Quads")

Finally we can combined these sorted quads into one sorted list like this.

![Merge Sort Sorted](./images/merge-sort-sorted.jpg?raw=true "Merge Sort Sorted")
