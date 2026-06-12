class Solution:
    def constructProductMatrix(self, grid: list[list[int]]) -> list[list[int]]:
        n = len(grid)
        m = len(grid[0])
        MOD = 12345
        
        p = [[0] * m for _ in range(n)]
        
       
        pref = 1
        for i in range(n):
            for j in range(m):
                p[i][j] = pref
                pref = (pref * grid[i][j]) % MOD
                
        
        suff = 1
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                p[i][j] = (p[i][j] * suff) % MOD
                suff = (suff * grid[i][j]) % MOD
                
        return p