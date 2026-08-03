class Solution:

    def stoneGameIII(self, stoneValue: list[int]) -> str:
        n = len(stoneValue)
        dp = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            take = 0
            best = float("-inf")
            for k in range(1, 4):
                if i + k <= n:
                    take += stoneValue[i + k - 1]
                    best = max(best, take - dp[i + k])
            dp[i] = best
        if dp[0] > 0:
            return "Alice"
        elif dp[0] < 0:
            return "Bob"
        return "Tie"
