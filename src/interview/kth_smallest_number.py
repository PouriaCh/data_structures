"""Return the k-th smallest value from an array using a max-heap.

Args:
    nums: Iterable of integers (duplicates allowed).
    k: 1-indexed rank to extract.

Returns:
    The k-th smallest value.

Example:
    >>> find_kth_smallest([3, 2, 1, 5, 6, 4], 2)
    2
"""
from data_structures.max_heap import MaxHeap


def find_kth_smallest(nums, k):
    heap = MaxHeap()
    for item in nums:
        if len(heap.heap) < k:
            heap.insert(item)
            continue
        if item < heap.heap[0]:
            heap.remove()
            heap.insert(item)
        else:
            continue
    return heap.heap[0]
    

if __name__ == "__main__":
    nums = [[3, 2, 1, 5, 6, 4], [6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6], [3, 2, 3, 1, 2, 4, 5, 5, 6]]
    ks = [2, 3, 4, 7]
    expected_outputs = [2, 3, 4, 5]

    for i, arr in enumerate(nums):
        print(f"Test case {i+1}...")
        print(f"Input: {arr} with k = {ks[i]}")
        result = find_kth_smallest(arr, ks[i])
        print(f"Output: {result}")
        print(f"Expected output: {expected_outputs[i]}")
        print(f"Test passed: {result == expected_outputs[i]}")
        print("---------------------------------------")
