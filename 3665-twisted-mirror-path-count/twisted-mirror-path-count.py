class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])

        right = [[-1] * n for _ in range(m)]
        down = [[-1] * n for _ in range(m)]

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                idx = i * n + j

                if grid[i][j] == 0:
                    right[i][j] = idx
                    down[i][j] = idx
                else:
                    if i + 1 < m:
                        right[i][j] = down[i + 1][j]
                    if j + 1 < n:
                        down[i][j] = right[i][j + 1]

        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1

        for i in range(m):
            for j in range(n):
                if dp[i][j] == 0:
                    continue

                if j + 1 < n:
                    nxt = right[i][j + 1]
                    if nxt != -1:
                        x, y = divmod(nxt, n)
                        dp[x][y] = (dp[x][y] + dp[i][j]) % MOD

                if i + 1 < m:
                    nxt = down[i + 1][j]
                    if nxt != -1:
                        x, y = divmod(nxt, n)
                        dp[x][y] = (dp[x][y] + dp[i][j]) % MOD

        return dp[m - 1][n - 1]