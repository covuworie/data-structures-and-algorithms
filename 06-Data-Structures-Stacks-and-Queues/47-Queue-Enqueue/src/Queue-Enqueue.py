from typing import Optional

class Node:
    def __init__(self, value: int) -> None:
        self.value = value
        self.next: Optional[Node] = None
        

class Queue:
    def __init__(self, value: int) -> None:
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def print_queue(self) -> None:
        temp = self.first
        while temp is not None:
            print(temp.value)
            temp = temp.next
        
    def enqueue(self, value: int) -> None:
        new_node = Node(value)
        if self.first is None:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1
        

my_queue = Queue(1)
my_queue.enqueue(2)

my_queue.print_queue()
