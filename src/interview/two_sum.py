"""Two Sum (hash map approach).

Given `nums` and `target`, return indices of two elements whose sum equals `target`.

Notes:
    - Solve in a single pass using a hash map from value to index.
    - Return an empty list when no such pair exists.
    - Time complexity: O(n); space: O(n).

Example:
    >>> two_sum([3, 2, 4], 6)
    [1, 2]
"""
# WRITE TWO_SUM FUNCTION HERE #
def two_sum(nums, target):
    num_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i] 
        num_map[num] = i
    return [] 
###############################
    
if __name__ == "__main__":
    print(two_sum([5, 1, 7, 2, 9, 3], 10))
    print(two_sum([4, 2, 11, 7, 6, 3], 9))
    print(two_sum([10, 15, 5, 2, 8, 1, 7], 12))
    print(two_sum([1, 3, 5, 7, 9], 10))
    print(two_sum([1, 2, 3, 4, 5], 10))
    print(two_sum([1, 2, 3, 4, 5], 7))
    print(two_sum([1, 2, 3, 4, 5], 3))
    print(two_sum([], 0))
