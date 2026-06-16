class Solution:
    def longestValidParentheses(self, s: str) -> int:
        def get_max(sequence, open_char, close_char):
            max_len = open_count = close_count = 0
            for char in sequence:
                if char == open_char:
                    open_count += 1
                else:
                    close_count += 1
                
                if open_count == close_count:
                    max_len = max(max_len, 2 * close_count)
                elif close_count > open_count:
                    open_count = close_count = 0
            return max_len

        return max(get_max(s, '(', ')'), get_max(s[::-1], ')', '('))