from typing import Any


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        node = Node(value)
        self.head = node
        self.tail = node
        self.length = 1
    
    def append(self, value) -> bool:
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def pop(self) -> Node:
        if self.length == 0:
            return None

        pop_node = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            temp_node = self.head
            while temp_node.next is not self.tail:
                temp_node = temp_node.next
            self.tail = temp_node
            self.tail.next = None
        self.length -= 1
        return pop_node

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self) -> Node:
        if self.length == 0:
            return None

        pop_node = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            temp_head = self.head.next
            self.head.next = None
            self.head = temp_head
        self.length -= 1
        return pop_node

    def get(self, index: int) -> Node:
        if 0 <= index < self.length:
            temp_node = self.head
            for _ in range(index):
                temp_node = temp_node.next
            return temp_node
        return None

    def set_value(self, index: int, value: Any) -> bool:
        target_node = self.get(index)
        if target_node is not None:
            target_node.value = value
            return True
        return False

    def insert(self, index: int, value: Any) -> bool:
        if 0 <= index <= self.length:
            previous_node = self.get(index - 1)
            if previous_node is None:
                return self.prepend(value)
            if previous_node.next is None:
                return self.append(value)
            new_node = Node(value)
            new_node.next = previous_node.next
            previous_node.next = new_node
            self.length += 1
            return True
        return False

    def remove(self, index: int) -> Node:
        if 0 <= index <= self.length:
            previous_node = self.get(index - 1)
            if previous_node is None:
                return self.pop_first()
            if previous_node.next is None:
                return self.pop()
            target_node = previous_node.next
            previous_node.next = target_node.next
            target_node.next = None
            self.length -= 1
            return target_node
        return None

    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        post_temp = temp.next
        prev_temp = None
        for _ in range(self.length):
            post_temp = temp.next
            temp.next = prev_temp
            prev_temp = temp
            temp = post_temp

    def remove_duplicates(self) -> Node:
        if self.head is None:
            return None
        output = self.head
        temp = self.head.next
        values = set()
        values.add(output.value)
        while temp:
            if temp.value not in values:
                values.add(temp.value)
                output.next = temp
                output = output.next
            else:
                output.next = temp.next
            temp = temp.next
        return output

    def print_list(self):
        print(30 * "#")
        temp_node = self.head
        while temp_node is not None:
            print(temp_node.value)
            temp_node = temp_node.next

    def reverse_between(self, start_index: int, end_index: int):
        if not self.head or not self.head.next:
            return None
        start_node = self.head
        for _ in range(start_index):
            start_node = start_node.next
        end_node = start_node
        for _ in range(end_index - start_index):
            if end_node:
                end_node = end_node.next
        
        temp = start_node
        start_node = end_node
        end_node = temp
        after = temp.next
        before = None
        while temp:
            after = temp.next
            temp.next = before
            before = temp
            temp = after
