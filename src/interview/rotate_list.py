"""Rotate a list of integers to the right by ``k`` positions in-place.

Args:
    nums: List of integers to rotate.
    k: Non-negative number of steps to rotate to the right.

Returns:
    None. The input list is modified directly.

Example:
    >>> nums = [1, 2, 3, 4, 5, 6, 7]
    >>> rotate(nums, 3)
    >>> nums
    [5, 6, 7, 1, 2, 3, 4]
"""

def rotate(nums, k):
    length = len(nums)
    if length <= 1 or k == 0 or k == length:
        return None
    if length < k:
        k %= length
    while k > 0:
        for i in range(len(nums) - 2, -1, -1):
            nums[i], nums[i+1] = nums[i+1], nums[i]
        k -= 1

