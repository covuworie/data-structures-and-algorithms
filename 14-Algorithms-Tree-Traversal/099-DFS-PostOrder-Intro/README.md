# 99. Depth First Search (DFS): PostOrder - Intro

We mentioned previously that for tree traversal there would be 3 types of **Depth First Search (DFS)** that we would look at. The second one that we are going to look at is called **PostOrder** and the way we will add the numbers to the list is like this.

We will start at the top with the 47 like in all tree traversals. However, the difference here is that we will just visit the node first without writing the value to the `results` list yet.

![DFS 47](./images/dfs-47.jpg?raw=true "DFS 47")

and after that we are just going to keep moving to the left. So we will visit the 21 and then the 18. Since this is as far as we can go to the left, the value of 18 will be written to the results list. So the order we do this in is we look left, then we look right and then we add the value of that node to the results list. 

![DFS 18](./images/dfs-18.jpg?raw=true "DFS 18")

Now we will then come back up to the 21 and it has gone left already so it will visit the 27 on the right. That node will look to the left and then to the right and find no node so it will write it's value to the `results` list.

![DFS 27](./images/dfs-27.jpg?raw=true "DFS 27")

Next we come back up to the 21. It has gone left, it has gone right and now we write its value to the `results` list.

![DFS 21](./images/dfs-21.jpg?raw=true "DFS 21")

Next we come back up to the root 47 node. It has gone left, so now it visits the 76 node on the right. Now we always start by going left, so from the 76 we will visit the 52 node. The 52 will look left and it will look right and as there are no nodes there, it will write it's value to the `results` list.

![DFS 52](./images/dfs-52.jpg?raw=true "DFS 52")

We will continue in this manner eventually writing the root 47 node to the `results` list as the final step and we are done.

![DFS Done](./images/dfs-done.jpg?raw=true "DFS Done")
