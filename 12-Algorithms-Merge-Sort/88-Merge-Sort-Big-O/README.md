# 88. Merge Sort: Big O

## Space Complexity

Now let's look at the Big O for **merge sort**. The first thing we will look at is the space complexity. Remember we start out with an original unsorted list like this.

![Merge Sort Unsorted](./images/merge-sort-unsorted.jpg?raw=true "Merge Sort Unsorted")

We then create two new lists called `left` and `right` by splitting the list in half. We continue breaking down these lists until we have new lists that each contain 1 item. In this case we have 8 new lists like this.

![Merge Sort Unsorted Broken](./images/merge-sort-unsorted-broken.jpg?raw=true "Merge Sort Unsorted Broken")

So the number of items stored in memory has doubled. That means that this breaking down process is *O(n)* for space complexity.

Recall that the previous sorting algorithms we looked at all sort the list *in place* - bubble, selection and insertion sort. Those algorithms take the original list and move items around inside it in order to sort the list. Merge sort is different in the sense that it creates *new lists*.

## Time Complexity

Let's now look at the time complexity of merge sort. The process of breaking the above list of 8 items in half to obtain 8 lists of 1 item, took only 3 steps. *2 <sup>3</sup> = 8* so this process is *O(log n)*. 

Now let's consider what happens when we start merging the lists back together in each step like this.

![Merge Sort Sorted Pairs](./images/merge-sort-sorted-pairs.jpg?raw=true "Merge Sort Sorted Pairs")

 Think back to the helper `merge` function. It consists of while loops that go through each item in `left` and `right` one-by-one in order to combine them. So this process is *O(n)* due to having to go through every item in the list.

So combining these time complexities we see that the overall time complexity for merge sort is **O(n log n)**. On a graph this looks like this.

![Merge Sort Big O Graph](./images/merge-sort-Big-O.jpg?raw=true "Merge Sort Big O Graph")

The first 3 sorting algorithms we created were O(n<sup>2</sup>). But merge sort is far more efficient. In fact O(n log n) is the most efficient that you can make a sorting algorithm that sorts multiple types of data. 

There are certain efficiencies when sorting *only* numbers that some algorithms can take advantage of to sort more efficiently. However, these algorithms have the limitation that they can only sort numbers.
