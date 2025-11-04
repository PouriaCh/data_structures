from typing import Any, Optional


class Node:
    def __init__(self, value: Any):
        self.value = value
        self.next = None


class Stack:
    def __init__(self, value: Any):
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    def push(self, value: Any) -> bool:
        new_node = Node(value)
        if self.height == 0:
            self.top = new_node
        new_node.next = self.top
        self.top = new_node
        self.height += 1
        return True

    def pop(self) -> Optional[Node]:
        if self.height == 0:
            return None
        temp = self.top
        if self.height == 1:
            self.top = None
        else:
            self.top = temp.next
            temp.next = None
        self.height -= 1
        return temp

    def print_stack(self) -> None:
        temp = self.top
        while temp:
            print(temp.value)
            temp = temp.next


class Queue:
    def __init__(self, value: Any):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def enqueue(self, value: Any):
        new_node = Node(value)
        if self.length == 0:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1
        return True

    def dequeue(self) -> Optional[Node]:
        if self.length == 0:
            return None
        temp = self.first
        if self.length == 1:
            self.first = None
            self.last = None
        else:
            self.first = temp.next
            temp.next = None
        self.length -= 1
        return temp

    def print_queue(self) -> None:
        temp = self.first
        while temp:
            print(temp.value)
            temp = temp.next
