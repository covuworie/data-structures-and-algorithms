# 93. Quick Sort: Big O

## Time Complexity

Let's now look at the time complexity of quick sort. The first step in quick sort is to run the `pivot` function. That function loops through all the items in the list so it's *O(n)*. 

However, the recursive part is done via divide-and-conquer - we've seen this before. Let's say there was approximately 8 items and the recursive part was done in 3 steps so *2 <sup>3</sup> = 8* so this process is *O(log n)*. So **quick sort** has a time complexity of **O(n log n)** just like merge sort. On a graph this looks like this and we can see that it is much more efficient than *O(n<sup>2</sup>)*.

![Merge Sort Big O Graph](./images/quick-sort-Big-O.jpg?raw=true "Merge Sort Big O Graph")

This complexity only holds for the best case and the average case. For the worse case it's a different scenario. The worse case is if the list is already sorted `[1, 2, 3, 4, 5, 6, 7]`. We start out with the pivot point being the 1 and we don't move anything else as it's already sorted. Normally we run quicksort on the lower and upper portions. In this case there is only an upper portion so we run quicksort on that. Again we move nothing in the list as it's already sorted. So we run the `pivot` function, which has *O(n)* complexity, n times in this scenario as we have to do it for every item in the list. Consequently the worse case scenario is *O(n<sup>2</sup>)*.

So if you have sorted data or almost sorted data then it might actually be better to use an algorithm like *insertion sort* since we saw that it has a best case complexity of *O(n)* in this scenario.

## Space Complexity

The space complexity for **quick sort** was not discussed in the course. However, the space complexity is calculated based on the space used in the recursion stack. Note that it's essentially O(1) for each function call on the call stack since the list is sorted *in place*. The worst case space used will be *O(n)* when the list is already sorted and we need to make n recursive calls. The average case space used will *O(log n)* as we make *log n* recursive calls. This is where quick sort is more efficient than merge sort which has a space complexity of *O(n)*.
