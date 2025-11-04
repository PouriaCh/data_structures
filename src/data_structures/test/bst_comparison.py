"""
Runtime Comparison: 
1. contains (iterative) vs r_contains (recursive)
2. insert (iterative) vs r_insert (recursive)
"""

from data_structures.binary_search_tree import BinarySearchTree
import time

# ============================================================================
# 1. CONTAINS COMPARISON
# ============================================================================
print("\n" + "="*60)
print("1. CONTAINS: Iterative vs Recursive")
print("="*60)

# Build balanced tree
test_tree = BinarySearchTree()
values = [50, 25, 75, 12, 37, 62, 87, 6, 18, 31, 43, 56, 68, 81, 93]
for val in values:
    test_tree.insert(val)

# Test values
test_values = [50, 25, 93, 100]  # Root, middle, leaf, not found

print(f"{'Value':<10} {'Iterative (μs)':<20} {'Recursive (μs)':<20} {'Faster':<10}")
print("-"*60)

iterations = 50000

for val in test_values:
    # Time iterative
    start = time.time()
    for _ in range(iterations):
        test_tree.contains(val)
    iterative_time = (time.time() - start) / iterations * 1_000_000
    
    # Time recursive
    start = time.time()
    for _ in range(iterations):
        test_tree.r_contains(val)
    recursive_time = (time.time() - start) / iterations * 1_000_000
    
    faster = "Iterative" if iterative_time < recursive_time else "Recursive"
    print(f"{val:<10} {iterative_time:<20.3f} {recursive_time:<20.3f} {faster:<10}")

# ============================================================================
# 2. INSERT COMPARISON
# ============================================================================
print("\n" + "="*60)
print("2. INSERT: Iterative vs Recursive")
print("="*60)

# Values to insert
insert_values = [50, 25, 75, 12, 37, 62, 87, 6, 18, 31, 43, 56, 68, 81, 93]

print(f"{'Iterations':<15} {'Iterative (μs)':<20} {'Recursive (μs)':<20} {'Faster':<10}")
print("-"*60)

insert_iterations = 10000

# Time iterative insert
tree_iterative = BinarySearchTree()
start = time.time()
for _ in range(insert_iterations):
    # Rebuild tree each time for fair comparison
    tree_iterative = BinarySearchTree()
    for val in insert_values:
        tree_iterative.insert(val)
iterative_insert_time = (time.time() - start) / insert_iterations * 1_000_000

# Time recursive insert
tree_recursive = BinarySearchTree()
start = time.time()
for _ in range(insert_iterations):
    # Rebuild tree each time for fair comparison
    tree_recursive = BinarySearchTree()
    for val in insert_values:
        tree_recursive.r_insert(val)
recursive_insert_time = (time.time() - start) / insert_iterations * 1_000_000

faster = "Iterative" if iterative_insert_time < recursive_insert_time else "Recursive"
print(f"{insert_iterations:<15} {iterative_insert_time:<20.3f} {recursive_insert_time:<20.3f} {faster:<10}")

# ============================================================================
# SUMMARY
# ============================================================================
print("\n" + "="*60)
print("SUMMARY")
print("="*60)
print("Contains: Iterative is faster (less function call overhead)")
print("Insert: Iterative is faster (less function call overhead)")
print("\nVerdict: Recursion is NOT always better!")
print("        ✅ Iterative: Faster, less memory, no stack overflow")
print("        ✅ Recursive: Cleaner code, but slower & uses stack space")
print("="*60)

