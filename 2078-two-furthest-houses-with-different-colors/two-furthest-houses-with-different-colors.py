class Solution:
    def maxDistance(self, colors: list[int]) -> int:
        n = len(colors)
    
        for i in range(n - 1, -1, -1):
            if colors[i] != colors[0]:
                ans1 = i
                break
            
        for i in range(n):
            if colors[i] != colors[-1]:
                ans2 = (n - 1) - i
                break
            
        return max(ans1, ans2)