class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        ans = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0:
                    stack = [(i, j)]
                    total = 0
                    total += grid[i][j]
                    grid[i][j] = 0

                    while stack:
                        r, c = stack.pop()

                        for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                            if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] > 0:
                                total += grid[nr][nc]
                                grid[nr][nc] = 0
                                stack.append((nr, nc))

                    if total % k == 0:
                        ans += 1

        return ans