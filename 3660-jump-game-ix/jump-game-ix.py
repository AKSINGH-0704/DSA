class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n == 0:
            return []
            
        prefix_max = [0] * n
        prefix_max[0] = nums[0]
        for i in range(1, n):
            prefix_max[i] = max(prefix_max[i-1], nums[i])
            
        suffix_min = [0] * n
        suffix_min[-1] = nums[-1]
        for i in range(n-2, -1, -1):
            suffix_min[i] = min(suffix_min[i+1], nums[i])
            
        ans = [0] * n
        start = 0
        
        while start < n:
            end = start
            while end < n - 1 and prefix_max[end] > suffix_min[end + 1]:
                end += 1
                
            comp_max = max(nums[start:end + 1])
            for i in range(start, end + 1):
                ans[i] = comp_max
                
            start = end + 1
            
        return ans