# 52. BST: Constructor

The code defines two classes, **Node** and the **BinarySearchTree**.

The Node class has one responsibility - to create new nodes. It has a *left* and a *right* to refer to the two arrows that point from the node.

![Binary Search Tree Node](./images/binary-search-tree-node.jpg?raw=true "Binary Search Tree Node")

So in a similar manner to what we have seen previosuly, our Node constructor looks like this.

![Binary Search Tree Node Constructor](./images/binary-search-tree-node-constructor.jpg?raw=true "Binary Search Tree Node Constructor")

Remember that each node in the tree needs to have a parent node pointing at it except for the root node. In order to get to the root node we need a variable pointing at it. We call this variable *root*.

![Binary Search Tree Root](./images/binary-search-tree-root.jpg?raw=true "Binary Search Tree Root")

However, instead of the BinarySearchTree constructor first creating a new node using the Node constructor and then pointing root to this new node we decide to initialize an empty tree by pointing root to None.

![Binary Search Tree Constructor](./images/binary-search-tree-constructor.jpg?raw=true "Stack Constructor")

We will then add nodes using the `insert` method. Notice that this choice of whether to create a new node during initialization or to initialize an empty data structure is arbitrary. We could have taken this approach with the LinkedList or other data structures we have seen so far.
