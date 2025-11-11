"""
List: Max Profit ( ** Interview Question)

You are given a list of integers representing stock prices for a certain company over a period of time, 
where each element in the list corresponds to the stock price for a specific day. You are allowed to buy 
one share of the stock on one day and sell it on a later day. Your task is to write a function called max_profit
that takes the list of stock prices as input and returns the maximum profit you can make by buying and selling at the right time.

Note that you must buy the stock before selling it, and you are allowed to make only one transaction (buy once and sell once).

Constraints:
- Each element of the input list is a positive integer representing the stock price for a specific day.

Function signature: def max_profit(prices):

Example:
Input: prices = [7, 1, 5, 3, 6, 4]
Function call: profit = max_profit(prices)
Output: profit = 5

Explanation: The maximum profit can be achieved by buying the stock on day 2 (price 1) and selling it on 
day 5 (price 6), resulting in a profit of 6 - 1 = 5.
"""

import unittest


def max_profit(prices):
    if len(prices) <= 1:
        return 0

    max_profit = 0
    min_price = prices[0]

    for price in prices[1:]:
        min_price = min(min_price, price)
        profit = price - min_price
        max_profit = max(profit, max_profit)
    
    return max_profit


class TestMaxProfit(unittest.TestCase):
    def test_mixed_prices(self):
        prices = [7, 1, 5, 3, 6, 4]
        self.assertEqual(max_profit(prices), 5)

    def test_descending_prices(self):
        prices = [7, 6, 4, 3, 1]
        self.assertEqual(max_profit(prices), 0)

    def test_ascending_prices(self):
        prices = [1, 2, 3, 4, 5, 6]
        self.assertEqual(max_profit(prices), 5)

    def test_flat_prices(self):
        prices = [5, 5, 5, 5]
        self.assertEqual(max_profit(prices), 0)

    def test_single_entry(self):
        prices = [10]
        self.assertEqual(max_profit(prices), 0)


if __name__ == "__main__":
    unittest.main()
