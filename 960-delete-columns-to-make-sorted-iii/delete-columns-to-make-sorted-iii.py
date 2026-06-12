class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        rows = len(strs)
        cols = len(strs[0])
        dp = [1] * cols
        
        for i in range(cols):
            for j in range(i):
                valid = True
                for k in range(rows):
                    if strs[k][j] > strs[k][i]:
                        valid = False
                        break
                if valid:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        return cols - max(dp)