"""Emit the running maximum of a stream using a max-heap.

Args:
    nums: Iterable of integers.

Returns:
    List where ``result[i]`` equals ``max(nums[0:i+1])``.

Example:
    >>> stream_max([1, 3, 2, 5, 4])
    [1, 3, 3, 5, 5]
"""
from data_structures.max_heap import MaxHeap


def stream_max(nums):
    stream_output = []
    heap = MaxHeap()
    for item in nums:
        if len(heap.heap) == 0:
            heap.insert(item)
        if item > heap.heap[0]:
            heap.remove()
            heap.insert(item)
        stream_output.append(heap.heap[0])
    return stream_output


if __name__ == "__main__":
    test_cases = [
        ([], []),
        ([1], [1]),
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
        ([1, 2, 2, 1, 3, 3, 3, 2, 2], [1, 2, 2, 2, 3, 3, 3, 3, 3]),
        ([-1, -2, -3, -4, -5], [-1, -1, -1, -1, -1]),
    ]

    for i, (nums, expected) in enumerate(test_cases):
        result = stream_max(nums)
        print(f"\nTest {i+1}")
        print(f"Input: {nums}")
        print(f"Expected Output: {expected}")
        print(f"Actual Output: {result}")
        print("Status:", "Passed" if result == expected else "Failed")
