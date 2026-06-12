class Solution:
    def countPartitions(self, nums):
        s = 0
        for x in nums:
            s += x
        if s % 2 == 0:
            return len(nums) - 1
        return 0
