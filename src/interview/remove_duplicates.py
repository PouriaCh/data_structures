"""Deduplicate a sorted list in-place using two pointers.

Args:
    nums: Sorted list of integers (may include duplicates).

Returns:
    Length of the prefix that now contains the unique values. The list is
    modified so that ``nums[:length]`` holds the deduplicated sequence.

Example:
    >>> nums = [0, 0, 1, 1, 2]
    >>> remove_duplicates(nums)
    3
    >>> nums[:3]
    [0, 1, 2]
"""

import unittest

# WRITE REMOVE_DUPLICATES FUNCTION HERE #
# def remove_duplicates(mylist):
#     initial_length = len(mylist)
#     if initial_length == 0:
#         return 0
#     total_duplicates = 0
#     for i in range(1, initial_length):
#         if mylist[i - 1] == mylist[i]:

#             total_duplicates += 1
#     return initial_length - total_duplicates

def remove_duplicates(nums):
    if not nums:
        return 0
 
    write_pointer = 1
 
    for read_pointer in range(1, len(nums)):
        if nums[read_pointer] != nums[read_pointer - 1]:
            nums[write_pointer] = nums[read_pointer]
            write_pointer += 1
 
    return write_pointer
#########################################


class TestRemoveDuplicates(unittest.TestCase):
    """
    Unit tests for the remove_duplicates function.
    """

    def test_example_from_docstring(self):
        """Test the example provided in the docstring."""
        nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
        expected_length = 5
        expected_unique = [0, 1, 2, 3, 4]
        
        new_length = remove_duplicates(nums)
        
        self.assertEqual(new_length, expected_length)
        self.assertEqual(nums[:new_length], expected_unique)

    def test_empty_list(self):
        """Test with an empty list."""
        nums = []
        expected_length = 0
        expected_unique = []
        
        new_length = remove_duplicates(nums)
        
        self.assertEqual(new_length, expected_length)
        self.assertEqual(nums[:new_length], expected_unique)

    def test_all_duplicates(self):
        """Test with a list containing all duplicates."""
        nums = [1, 1, 1, 1, 1]
        expected_length = 1
        expected_unique = [1]
        
        new_length = remove_duplicates(nums)
        
        self.assertEqual(new_length, expected_length)
        self.assertEqual(nums[:new_length], expected_unique)

    def test_no_duplicates(self):
        """Test with a list containing no duplicates."""
        nums = [1, 2, 3, 4, 5]
        expected_length = 5
        expected_unique = [1, 2, 3, 4, 5]
        
        new_length = remove_duplicates(nums)
        
        self.assertEqual(new_length, expected_length)
        self.assertEqual(nums[:new_length], expected_unique)

    def test_some_duplicates(self):
        """Test with a list containing some duplicates."""
        nums = [1, 1, 2, 2, 3, 4, 5, 5]
        expected_length = 5
        expected_unique = [1, 2, 3, 4, 5]
        
        new_length = remove_duplicates(nums)
        
        self.assertEqual(new_length, expected_length)
        self.assertEqual(nums[:new_length], expected_unique)

    def test_single_element(self):
        """Test with a list containing only one element."""
        nums = [42]
        expected_length = 1
        expected_unique = [42]
        
        new_length = remove_duplicates(nums)
        
        self.assertEqual(new_length, expected_length)
        self.assertEqual(nums[:new_length], expected_unique)

    def test_two_elements_same(self):
        """Test with two identical elements."""
        nums = [5, 5]
        expected_length = 1
        expected_unique = [5]
        
        new_length = remove_duplicates(nums)
        
        self.assertEqual(new_length, expected_length)
        self.assertEqual(nums[:new_length], expected_unique)

    def test_two_elements_different(self):
        """Test with two different elements."""
        nums = [1, 2]
        expected_length = 2
        expected_unique = [1, 2]
        
        new_length = remove_duplicates(nums)
        
        self.assertEqual(new_length, expected_length)
        self.assertEqual(nums[:new_length], expected_unique)

    def test_negative_numbers(self):
        """Test with negative numbers."""
        nums = [-3, -3, -2, -1, -1, 0, 0, 1]
        expected_length = 5
        expected_unique = [-3, -2, -1, 0, 1]
        
        new_length = remove_duplicates(nums)
        
        self.assertEqual(new_length, expected_length)
        self.assertEqual(nums[:new_length], expected_unique)

    def test_zeros(self):
        """Test with zeros."""
        nums = [0, 0, 0, 0]
        expected_length = 1
        expected_unique = [0]
        
        new_length = remove_duplicates(nums)
        
        self.assertEqual(new_length, expected_length)
        self.assertEqual(nums[:new_length], expected_unique)

    def test_large_list(self):
        """Test with a larger list."""
        nums = [1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 5, 5, 5, 5, 5]
        expected_length = 5
        expected_unique = [1, 2, 3, 4, 5]
        
        new_length = remove_duplicates(nums)
        
        self.assertEqual(new_length, expected_length)
        self.assertEqual(nums[:new_length], expected_unique)

    def test_consecutive_duplicates_at_start(self):
        """Test with consecutive duplicates at the start."""
        nums = [1, 1, 1, 2, 3, 4]
        expected_length = 4
        expected_unique = [1, 2, 3, 4]
        
        new_length = remove_duplicates(nums)
        
        self.assertEqual(new_length, expected_length)
        self.assertEqual(nums[:new_length], expected_unique)

    def test_consecutive_duplicates_at_end(self):
        """Test with consecutive duplicates at the end."""
        nums = [1, 2, 3, 4, 4, 4]
        expected_length = 4
        expected_unique = [1, 2, 3, 4]
        
        new_length = remove_duplicates(nums)
        
        self.assertEqual(new_length, expected_length)
        self.assertEqual(nums[:new_length], expected_unique)

    def test_alternating_pattern(self):
        """Test with alternating unique and duplicate pattern."""
        nums = [1, 1, 2, 3, 3, 4, 5, 5, 6]
        expected_length = 6
        expected_unique = [1, 2, 3, 4, 5, 6]
        
        new_length = remove_duplicates(nums)
        
        self.assertEqual(new_length, expected_length)
        self.assertEqual(nums[:new_length], expected_unique)


if __name__ == '__main__':
    unittest.main()
