class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)
        t = "".join(sorted(s))
        
        if s == t:
            return 0
            
        if n <= 2:
            return -1
            
        L = -1
        R = -1
        for i in range(n):
            if s[i] != t[i]:
                if L == -1:
                    L = i
                R = i
                
        if R - L + 1 < n:
            return 1
            
        if s.find(t[0], 0, n - 1) != -1 or s.find(t[-1], 1, n) != -1:
            return 2
            
        return 3