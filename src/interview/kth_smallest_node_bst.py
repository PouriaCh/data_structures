"""Retrieve the k-th smallest value from a BST via in-order traversal.

Classes:
    KthSmallestNode: Extends ``BinarySearchTree`` with ``kth_smallest(k)``.

Returns:
    Node value when ``k`` is within bounds, otherwise ``None``.

Example:
    >>> bst = KthSmallestNode()
    >>> for value in (5, 3, 7):
    ...     bst.insert(value)
    >>> bst.kth_smallest(2)
    5
"""

from typing import List
from data_structures.binary_search_tree import BinarySearchTree, Node


class KthSmallestNode(BinarySearchTree):
    def __init__(self):
        super().__init__()
    
    def kth_smallest(self, k: int):
        if self.root is None:
            return None

        results: List[int] = []
        
        def traverse(current_node: Node):
            if current_node.left is not None:
                traverse(current_node.left)
            results.append(current_node.value)
            if current_node.right is not None:
                traverse(current_node.right)
        
        traverse(self.root)

        if (k - 1) >= 0 and (k - 1) < len(results):
            return results[k - 1]
        return None


if __name__ == "__main__":
    bst = KthSmallestNode()

    bst.insert(5)
    bst.insert(3)
    bst.insert(7)
    bst.insert(2)
    bst.insert(4)
    bst.insert(6)
    bst.insert(8)

    print(bst.kth_smallest(1))  # Expected output: 2
    print(bst.kth_smallest(3))  # Expected output: 4
    print(bst.kth_smallest(6))  # Expected output: 7
