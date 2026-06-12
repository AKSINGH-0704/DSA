class Solution:
    def romanToInt(self, s: str) -> int:
        vals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        total = 0
        n = len(s)
        
        for i in range(n):
            if i + 1 < n and vals[s[i]] < vals[s[i + 1]]:
                total -= vals[s[i]]
            else:
                total += vals[s[i]]
                
        return total