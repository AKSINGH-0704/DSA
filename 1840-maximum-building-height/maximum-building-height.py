class Solution:
    def maxBuilding(self, n: int, r: list[list[int]]) -> int:
        r.append([1, 0])
        r.sort()
        m = len(r)
        
        for i in range(1, m):
            r[i][1] = min(r[i][1], r[i-1][1] + (r[i][0] - r[i-1][0]))
        
        for i in range(m - 2, -1, -1):
            r[i][1] = min(r[i][1], r[i+1][1] + (r[i+1][0] - r[i][0]))
        
        ans = 0
        for i in range(m - 1):
            x1, h1 = r[i]
            x2, h2 = r[i+1]
            ans = max(ans, (h1 + h2 + (x2 - x1)) // 2)
            
        ans = max(ans, r[-1][1] + (n - r[-1][0]))
        
        return ans