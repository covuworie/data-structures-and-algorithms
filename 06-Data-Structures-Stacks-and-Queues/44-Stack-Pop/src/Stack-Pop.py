from typing import Optional, Union

class Node:
    def __init__(self, value: int) -> None:
        self.value = value
        self.next: Optional[Node] = None
        

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

    def push(self, value: int) -> bool:
        new_node = Node(value)
        if self.height == 0:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1
        return True

    def pop(self) -> Union[Node, None]:
        if self.height == 0:
            return None
        temp = self.top
        self.top = self.top.next
        temp.next = None
        self.height -= 1
        return temp.value  # for testing only - return the actual node
    

my_stack = Stack(7)
my_stack.push(23)
my_stack.push(3)
my_stack.push(11)

print(my_stack.pop(), '\n')

my_stack.print_stack()
