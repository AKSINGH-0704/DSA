class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort()
        n = len(events)
        suffix_max = [0] * n
        suffix_max[-1] = events[-1][2]
        
        for i in range(n - 2, -1, -1):
            suffix_max[i] = max(events[i][2], suffix_max[i + 1])
            
        start_times = [e[0] for e in events]
        max_sum = 0
        
        for i in range(n):
            val = events[i][2]
            idx = bisect.bisect_left(start_times, events[i][1] + 1)
            if idx < n:
                val += suffix_max[idx]
            if val > max_sum:
                max_sum = val
            
        return max_sum