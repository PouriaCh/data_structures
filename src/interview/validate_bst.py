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
        current_value = dfs_in_order_result.pop(0)
        while len(dfs_in_order_result) > 0:
            next_value = dfs_in_order_result.pop(0)
            if current_value >= next_value:
                return False
            current_value = next_value
        return True


if __name__ == "__main__":
    my_tree = ValidateBST()

    for value in (47, 21, 76, 18, 27, 52, 82):
        my_tree.insert(value)

    print("BST is valid:")
    print(my_tree.is_valid_bst())
