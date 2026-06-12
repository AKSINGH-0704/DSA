import collections

class Solution:
    def canPartitionGrid(self, grid: list[list[int]]) -> bool:
        m = len(grid)
        n = len(grid[0])
        
        row_sums = [sum(row) for row in grid]
        col_sums = [0] * n
        for i in range(m):
            for j in range(n):
                col_sums[j] += grid[i][j]
                
        total_sum = sum(row_sums)
        
        def check_section(r1, r2, c1, c2, d, freq_dict):
            H = r2 - r1 + 1
            W = c2 - c1 + 1
            
            if H == 1 and W == 1:
                return grid[r1][c1] == d
            elif H == 1:
                return grid[r1][c1] == d or grid[r1][c2] == d
            elif W == 1:
                return grid[r1][c1] == d or grid[r2][c1] == d
            else:
                return freq_dict.get(d, 0) > 0
                
        # 1. Check Horizontal Cuts
        top_freq = collections.defaultdict(int)
        bottom_freq = collections.defaultdict(int)
        
        for i in range(m):
            for j in range(n):
                bottom_freq[grid[i][j]] += 1
                
        top_sum = 0
        for i in range(m - 1):
            top_sum += row_sums[i]
            
            for j in range(n):
                v = grid[i][j]
                top_freq[v] += 1
                bottom_freq[v] -= 1
                
            bottom_sum = total_sum - top_sum
            d = abs(top_sum - bottom_sum)
            
            if d == 0:
                return True
                
            if top_sum > bottom_sum:
                if check_section(0, i, 0, n - 1, d, top_freq):
                    return True
            else:
                if check_section(i + 1, m - 1, 0, n - 1, d, bottom_freq):
                    return True
                    
        # 2. Check Vertical Cuts
        left_freq = collections.defaultdict(int)
        right_freq = collections.defaultdict(int)
        
        for i in range(m):
            for j in range(n):
                right_freq[grid[i][j]] += 1
                
        left_sum = 0
        for j in range(n - 1):
            left_sum += col_sums[j]
            
            for i in range(m):
                v = grid[i][j]
                left_freq[v] += 1
                right_freq[v] -= 1
                
            right_sum = total_sum - left_sum
            d = abs(left_sum - right_sum)
            
            if d == 0:
                return True
                
            if left_sum > right_sum:
                if check_section(0, m - 1, 0, j, d, left_freq):
                    return True
            else:
                if check_section(0, m - 1, j + 1, n - 1, d, right_freq):
                    return True
                    
        return False