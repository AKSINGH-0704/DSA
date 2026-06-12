class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums) - 2
        seen = [False] * n
        res = []
        for x in nums:
            if seen[x]:
                res.append(x)
                if len(res) == 2:
                    return res
            else:
                seen[x] = True
        return res
