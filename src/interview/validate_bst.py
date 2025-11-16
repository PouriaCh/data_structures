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


my_tree = ValidateBST()

my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)

print("BST is valid:")
print(my_tree.is_valid_bst())



"""
    EXPECTED OUTPUT:
    ----------------
    BST is valid:
    True

"""
