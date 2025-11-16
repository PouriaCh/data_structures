"""Bubble sort helper for linked lists.

Classes:
    BubbleSortLL: `LinkedList` subclass that exposes `bubble_sort()` to sort
        values in-place with an early-exit optimization.

Example:
    >>> ll = BubbleSortLL(4)
    >>> ll.append(2)
    >>> ll.bubble_sort()
"""

from data_structures.linked_list import LinkedList


class BubbleSortLL(LinkedList):
    def __init__(self, value: int):
        super().__init__(value)

    def bubble_sort(self):
        if self.length <= 1:
            return None
        for i in range(self.length - 1, 0, -1):
            temp = self.head
            swap_occurred = False
            for _ in range(i):
                if temp != self.tail and temp.next is not None and temp.next.value < temp.value:
                    temp.value, temp.next.value = temp.next.value, temp.value
                    swap_occurred = True
                temp = temp.next
            if not swap_occurred:
                break

        # Refresh tail pointer to last node after in-place swaps.
        current = self.head
        while current.next is not None:
            current = current.next
        self.tail = current

"""
    EXPECTED OUTPUT:
    ----------------
    Linked List Before Sort:
    4
    2
    6
    5
    1
    3

    Sorted Linked List:
    1
    2
    3
    4
    5
    6

"""


if __name__ == "__main__":
    my_linked_list = BubbleSortLL(4)
    my_linked_list.append(2)
    my_linked_list.append(6)
    my_linked_list.append(5)
    my_linked_list.append(1)
    my_linked_list.append(3)

    print("Linked List Before Sort:")
    my_linked_list.print_list()

    my_linked_list.bubble_sort()

    print("Sorted Linked List:")
    my_linked_list.print_list()
