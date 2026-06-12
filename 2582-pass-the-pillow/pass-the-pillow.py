class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        cycle = 2 * (n - 1)
        t = time % cycle
        if t < n:
            return t + 1
        return 2 * n - t - 1
