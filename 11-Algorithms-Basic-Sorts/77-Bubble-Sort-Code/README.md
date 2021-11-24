# 76. Bubble Sort: Code

Now we are going to look at the code for **bubble sort**. There will be two approaches, the first is the conventional iterative approach which was covered in the course. However, I've also implemented a recursive version for comparison. Both functions do the same thing, they take a list as a parameter and they sort in the list *in-place* in ascending order.

In the iterative approach we can clearly see the two loops described in the last lesson, the comparison between the i-th and (i-1)-th value and the swap of the values.

In the recursive approach we can clearly see the loop through the list, the comparison between the i-th and (i-1)-th value and the swap of the values and how the code calls itself with a smaller list, concatenating the result with the rest of the list in the recursive case. We can also see the base case where the length of the list is one and the code simply returns the list.

I timed these two methods and found the recursive approach to be quite a bit slower. It's also less efficient from a memory perspective. This is due to the extra instances of the function that are pushed onto the call stack.
