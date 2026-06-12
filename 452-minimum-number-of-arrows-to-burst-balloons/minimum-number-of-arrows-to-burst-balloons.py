class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        
        points.sort(key=lambda x: x[1])
        arrows = 1
        arrow_pos = points[0][1]
        
        for start, end in points[1:]:
            if start > arrow_pos:
                arrows += 1
                arrow_pos = end
                
        return arrows
