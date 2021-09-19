from typing import Optional, Union

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
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
        
    def append(self, value: int) -> bool:
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def pop(self) -> Union[Node, None]:
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while(temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def prepend(self, value: int) -> bool:
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self) -> Union[Node, None]:
        # edge case - no items
        if self.length == 0:
            return None
        # main case - 2 or more items
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        # edge case - 1 item
        if self.length == 0:
            self.tail = None
        return temp.value  # for testing => should return the Node


my_linked_list = LinkedList(2)
my_linked_list.append(1)


# (2) Items - Returns 2 Node
print(my_linked_list.pop_first())
# (1) Item -  Returns 1 Node
print(my_linked_list.pop_first())
# (0) Items - Returns None
print(my_linked_list.pop_first())


