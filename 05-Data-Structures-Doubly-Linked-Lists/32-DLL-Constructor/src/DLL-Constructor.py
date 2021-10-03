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
  

my_doubly_linked_list = DoublyLinkedList(7)

my_doubly_linked_list.print_list()
print(f"Head value: {my_doubly_linked_list.head.value}")
print(f"Tail value: {my_doubly_linked_list.tail.value}")
print(f"Length: {my_doubly_linked_list.length}")  
