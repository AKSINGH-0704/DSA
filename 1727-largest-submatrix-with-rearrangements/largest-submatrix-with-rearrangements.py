class Solution:
    def largestSubmatrix(self, matrix: list[list[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        max_area = 0
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] != 0 and i > 0:
                    matrix[i][j] += matrix[i - 1][j]
            
            curr_row = sorted(matrix[i], reverse=True)
            
            for j in range(n):
                max_area = max(max_area, curr_row[j] * (j + 1))
                
        return max_area