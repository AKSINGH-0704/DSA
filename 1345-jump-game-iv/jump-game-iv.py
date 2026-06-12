class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        if n <= 1:
            return 0
            
        graph = collections.defaultdict(list)
        for i, val in enumerate(arr):
            graph[val].append(i)
            
        q = collections.deque([0])
        visited = {0}
        steps = 0
        
        while q:
            for _ in range(len(q)):
                curr = q.popleft()
                
                if curr == n - 1:
                    return steps
                    
                for neighbor in graph[arr[curr]]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        q.append(neighbor)
                        
                del graph[arr[curr]]
                
                for neighbor in (curr - 1, curr + 1):
                    if 0 <= neighbor < n and neighbor not in visited:
                        visited.add(neighbor)
                        q.append(neighbor)
                        
            steps += 1
            
        return -1