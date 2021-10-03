# 32. DLL: Constructor

A doubly linked list is similar to the linked list we have seen previously except for it also has arrows pointing to the previous node.

![Doubly List List](./images/doubly-linked-list.jpg?raw=true "Doubly Linked List")

The code defines two classes, **Node** and the **DoublyLinkedList**.

The Node class has one responsibility - to create new nodes. We abstract this to a separate class as the following methods of the DoublyLinkedList all create a new Node.

```
class DoublyLinkedList:
    def __init__(self, value):
        create new Node
    def append(self, value):
        create new Node
        add Node to end
    def prepend(self, value):
        create new Node
        add Node to beginning
    def insert(self, index, value):
        create new Node
        insert Node at index
```

From the code, we can see that the Node constructor is similar to the one for the LinkedList except it also contains a prev field that points to None. In dictionary terms it builds something that looks like this.

```
{
    "value": 7,
    "next" None,
    "prev": None
}
```

The DoublyLinkedList constructor is identical to the LinkedList one in that it creates a new node using the Node constructor, then points head and tail to this node and initializes the length to 1.

![Doubly Linked List Constructor](./images/doubly-linked-list-constructor.jpg?raw=true "Doubly Linked List Constructor")
