# Binary Search Tree (BST) Overview

## What is a BST?

A **Binary Search Tree** is a binary tree data structure where:
- Each node has at most 2 children (left and right)
- For any node, all values in the **left subtree** are **less than** the node's value
- All values in the **right subtree** are **greater than** the node's value
- This property holds recursively for every node

## Visual Example

```
         8
       /   \
      3     10
     / \      \
    1   6      14
       / \    /
      4   7  13
```

**BST Property**: 
- Left child < Parent < Right child
- All left descendants < Node < All right descendants

## Key Properties

1. **Ordered Structure**: Maintains elements in sorted order (in-order traversal)
2. **Hierarchical Search**: Can eliminate half the tree at each step
3. **No Guaranteed Balance**: Can become unbalanced (worst case: linear list)
4. **Dynamic Size**: Grows and shrinks as needed

## Your Implementation

Based on your code, you have:

✅ **Node Class**: Basic node with value, left, and right pointers
✅ **Insert Operation**: Iteratively adds nodes maintaining BST property
✅ **Contains Operation**: Searches for a value

## Core Operations & Complexity

### 1. **Insert** - `insert(value)`
- **Average**: O(log n)
- **Worst Case**: O(n) - when tree is unbalanced (like a linked list)
- **Best Case**: O(log n) - when tree is balanced

**Algorithm**:
```
1. Start at root
2. If value < current → go left
3. If value > current → go right
4. If spot is empty → insert
5. If duplicate → return False
```

### 2. **Search/Contains** - `contains(value)`
- **Average**: O(log n)
- **Worst Case**: O(n)
- **Best Case**: O(1) - if root is the value

**Algorithm**:
```
1. Start at root
2. If value == current → found!
3. If value < current → search left subtree
4. If value > current → search right subtree
5. If null reached → not found
```

## Missing Operations (Common in BST)

### 3. **Delete** - `delete(value)`
- **Complexity**: O(log n) average, O(n) worst case
- **Cases**: 
  - Leaf node → simple deletion
  - One child → replace with child
  - Two children → replace with inorder successor/predecessor

### 4. **Traversals**
- **In-order** (Left, Root, Right): Returns sorted order - O(n)
- **Pre-order** (Root, Left, Right): O(n)
- **Post-order** (Left, Right, Root): O(n)
- **Level-order** (BFS): O(n)

### 5. **Find Min/Max**
- **Min**: Follow leftmost path - O(log n)
- **Max**: Follow rightmost path - O(log n)

### 6. **Height/Depth**
- **Average**: O(log n)
- **Worst**: O(n)

## Advantages

✅ **Fast Search**: O(log n) average case (vs O(n) in array)
✅ **Dynamic Size**: No need to pre-allocate
✅ **Sorted Order**: In-order traversal gives sorted sequence
✅ **Flexible**: Can efficiently find range queries, nearest values
✅ **Memory Efficient**: Only stores pointers (compared to array)

## Disadvantages

❌ **No Guaranteed Balance**: Can degrade to O(n) operations
❌ **No Random Access**: Can't access by index
❌ **Extra Memory**: Each node needs 3 pointers (value, left, right)
❌ **Complex Deletion**: Requires careful handling of multiple cases

## When to Use BST

- ✅ **Frequent search operations** on sorted data
- ✅ **Dynamic data** where insertions/deletions are common
- ✅ **Range queries** (find all values between min and max)
- ✅ **Finding predecessor/successor** of a value
- ✅ **Maintaining sorted data** without full sorting

## When NOT to Use BST

❌ **Static data** → Use sorted array (better cache locality)
❌ **Need guaranteed O(log n)** → Use balanced BST (AVL, Red-Black)
❌ **Memory constrained** → Each node has overhead
❌ **Frequent duplicates** → BST typically doesn't handle well

## BST vs Other Data Structures

| Operation | BST | Sorted Array | Hash Table |
|-----------|-----|--------------|------------|
| Search | O(log n) avg | O(log n) | O(1) avg |
| Insert | O(log n) avg | O(n) | O(1) avg |
| Delete | O(log n) avg | O(n) | O(1) avg |
| Traverse (sorted) | O(n) | O(n) | N/A |
| Range Query | O(log n + k) | O(log n + k) | O(n) |

## Common BST Variants

1. **Balanced BSTs**:
   - **AVL Tree**: Self-balancing, maintains height balance
   - **Red-Black Tree**: More relaxed balance, faster inserts
   - **Splay Tree**: Recently accessed items move to root

2. **Specialized BSTs**:
   - **B-Tree**: Used in databases (multiple keys per node)
   - **Trie**: Tree for strings (not exactly BST but tree-based)

## Your Code Analysis

```python
class BinarySearchTree:
    def insert(self, value) -> bool:
        # ✅ Correctly maintains BST property
        # ✅ Returns False for duplicates
        # ⚠️  Uses iterative approach (good for space)
    
    def contains(self, value) -> bool:
        # ✅ Efficient search using BST property
        # ✅ Returns False if not found
        # ✅ Iterative (no recursion stack)
```

**Strengths**:
- Clean, iterative implementation
- No recursion (saves stack space)
- Handles duplicates correctly

**Potential Improvements**:
- Add recursive versions (often cleaner code)
- Implement delete operation
- Add traversal methods (in-order, pre-order, etc.)
- Add min/max finders
- Add height/balance checking

## Real-World Applications

1. **Databases**: Indexing and searching records
2. **File Systems**: Directory structures
3. **Expression Parsing**: Compiler syntax trees
4. **Priority Queues**: Can be used (though heaps are better)
5. **Auto-complete**: Prefix searching
6. **Symbol Tables**: Programming language implementations

## Key Takeaways

1. **BST = Ordered Binary Tree**: Maintains sort property
2. **Search = O(log n)**: But only if balanced!
3. **Dynamic Structure**: Great for changing data
4. **Versatile**: Supports many operations efficiently
5. **Balance Matters**: Unbalanced tree = poor performance

