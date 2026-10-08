class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        def is_valid(s):
            balance = 0
            for ch in s:
                if ch == '(':
                    balance += 1
                elif ch == ')':
                    balance -= 1
                    if balance < 0:
                        return False
            return balance == 0

        level = {s}

        while True:
            valid = [x for x in level if is_valid(x)]
            if valid:
                return valid

            next_level = set()

            for x in level:
                for i in range(len(x)):
                    if x[i] in "()":
                        next_level.add(x[:i] + x[i + 1:])

            level = next_level