from typing import Optional, Union

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
        
    def enqueue(self, value: int) -> bool:
        new_node = Node(value)
        if self.first is None:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1
        return True

    def dequeue(self) -> Union[Node, None]:
        if self.length == 0:
            return None
        temp = self.first
        if self.length == 1:
            self.first = None
            self.last = None
        else:
            self.first = self.first.next
            temp.next = None
        self.length -= 1
        return temp.value  # for testing only - should return the actual node

 
my_queue = Queue(1)
my_queue.enqueue(2)

# (2) Items - Returns 2 Node
print(my_queue.dequeue())
# (1) Item -  Returns 1 Node
print(my_queue.dequeue())
# (0) Items - Returns None
print(my_queue.dequeue())