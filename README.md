# Data Structures & Algorithms

A comprehensive Python implementation of fundamental data structures, algorithms, and coding interview problems.

## 📚 Overview

This repository contains clean, well-documented implementations of essential data structures and algorithms, along with solutions to common coding interview problems. All implementations follow best practices and include Google-style docstrings for clarity.

## 🏗️ Data Structures

### Linear Data Structures
- **Linked List** - Singly linked list supporting append, prepend, pop, insert, remove, reverse, and traversal helpers
- **Doubly Linked List** - Bidirectional list with head/tail operations and node removal
- **Stack & Queue** - Classic LIFO and FIFO structures implemented with Python lists
- **Hash Table** - Open addressing hash table with collision handling

### Tree & Heap Structures
- **Binary Search Tree (BST)** - Insert, delete, search, and traversal utilities
- **Min Heap** - Priority queue keeping the minimum value at the root
- **Max Heap** - Priority queue keeping the maximum value at the root

### Graph Structures
- **Graph** - Adjacency list implementation with breadth-first and depth-first traversals

## 🔄 Algorithms

### Sorting Algorithms
- **Bubble Sort (Linked List)** - Stable linked list variant with early termination optimization
- **Selection Sort (Linked List)** - In-place linked list sorting routine
- **Insertion Sort (Linked List)** - Efficient sorter for nearly sorted linked lists
- **Merge Sort** - Divide-and-conquer sort for arrays
- **Quick Sort** - In-place partition-based sort
- **Basic Sorts** - Collection of introductory sorting implementations

## 💼 Interview Problems

Solutions to common coding interview questions organized by topic:

### Linked List Problems
- Bubble Sort on Linked List
- Selection Sort on Linked List
- Insertion Sort on Linked List

### Binary Tree Problems
- Validate Binary Search Tree
- Invert Binary Tree
- Kth Smallest Node in BST
- Sorted List to BST

### Array & Hash Table Problems
- Two Sum
- Group Anagrams
- Subarray Sum
- Find Set Pairs
- Find Max Min
- Find Longest String
- Remove Duplicates
- Remove List Element
- Kth Largest Number
- Kth Smallest Number
- Max Stream Element
- Max Trade Profit

### Hash Table & Miscellaneous Problems
- Item in Common (Hash Table)

## 📁 Project Structure

```
data_structures/
├── src/
│   ├── data_structures/      # Core data structure implementations
│   │   ├── linked_list.py
│   │   ├── doubly_linked_list.py
│   │   ├── binary_search_tree.py
│   │   ├── hash_table.py
│   │   ├── stack_and_queue.py
│   │   ├── min_heap.py
│   │   ├── max_heap.py
│   │   └── graph.py
│   ├── algorithms/           # Algorithm implementations
│   │   ├── basic_sorts.py
│   │   ├── merge_sort.py
│   │   └── quick_sort.py
│   └── interview/            # Coding interview solutions
│       ├── bubble_sort_linked_list.py
│       ├── selection_sort_linked_list.py
│       ├── insertion_sort_linked_list.py
│       ├── find_longest_string.py
│       ├── find_max_min.py
│       ├── find_set_pairs.py
│       ├── group_anagrams.py
│       ├── hast_table_1.py
│       ├── invert_binary_tree.py
│       ├── kth_largest_number.py
│       ├── kth_smallest_node_bst.py
│       ├── kth_smallest_number.py
│       ├── max_stream_element.py
│       ├── max_trade_profit.py
│       ├── remove_duplicates.py
│       ├── remove_list_element.py
│       ├── sorted_list_to_bst.py
│       ├── subarray_sum.py
│       ├── two_sum.py
│       └── validate_bst.py
└── README.md
```

## 🚀 Getting Started

### Prerequisites

- Python 3.7 or higher
- Poetry (for dependency management)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/PouriaCh/data_structures.git
cd data_structures
```

2. Install dependencies using Poetry:
```bash
poetry install
```

3. Activate the virtual environment:
```bash
poetry shell
```

## 💻 Usage Examples

### Linked List

```python
from src.data_structures.linked_list import LinkedList

# Create a linked list
ll = LinkedList(4)
ll.append(2)
ll.append(6)
ll.append(1)
ll.append(3)

# Sort the list
ll.print_list()

# Reverse the list
ll.reverse()
ll.print_list()
```

### Binary Search Tree

```python
from src.data_structures.binary_search_tree import BinarySearchTree

# Create a BST
bst = BinarySearchTree()
bst.insert(5)
bst.insert(3)
bst.insert(7)
bst.insert(1)
bst.insert(4)

# Search for a value
result = bst.contains(4)
print(result)  # True
```

## 📝 Features

- ✅ Clean, readable code with comprehensive documentation
- ✅ Google-style docstrings for all classes and methods
- ✅ Well-organized project structure
- ✅ Interview-ready implementations
- ✅ Edge case handling
- ✅ Type hints for better code clarity

## 🧪 Testing

Each implementation includes test cases and examples. Run individual files to see the implementations in action.

## 📖 Documentation

- All data structures include detailed docstrings
- Method descriptions explain parameters and return values
- Algorithm implementations include complexity analysis where applicable

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is open source and available under the MIT License.

## 👤 Author

**Pouria Chalangari**

- GitHub: [@PouriaCh](https://github.com/PouriaCh)

---

⭐ If you find this project helpful, please consider giving it a star!
