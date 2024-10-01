class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 얼마든지 사고 되팔 수 있다..
        # 이익이 생기지 않는다면 그냥 그날 바로 팔아서 0임.

        # Greedy.. -> 하루간격 편차 계산. 음수면 0으로.
        length = len(prices)
        max_profit = 0
        for i in range(length-1):
            max_profit += max(0, prices[i+1]-prices[i])

        return max_profit
        