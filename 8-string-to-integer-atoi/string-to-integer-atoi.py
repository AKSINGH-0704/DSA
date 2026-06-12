class Solution:
    def myAtoi(self, s: str) -> int:
        i, n = 0, len(s)
        
        while i < n and s[i] == ' ':
            i += 1
            
        if i == n:
            return 0
            
        sign = 1
        if s[i] == '-':
            sign = -1
            i += 1
        elif s[i] == '+':
            i += 1
            
        result = 0
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        
        while i < n and s[i].isdigit():
            result = result * 10 + int(s[i])
            i += 1
            
        result *= sign
        
        if result < INT_MIN:
            return INT_MIN
        elif result > INT_MAX:
            return INT_MAX
            
        return result