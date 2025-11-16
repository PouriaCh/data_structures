"""Return the max and min values from a list in one pass.

Args:
    mylist: Sequence of integers. Can be empty.

Returns:
    ``(max_value, min_value)`` when the list has data, otherwise ``None``.

Example:
    >>> find_max_min([5, 3, 8, 1, 6, 9])
    (9, 1)
"""

import unittest


def find_max_min(mylist):
    if len(mylist) == 0:
        return None
    min_value = mylist[0]
    max_value = mylist[0]
    i = 1
    while i < len(mylist):
        num = mylist[i]
        if min_value > num:
            min_value = num
        if max_value < num:
            max_value = num
        i += 1
    return (max_value, min_value)


class TestFindMaxMin(unittest.TestCase):
    """
    Unit tests for the find_max_min function.
    """

    def test_example_from_docstring(self):
        """Test the example provided in the docstring."""
        mylist = [5, 3, 8, 1, 6, 9]
        expected = (9, 1)
        
        result = find_max_min(mylist)
        
        self.assertEqual(result, expected)

    def test_single_element(self):
        """Test with a list containing only one element."""
        mylist = [42]
        expected = (42, 42)
        
        result = find_max_min(mylist)
        
        self.assertEqual(result, expected)

    def test_empty_list(self):
        """Test with an empty list."""
        mylist = []
        expected = None
        
        result = find_max_min(mylist)
        
        self.assertIsNone(result)

    def test_all_positive_numbers(self):
        """Test with all positive numbers."""
        mylist = [10, 20, 30, 5, 15]
        expected = (30, 5)
        
        result = find_max_min(mylist)
        
        self.assertEqual(result, expected)

    def test_all_negative_numbers(self):
        """Test with all negative numbers."""
        mylist = [-5, -10, -3, -20, -1]
        expected = (-1, -20)
        
        result = find_max_min(mylist)
        
        self.assertEqual(result, expected)

    def test_mixed_positive_negative(self):
        """Test with mixed positive and negative numbers."""
        mylist = [-5, 10, -3, 8, -1, 2]
        expected = (10, -5)
        
        result = find_max_min(mylist)
        
        self.assertEqual(result, expected)

    def test_duplicate_values(self):
        """Test with duplicate values in the list."""
        mylist = [5, 5, 5, 5, 5]
        expected = (5, 5)
        
        result = find_max_min(mylist)
        
        self.assertEqual(result, expected)

    def test_max_at_beginning(self):
        """Test when maximum value is at the beginning."""
        mylist = [100, 1, 2, 3, 4, 5]
        expected = (100, 1)
        
        result = find_max_min(mylist)
        
        self.assertEqual(result, expected)

    def test_max_at_end(self):
        """Test when maximum value is at the end."""
        mylist = [1, 2, 3, 4, 5, 100]
        expected = (100, 1)
        
        result = find_max_min(mylist)
        
        self.assertEqual(result, expected)

    def test_min_at_beginning(self):
        """Test when minimum value is at the beginning."""
        mylist = [-100, 1, 2, 3, 4, 5]
        expected = (5, -100)
        
        result = find_max_min(mylist)
        
        self.assertEqual(result, expected)

    def test_min_at_end(self):
        """Test when minimum value is at the end."""
        mylist = [5, 4, 3, 2, 1, -100]
        expected = (5, -100)
        
        result = find_max_min(mylist)
        
        self.assertEqual(result, expected)

    def test_max_and_min_at_same_position(self):
        """Test when max and min are the same (single element)."""
        mylist = [7]
        expected = (7, 7)
        
        result = find_max_min(mylist)
        
        self.assertEqual(result, expected)

    def test_large_numbers(self):
        """Test with large numbers."""
        mylist = [1000000, 999999, 1, 500000]
        expected = (1000000, 1)
        
        result = find_max_min(mylist)
        
        self.assertEqual(result, expected)

    def test_zeros(self):
        """Test with zeros in the list."""
        mylist = [0, -5, 10, 0, -3]
        expected = (10, -5)
        
        result = find_max_min(mylist)
        
        self.assertEqual(result, expected)

    def test_ascending_order(self):
        """Test with numbers in ascending order."""
        mylist = [1, 2, 3, 4, 5]
        expected = (5, 1)
        
        result = find_max_min(mylist)
        
        self.assertEqual(result, expected)

    def test_descending_order(self):
        """Test with numbers in descending order."""
        mylist = [5, 4, 3, 2, 1]
        expected = (5, 1)
        
        result = find_max_min(mylist)
        
        self.assertEqual(result, expected)

    def test_two_elements(self):
        """Test with exactly two elements."""
        mylist = [10, 5]
        expected = (10, 5)
        
        result = find_max_min(mylist)
        
        self.assertEqual(result, expected)

    def test_two_elements_reversed(self):
        """Test with two elements in reverse order."""
        mylist = [5, 10]
        expected = (10, 5)
        
        result = find_max_min(mylist)
        
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
    
