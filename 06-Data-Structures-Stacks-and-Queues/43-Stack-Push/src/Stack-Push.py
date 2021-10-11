from typing import Optional

class Node:
    def __init__(self, value: int) -> None:
        self.value = value
        self.next: Optional[None] = None
        

class Stack:
    def __init__(self, value: int) -> None:
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    def print_stack(self) -> None:
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def push(self, value: int) -> None:
        new_node = Node(value)
        if self.height == 0:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1
 

my_stack = Stack(2)
my_stack.push(1)

my_stack.print_stack()
