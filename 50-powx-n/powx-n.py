class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0
            
        p = abs(n)
        ans = 1.0
        
        while p > 0:
            if p % 2 == 1:
                ans *= x
            x *= x
            p //= 2
            
        if n < 0:
            return 1.0 / ans
        return ans