import unittest

from interview.find_longest_string import find_longest_string
from interview.find_max_min import find_max_min
from interview.find_set_pairs import find_pairs
from interview.group_anagrams import group_anagrams
from interview.hast_table import item_in_common
from interview.max_stream_element import stream_max
from interview.max_sub_array import max_subarray
from interview.max_trade_profit import max_profit
from interview.remove_duplicates import remove_duplicates
from interview.remove_list_element import remove_element
from interview.rotate_list import rotate
from interview.subarray_sum import subarray_sum
from interview.two_sum import two_sum


class TestTwoSum(unittest.TestCase):
    def test_pair_exists(self):
        self.assertEqual(two_sum([5, 1, 7, 2, 9, 3], 10), [1, 4])

    def test_no_pair(self):
        self.assertEqual(two_sum([1, 2, 3, 4, 5], 50), [])


class TestSubarraySum(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(subarray_sum([1, 2, 3, 4, 5], 9), [1, 3])

    def test_with_negatives(self):
        self.assertEqual(subarray_sum([-1, 2, 3, -4, 5], 0), [0, 3])

    def test_no_match(self):
        self.assertEqual(subarray_sum([2, 3, 4], 1), [])


class TestFindPairs(unittest.TestCase):
    def test_pairs_found(self):
        result = find_pairs([1, 2, 3, 4, 5], [2, 4, 6, 8, 10], 7)
        self.assertEqual(result, [(1, 6), (3, 4), (5, 2)])

    def test_no_pairs(self):
        self.assertEqual(find_pairs([1, 2], [3, 4], 100), [])


class TestGroupAnagrams(unittest.TestCase):
    @staticmethod
    def _normalize(groups):
        return sorted([tuple(sorted(group)) for group in groups])

    def test_grouping(self):
        grouped = group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
        expected = [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
        self.assertEqual(self._normalize(grouped), self._normalize(expected))


class TestItemInCommon(unittest.TestCase):
    def test_common_found(self):
        self.assertTrue(item_in_common([1, 2, 3], [4, 3, 6]))

    def test_no_common(self):
        self.assertFalse(item_in_common([1, 2], [3, 4]))


class TestRemoveDuplicates(unittest.TestCase):
    def test_mixed_duplicates(self):
        nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
        new_length = remove_duplicates(nums)
        self.assertEqual(new_length, 5)
        self.assertEqual(nums[:new_length], [0, 1, 2, 3, 4])

    def test_empty_list(self):
        nums = []
        self.assertEqual(remove_duplicates(nums), 0)


class TestRemoveElement(unittest.TestCase):
    def test_remove_value(self):
        nums = [3, 2, 2, 3]
        new_length = remove_element(nums, 3)
        self.assertEqual(new_length, 2)
        self.assertEqual(nums[:new_length], [2, 2])

    def test_value_not_present(self):
        nums = [1, 2, 3]
        new_length = remove_element(nums, 0)
        self.assertEqual(new_length, 3)
        self.assertEqual(nums[:new_length], [1, 2, 3])


class TestRotateList(unittest.TestCase):
    def test_rotate_three(self):
        nums = [1, 2, 3, 4, 5, 6, 7]
        rotate(nums, 3)
        self.assertEqual(nums, [5, 6, 7, 1, 2, 3, 4])

    def test_rotate_more_than_length(self):
        nums = [9, 8, 7, 6]
        rotate(nums, 7)
        self.assertEqual(nums, [8, 7, 6, 9])


class TestFindLongestString(unittest.TestCase):
    def test_regular_case(self):
        self.assertEqual(find_longest_string(['apple', 'banana', 'kiwi']), 'banana')

    def test_empty_input(self):
        self.assertEqual(find_longest_string([]), "")


class TestFindMaxMin(unittest.TestCase):
    def test_values(self):
        self.assertEqual(find_max_min([5, 3, 8, 1, 6, 9]), (9, 1))

    def test_empty_list(self):
        self.assertIsNone(find_max_min([]))


class TestMaxSubarray(unittest.TestCase):
    def test_mixed_numbers(self):
        self.assertEqual(max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)

    def test_all_negative(self):
        self.assertEqual(max_subarray([-5, -2, -3]), -2)


class TestMaxTradeProfit(unittest.TestCase):
    def test_profit_exists(self):
        self.assertEqual(max_profit([7, 1, 5, 3, 6, 4]), 5)

    def test_no_profit(self):
        self.assertEqual(max_profit([7, 6, 4, 3, 1]), 0)


class TestStreamMax(unittest.TestCase):
    def test_increasing_stream(self):
        self.assertEqual(stream_max([1, 3, 2, 5, 4]), [1, 3, 3, 5, 5])

    def test_empty_stream(self):
        self.assertEqual(stream_max([]), [])
