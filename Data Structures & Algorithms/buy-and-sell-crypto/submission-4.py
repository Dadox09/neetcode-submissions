class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #need a sliding window
        buy = 0
        max_profit = 0
        for sell in range(1, len(prices)):
            if prices[sell] <= prices[buy]:
                buy = sell
            else:
                profit = prices[sell] - prices[buy]
                max_profit = max(profit, max_profit)
        return max_profit