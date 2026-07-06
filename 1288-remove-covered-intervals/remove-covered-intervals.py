class Solution:
    def removeCoveredIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], -x[1]))
        
        count = 0
        max_right = 0
        
        for _, r in intervals:
            if r > max_right:
                count += 1
                max_right = r
                
        return count