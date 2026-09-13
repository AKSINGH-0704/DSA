class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        a = [(i, j) for i in range(n) for j in range(n) if img1[i][j]]
        b = [(i, j) for i in range(n) for j in range(n) if img2[i][j]]
        
        shifts = {}
        ans = 0
        
        for i, j in a:
            for x, y in b:
                shift = (x - i, y - j)
                shifts[shift] = shifts.get(shift, 0) + 1
                ans = max(ans, shifts[shift])
        
        return ans