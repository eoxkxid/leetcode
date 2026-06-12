class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        for i in range(1, len(prices)):
            # 가격이 상승한 날이면 그 차익을 얻는다
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]

        return profit