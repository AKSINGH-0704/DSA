class Solution:
    def reverseDegree(self, s: str) -> int:
        total = 0

        for i, ch in enumerate(s):
            value = 26 - (ord(ch) - ord('a'))
            position = i + 1
            total += value * position

        return total