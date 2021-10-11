class Node:
    def __init__(self, value: int) -> None:
        self.value = value
        self.next = None
        

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


my_stack = Stack(4)

my_stack.print_stack()

