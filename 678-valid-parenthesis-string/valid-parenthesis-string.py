class Solution:
    def checkValidString(self, s: str) -> bool:
        low = high = 0

        for c in s:
            if c == '(':
                low += 1
                high += 1
            elif c == ')':
                low = max(0, low - 1)
                high -= 1
            else:
                low = max(0, low - 1)
                high += 1

            if high < 0:
                return False

        return low == 0