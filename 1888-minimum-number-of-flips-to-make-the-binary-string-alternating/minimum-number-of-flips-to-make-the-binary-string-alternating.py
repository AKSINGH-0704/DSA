class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        s = s + s
        
        diff1 = 0
        diff2 = 0
        res = n
        
        for i in range(2 * n):
            if s[i] != ("0" if i % 2 == 0 else "1"):
                diff1 += 1
            if s[i] != ("1" if i % 2 == 0 else "0"):
                diff2 += 1
            
            if i >= n:
                if s[i - n] != ("0" if (i - n) % 2 == 0 else "1"):
                    diff1 -= 1
                if s[i - n] != ("1" if (i - n) % 2 == 0 else "0"):
                    diff2 -= 1
            
            if i >= n - 1:
                if diff1 < res: res = diff1
                if diff2 < res: res = diff2
                
        return res