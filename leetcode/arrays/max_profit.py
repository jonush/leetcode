"""
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.
"""

def maxProfit(prices) -> int:
    """
    Given a list of prices for a stock,
    find the max profit from buying and selling at a certain price
    
    - buy price must be lower than sell price
    - must buy before selling
    - if there is no optimal profit, do not buy/sell -> profit = 0
    """
    # three conditions:
    # 1. buy first [i] before sell [i:]
    # 2. buy price < sell price
    # 3. max distance between buy and sell

    # initialize the max_profit, and min_price (with upper bound)
    max_profit, min_price = 0, float('inf')
    
    # iterate through the prices
    for price in prices:
        # calculate the min_price (from upper bound to current iterated price)
        min_price = min(min_price, price)
        # calculate profit from current price - lowest price
        profit = price - min_price
        # calculate max_profit
        max_profit = max(max_profit, profit)
        
    return max_profit

test = [1,6,3,9,12]
maxProfit(test)

"""
TIME & SPACE COMPLEXITY

TIME: O(n)

The solution iterates through the list of prices using a for loop which is an O(n) operation. Inside, it calculates the min and max to calculate the best buy and sell prices.

SPACE: O(1)

The solution utilizes no additional data structures but iterates through the given input list.
"""