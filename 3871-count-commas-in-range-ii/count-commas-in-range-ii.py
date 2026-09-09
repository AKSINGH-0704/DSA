class Solution:
    def countCommas(self, n: int) -> int:
        ans = 0
        p = 1000
        while p <= n:
            ans += n - p + 1
            p *= 1000
        return ans