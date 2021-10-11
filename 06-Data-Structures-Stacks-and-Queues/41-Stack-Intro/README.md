# 41. Stack: Intro

## What is a Stack?

A **Stack** is a *data structure* consisting of items. A stack allows us to *push* items on to the top of it and *pop* items off of the top of it. What makes a stack unique is that you can only pop the last item that was pushed on to the top of the stack. This is called *LIFO* - Last In First Out.

### How is a Stack Implemented?

There are a few different ways to implement a stack.

1. The simplest way is to use a **List** but only *add* or *remove* items from the same end.

| 11 | 3  | 23 | 7  |
| ---|----|----|----|
| 0  | 1  | 2  | 3  |

Adding or removing from the left side is O(n) as it requires reindexing. So it makes sense to add and remove from the right side since we saw previously that both of these operations are O(1). However, conceptually the stack would look more like a 90 degrees rotation of this.

|   **7**    |
|------------|
|<sub>3</sub>|
|   **23**   |
|<sub>2</sub>|
|   **3**    |
|<sub>1</sub>|
|   **11**   |
|<sub>0</sub>|

2. A more challenging way (which we will be implementing) is to use a **LinkedList** but only *add* or *remove* items from the same end.

![Linked List](./images/linked-list.jpg?raw=true "Linked List")

Removing from the right side is O(n) as it requires iteration through the list. Adding is 0(1). So it makes sense to add and remove from the left side since we saw previously that both of these operations are O(1). However, conceptually the stack would look more like a 90 degrees rotation of this where the arrows *must* point downwards.

![Linked List Stack](./images/linked-list-stack.jpg?raw=true "Linked List Stack")

Head is renamed as *top* and since we will be only pushing or popping items from one end we remove the tail variable. We will repurpose the `pop_first` and `prepend` methods that we wrote previously to `pop` and `push` items on to the stack.
