class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        ans = 0
        i = 0

        def is_palindrome(l: int, r: int) -> bool:
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        while i <= n - k:
         
            if is_palindrome(i, i + k - 1):
                ans += 1
                i += k 
            elif i + k < n and is_palindrome(i, i + k):
                ans += 1
                i += k + 1 
            else:
                i += 1 

        return ans