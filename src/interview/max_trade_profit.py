"""Compute the best profit from a single buy/sell transaction.

Args:
    prices: Sequence of daily stock prices.

Returns:
    Maximum achievable profit from one buy followed by one sell. Returns 0
    when no profitable trade exists.
"""

import unittest


def max_profit(prices):
    if len(prices) <= 1:
        return 0

    best_profit = 0
    min_price = prices[0]

    for price in prices[1:]:
        min_price = min(min_price, price)
        profit = price - min_price
        best_profit = max(profit, best_profit)
    
    return best_profit


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
