class Solution:
    def minimumDistance(self, nums: list[int]) -> int:
        d = {}
        z = -1
        for i, v in enumerate(nums):
            l = d.setdefault(v, [])
            l.append(i)
            if len(l) > 2:
                c = (l[-1] - l[-3]) * 2
                if z == -1 or c < z:
                    z = c
        return z