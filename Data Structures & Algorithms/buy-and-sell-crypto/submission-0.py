class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = profit = sell = 0
        buy = prices[0]

        for sellPosition in range(1, len(prices)):
            sell = prices[sellPosition]
            profit = sell - buy

            if profit > maxProfit:
                maxProfit = profit
            
            if sell < buy:
                buy = sell

        return maxProfit