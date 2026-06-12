class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        def canWalk(day):
            # Create grid and mark water cells
            grid = [[0] * col for _ in range(row)]
            for i in range(day):
                r, c = cells[i]
                grid[r-1][c-1] = 1
            
            queue = collections.deque()
            
            # Start BFS from top row
            for c in range(col):
                if grid[0][c] == 0:
                    queue.append((0, c))
                    grid[0][c] = 2  # Mark as visited
            
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            
            while queue:
                r, c = queue.popleft()
                if r == row - 1:
                    return True
                
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < row and 0 <= nc < col and grid[nr][nc] == 0:
                        grid[nr][nc] = 2  # Mark as visited
                        queue.append((nr, nc))
            
            return False

        # Binary search for the last valid day
        left, right = 1, len(cells)
        ans = 0
        
        while left <= right:
            mid = (left + right) // 2
            if canWalk(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
                
        return ans