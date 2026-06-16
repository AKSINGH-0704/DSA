class Solution:
    def processStr(self, s: str) -> str:
        res = ""
        for char in s:
            if char == '*':
                res = res[:-1]
            elif char == '#':
                res = res + res
            elif char == '%':
                res = res[::-1]
            else:
                res += char
        return res