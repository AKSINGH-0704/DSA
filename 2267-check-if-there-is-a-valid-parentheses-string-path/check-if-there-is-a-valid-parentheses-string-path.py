class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        
        if (m + n - 1) % 2 != 0:
            return False
            
        if grid[0][0] == ')' or grid[m - 1][n - 1] == '(':
            return False

        max_balance = (m + n - 1) // 2
        
        visited = set()

        def dfs(r: int, c: int, bal: int) -> bool:
            bal += 1 if grid[r][c] == '(' else -1
            
            if bal < 0 or bal > max_balance:
                return False
                
            if r == m - 1 and c == n - 1:
                return bal == 0
                
            state = (r, c, bal)
            if state in visited:
                return False
            visited.add(state)

            if r + 1 < m and dfs(r + 1, c, bal):
                return True
            if c + 1 < n and dfs(r, c + 1, bal):
                return True

            return False

        return dfs(0, 0, 0)