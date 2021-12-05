# 87. Merge Sort: Code

Let's take a look at the code for the `merge_sort` function.

The code starts off by defining the base case which simply returns the list with one item. This case is reached after we have repeatedly broken the list in half.

Next comes the code that repeatedly breaks lists in half. First the midpoint of the list is found. Note that we call the `int` function on this value to deal with a list with an odd number of items. We could just as easily used the `math.floor` function.

Next comes the code that splits the list in half by creating two different lists. A `left` list that gives the value at every index up to and not including `mid` and a `right` that gives the remaining part of the list. If `my_list = [3, 1, 4, 2]` then `left = [3, 1]` and `right = [4, 2]`.

Then what we want to return is the `left` and `right` lists merged. However, we have a problem here because the `merge` function only works on sorted lists! So `left` and `right` need to be broken in half again. The function that breaks lists in half is the `merge_sort` function itself, so the code calls the `merge_sort` function on `left` and `right` again. This must happen until eventually we have one item in `left` and `right` which means by definition they are sorted. This is the recursive part of the code.

![Merge Sort Code](./images/merge-sort-code.jpg?raw=true "Merge Sort Code")

We can see that for this example this will result in lists containing only one item and the if condition corresponding to the base case will be true, which will simply return `my_list. So the `merge` function will now merge the 2 and 4 and also merge the 1 and 3. And then the code will do it again to merge the 1, 2, 3 and 4. And now the entire list is sorted.



