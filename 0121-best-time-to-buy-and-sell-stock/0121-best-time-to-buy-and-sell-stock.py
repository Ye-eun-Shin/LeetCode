class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        mini = prices[0]
        for i in range(1,len(prices)):
            if mini>prices[i]:
                mini = prices[i]
            else:
                max_profit = max(max_profit, prices[i]-mini)
            
        return max_profit