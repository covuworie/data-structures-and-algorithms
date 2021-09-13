# 17. Linked List Intro

## What is a Linked List?

A **Linked List** is a *data structure* consisting of nodes. It has a variable called *head* that points to the first node and a variable called *tail* that points to the last node. Each node points to the *next* and the last node points to *None*.

![Linked List](./images/linked-list.jpg?raw=true "Linked List")

To emphasize that the nodes are spread out in different locations in memory, let's look at the memory-space of a linked list.

![Linked List in Memory](./images/linked-list-memory.jpg?raw=true "Linked List in Memory")

Since one node points to the next, it is possible to find all of the nodes. This is different to a **List** which looks something like this. 

![List in Memory](./images/list-memory.jpg?raw=true "List in Memory")

Because these are all in a contiguous place in memory we can have indexes and access those indexes O(1). We can map each index to a specific address in memory.
