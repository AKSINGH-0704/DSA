class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        c = [0] * 31
        for x in nums:
            for b in range(31):
                c[b] += (x >> b) & 1
        ans = 0
        for _ in range(k):
            x = 0
            for b in range(31):
                if c[b]:
                    x |= 1 << b
                    c[b] -= 1
            ans = (ans + x * x) % (10**9 + 7)
        return ans