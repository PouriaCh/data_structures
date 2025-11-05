"""
BST: Validate BST ( ** Interview Question)

You are tasked with writing a method called is_valid_bst in the BinarySearchTree class that 
checks whether a binary search tree is a valid binary search tree.

Your method should use the dfs_in_order method to get the node values of the binary search tree 
in ascending order, and then check whether each node value is greater than the previous node value.

If the node values are not sorted in ascending order, the method should return False, indicating 
that the binary search tree is not valid.
If all node values are sorted in ascending order, the method should return True, 
indicating that the binary search tree is a valid binary search tree.

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