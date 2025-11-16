"""Insertion sort helper for linked lists.

Classes:
    InsertionSortLL: `LinkedList` subclass whose ``insertion_sort`` method
        rebuilds the list in-place by walking the sorted prefix.

Example:
    >>> ll = InsertionSortLL(4)
    >>> ll.append(2)
    >>> ll.insertion_sort()
"""

from data_structures.linked_list import LinkedList


class InsertionSortLL(LinkedList):
    def __init__(self, value: int):
        super().__init__(value)
    
    def insertion_sort(self):
        if self.length <= 1:
            return None
        
        sorted_list_head = self.head
        unsorted_list_head = self.head.next
        sorted_list_head.next = None
        
        while unsorted_list_head is not None:
            current = unsorted_list_head
            unsorted_list_head = unsorted_list_head.next
            
            if current.value < sorted_list_head.value:
                current.next = sorted_list_head
                sorted_list_head = current
            else:
                search_pointer = sorted_list_head
                while search_pointer.next is not None and current.value > search_pointer.next.value:
                    search_pointer = search_pointer.next
                current.next = search_pointer.next
                search_pointer.next = current
        
        self.head = sorted_list_head
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        self.tail = temp 


if __name__ == "__main__":
    my_linked_list = InsertionSortLL(4)
    my_linked_list.append(2)
    my_linked_list.append(6)
    my_linked_list.append(5)
    my_linked_list.append(1)
    my_linked_list.append(3)

    print("Linked List Before Sort:")
    my_linked_list.print_list()

    my_linked_list.insertion_sort()

    print("\nSorted Linked List:")
    my_linked_list.print_list()

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
