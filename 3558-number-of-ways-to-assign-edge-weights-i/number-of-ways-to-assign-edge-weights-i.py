class Solution:
    def assignEdgeWeights(self, edges: list[list[int]]) -> int:
        n = len(edges) + 1
        adj = [[] for _ in range(n + 1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        depths = [0] * (n + 1)
        queue = deque([1])
        visited = {1}
        max_depth = 0
        
        while queue:
            u = queue.popleft()
            max_depth = max(max_depth, depths[u])
            for v in adj[u]:
                if v not in visited:
                    visited.add(v)
                    depths[v] = depths[u] + 1
                    queue.append(v)
                    
        return pow(2, max_depth - 1, 10**9 + 7)