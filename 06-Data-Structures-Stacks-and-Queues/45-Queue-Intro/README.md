# 45. Queue: Intro

## What is a Queue?

A **Queue** is a *data structure* consisting of items. A queue allows us to *enqueue* (i.e. add) items to the end of it and *dequeue* (i.e. remove) items from the front of it. What makes a queue unique is that you can only dequeue the item at the front of the queue. This is called *FIFO* - First In First Out.

### How is a Queue Implemented?

There are a few data structures that we could use to implement a queue.

1. One way is to use a **List** but only *add* items at one end and *remove* items from the opposite end.

| 11 | 3  | 23 | 7  |
| ---|----|----|----|
| 0  | 1  | 2  | 3  |

Adding or removing from the right side is O(1). Adding or removing from the left side is O(n) since it requires reindexing. Irrespective of which side we add or remove an item from we will always have one end which is O(n) which is not optimal.

2. Another way is to use a **LinkedList**. Removing from the right side is O(n) as it requires iteration through the list whereas adding is O(1). Adding or removing from the left side is O(1). It is clear that we don't want to dequeue an item from the right side of the list like this.

![Linked List Dequeue Right](./images/linked-list-dequeue-right.jpg?raw=true "Linked List Dequeue Right")

The most efficient way is to use a linked list where items are enqueued on the right side and dequeued from the left side.

![Linked List Enqueue Dequeue](./images/linked-list-enqueue-dequeue.jpg?raw=true "Linked List Enqueue Dequeue")

Head is renamed as *first* and tail is renamed as *last*.

![Linked List Queue](./images/linked-list-queue.jpg?raw=true "Linked List Queue")

We will repurpose the `append` and `pop_first` methods that we wrote previously to `enqueue` and `dequeue` items.
