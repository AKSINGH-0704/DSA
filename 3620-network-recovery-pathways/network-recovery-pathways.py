import heapq
import collections

class Solution:
    def findMaxPathScore(self, edges: list[list[int]], online: list[bool], k: int) -> int:
        n = len(online)
        adj = collections.defaultdict(list)
        unique_costs = set()
        
        for u, v, cost in edges:
            if online[u] and online[v]:
                adj[u].append((v, cost))
                unique_costs.add(cost)
        
        sorted_costs = sorted(list(unique_costs))
        def can_achieve(min_edge_cost):
            dist = {i: float('inf') for i in range(n)}
            dist[0] = 0
            pq = [(0, 0)] 
            
            while pq:
                d, u = heapq.heappop(pq)
                
                if d > dist[u]: continue
                if u == n - 1: return d <= k
                
                for v, cost in adj[u]:
                    if cost >= min_edge_cost:
                        if dist[u] + cost < dist[v]:
                            dist[v] = dist[u] + cost
                            heapq.heappush(pq, (dist[v], v))
            
            return dist[n - 1] <= k
        left, right = 0, len(sorted_costs) - 1
        ans = -1
        
        while left <= right:
            mid = (left + right) // 2
            if can_achieve(sorted_costs[mid]):
                ans = sorted_costs[mid]
                left = mid + 1 
            else:
                right = mid - 1
                
        return ans