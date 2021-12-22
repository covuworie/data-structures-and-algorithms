# 97. Depth First Search (DFS): PreOrder - Intro

We mentioned previously that for tree traversal there would be 3 types of **Depth First Search (DFS)** that we would look at. The first one that we are going to look at is called **PreOrder** and the way we will add the numbers to the list is like this.

We will start at the top and add the 47 to the list.

![DFS 47](./images/dfs-47.jpg?raw=true "DFS 47")

and after that we are just going to keep moving to the left. So we will add the 21 and then the 18.

![DFS 21-18](./images/dfs-21-18.jpg?raw=true "DFS 21-18")

Since this is as far as we can go to the left, we will then come back up to the 21 and go to the 27 on the right.

![DFS 27](./images/dfs-27.jpg?raw=true "DFS 27")

Now we have looked at everything to the left of the 47 root node. So now we will go back up to the root node and we will go right to the 76.

![DFS 76](./images/dfs-76.jpg?raw=true "DFS 76")

And then after the 76 we always go left first. So we will go to the 52.

![DFS 52](./images/dfs-52.jpg?raw=true "DFS 52")

We will then come back up to 76 since we can't go any further left and so we will go right to the 82 and we are done.

![DFS 82](./images/dfs-82.jpg?raw=true "DFS 82")
