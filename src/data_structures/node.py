from typing import Any


class LinkedListNode:
    def __init__(self, value: Any):
        self.value = value
        self.next = None


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
