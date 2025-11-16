"""Find the maximum-sum contiguous subarray (Kadane’s problem).

Args:
    nums: List of integers. May be empty.

Returns:
    Largest possible sum of a contiguous subarray. Returns 0 when ``nums`` is empty.

Notes:
    - Subarray must contain at least one element unless the list is empty.
    - Negative numbers are allowed; the algorithm must still identify the best run.
    - Handle the empty-list edge case explicitly instead of raising.

Example:
    >>> max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
    6
"""

def max_subarray(nums):
    if len(nums) == 0:
        return 0
    
    current_sum = nums[0]
    best_sum = nums[0]
    
    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        best_sum = max(best_sum, current_sum)
    
    return best_sum
