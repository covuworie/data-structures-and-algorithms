from typing import Optional

class Node:
    def __init__(self, value: int) -> None:
        self.value = value
        self.next: Optional[int] = None
        

class LinkedList:
    def __init__(self, value: int) -> None:
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self) -> None:
        node = self.head
        while node is not None:
            print(node.value)
            node = node.next
        
    def append(self, value: int) -> None:
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1


my_linked_list = LinkedList(1)

my_linked_list.append(2)

my_linked_list.print_list()
                         