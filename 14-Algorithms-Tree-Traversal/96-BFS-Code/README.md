# 96. BFS: Code

Now let's look write the code for **Breadth First Search (BFS)**. It's important to point out that this is a method in the `BinarySearchTree` class and therefore it takes the `self` keyword as its only parameter.

We can see from the code that at the top of the method we initialize the `queue` with the `root` node. We use a list here due to familiarity with lists in the course, however, from a Big O perspective it would be more efficient to use a *queue* (`push` and `pop` are O(1)) or *linked list* (`append` and `pop_first` are O(1)) data structure. We also initialize the `results` as an empty list and immediately deal with the edge case of the tree being empty by returning the empty `results`.

![BFS Root](./images/bfs-root.jpg?raw=true "BFS Root")

Note that it is essential to put the `root` node in the `queue` first as the while loop runs while there are items still in the queue. If we didn't do this first the while loop would never run!

Inside the loop the first thing we do is pop the first node from the `queue` (this is O(n)) and set it equal to a variable `current_node`.

![BFS Pop First](./images/bfs-pop-first.jpg?raw=true "BFS Pop First")

This variable essentially helps us to iterate through the tree similar to what we did with the `contains` method. Then next we append the `current_node` value to the `results` list.

![BFS Append Value](./images/bfs-append-value.jpg?raw=true "BFS Append Value")

Next we look to the left of `current_node` to see if there is a node there. If there is one there, then we append it to the `queue`. Then we do the same on the right.

![BFS Append Nodes](./images/bfs-append-nodes.jpg?raw=true "BFS Append Nodes")

Then we go through the while loop again and again. Everything is the same until we reach this situation.

![BFS Pop 18](./images/bfs-pop-18.jpg?raw=true "BFS Pop 18")

 Now the 18 doesn't have anything on the left or the right so it's value simply gets appended to the `results` list. The same is true for the 27, 52 and 82. Now the queue is empty and the while loop stops running.

![BFS Done](./images/bfs-done.jpg?raw=true "BFS Done")

The only thing that is left to do is to return `results`.
