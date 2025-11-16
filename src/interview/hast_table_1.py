"""Detect whether two lists share any value using a hash table.

Args:
    list1: First list of integers.
    list2: Second list of integers.

Returns:
    ``True`` if any element appears in both inputs, otherwise ``False``.

Example:
    >>> item_in_common([1, 2, 5], [3, 4, 5])
    True
"""

from typing import List

from data_structures.hash_table import HashTable


def item_in_common(list1: List[int], list2: List[int]) -> bool:
    hash_table = HashTable(size=len(list1))
    for item in list1:
        hash_table.set_item(str(item), True)
    for item in list2:
        if hash_table.get_item(str(item)):
            return True
    return False


if __name__ == "__main__":
    a = [1, 2, 4]
    b = [4, 8, 3]
    print(item_in_common(a, b))
