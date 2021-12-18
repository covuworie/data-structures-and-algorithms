# 95. Breadth First Search (BFS): Intro

Now let's look at the steps required to do **Breadth First Search (BFS)**. Remember BFS is the algorithm that starts at the top and then visits the second row and then the third row and so on.

The way we are going to do BFS is to create 2 lists:

1. `queue` will store the nodes in the order that we visit them
2. `results` will store the values at the nodes

We will start at the root node like this,

![BFS Root](./images/bfs-root.jpg?raw=true "BFS Root")

An important point to note is that in `queue` we store the *entire node*, recall that's the *value* as well as *left* and *right*. Let's change the value of the node to blue to emphasize that it's the entire node like so,

![BFS Root Blue](./images/bfs-root-blue.jpg?raw=true "BFS Root Blue")

Now we need to do something with the `value` and `left` and `right`. So:

1. First we will move the `value` to the `results` list. We will change it's color to green like this to emphasize that in this list we are only storing the value.

![BFS Root Results](./images/bfs-root-results.jpg?raw=true "BFS Root Results")

2. Then we store the `left` in the queue. 

3. And we will do the same for the `right` like so.

![BFS 47](./images/bfs-47.jpg?raw=true "BFS 47")

Then we will go through the same 3 steps with the value on the `left` and the `right` with the 21 like so.

![BFS 21](./images/bfs-21.jpg?raw=true "BFS 21")

And then we repeat the process again for the 76.

![BFS 76](./images/bfs-76.jpg?raw=true "BFS 76")

When we repeat the process this time, we have a value 18, but it doesn't have anything on the `left` or the `right` as it's a leaf node. So we only need to do step 1 which pushes the value into the results list. The same for the 27, 52 and 86 and we end up in this state.

![BFS Done](./images/bfs-done.jpg?raw=true "BFS Done")

We can see that the loop that we will create to do all of this will only run while there are still nodes in the `queue`. When the `queue` is empty that means we have visited every node in the tree. The only thing left to do at that point is to return the `results` list.

There is something else that is interesting about BFS. If we look at the numbers in the `results` list, if you take the first number and put it at the root and you take the next two numbers and put them in the next row and you take the next 4 numbers and put them in the third row then you can reconstruct the tree.

![BFS Reconstruct](./images/bfs-reconstruct.jpg?raw=true "BFS Reconstruct")
