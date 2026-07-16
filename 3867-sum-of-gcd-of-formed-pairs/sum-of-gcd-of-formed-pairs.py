import math

class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        n = len(nums)
        prefix_gcd = []
        current_max = 0
        for x in nums:
            current_max = max(current_max, x)
            prefix_gcd.append(math.gcd(x, current_max))
            
        prefix_gcd.sort()
        total_gcd_sum = 0
        left = 0
        right = n - 1
        
        while left < right:
            pair_gcd = math.gcd(prefix_gcd[left], prefix_gcd[right])
            total_gcd_sum += pair_gcd
            left += 1
            right -= 1
            
        return total_gcd_sum