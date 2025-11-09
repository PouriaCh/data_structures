"""
List: Remove Element ( ** Interview Question)

Given a list of integers nums and an integer val, write a function remove_element that removes all occurrences 
of val in the list in-place and returns the new length of the modified list. The function should not allocate 
extra space for another list; instead, it should modify the input list in-place with O(1) extra memory.

Input:
A list of integers nums. An integer val representing the value to be removed from the list.

Output:
An integer representing the new length of the modified list after removing all occurrences of val.

Constraints:
- Do not use any built-in list methods, except for pop() to remove elements.
- It is okay to have extra space at the end of the modified list after removing elements.

"""

import unittest


# WRITE THE REMOVE_ELEMENT FUNCTION HERE #
def remove_element(nums, val):
    i = 0
    while i < len(nums):
        if nums[i] == val:
            nums.pop(i)
        else:
            i += 1
    return len(nums)

##########################################


class TestRemoveElement(unittest.TestCase):
    """
    Unit tests for the remove_element function.
    """

    def test_remove_single_instance_middle(self):
        """Test removing a single instance of a value in the middle of the list."""
        nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        val = 1
        expected_result = [-2, -3, 4, -1, 2, -5, 4]
        expected_length = 7
        
        new_length = remove_element(nums, val)
        
        self.assertEqual(new_length, expected_length)
        self.assertEqual(nums[:new_length], expected_result)

    def test_remove_value_at_end(self):
        """Test removing a value that's located at the end of the list."""
        nums = [1, 2, 3, 4, 5, 6]
        val = 6
        expected_result = [1, 2, 3, 4, 5]
        expected_length = 5
        
        new_length = remove_element(nums, val)
        
        self.assertEqual(new_length, expected_length)
        self.assertEqual(nums[:new_length], expected_result)

    def test_remove_value_at_start(self):
        """Test removing a value that's located at the start of the list."""
        nums = [-1, -2, -3, -4, -5]
        val = -1
        expected_result = [-2, -3, -4, -5]
        expected_length = 4
        
        new_length = remove_element(nums, val)
        
        self.assertEqual(new_length, expected_length)
        self.assertEqual(nums[:new_length], expected_result)

    def test_remove_from_empty_list(self):
        """Test attempting to remove a value from an empty list."""
        nums = []
        val = 1
        expected_result = []
        expected_length = 0
        
        new_length = remove_element(nums, val)
        
        self.assertEqual(new_length, expected_length)
        self.assertEqual(nums, expected_result)

    def test_remove_all_instances_repeated_value(self):
        """Test removing all instances of a repeated value."""
        nums = [1, 1, 1, 1, 1]
        val = 1
        expected_result = []
        expected_length = 0
        
        new_length = remove_element(nums, val)
        
        self.assertEqual(new_length, expected_length)
        self.assertEqual(nums[:new_length], expected_result)

    def test_remove_multiple_instances_scattered(self):
        """Test removing multiple instances of a value scattered throughout the list."""
        nums = [3, 2, 2, 3]
        val = 3
        expected_result = [2, 2]
        expected_length = 2
        
        new_length = remove_element(nums, val)
        
        self.assertEqual(new_length, expected_length)
        self.assertEqual(nums[:new_length], expected_result)

    def test_remove_value_not_in_list(self):
        """Test removing a value that doesn't exist in the list."""
        nums = [1, 2, 3, 4, 5]
        val = 6
        expected_result = [1, 2, 3, 4, 5]
        expected_length = 5
        
        new_length = remove_element(nums, val)
        
        self.assertEqual(new_length, expected_length)
        self.assertEqual(nums[:new_length], expected_result)


if __name__ == '__main__':
    unittest.main()
