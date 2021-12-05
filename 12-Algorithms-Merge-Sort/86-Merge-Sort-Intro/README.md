# 86. Merge Sort: Intro

Let's talk about how we are going to implement **mergesort**. Recall that mergesort needs to break an unsorted list like this,

![Merge Sort Unsorted](./images/merge-sort-unsorted.jpg?raw=true "Merge Sort Unsorted")

in half and then break it in half again and then keep breaking it in half until we have only one item in each of the resulting lists like this.

![Merge Sort Unsorted](./images/merge-sort-unsorted-broken.jpg?raw=true "Merge Sort Unsorted Broken")

Then we can use the helper `merge` function that takes pairs of *sorted lists* and combines them like this,

![Merge Sort Sorted Pairs](./images/merge-sort-sorted-pairs.jpg?raw=true "Merge Sort Sorted Pairs")

and then like this,

![Merge Sort Sorted Quads](./images/merge-sort-sorted-quads.jpg?raw=true "Merge Sort Sorted Quads")

and then finally like, resulting in the original list being sorted.

![Merge Sort Sorted](./images/merge-sort-sorted.jpg?raw=true "Merge Sort Sorted")

So we will have the following bits of code or steps:

1. *Breaks lists in half*
    - We will use *recursion* as a) we are doing the same thing over and over and b) we are making the problem smaller (by definition due to breaking lists in half!)
2. *Base case*: when the `len(the_list)` is 1
3. Uses the `merge` function to *put pairs of sorted lists together*