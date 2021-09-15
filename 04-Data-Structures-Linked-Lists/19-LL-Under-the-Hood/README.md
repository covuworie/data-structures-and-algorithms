# 19. LL: Under the Hood

## What is the Node?

The **node** of a Linked List is both the *value* and the *pointer*. 

![Linked List Node](./images/linked-list-node.jpg?raw=true "Linked List Node")

Still what is it? Essentially it is very similary to a *dictionary*.

```
{
    "value": 4,
    "next: None
}
```

## What is the Linked List?

The **Linked List** can be considered to be like a set of *nested dictionaries* (the nodes) where the *next* key in each dictionary points to the next dictionary (node). *Head* is a variable that points to the set of nested dictionaries and *tail* points to the last node. 

![Linked List Nested Dicts](./images/linked-list-nested-dicts.jpg?raw=true "Linked List Nested Dicts")

This is basically what is happening under the hood when you see the following Linked List.

![Linked List Node](../18-LL-Big-O/images/linked-list-append-end.jpg?raw=true "Linked List Node")


#### Example

The code defines this set of nest dictionaries and shows how we can access the value of the third node. A comparison is shown of how we would access the same value in a Linked List. You can see the syntax is a little bit different than if using dictionaries. But the idea of items at different locations in memory that point to one another is similar.
