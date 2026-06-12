class Solution:
    def minimumDistance(self, nums: list[int]) -> int:
        p, r = {}, -1
        for i, v in enumerate(nums):
            l = p.setdefault(v, [])
            l.append(i)
            if len(l) > 2:
                d = (l[-1] - l[-3]) * 2
                if r < 0 or d < r: 
                    r = d
        return r