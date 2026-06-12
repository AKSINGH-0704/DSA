class Solution:
    def getMinDistance(self, nums: list[int], target: int, start: int) -> int:
        r = 10000
        for i, v in enumerate(nums):
            if v == target:
                d = abs(i - start)
                if d < r:
                    r = d
        return r