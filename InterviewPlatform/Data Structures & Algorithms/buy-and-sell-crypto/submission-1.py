class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_prices = prices[0]
        profit = 0

        for i in prices:
            min_prices = min(min_prices, i)
            profit = max(profit, i - min_prices )

        return profit