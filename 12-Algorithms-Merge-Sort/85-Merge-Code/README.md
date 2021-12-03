# 85. Merge: Code

Let's take a look at the code for the `merge` function. The first key point is that we cannot use for loops as we do not know how many items we are going to take from each list to begin with. We are going to have to use while loops.

The code starts off by defining the `combined` list that we will be adding the sorted items into and the indices for the two lists i and j.

![Merge Code Indices](./images/merge-code-indices.jpg?raw=true "Merge Code Indices")

Next the while loop runs as long as both lists still have items in them. If either loop becomes empty then we will break out of the loop. We next compare the value of items in the two lists, adding the item from the first list to the combined list if its value is less than the value in the second list and vice versa. We then move the index over by 1 whenever we add an item from that list into the combined list. After the first two iterations it will look like this.

![Merge Code Append](./images/merge-code-append.jpg?raw=true "Merge Code Append")

Items continue being added to the combined list until the second list is empty and we break out of the while loop.

![Merge Code Empty](./images/merge-code-empty.jpg?raw=true "Merge Code Empty")

So now we have to get the two items in list 1 into the combined list. This is simple since they are already sorted so we can just use a while loop as in the course. Of course the other possibility is if second list had items and the first list was empty. We can deal with this scenario in exactly the same way like this.

![Merge Code Append Rest](./images/merge-code-append-rest.jpg?raw=true "Merge Code Append Rest")

I instead choose to use `+=` *augmented* concatenation as it's simpler and of similar O(n) complexity. Essentially it's the same as `list.extend()` with a re-assignment to the same reference. 
