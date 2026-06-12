class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        known = {0, firstPerson}
        meetings.sort(key=lambda x: x[2])
        
        i = 0
        while i < len(meetings):
            curr_time = meetings[i][2]
            current_batch = []
            while i < len(meetings) and meetings[i][2] == curr_time:
                current_batch.append(meetings[i])
                i += 1
            
            adj = defaultdict(list)
            involved = set()
            
            for x, y, t in current_batch:
                adj[x].append(y)
                adj[y].append(x)
                involved.add(x)
                involved.add(y)
            
            queue = deque()
            for person in involved:
                if person in known:
                    queue.append(person)
            
            while queue:
                u = queue.popleft()
                for v in adj[u]:
                    if v not in known:
                        known.add(v)
                        queue.append(v)
                        
        return list(known)