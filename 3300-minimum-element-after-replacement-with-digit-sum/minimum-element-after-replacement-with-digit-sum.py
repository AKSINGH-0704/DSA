class Solution:
    def minElement(self, nums: List[int]) -> int:
        ans = float('inf')
        
        for num in nums:
            curr = 0
            while num > 0:
                curr += num % 10
                num //= 10
            if curr < ans:
                ans = curr
                
        return ans