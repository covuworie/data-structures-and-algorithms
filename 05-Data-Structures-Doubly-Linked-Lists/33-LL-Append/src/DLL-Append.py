from typing import Optional

class Node:
    def __init__(self, value: int) -> None:
        self.value = value
        self.next: Optional[Node] = None
        self.prev: Optional[Node] = None
        

class DoublyLinkedList:
    def __init__(self, value: int) -> None:
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self) -> None:
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
        
    def append(self, value: int) -> bool:
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True
  

my_doubly_linked_list = DoublyLinkedList(1)
my_doubly_linked_list.append(2)

my_doubly_linked_list.print_list()

