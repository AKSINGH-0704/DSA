import heapq

class Solution:
    def findSafeWalk(self, grid: list[list[int]], health: int) -> bool:
        m, n = len(grid), len(grid[0])
        cost = [[float('inf')] * n for _ in range(m)]

        start_cost = grid[0][0]
        cost[0][0] = start_cost
        
        pq = [(start_cost, 0, 0)]
        
        while pq:
            curr_cost, r, c = heapq.heappop(pq)
            
            if r == m - 1 and c == n - 1:
                return curr_cost < health
            
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n:
                    new_cost = curr_cost + grid[nr][nc]
                    if new_cost < cost[nr][nc]:
                        cost[nr][nc] = new_cost
                        heapq.heappush(pq, (new_cost, nr, nc))
                        
        return False