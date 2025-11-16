"""Selection sort helper for linked lists.

Classes:
    SelectionSortLL: `LinkedList` subclass with an in-place selection sort.

Example:
    >>> ll = SelectionSortLL(3)
    >>> ll.append(1)
    >>> ll.selection_sort()
"""

from data_structures.linked_list import LinkedList


class SelectionSortLL(LinkedList):
    def __init__(self, value: int):
        super().__init__(value)
    
    def selection_sort(self):
        if self.length <= 1:
            return None
        current_node = self.head
        while current_node.next is not None:
            smallest_node = current_node
            inner_current_node = current_node.next
            while inner_current_node is not None:
                if inner_current_node.value < smallest_node.value:
                    smallest_node = inner_current_node
                inner_current_node = inner_current_node.next
            if smallest_node != current_node:
                smallest_node.value, current_node.value = current_node.value, smallest_node.value
            current_node = current_node.next

        # update head and tail
        current = self.head
        while current.next is not None:
            current = current.next
        self.tail = current


# Test Cases:
# -----------------------------------

# Test 1: Empty list
print("Test 1: Empty list")
ll1 = SelectionSortLL(5)
ll1.head = None
ll1.length = 0
ll1.selection_sort()
ll1.print_list()  # Should print: empty 
print("-" * 30)

# Test 2: Single element
print("Test 2: Single element")
ll2 = SelectionSortLL(5)
ll2.selection_sort()
ll2.print_list()  # Should print: 5
print("-" * 30)

# Test 3: Already sorted list
print("Test 3: Already sorted list")
ll3 = SelectionSortLL(1)
ll3.append(2)
ll3.append(3)
ll3.selection_sort()
ll3.print_list()  # Should print: 1 -> 2 -> 3
print("-" * 30)

# Test 4: Reverse order
print("Test 4: Reverse order")
ll4 = SelectionSortLL(3)
ll4.append(2)
ll4.append(1)
ll4.selection_sort()
ll4.print_list()  # Should print: 1 -> 2 -> 3
print("-" * 30)

# Test 5: Random order
print("Test 5: Random order")
ll5 = SelectionSortLL(2)
ll5.append(1)
ll5.append(3)
ll5.selection_sort()
ll5.print_list()  # Should print: 1 -> 2 -> 3
print("-" * 30)

# Test 6: List with duplicates
print("Test 6: List with duplicates")
ll6 = SelectionSortLL(3)
ll6.append(2)
ll6.append(2)
ll6.append(1)
ll6.append(3)
ll6.selection_sort()
ll6.print_list()  # Should print: 1 -> 2 -> 2 -> 3 -> 3
print("-" * 30)
