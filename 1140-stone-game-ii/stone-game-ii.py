class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        suffix = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1] + piles[i]

        @lru_cache(None)
        def dp(i, m):
            if i >= n:
                return 0
            if i + 2 * m >= n:
                return suffix[i]

            ans = 0
            for x in range(1, 2 * m + 1):
                ans = max(ans, suffix[i] - dp(i + x, max(m, x)))
            return ans

        return dp(0, 1)