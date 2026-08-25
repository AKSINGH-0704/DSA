class Solution:
    def missingMultiple(self, nums, k):
        seen = set(nums)
        x = k

        while x in seen:
            x += k

        return x