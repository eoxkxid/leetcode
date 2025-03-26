class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price  # Update the lowest price so far
            elif price - min_price > max_profit:
                max_profit = price - min_price  # Update max profit if current profit is higher

        return max_profit

'''
float('inf') means infinity.
It's a built-in way to represent a number that's larger than any other number.
There is also float('-inf') for negative infinity.

Note:
In the line `if price < min_price:`
This means that if the current price is smaller than the lowest price we've seen so far, we update it.
If the price is higher, we check if selling now would give us a better profit.
'''
