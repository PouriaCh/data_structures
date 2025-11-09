"""
List: Find Longest String ( ** Interview Question)

Write a Python function called find_longest_string that takes a list of strings as an input and returns the longest 
string in the list. The function should iterate through each string in the list, check its length, and keep track of 
the longest string seen so far. Once it has looped through all the strings, the function should return the longest string found.

Example:
string_list = ['apple', 'banana', 'kiwi', 'pear']
longest = find_longest_string(string_list)
print(longest)  # expected output: 'banana'

"""

import unittest

# WRITE FIND_LONGEST_STRING FUNCTION HERE #
def find_longest_string(input_list):
    if len(input_list) == 0:
        return ""
    max_length = len(input_list[0])
    max_index = 0
    i = 1
    while i < len(input_list):
        length = len(input_list[i])
        if length > max_length:
            max_length = length
            max_index = i
        i += 1
    return input_list[max_index]
###########################################


class TestFindLongestString(unittest.TestCase):
    """
    Unit tests for the find_longest_string function.
    """

    def test_example_from_docstring(self):
        """Test the example provided in the docstring."""
        string_list = ['apple', 'banana', 'kiwi', 'pear']
        expected = 'banana'
        
        result = find_longest_string(string_list)
        
        self.assertEqual(result, expected)

    def test_single_string(self):
        """Test with a list containing only one string."""
        string_list = ['hello']
        expected = 'hello'
        
        result = find_longest_string(string_list)
        
        self.assertEqual(result, expected)

    def test_empty_list(self):
        """Test with an empty list."""
        string_list = []
        expected = ""
        
        result = find_longest_string(string_list)
        
        self.assertEqual(result, expected)

    def test_all_same_length(self):
        """Test with all strings having the same length."""
        string_list = ['cat', 'dog', 'bat']
        # Should return the first one encountered
        expected = 'cat'
        
        result = find_longest_string(string_list)
        
        self.assertEqual(result, expected)

    def test_longest_at_beginning(self):
        """Test when the longest string is at the beginning of the list."""
        string_list = ['programming', 'code', 'python']
        expected = 'programming'
        
        result = find_longest_string(string_list)
        
        self.assertEqual(result, expected)

    def test_longest_at_end(self):
        """Test when the longest string is at the end of the list."""
        string_list = ['a', 'ab', 'abc', 'abcd', 'abcde']
        expected = 'abcde'
        
        result = find_longest_string(string_list)
        
        self.assertEqual(result, expected)

    def test_longest_in_middle(self):
        """Test when the longest string is in the middle of the list."""
        string_list = ['short', 'verylongstring', 'also']
        expected = 'verylongstring'
        
        result = find_longest_string(string_list)
        
        self.assertEqual(result, expected)

    def test_strings_with_spaces(self):
        """Test with strings containing spaces."""
        string_list = ['hello world', 'hi', 'good morning']
        expected = 'good morning'
        
        result = find_longest_string(string_list)
        
        self.assertEqual(result, expected)

    def test_empty_strings(self):
        """Test with list containing empty strings."""
        string_list = ['', 'a', '', 'ab', '']
        expected = 'ab'
        
        result = find_longest_string(string_list)
        
        self.assertEqual(result, expected)

    def test_single_character_strings(self):
        """Test with single character strings."""
        string_list = ['a', 'b', 'c', 'd']
        # Should return the first one
        expected = 'a'
        
        result = find_longest_string(string_list)
        
        self.assertEqual(result, expected)

    def test_very_long_strings(self):
        """Test with very long strings."""
        string_list = ['short', 'a' * 100, 'medium' * 10]
        expected = 'a' * 100
        
        result = find_longest_string(string_list)
        
        self.assertEqual(result, expected)

    def test_mixed_case_strings(self):
        """Test with strings of different cases."""
        string_list = ['Python', 'JAVA', 'javascript']
        expected = 'javascript'
        
        result = find_longest_string(string_list)
        
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
