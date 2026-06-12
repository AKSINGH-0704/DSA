from typing import List

class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        num_layers = min(m, n) // 2
        
        for layer in range(num_layers):
            # Define the boundaries of the current layer
            top, bottom = layer, m - 1 - layer
            left, right = layer, n - 1 - layer
            
            # 1. Extract the layer into a 1D array
            elements = []
            
            # Top row (left to right)
            for j in range(left, right):
                elements.append(grid[top][j])
            # Right column (top to bottom)
            for i in range(top, bottom):
                elements.append(grid[i][right])
            # Bottom row (right to left)
            for j in range(right, left, -1):
                elements.append(grid[bottom][j])
            # Left column (bottom to top)
            for i in range(bottom, top, -1):
                elements.append(grid[i][left])
                
            # 2. Calculate effective rotations and rotate the 1D array
            length = len(elements)
            rotations = k % length
            
            # A counter-clockwise rotation shifts elements forward in our perimeter array
            rotated = elements[rotations:] + elements[:rotations]
            
            # 3. Put the rotated elements back into the grid
            idx = 0
            
            for j in range(left, right):
                grid[top][j] = rotated[idx]
                idx += 1
            for i in range(top, bottom):
                grid[i][right] = rotated[idx]
                idx += 1
            for j in range(right, left, -1):
                grid[bottom][j] = rotated[idx]
                idx += 1
            for i in range(bottom, top, -1):
                grid[i][left] = rotated[idx]
                idx += 1
                
        return grid