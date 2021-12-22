# 101. Depth First Search (DFS): InOrder - Intro

We mentioned previously that for tree traversal there would be 3 types of **Depth First Search (DFS)** that we would look at. The third one that we are going to look at is called **InOrder** and the way we will add the numbers to the list is like this.

We will start at the top with the 47 like in all tree traversals. Just like in **PostOrder** we will just visit the node first without writing the value to the `results` list yet.

![DFS Start](./images/dfs-start.jpg?raw=true "DFS Start")

and after that we are just going to keep moving to the left. So we will visit the 21 and then the 18. The 18 will try to go left and since there is no node there the value of 18 will be written to the results list. 

![DFS 18](./images/dfs-18.jpg?raw=true "DFS 18")

At this point the tree looks identical to how it did for **PostOrder**. However, instead of going left then right and then writing the value of the node to the results list, **InOrder** goes left, writes the value of the node to the `results` list and then goes right.

Now we will then come back up to the 21 and it has gone left already, so it will write it's value to the `results` list.

![DFS 21](./images/dfs-21.jpg?raw=true "DFS 21")

Now we visit the 27 on the right. The 27 will go left and write its value to the `results` list.

![DFS 27](./images/dfs-27.jpg?raw=true "DFS 27")

Then it will go right and that brings us back up to the root 47 node. It has gone left, so now it writes its value to the `results` list.

![DFS 47](./images/dfs-47.jpg?raw=true "DFS 47")

Now it goes right to the 76 and then the 76 goes left to the 52 and writes its value to the `results` list. We will continue in this manner eventually writing the 82 node to the `results` list as the final step and we are done.

![DFS Done](./images/dfs-done.jpg?raw=true "DFS Done")

If we look at the order in which the values in the tree were written to the `results` list we see that it is in *ascending numerical order* `[18, 21, 27, 47, 52, 76, 82]`.
