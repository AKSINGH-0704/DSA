class Solution:
    def findMissingElements(self, nums: list[int]) -> list[int]:
        min_val = min(nums)
        max_val = max(nums)
        num_set = set(nums)
        return [i for i in range(min_val, max_val + 1) if i not in num_set]
