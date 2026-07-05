class Solution:
    def pathsWithMaxScore(self, board: list[str]) -> list[int]:
        n = len(board)
        MOD = 10**9 + 7
        
        dp = [[(-1, 0)] * n for _ in range(n)]
        dp[n-1][n-1] = (0, 1)
        
        for r in range(n - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                if board[r][c] == 'X' or (r == n - 1 and c == n - 1):
                    continue
                
                max_s, paths = -1, 0
                for nr, nc in [(r + 1, c), (r, c + 1), (r + 1, c + 1)]:
                    if nr < n and nc < n and dp[nr][nc][0] != -1:
                        score, count = dp[nr][nc]
                        current_val = int(board[r][c]) if board[r][c] != 'E' else 0
                        
                        if score + current_val > max_s:
                            max_s = score + current_val
                            paths = count
                        elif score + current_val == max_s:
                            paths = (paths + count) % MOD
                
                dp[r][c] = (max_s, paths)
        res = dp[0][0]
        return [res[0], res[1]] if res[0] != -1 else [0, 0]