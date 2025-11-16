"""Convert a sorted list into a height-balanced BST via divide-and-conquer.

The module exposes ``BinarySearchTree.sorted_list_to_bst(nums)`` which picks the
middle element as the root, recurses on both halves, and returns the new root.

Example:
    >>> bst = BinarySearchTree()
    >>> bst.sorted_list_to_bst([-10, -3, 0, 5, 9])
"""
