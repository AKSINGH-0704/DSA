from typing import List

class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        nums.sort(key=lambda x: x * x)

        n = len(nums)
        mid = n // 2

        return sum(x * x for x in nums[mid:]) - sum(x * x for x in nums[:mid])