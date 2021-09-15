# 20. LL: Constructor

The code defines two classes, **Node** and the **LinkedList**.

The Node class has one responsibility - to create new nodes. We abstract this to a separate class as the following methods of the LinkedList all create a new Node.

```
class LinkedList:
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

From the code, we can see that the LinkedList constructor creates a new node using the Node constructor, then points head and tail to this node and initializes the length to 1.

![Linked List Constructor](./images/linked-list-constructor.jpg?raw=true "Linked List Constructor")
