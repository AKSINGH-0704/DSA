from typing import List

class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse=True)
        ans = 0
        
        for i in range(len(cost)):
            if i % 3 != 2:
                ans += cost[i]
                
        return ans