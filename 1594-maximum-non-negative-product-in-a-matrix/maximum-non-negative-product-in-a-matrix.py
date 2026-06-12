class Solution:
    def maxProductPath(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        MOD = 10**9 + 7
        
        max_dp = [[0] * n for _ in range(m)]
        min_dp = [[0] * n for _ in range(m)]
        
        max_dp[0][0] = min_dp[0][0] = grid[0][0]
        
        for i in range(1, m):
            max_dp[i][0] = min_dp[i][0] = max_dp[i-1][0] * grid[i][0]
            
        for j in range(1, n):
            max_dp[0][j] = min_dp[0][j] = max_dp[0][j-1] * grid[0][j]
            
        for i in range(1, m):
            for j in range(1, n):
                v = grid[i][j]
                
                if v == 0:
                    max_dp[i][j] = min_dp[i][j] = 0
                elif v > 0:
                    max_dp[i][j] = max(max_dp[i-1][j], max_dp[i][j-1]) * v
                    min_dp[i][j] = min(min_dp[i-1][j], min_dp[i][j-1]) * v
                else:
                    max_dp[i][j] = min(min_dp[i-1][j], min_dp[i][j-1]) * v
                    min_dp[i][j] = max(max_dp[i-1][j], max_dp[i][j-1]) * v
                    
        ans = max_dp[-1][-1]
        
        return ans % MOD if ans >= 0 else -1