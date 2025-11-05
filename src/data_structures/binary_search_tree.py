import re
from typing import List
from unittest import result


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value) -> bool:
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while True:
            if temp.value == new_node.value:
                return False
            if temp.value > new_node.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.value < new_node.value:
                    if temp.right is None:
                        temp.right = new_node
                        return True
                    temp = temp.right

    def contains(self, value) -> bool:
        temp = self.root
        while temp:
            if temp.value == value:
                return True
            if temp.value > value:
                temp = temp.left
            elif temp.value < value:
                temp = temp.right
        return False

    def __r_contains(self, current_node, value) -> bool:
        # if node is None
        if current_node is None:
            return False
        # current node's value
        if current_node.value == value:
            return True
        # traverse to left or right nodes
        if value > current_node.value:
            return self.__r_contains(current_node.right, value)
        else:
            return self.__r_contains(current_node.left, value)
    
    def r_contains(self, value):
        return self.__r_contains(self.root, value)

    def __r_insert(self, current_node, value):
        if current_node is None:
            return Node(value)
        if value > current_node.value:
            current_node.right = self.__r_insert(current_node.right, value)
        if value < current_node.value:
            current_node.left = self.__r_insert(current_node.left, value)
        return current_node

    def r_insert(self, value):
        if self.root is None:
            self.root = Node(value)
        self.__r_insert(self.root, value)

    def __r_delete(self, current_node, value):
        if current_node is None:
            return None
        if value > current_node.value:
            current_node.right = self.__r_delete(current_node.right, value)
        elif value < current_node.value:
            current_node.left = self.__r_delete(current_node.left, value)
        else:
            if current_node.left is None and current_node.right is None:
                return None
            elif current_node.left is None:
                current_node = current_node.right
            elif current_node.right is None:
                current_node = current_node.left
            else:
                sub_tree_min = BinarySearchTree.min_value(current_node.right)
                current_node.value = sub_tree_min
                current_node.right = self.__r_delete(current_node.right, sub_tree_min)
        return current_node
    
    def r_delete(self, value):
        self.__r_delete(self.root, value)

    @staticmethod
    def min_value(current_node):
        while current_node.left is not None:
            current_node = current_node.left
        return current_node.value
    
    @staticmethod
    def max_value(current_node):
        while current_node.right is not None:
            current_node = current_node.right
        return current_node.value

    def print_tree(self):
        """Print the tree structure in a visual format (Right on top, Left on bottom)"""
        if self.root is None:
            print("Tree is empty")
            return
        print(str(self.root.value))
        if self.root.left or self.root.right:
            if self.root.right:
                self._print_tree(self.root.right, "", False)  # Right child first (top)
            if self.root.left:
                self._print_tree(self.root.left, "", True)     # Left child second (bottom)

    def _print_tree(self, node, prefix, is_left):
        """Helper method for printing tree"""
        if node:
            symbol = "└── " if is_left else "├── "
            print(prefix + symbol + str(node.value))
            
            if node.left or node.right:
                extend = prefix + ("    " if is_left else "│   ")
                # Print right child first (top) if exists
                if node.right:
                    self._print_tree(node.right, extend, False)
                # Print left child second (bottom) if exists
                if node.left:
                    self._print_tree(node.left, extend, True)

    def BFS(self):
        queue: List[Node] = []
        queue.append(self.root)
        results: List[int] = []
        while len(queue) > 0:
            current_node = queue.pop(0)
            results.append(current_node.value)
            if current_node.left is not None:
                queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)
        return results

    def dfs_pre_order(self):
        results: List[int] = []

        def traverse(current_node: Node):
            results.append(current_node.value)
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)
    
        traverse(self.root)
        return results

    def dfs_post_order(self):
        results: List[int] = []

        def traverse(current_node: Node):
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)
            results.append(current_node.value)
    
        traverse(self.root)
        return results
    
    def dfs_in_order(self):
        results: List[int] = []

        def traverse(current_node: Node):
            if current_node.left is not None:
                traverse(current_node.left)
            results.append(current_node.value)
            if current_node.right is not None:
                traverse(current_node.right)
    
        traverse(self.root)
        return results


# Example usage
if __name__ == "__main__":
    bst = BinarySearchTree()
    bst.insert(47)
    bst.insert(21)
    bst.insert(76)
    bst.insert(18)
    bst.insert(27)
    bst.insert(52)
    bst.insert(82)
    
    print("BST Structure:")
    bst.print_tree()
   
    print(f"BFS: {bst.BFS()}")
    print(f"DFS PreOrder: {bst.dfs_pre_order()}")
    print(f"DFS PostOrder: {bst.dfs_post_order()}")
    print(f"DFS InOrder: {bst.dfs_in_order()}")