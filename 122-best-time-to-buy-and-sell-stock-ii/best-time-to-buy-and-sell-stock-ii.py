class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(1, len(prices)):
            comp = prices[i] - prices[i-1]
            if comp > 0:
                profit = profit + comp 
        return profit


        