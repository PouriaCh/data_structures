"""Return the max and min values from a list in one pass.

Args:
    mylist: Sequence of integers. Can be empty.

Returns:
    ``(max_value, min_value)`` when the list has data, otherwise ``None``.

Example:
    >>> find_max_min([5, 3, 8, 1, 6, 9])
    (9, 1)
"""

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
    
