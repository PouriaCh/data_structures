"""Validate that a BST’s in-order traversal is strictly ascending.

Classes:
    ValidateBST: Subclass of ``BinarySearchTree`` exposing ``is_valid_bst``.

Example:
    >>> tree = ValidateBST()
    >>> for value in (47, 21, 76):
    ...     tree.insert(value)
    >>> tree.is_valid_bst()
    True
"""

from data_structures.binary_search_tree import BinarySearchTree


class ValidateBST(BinarySearchTree):
    def __init__(self):
        super().__init__()
    
    def is_valid_bst(self) -> bool:
        dfs_in_order_result = self.dfs_in_order()
        for idx in range(1, len(dfs_in_order_result)):
            if dfs_in_order_result[idx - 1] > dfs_in_order_result[idx]:
                return False
        return True


if __name__ == "__main__":
    my_tree = ValidateBST()

    for value in (47, 21, 76, 18, 27, 52, 82):
        my_tree.insert(value)

    print(f"BST is valid? {my_tree.is_valid_bst()}")
