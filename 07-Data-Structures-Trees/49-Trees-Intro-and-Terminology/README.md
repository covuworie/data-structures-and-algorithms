# 49. Trees: Intro & Terminology 

## Relationship Between a Binary Tree and a Linked List

We have already seen a tree in this course. A Linked List is a tree which doesn't fork. We will use this as the starting point for creating a tree in this section.

A **Binary Tree** node looks like this:

![Binary Tree Node](./images/binary-tree-node.jpg?raw=true "Binary Tree Node")

Similarly to a linked list node it can be represented by the following dictionary:

```
{
    "value": 4,
    "left" None,
    "right": None
}
```

Let's build out a small binary tree. This node can of course point to other nodes like this:

![Small Binary Tree](./images/binary-tree-small.jpg?raw=true "Small Binary Tree")

This tree of course can be thought of as dictionaries like this:

```
{
    "value": 4,
    "left": {
        "value": 3,
        "left": None,
        "right": None
    },
    "right": {
        "value": 23,
        "left": None,
        "right": None
    },
}
```

The way we have designed our nodes with values *left* and *right*, every node is set up so that it can only point to two other nodes. This is a binary tree. But more generally trees do not have to be limited in this way.

## Terminology

### Tree

- In a **Full** binary tree every node either points to *zero* or *two* nodes.

![Full Binary Tree](./images/binary-tree-full.jpg?raw=true "Full Binary Tree")

- In a **Perfect** binary tree every level in the tree is completely filled with nodes all the way across.

![Perfect Binary Tree](./images/binary-tree-perfect.jpg?raw=true "Perfect Binary Tree")

A perfect tree is also a complete tree as described below.

- In a **Complete** binary tree the tree is filled from left to right with no gaps.

![Complete Binary Tree](./images/binary-tree-complete.jpg?raw=true "Complete Binary Tree")

### Node

The 4 is a **Parent** node of the 3 and 23 nodes. The 4 node is also the **Root** node as it has no parent.

![Binary Tree Parent Node](./images/binary-tree-parent-node.jpg?raw=true "Binary Tree Parent Node")

The 3 and 23 node are **Child** nodes of the 4 node. The 3 and 23 nodes are also **Sibling** nodes as they share the same parent node. The 3 and 23 node are also **Leaf** nodes as they have no child nodes.

![Binary Tree Child Node](./images/binary-tree-child-node.jpg?raw=true "Binary Tree Child Node")



## What is a Tree?

Wikipedia states that a **Tree** is a *hierarchical data structure* that can be defined recursively as a collection of nodes, where each node is a data structure consisting of a value and a list of references to nodes. The start of the tree is the *root* node and the reference nodes are the *children*. No reference is duplicated and none points to the root.

![Binary Tree](./images/binary-tree.jpg?raw=true "Binary Tree")
