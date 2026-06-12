import heapq
from typing import List

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        
        available = [i for i in range(n)]
        occupied = [] 
        heapq.heapify(available)
        
        count = [0] * n
        
        for start, end in meetings:
            while occupied and occupied[0][0] <= start:
                _, room = heapq.heappop(occupied)
                heapq.heappush(available, room)
                
            if available:
                room = heapq.heappop(available)
                heapq.heappush(occupied, (end, room))
            else:
                finish_time, room = heapq.heappop(occupied)
                heapq.heappush(occupied, (finish_time + end - start, room))
                
            count[room] += 1
            
        return count.index(max(count))