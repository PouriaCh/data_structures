"""Remove all occurrences of ``val`` from a list in-place.

Args:
    nums: List of integers to mutate.
    val: Value to remove.

Returns:
    Length of the array after deletions. Elements beyond that length are
    unspecified.

Example:
    >>> nums = [3, 2, 2, 3]
    >>> remove_element(nums, 3)
    2
    >>> nums[:2]
    [2, 2]
"""

# WRITE THE REMOVE_ELEMENT FUNCTION HERE #
def remove_element(nums, val):
    i = 0
    while i < len(nums):
        if nums[i] == val:
            nums.pop(i)
        else:
            i += 1
    return len(nums)
