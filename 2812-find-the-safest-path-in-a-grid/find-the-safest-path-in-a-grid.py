import heapq
from collections import deque

class Solution:
    def maximumSafenessFactor(self, grid: list[list[int]]) -> int:
        n = len(grid)
        dist = [[float('inf')] * n for _ in range(n)]
        queue = deque()
        
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    dist[r][c] = 0
                    queue.append((r, c))
                    
        while queue:
            r, c = queue.popleft()
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and dist[nr][nc] == float('inf'):
                    dist[nr][nc] = dist[r][c] + 1
                    queue.append((nr, nc))
                    
        pq = [(-dist[0][0], 0, 0)]
        dist[0][0] = -1 # Mark as visited
        
        while pq:
            d, r, c = heapq.heappop(pq)
            d = -d
            
            if r == n - 1 and c == n - 1:
                return d
            
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and dist[nr][nc] != -1:
                    new_dist = min(d, dist[nr][nc])
                    heapq.heappush(pq, (-new_dist, nr, nc))
                    dist[nr][nc] = -1 
                    
        return 0