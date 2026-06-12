class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        total = 0
        
        for i in range(k):
            val = happiness[i] - i
            if val <= 0:
                break
            total += val
            
        return total