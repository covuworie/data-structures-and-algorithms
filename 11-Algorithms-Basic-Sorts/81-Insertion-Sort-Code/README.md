# 81. Insertion Sort: Code

Now we are going to look at the code for **insertion sort**. There will be two approaches, the first is the conventional iterative approach which was covered in the course. However, I've also implemented a recursive version for comparison. Both functions do the same thing, they take a list as a parameter and they sort in the list *in-place* in ascending order.

In the iterative approach we can clearly see that the outer loop starts at the second item in the list. We also see that we need a variable `temp` to hold the value of that item. We compare the value of this item to the value of the item before it which is indexed by j. In this case it's greater so no insertion is done. 

![Insertion Sort Indices](./images/insertion-sort-indices.jpg?raw=true "Insertion Sort Indices")

The first time we have an item that will be less than the item before it will be the 3 so let's skip ahead to that point which looks like this.

![Insertion Sort 3](./images/insertion-sort-3.jpg?raw=true "Insertion Sort 3")

We can see that the inner loop iterates over the values before the `temp` item in the list performing insertions if the value is less than the one before it. The insertion is achieved by first moving the item before it to the open spot on the right like this.

![Insertion Sort Right](./images/insertion-sort-right.jpg?raw=true "Insertion Sort Right")

Then the temp value is moved to the open spot on the left like this.

![Insertion Sort Left](./images/insertion-sort-left.jpg?raw=true "Insertion Sort Left")

You can see that if the value of the item at `temp` is never less than the value before it then the inner loop is exited and no insertion is performed.

In the recursive approach we can see that the structure of the code is similar with the two loops and that the insertion is of items is performed in the same way. The approach is to divide the list into two subsets – a sorted subset and an unsorted subset. Initially, the sorted subset consists of only the first element. Then for each iteration, the next element from the unsorted subset is removed and inserted in the appropriate location in the sorted subset. This is done by recursively calling the method on the remaining unsorted subset. This repeats until no input elements remain in the unsorted subset.
