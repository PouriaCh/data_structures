"""Return the longest string from a list.

Args:
    input_list: Sequence of strings. May be empty.

Returns:
    The first string with maximal length, or ``""`` when the list is empty.

Example:
    >>> find_longest_string(['apple', 'banana', 'kiwi'])
    'banana'
"""

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
