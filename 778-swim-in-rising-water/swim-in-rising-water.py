class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)

        for t in range(n * n):
            if grid[0][0] > t:
                continue

            stack = [(0, 0)]
            visited = set([(0, 0)])

            while stack:
                r, c = stack.pop()

                if r == n - 1 and c == n - 1:
                    return t

                for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    nr, nc = r + dr, c + dc

                    is_in_bounds = 0 <= nr < n and 0 <= nc < n
                    is_not_visited = (nr, nc) not in visited
                    
                    if is_in_bounds and is_not_visited:
                        if grid[nr][nc] <= t:
                            visited.add((nr, nc))
                            stack.append((nr, nc))
        
        return -1