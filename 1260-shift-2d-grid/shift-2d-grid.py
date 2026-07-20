class Solution:
    def shiftGrid(self, grid: list[list[int]], k: int) -> list[list[int]]:
        m, n = len(grid), len(grid[0])
        total_elements = m * n
        
        flat = [val for row in grid for val in row]
        
        k = k % total_elements
        
        shifted = flat[-k:] + flat[:-k]
        
        return [shifted[i * n : (i + 1) * n] for i in range(m)]