import unittest

from interview.invert_binary_tree import BinarySearchTree, tree_to_list
from interview.kth_largest_number import find_kth_largest
from interview.kth_smallest_node_bst import KthSmallestNode
from interview.kth_smallest_number import find_kth_smallest
from interview.validate_bst import ValidateBST


class TestKthLargest(unittest.TestCase):
    def test_basic_case(self):
        self.assertEqual(find_kth_largest([3, 2, 1, 5, 6, 4], 2), 5)

    def test_with_duplicates(self):
        self.assertEqual(find_kth_largest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4), 4)


class TestKthSmallest(unittest.TestCase):
    def test_basic_case(self):
        self.assertEqual(find_kth_smallest([3, 2, 1, 5, 6, 4], 2), 2)

    def test_with_duplicates(self):
        self.assertEqual(find_kth_smallest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4), 3)


class TestKthSmallestNode(unittest.TestCase):
    def test_kth_smallest_lookup(self):
        bst = KthSmallestNode()
        for value in (5, 3, 7, 2, 4, 6, 8):
            bst.insert(value)
        self.assertEqual(bst.kth_smallest(1), 2)
        self.assertEqual(bst.kth_smallest(4), 5)
        self.assertIsNone(bst.kth_smallest(10))


class TestValidateBST(unittest.TestCase):
    def test_valid_bst(self):
        tree = ValidateBST()
        for value in (47, 21, 76, 18, 27, 52, 82):
            tree.insert(value)
        self.assertTrue(tree.is_valid_bst())

    def test_invalid_bst(self):
        tree = ValidateBST()
        for value in (10, 5, 15):
            tree.insert(value)
        tree.root.left.value = 20  # Break BST invariant
        self.assertFalse(tree.is_valid_bst())


class TestInvertBinaryTree(unittest.TestCase):
    def test_inversion(self):
        bst = BinarySearchTree()
        for value in (47, 21, 76, 18, 27, 52, 82):
            bst.r_insert(value)
        bst.invert()
        self.assertEqual(tree_to_list(bst.root), [47, 76, 21, 82, 52, 27, 18])
