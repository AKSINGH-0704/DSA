class Solution:
    def minScore(self, n: int, roads: list[list[int]]) -> int:
        graph = collections.defaultdict(list)
        for u, v, d in roads:
            graph[u].append((v, d))
            graph[v].append((u, d))
            
        min_score = float('inf')
        visited = set()
        queue = collections.deque([1])
        visited.add(1)
        
        while queue:
            curr = queue.popleft()
            for neighbor, distance in graph[curr]:
                min_score = min(min_score, distance)
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
                    
        return min_score