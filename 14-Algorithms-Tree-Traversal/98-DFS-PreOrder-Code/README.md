# 98. DFS: PreOrder - Code

Now let's look at the code for **Depth First Search (DFS) PreOrder**. It's important to point out that this is a method in the `BinarySearchTree` class and therefore it takes the `self` keyword as its only parameter.

It's best to put the code up and then explain it. In the code we have a `results` array that returns the node values. It initiliazed to a empty list. We also show the tree and a call stack to the bottom right to help explain the steps of what is happening.

![DFS PreOrder Setup](./images/dfs-preorder-setup.jpg?raw=true "DFS PreOrder Setup")

We can see that we have a recursive function called `traverse` that is inside of the method. This function takes the `current_node` as its parameter. The first thing the function does is take the value of that node and write it to the `results` list. Then if there is a node to the left of it then it calls `traverse` again on that node and if there is a one to the right of it then it calls `traverse` again on that node also. 

The way this is all initiated is by calling `traverse` on the `root` node. That pushes an instance of `traverse` on to the call stack with a node value of 47. The first thing the function does is append the value of that node to `results`.

![DFS PreOrder Root](./images/dfs-preorder-root.jpg?raw=true "DFS PreOrder Root")

Then the code looks to the left to see if there is a node there and if there is it calls `traverse` again. That pushes another instance of `traverse` on to the call stack with the a node value of 21. Because this instance is at the top of the call stack it is the one that is running now. The first thing it does is to append the node value of 21 to `results`.

![DFS PreOrder 21](./images/dfs-preorder-21.jpg?raw=true "DFS PreOrder 21")

It now looks to the left to see if there is a node and there is the 18. So `traverse` is called again pushing that instance on to the call stack now. The first thing it does is to append the node value of 18 to `results`.

![DFS PreOrder 18](./images/dfs-preorder-18.jpg?raw=true "DFS PreOrder 18")

Now the 18 doesn't have anything on the left or the right so now that instance gets popped off the call stack.

![DFS PreOrder 18 Pop](./images/dfs-preorder-18-pop.jpg?raw=true "DFS PreOrder 18 Pop")

So now the 21 is at the top of the call stack again. It's already gone left and now it needs to go right. The node to the right of the 21 is the 27 and a new instance of `traverse` with a value of 27 gets pushed on to the call stack. Again the first thing that happens is that value gets appended to the results list.

![DFS PreOrder 27](./images/dfs-preorder-27.jpg?raw=true "DFS PreOrder 27")

The 27 has no node to the left or to the right and so that gets popped from the call stack. The 21 is now on the top of the call stack and it has already gone left and right so that gets popped off the call stack. So now the 47 is at the top of the call stack again. 

![DFS PreOrder 47](./images/dfs-preorder-47.jpg?raw=true "DFS PreOrder 47")

It's already gone left and now it needs to go right. The steps described previously continue in a similar manner until the whole tree has been traversed like so.

![DFS PreOrder Done](./images/dfs-preorder-done.jpg?raw=true "DFS PreOrder Done")

The only thing that is left to do is to return `results`.
