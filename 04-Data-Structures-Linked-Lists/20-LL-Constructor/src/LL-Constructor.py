from typing import Optional

class Node:
    def __init__(self, value: int) -> None:
        self.value = value
        self.next: Optional[Node] = None


class LinkedList:
    def __init__(self, value: int) -> None:
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

 
my_linked_list = LinkedList(4)

print(f"Head value: {my_linked_list.head.value}")
print(f"Tail value: {my_linked_list.tail.value}")
print(f"Length: {my_linked_list.length}")                                                                                                                                                                                                                                                              
