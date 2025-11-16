"""Compute the best profit from a single buy/sell transaction.

Args:
    prices: Sequence of daily stock prices.

Returns:
    Maximum achievable profit from one buy followed by one sell. Returns 0
    when no profitable trade exists.
"""

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

