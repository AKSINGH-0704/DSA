class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        for k in range(1, 61):
            remain = num1 - k * num2
            if remain >= k and remain.bit_count() <= k:
                return k
        return -1
