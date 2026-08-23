class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        half = n // 2

        left_q = num[:half].count('?')
        right_q = num[half:].count('?')

        left_sum = sum(int(x) for x in num[:half] if x != '?')
        right_sum = sum(int(x) for x in num[half:] if x != '?')

        diff = left_sum - right_sum
        q_diff = left_q - right_q

        return diff != -q_diff * 4.5