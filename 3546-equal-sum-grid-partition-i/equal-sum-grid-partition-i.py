class Solution:
    def canPartitionGrid(self, grid: list[list[int]]) -> bool:
        m = len(grid)
        n = len(grid[0])
        
        row_sums = [sum(row) for row in grid]
        total = sum(row_sums)
        
        if total % 2 != 0:
            return False
            
        target = total // 2
        
        # Check horizontal cuts
        curr = 0
        for i in range(m - 1):
            curr += row_sums[i]
            if curr == target:
                return True
                
        # Calculate column sums efficiently
        col_sums = [0] * n
        for row in grid:
            for j in range(n):
                col_sums[j] += row[j]
                
        # Check vertical cuts
        curr = 0
        for j in range(n - 1):
            curr += col_sums[j]
            if curr == target:
                return True
                
        return False