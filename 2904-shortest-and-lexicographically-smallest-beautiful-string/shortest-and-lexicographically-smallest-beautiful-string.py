class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        ones = 0
        left = 0
        ans = ""

        for right in range(len(s)):
            ones += s[right] == "1"

            while ones > k:
                ones -= s[left] == "1"
                left += 1

            while left <= right and ones == k and s[left] == "0":
                left += 1

            if ones == k:
                cur = s[left:right + 1]
                if not ans or len(cur) < len(ans) or (len(cur) == len(ans) and cur < ans):
                    ans = cur

        return ans