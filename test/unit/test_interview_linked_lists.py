import unittest

from data_structures.linked_list import LinkedList
from interview.bubble_sort_linked_list import BubbleSortLL
from interview.insertion_sort_linked_list import InsertionSortLL
from interview.selection_sort_linked_list import SelectionSortLL


def build_linked_list(cls, values):
    if not values:
        return None

    linked_list = cls(values[0])
    for value in values[1:]:
        linked_list.append(value)
    return linked_list


def to_python_list(linked_list):
    values = []
    current = linked_list.head
    while current is not None:
        values.append(current.value)
        current = current.next
    return values


class TestRemoveDuplicatesLL(unittest.TestCase):
    def test_remove_duplicates_empty_ll(self):
        ll = LinkedList(None)
        self.assertIsNone(ll.remove_duplicates())

    def test_remove_duplicates_no_duplicate(self):
        ll = build_linked_list(LinkedList, [4, 2, 6, 5, 1, 3])
        ll.remove_duplicates()
        self.assertEqual(to_python_list(ll), [4, 2, 6, 5, 1, 3])
    
    def test_remove_duplicates_sorted_values(self):
        ll = build_linked_list(LinkedList, [1, 1, 2, 3, 3, 4, 5, 5, 6])
        ll.remove_duplicates()
        self.assertEqual(to_python_list(ll), [1, 2, 3, 4, 5, 6])

    def test_remove_duplicates_shuffled_list(self):
        ll = build_linked_list(LinkedList, [4, 1, 6, 2, 4, 3, 1, 4, 5, 2, 1])
        ll.remove_duplicates()
        self.assertEqual(to_python_list(ll), [4, 1, 6, 2, 3, 5])


class TestBubbleSortLL(unittest.TestCase):
    def test_sorts_values(self):
        ll = build_linked_list(BubbleSortLL, [4, 2, 6, 5, 1, 3])
        ll.bubble_sort()
        self.assertEqual(to_python_list(ll), [1, 2, 3, 4, 5, 6])


class TestInsertionSortLL(unittest.TestCase):
    def test_sorts_values(self):
        ll = build_linked_list(InsertionSortLL, [4, 3, 2, 1])
        ll.insertion_sort()
        self.assertEqual(to_python_list(ll), [1, 2, 3, 4])


class TestSelectionSortLL(unittest.TestCase):
    def test_sorts_values_with_duplicates(self):
        ll = build_linked_list(SelectionSortLL, [3, 2, 2, 1, 3])
        ll.selection_sort()
        self.assertEqual(to_python_list(ll), [1, 2, 2, 3, 3])
