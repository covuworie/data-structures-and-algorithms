# 45. Queue: Intro

## What is a Queue?

A **Queue** is a *data structure* consisting of items. A queue allows us to *enque* (i.e. add) items to the end of it and *deque* (i.e. remove) items from the front of it. What makes a queue unique is that you can only deque the item at the front of the queue. This is called *FIFO* - First In First Out.

### How is a Queue Implemented?

There are a few data structures that we could use to implement a queue.

1. One way is to use a **List** but only *add* items at one end and *remove* items from the opposite end.

| 11 | 3  | 23 | 7  |
| ---|----|----|----|
| 0  | 1  | 2  | 3  |

Adding or removing from the right side is O(1). Adding or removing from the left side is O(n) since it requires reindexing. Irrespective of which side we add or remove an item from we will always have one end which is O(n) which is not optimal.

2. Another way is to use a **LinkedList**. Removing from the right side is O(n) as it requires iteration through the list whereas adding is O(1). Adding or removing from the left side is O(1). It is clear that we don't want to deque an item from the right side of the list like this.

![Linked List Deque Right](./images/linked-list-deque-right.jpg?raw=true "Linked List Deque Right")

The most efficient way is to use a linked list where items are enqued on the right side and dequed from the left side.

![Linked List Enque Deque](./images/linked-list-enque-deque.jpg?raw=true "Linked List Enque Deque")

Head is renamed as *first* and tail is renamed as *last*.

![Linked List Queue](./images/linked-list-queue.jpg?raw=true "Linked List Queue")

We will repurpose the `append` and `pop_first` methods that we wrote previously to `enque` and `deque` items.
