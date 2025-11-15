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

import unittest


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


class TestRotate(unittest.TestCase):
    def test_rotate_three_steps(self):
        nums = [1, 2, 3, 4, 5, 6, 7]
        rotate(nums, 3)
        self.assertEqual(nums, [5, 6, 7, 1, 2, 3, 4])

    def test_rotate_zero_steps(self):
        nums = [10, 20, 30]
        rotate(nums, 0)
        self.assertEqual(nums, [10, 20, 30])

    def test_rotate_k_equals_length(self):
        nums = [4, 5, 6, 7]
        rotate(nums, len(nums))
        self.assertEqual(nums, [4, 5, 6, 7])

    def test_rotate_more_than_length(self):
        nums = [9, 8, 7, 6]
        rotate(nums, 7)
        self.assertEqual(nums, [8, 7, 6, 9])

    def test_single_element_list(self):
        nums = [42]
        rotate(nums, 5)
        self.assertEqual(nums, [42])


if __name__ == "__main__":
    unittest.main()
