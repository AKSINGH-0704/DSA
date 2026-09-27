class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []

        for ch in s:
            if ch == '(':
                stack.append("")

            elif ch == ')':
                reversed_part = stack.pop()[::-1]

                if stack:
                    stack[-1] += reversed_part
                else:
                    stack.append(reversed_part)

            else:
                if stack:
                    stack[-1] += ch
                else:
                    stack.append(ch)

        return "".join(stack)