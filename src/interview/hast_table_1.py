"""
Given two list, check if a common item exists in both lists.
[1, 2, 5], [3, 4, 5] => True
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from typing import List
from hash_table import HashTable


def item_in_common(list1: List[int], list2: List[int]) -> bool:
    hash_table = HashTable(size=len(list1))
    for item in list1:
        hash_table.set_item(str(item), True)
    for item in list2:
        item_found = hash_table.get_item(str(item))
        return False if not item_found else item_found

a = [1, 2, 4]
b = [4, 8, 3]
print(item_in_common(a, b))
