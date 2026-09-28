class Solution:
    def maxDepth(self, s: str) -> int:
        depth = 0
        max_depth = 0

        for ch in s:
            # Opening parenthesis increases the current depth
            if ch == '(':
                depth += 1

                # Update the maximum depth
                max_depth = max(max_depth, depth)

            # Closing parenthesis decreases the current depth
            elif ch == ')':
                depth -= 1

        return max_depth