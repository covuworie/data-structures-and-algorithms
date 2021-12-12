# 92. Quick Sort: Code

Let's now write the code for quicksort. Remember that the `quick_sort` function is going to use the `pivot` function that makes the list look like this.

![Quicksort Pivot](./images/quicksort-pivot.jpg?raw=true "Quicksort Pivot")

What the `quick_sort` function is going to do is to recursively call `pivot` again on the portions of the list either side of the `pivot_index`.

![Quicksort Pivot Recursive](./images/quicksort-pivot-recursive.jpg?raw=true "Quicksort Pivot Recursive")

Initially, the `quick_sort` function takes the list `my_list`, the `left` index and the `right` index as its parameters. Initially `left = 0` and `right = 6` corresponding to the start and end of the entire list. The first line of code calls `pivot` with these three variables and stores the result in the `pivot_index` variable like so.

![Quicksort Pivot Index](./images/quicksort-pivot-index.jpg?raw=true "Quicksort Pivot Index")

The code then recursively calls `pivot` on the lower part of the list (`left` through `pivot_index - 1`) and on the upper part of the list (`pivot_index + 1` through `right`).

![Quicksort Pivot Left Right](./images/quicksort-pivot-left-right.jpg?raw=true "Quicksort Pivot Left Right")

The recursive calls are made until the list is fully sorted and there is only one item in the left and right lists. In other words, there is only one item in the lsit when the `left` is equal to the `right`. This is the base case. So we only call those 3 lines of code if `left` is less than `right`. 

![Quicksort Base Case](./images/quicksort-base-case.jpg?raw=true "Quicksort Base Case")

The only thing left to do is to return `my_list`.

Notice that the code is refactored so that we don't have to pass the `left` and `right` index every time `quick_sort` is called. We rename `quick_sort` to `quick_sort_helper` and create a `quick_sort` function that only takes `my_list` as a parameter. This function simply returns the result of calling `quick_sort_helper` with the start and end indices of the list as `left` and `right`. 
