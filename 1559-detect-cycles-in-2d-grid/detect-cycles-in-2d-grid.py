import collections
from typing import List

class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        def bfs(start_r: int, start_c: int) -> bool:
            q = collections.deque([(start_r, start_c, -1, -1)])
            visited[start_r][start_c] = True
            target_char = grid[start_r][start_c]
            
            while q:
                r, c, pr, pc = q.popleft()
                
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    
                    if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == target_char:
                        
                        
                        if nr == pr and nc == pc:
                            continue
                            
                        if visited[nr][nc]:
                            return True
                            
                        visited[nr][nc] = True
                        q.append((nr, nc, r, c))
                        
            return False

        for i in range(m):
            for j in range(n):
                if not visited[i][j]:
                    if bfs(i, j):
                        return True
                        
        return False