class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        total = 1
        streak = 1
        
        for i in range(1, len(prices)):
            if prices[i] == prices[i-1] - 1:
                streak += 1
            else:
                streak = 1
            total += streak
            
        return total