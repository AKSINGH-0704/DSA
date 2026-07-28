class Solution:

    def smallestPalindrome(self, s: str) -> str:
        n = len(s)
        half_len = n // 2

        sorted_left = "".join(sorted(s[:half_len]))

        middle = s[half_len] if n % 2 != 0 else ""

        return sorted_left + middle + sorted_left[::-1]