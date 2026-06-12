class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        free = [-float('inf')] * (k + 1)
        hold_long = [-float('inf')] * (k + 1)
        hold_short = [-float('inf')] * (k + 1)
        
        free[0] = 0
        
        for price in prices:
            prev_free = free[:]
            prev_hold_long = hold_long[:]
            prev_hold_short = hold_short[:]
            
            for j in range(1, k + 1):
                hold_long[j] = max(prev_hold_long[j], prev_free[j-1] - price)
                hold_short[j] = max(prev_hold_short[j], prev_free[j-1] + price)
                free[j] = max(prev_free[j], prev_hold_long[j] + price, prev_hold_short[j] - price)
                
        return max(free)