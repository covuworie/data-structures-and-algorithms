# 84. Merge: Intro

Let's talk the `merge` function that we are going to code. It is a *helper function* that does a portion of the task that we wish to do. The job of the `merge` function is to take two *sorted lists* like this,

![Merge Pairs](./images/merge-pairs.jpg?raw=true "Merge Pairs")

and combine them into a new sorted list like this.

![Merge Merged](./images/merge-merged.jpg?raw=true "Merge Merged")

Let's walk through how we are going to do this. We are going to loop through each of these lists, the first with the variable i and the second with the variable j. What we will do is compare the values at i and j,

![Merge Compare](./images/merge-compare.jpg?raw=true "Merge Compare")

and whichever is lowest we will add to the new combined list. In this case it's the 1 in the left side list so we will add that to the list like this.

![Merge Compare Add](./images/merge-compare-add.jpg?raw=true "Merge Compare Add")

We then repeat this procedure looping through each of the lists until one of them is empty. In this case it will be the right side list like this.

![Merge Compare Empty](./images/merge-compare-empty.jpg?raw=true "Merge Compare Empty")

Once we have done this we will have another loop that loops through whichever list still has items and we will add these items to the list like this.

![Merge Merged](./images/merge-merged.jpg?raw=true "Merge Merged")
