# Mini-Course Cheat Sheet

Very-short reminders for the main structures in this repo. Each section links to the most relevant implementation and interview practice file.

---

## 1. Linear Containers (Arrays, Python Lists, Slices)
**Mental model:** Contiguous block of memory; random access is instant, inserts/removals cost proportional to the shift.

| Operation | Avg. Time | Notes |
| --- | --- | --- |
| Index read/write | `O(1)` | CPU-friendly cache hits. |
| Append / pop end | `O(1)` amortized | Python list over-allocates space. |
| Insert / delete middle | `O(n)` | Everything after the position shifts. |

- **Use when:** you need fast indexed access, binary search, or sliding windows.
- **Pitfalls:** forgetting to copy when slicing (`foo[:]`) or assuming deletes are cheap.
- **Repo refresher:** `src/interview/max_sub_array.py`, `src/interview/two_sum.py`.
- **Practice prompt:** Re-run `max_sub_array` but also return the start/end indices.

---

## 2. Linked Lists (Singly & Doubly)
**Mental model:** Nodes pointing to the next (and optionally previous) node; great for frequent insert/delete when you already have a pointer.

| Operation | Singly | Doubly | Notes |
| --- | --- | --- | --- |
| Insert/delete at head | `O(1)` | `O(1)` | Most efficient position. |
| Insert/delete at tail | `O(n)` unless tail pointer | `O(1)` with tail | Track `tail` to avoid traversal. |
| Search / index | `O(n)` | `O(n)` | Sequential scan only. |

- **Tricks:** swap node values to avoid pointer surgery during simple sorts (see `BubbleSortLL`).
- **Pitfalls:** losing references (forgetting to update `tail`) or not handling empty/singleton cases.
- **Repo refresher:** `src/data_structures/linked_list.py`, `src/interview/bubble_sort_linked_list.py`, `src/interview/remove_list_element.py`.
- **Practice prompt:** Implement a `reverse_between(left, right)` method in `LinkedList`.

---

## 3. Stacks & Queues
**Mental model:** Constrained linear structures—LIFO for stacks, FIFO for queues—often backed by lists or `collections.deque`.

| Structure | Core ops | Time | Typical uses |
| --- | --- | --- | --- |
| Stack | `push`, `pop`, `peek` | `O(1)` | DFS, undo, expression parsing |
| Queue | `enqueue`, `dequeue`, `front` | `O(1)` | BFS, producer/consumer |

- **Pitfalls:** using Python lists for queues without `collections.deque` (popped front is `O(n)`).
- **Repo refresher:** `src/data_structures/stack_and_queue.py`, `src/interview/max_stream_element.py`.
- **Practice prompt:** Implement a monotonic queue to maintain sliding-window maximums.

---

## 4. Hash Tables & Sets
**Mental model:** Key → bucket array via hashing; collisions resolved by chaining or probing.

| Operation | Avg. Time | Worst |
| --- | --- | --- |
| Insert / lookup / delete | `O(1)` amortized | `O(n)` if everything collides |

- **Strengths:** constant-time membership tests, flexible keys.
- **Pitfalls:** mutable keys (don’t hash lists), poor hash functions, forgetting load-factor rehash cost.
- **Repo refresher:** `src/data_structures/hash_table.py`, `src/interview/group_anagrams.py`, `src/interview/find_set_pairs.py`.
- **Practice prompt:** Re-implement `two_sum` using a custom `HashTable` from `src/data_structures/hash_table.py`.

---

## 5. Trees & Binary Search Trees
**Mental model:** Hierarchical structure with parent/child links. BST property: left subtree < node < right subtree.

| Operation | Balanced BST | Skewed |
| --- | --- | --- |
| Search / insert / delete | `O(log n)` | `O(n)` |

- **Traversals:** in-order (sorted output), pre-order (serialize), post-order (delete/evaluate). BFS via queue for level-order.
- **Pitfalls:** ignoring balance (use AVL/Red-Black/TreeMap equivalent if worst-case matters), mishandling parent pointers on delete.
- **Repo refresher:** `src/data_structures/binary_search_tree.py`, `src/interview/validate_bst.py`, `src/interview/kth_smallest_node_bst.py`.
- **Practice prompt:** Augment the BST node with subtree counts to support `kth_smallest` in `O(log n)`.

---

## 6. Heaps & Priority Queues
**Mental model:** Complete binary tree stored as an array; parent/child indices derived arithmetically.

| Operation | Min/Max Heap Time | Notes |
| --- | --- | --- |
| Insert (`heapify up`) | `O(log n)` | Append, bubble up. |
| Extract root | `O(log n)` | Swap with last, pop, bubble down. |
| Peek root | `O(1)` | No structural change. |

- **Patterns:** top-`k`, running medians, scheduling.
- **Pitfalls:** forgetting heaps are not sorted arrays; you only know the extreme element.
- **Repo refresher:** `src/data_structures/min_heap.py`, `src/data_structures/max_heap.py`, `src/interview/kth_largest_number.py`, `src/interview/kth_smallest_number.py`.
- **Practice prompt:** Implement a streaming median using one max-heap + one min-heap.

---

## 7. Graphs
**Mental model:** Vertices + edges (directed/undirected, weighted/unweighted). Represent via adjacency list for sparse graphs.

| Traversal | Data structure | When to use |
| --- | --- | --- |
| BFS | Queue | Shortest paths in unweighted graphs, level processing |
| DFS | Stack/recursion | Connectivity, cycle detection, topological sort |

- **Pitfalls:** not marking visited nodes (infinite loops), mixing zero-based/one-based indices.
- **Repo refresher:** `src/data_structures/graph.py`, `src/interview/invert_binary_tree.py` (tree BFS/DFS warm-up).
- **Practice prompt:** Add `shortest_path(start, target)` to `Graph` using BFS.

---

## 8. Algorithmic Patterns (Quick Reminders)
- **Sliding Window:** Maintain start/end pointers for contiguous problems; update counts/invariants incrementally. See `src/interview/subarray_sum.py`.
- **Two Pointers:** Opposite ends or fast/slow pointer techniques; excellent for deduping sorted data (`src/interview/remove_duplicates.py`).
- **Divide & Conquer:** Split, solve, combine; powers merge sort (`src/algorithms/merge_sort.py`) and quickselect.
- **Greedy:** Make locally optimal choice (e.g., `src/interview/max_trade_profit.py` for one-trade stock profit).
- **Heap + Hash Hybrid:** Track top-k frequent elements or streaming medians (combine `src/data_structures/min_heap.py` with `src/interview/max_stream_element.py`).

Use these heuristics to choose the structure before coding; the rest of the repo provides the concrete implementations.
