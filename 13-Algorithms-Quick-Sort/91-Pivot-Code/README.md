# 91. Pivot: Code

Let's now write the code for the `pivot` function. The first thing to realize is we have two different places where we need to swap items in the list. Since we will be doing this twice we will extract a function in order to swap items in `my_list` at `index1` and `index2` like this.

```
def swap(my_list: List[int], index1: int, index2: int) -> None:
    temp = my_list[index1]
    my_list[index1] = my_list[index2]
    my_list[index2] = temp
```

Let's look at the `pivot` function itself now. We can see from the code that it takes `my_list`, `pivot_index` and `end_index` as parameters. What we are going to do here is pass the function a `pivot_index = 0` and an `end_index = 6` which correspond to the start and end of the entire list. 

So we have already created our first variable `pivot_index`. We create the second variable `swap_index` by initializing it with the `pivot_index`. Our loop indexed by the `i` variable then runs from one more than `pivot_index` through to the `end_index` (note we add one since the `range` function does not include the last value).

![Pivot Code Index](./images/pivot-code-index.jpg?raw=true "Pivot Code Index")

Then the code next compares the value at `i` to the value at the `pivot_index`. The value is not less than so we do not enter the if statement and simply increment `i`. The comparison is done again and this time the value is less than so we first move the `swap_index` over by one and then call the `swap` function to swap the items at `i` and `swap_index` like so.

![Pivot Code First Swap](./images/pivot-code-first-swap.jpg?raw=true "Pivot Code First Swap")

If we continue running the for loop all the way until the end then the list will look like this.

![Pivot Code For End](./images/pivot-code-for-end.jpg?raw=true "Pivot Code For End")

What we now need to do is swap the items at `pivot_index` and `swap_index`. We do that by calling the `swap` function again like so.

![Pivot Code Second Swap](./images/pivot-code-second-swap.jpg?raw=true "Pivot Code Second Swap")

Now all that is left to do is to return the `swap_index`.
