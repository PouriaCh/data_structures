"""
BST: Kth Smallest Node ( ** Interview Question)

Given a binary search tree, find the kth smallest element in the tree. For example, 
if the tree contains the elements [1, 2, 3, 4, 5], the 3rd smallest element would be 3.

The solution to this problem usually involves traversing the tree in-order (left, root, right) 
and keeping track of the number of nodes visited until you find the kth smallest element. 
There are two main approaches to doing this:

    1. Iterative approach using a stack: This approach involves maintaining a stack of nodes 
    that still need to be visited, starting with the leftmost node. At each step, 
    you pop a node off the stack, decrement the kth smallest counter, and check whether you 
    have found the kth smallest element. If you have not, you continue traversing the tree by 
    moving to the right child of the current node.

    2. Recursive approach: This approach involves recursively traversing the tree in-order 
    and keeping track of the number of nodes visited until you find the kth smallest element. 
    You can use a helper function that takes a node and a value of k as input, and recursively 
    calls itself on the left and right children of the node until it finds the kth smallest element.

Both of these approaches have their own advantages and disadvantages, and the best approach to use may depend on the specific problem constraints and the interviewer's preferences.

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


"""
    EXPECTED OUTPUT:
    ----------------
    2
    4
    7

 """
