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
    while current:
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


class TestReverseBetween(unittest.TestCase):
    def test_01_middle_section(self):
        ll = build_linked_list(LinkedList, [1, 2, 3, 4, 5])
        ll.reverse_between(1, 3)
        self.assertEqual(to_python_list(ll), [1, 4, 3, 2, 5])

    def test_02_reverse_from_start(self):
        ll = build_linked_list(LinkedList, [10, 20, 30, 40])
        ll.reverse_between(0, 2)
        self.assertEqual(to_python_list(ll), [30, 20, 10, 40])

    def test_03_reverse_to_end(self):
        ll = build_linked_list(LinkedList, [1, 2, 3, 4, 5])
        ll.reverse_between(2, 4)
        self.assertEqual(to_python_list(ll), [1, 2, 5, 4, 3])
        self.assertEqual(ll.tail.value, 3)

    def test_04_full_list_reversal(self):
        ll = build_linked_list(LinkedList, [1, 2, 3])
        ll.reverse_between(0, 2)
        self.assertEqual(to_python_list(ll), [3, 2, 1])
        self.assertEqual(ll.tail.value, 1)

    def test_05_single_node_no_op(self):
        ll = build_linked_list(LinkedList, [42])
        ll.reverse_between(0, 0)
        self.assertEqual(to_python_list(ll), [42])
        self.assertEqual(ll.tail.value, 42)

    def test_06_start_equals_end(self):
        ll = build_linked_list(LinkedList, [1, 2, 3, 4, 5])
        ll.reverse_between(3, 3)
        self.assertEqual(to_python_list(ll), [1, 2, 3, 4, 5])
        self.assertEqual(ll.tail.value, 5)

    def test_07_two_nodes_swap(self):
        ll = build_linked_list(LinkedList, [1, 2])
        ll.reverse_between(0, 1)
        self.assertEqual(to_python_list(ll), [2, 1])
        self.assertEqual(ll.tail.value, 1)

    def test_08_reverse_last_two(self):
        ll = build_linked_list(LinkedList, [10, 20, 30, 40])
        ll.reverse_between(2, 3)
        self.assertEqual(to_python_list(ll), [10, 20, 40, 30])
        self.assertEqual(ll.tail.value, 30)

    def test_09_empty_list(self):
        ll = LinkedList(None)
        ll.pop()
        ll.reverse_between(0, 5)
        self.assertEqual(to_python_list(ll), [])
        self.assertIsNone(ll.head)

    def test_10_invalid_indices_do_nothing(self):

        ll = build_linked_list(LinkedList, [5, 10, 15])
        original_tail = ll.tail.value
        ll.reverse_between(10, 15)   # Out of bounds → should do nothing
        self.assertEqual(to_python_list(ll), [5, 10, 15])
        self.assertEqual(ll.tail.value, original_tail)

    def test_11_tail_correct_after_reversing_to_end(self):
        ll = build_linked_list(LinkedList, [1, 2, 3, 4])
        ll.reverse_between(1, 3)
        self.assertEqual(to_python_list(ll), [1, 4, 3, 2])
        self.assertEqual(ll.tail.value, 2)   # Original node at index 1 → now tail


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
