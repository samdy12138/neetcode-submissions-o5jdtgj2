class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price=prices[0]
        max_profit=0
        for i in range(1,len(prices)):
            today_price=prices[i]
            profit=today_price-min_price

            if today_price<min_price:
                min_price=today_price
            if profit>max_profit:
                max_profit=profit
        return max_profit

"""
I keep track of the lowest price so far.

For each day, I calculate the profit if I sell on that day.

The profit is today’s price minus the lowest price before.

If today’s price is lower than the lowest price, I update the lowest price.

If the profit is bigger than the max profit, I update the max profit.

At the end, I return the max profit.

The time complexity is O(n), and the space complexity is O(1).

"""

        