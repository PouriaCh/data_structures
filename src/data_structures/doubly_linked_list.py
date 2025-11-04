from typing import Any
from linked_list import Node


class DoublyNode(Node):
    def __init__(self, value: Any):
        super().__init__(value)
        self.prev = None


class DoublyLinkedList:
    def __init__(self, value: Any):
        node = DoublyNode(value)
        self.head = node
        self.tail = node
        self.length = 1

    def append(self, value: Any):
        node = DoublyNode(value)
        if self.length == 0:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = temp.prev
            temp.prev = None
            self.tail.next = None
        self.length -= 1
        return temp

    def prepend(self, value):
        node = Node(value)
        if self.length == 0:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = temp.next
            self.head.prev = None
            temp.next = None
        self.length -= 1
        return temp

    def get(self, index: int) -> Node:
        if index < 0 or index >= self.length:
            return None
        if index < self.length/2:
            temp = self.head
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length - index - 1):
                temp = temp.prev
        return temp
    
    def set_value(self, index: int, value: Any) -> bool:
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index: int, value: Any) -> bool:
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)

        before = self.get(index - 1)
        after = before.next
        new_node = Node(value)

        new_node.prev = before
        new_node.next = after
        before.next = new_node
        after.prev = new_node

        self.length += 1
        return True

    def remove(self, index) -> Node:
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()

        temp = self.get(index)
        before = temp.prev
        after = temp.next
        
        before.next = after
        after.prev = before
        temp.next = None
        temp.prev = None
        
        return temp

    def reverse(self):
        if self.head is None:
            return None
        temp = self.head
        after = temp.next
        while temp:
            temp.next = temp.prev
            temp.prev = after
            temp = after
            if after:
                after = after.next
            
        rev_temp = self.head
        self.head = self.tail
        self.tail = rev_temp
     
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next


dlist = DoublyLinkedList(1)
dlist.append(2)
dlist.print_list()