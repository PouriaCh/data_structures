"""
Heap: Kth Largest Element in an Array

You are given a list of numbers called nums and a number k. Your task is to write a function find_kth_largest(nums, k)
to find the kth largest number in the list. The list can contain duplicate numbers and k is guaranteed to be within the
range of the length of the list.

This function will take the following parameters:
    nums: A list of integers.
    k: An integer.

This function should return the kth largest number in nums.


Example 1:

nums = [3, 2, 1, 5, 6, 4]
k = 2
print(find_kth_largest(nums, k))
In the example above, the function should return 5. If we sort the list in descending order, it becomes [6, 5, 4, 3, 2, 1]. 
The 2nd largest number is 5, so the function returns 5.


Example 2:

nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
k = 4
print(find_kth_largest(nums, k))

In the example above, the function should return 4. If we sort the list in descending order, it becomes [6, 5, 5, 4, 3, 3, 2, 2, 1].
The 4th largest number is 4, so the function returns 4.

Note: For the purpose of this problem, we assume that duplicate numbers are counted as separate numbers. For example, 
in the second example above, the two 5s are counted as the 2nd and 3rd largest numbers, and the two 3s are counted 
as the 4th and 5th largest numbers. Please write your solution in Python and use a min heap data structure to solve 
this problem. The MinHeap class is provided for you.

Note: This is a separate function, not a method in the MinHeap class so you will need to indent all the way to the left.
"""
from data_structures.min_heap import MinHeap


def find_kth_largest(nums, k):
    heap = MinHeap()
    for item in nums:
        if len(heap.heap) < k:
            heap.insert(item)
            continue
        if item > heap.heap[0]:
            heap.remove()
            heap.insert(item)
        else:
            continue
    return heap.heap[0]

# Test cases
nums = [[3,2,1,5,6,4], [6,5,4,3,2,1], [1,2,3,4,5,6], [3,2,3,1,2,4,5,5,6]]
ks = [2, 3, 4, 7]
expected_outputs = [5, 4, 3, 2]

for i in range(len(nums)):
    print(f'Test case {i+1}...')
    print(f'Input: {nums[i]} with k = {ks[i]}')
    result = find_kth_largest(nums[i], ks[i])
    print(f'Output: {result}')
    print(f'Expected output: {expected_outputs[i]}')
    print(f'Test passed: {result == expected_outputs[i]}')
    print('---------------------------------------')


"""
    EXPECTED OUTPUT:
    ----------------
    Test case 1...
    Input: [3, 2, 1, 5, 6, 4] with k = 2
    Output: 5
    Expected output: 5
    Test passed: True
    ---------------------------------------
    Test case 2...
    Input: [6, 5, 4, 3, 2, 1] with k = 3
    Output: 4
    Expected output: 4
    Test passed: True
    ---------------------------------------
    Test case 3...
    Input: [1, 2, 3, 4, 5, 6] with k = 4
    Output: 3
    Expected output: 3
    Test passed: True
    ---------------------------------------
    Test case 4...
    Input: [3, 2, 3, 1, 2, 4, 5, 5, 6] with k = 7
    Output: 2
    Expected output: 2
    Test passed: True
    ---------------------------------------
"""
