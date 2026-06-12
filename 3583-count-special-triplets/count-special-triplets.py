class Solution:
    def specialTriplets(self, nums):
        MOD = 10**9 + 7
        
        right = {}
        for x in nums:
            right[x] = right.get(x, 0) + 1
        
        left = {}
        ans = 0
        
        for x in nums:
            right[x] -= 1
            target = x * 2
            
            ans += left.get(target, 0) * right.get(target, 0)
            ans %= MOD
            
            left[x] = left.get(x, 0) + 1
        
        return ans
