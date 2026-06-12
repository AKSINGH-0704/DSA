class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        count = 0
        
        for r in range(rows - 2):
            for c in range(cols - 2):
                
                vals = [
                    grid[r][c], grid[r][c+1], grid[r][c+2],
                    grid[r+1][c], grid[r+1][c+1], grid[r+1][c+2],
                    grid[r+2][c], grid[r+2][c+1], grid[r+2][c+2]
                ]
                
                
                if sorted(vals) != [1, 2, 3, 4, 5, 6, 7, 8, 9]:
                    continue
                    
                if (grid[r][c] + grid[r][c+1] + grid[r][c+2] != 15 or
                    grid[r+1][c] + grid[r+1][c+1] + grid[r+1][c+2] != 15 or
                    grid[r+2][c] + grid[r+2][c+1] + grid[r+2][c+2] != 15):
                    continue

                if (grid[r][c] + grid[r+1][c] + grid[r+2][c] != 15 or
                    grid[r][c+1] + grid[r+1][c+1] + grid[r+2][c+1] != 15 or
                    grid[r][c+2] + grid[r+1][c+2] + grid[r+2][c+2] != 15):
                    continue
                    
                if (grid[r][c] + grid[r+1][c+1] + grid[r+2][c+2] != 15 or
                    grid[r][c+2] + grid[r+1][c+1] + grid[r+2][c] != 15):
                    continue
                    
                count += 1
                
        return count