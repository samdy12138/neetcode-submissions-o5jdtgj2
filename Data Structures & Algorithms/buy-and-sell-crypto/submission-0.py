class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price=prices[0]
        max_profit=0

        for i in range(1, len(prices)):
            price_today=prices[i]

            profit=price_today-min_price

            if profit>max_profit:
                max_profit=profit

            if price_today<min_price:
                min_price=price_today
        return max_profit
        