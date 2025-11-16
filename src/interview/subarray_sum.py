"""Return indices of a contiguous subarray that sums to ``target``.

Args:
    nums: List of integers (may include negatives).
    target: Desired sum.

Returns:
    ``[start, end]`` indices for any matching subarray, or ``[]`` if none exist.

Example:
    >>> subarray_sum([1, 2, 3, 4, 5], 9)
    [1, 3]
"""
# WRITE TWO_SUM FUNCTION HERE #
def subarray_sum(nums, target):
    num_map = {0: -1}
    cumulative_sum = 0
    for i, num in enumerate(nums):
        cumulative_sum += num
        complement = cumulative_sum - target
        if complement in num_map:
            return [num_map[complement] + 1, i]
        num_map[cumulative_sum] = i
    return [] 
###############################
    
if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5]
    target = 9
    print(subarray_sum(nums, target))

    nums = [-1, 2, 3, -4, 5]
    target = 0
    print(subarray_sum(nums, target))

    nums = [2, 3, 4, 5, 6]
    target = 3
    print(subarray_sum(nums, target))

    nums = []
    target = 0
    print(subarray_sum(nums, target))
