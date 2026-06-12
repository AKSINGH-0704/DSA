class Solution:
    def numberOfSubmatrices(self, grid: list[list[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        ans = 0
        
        col_x = [0] * n
        col_y = [0] * n
        
        for i in range(m):
            row_x = 0
            row_y = 0
            for j in range(n):
                if grid[i][j] == 'X':
                    row_x += 1
                elif grid[i][j] == 'Y':
                    row_y += 1
                    
                col_x[j] += row_x
                col_y[j] += row_y
                
                if col_x[j] == col_y[j] and col_x[j] > 0:
                    ans += 1
                    
        return ans