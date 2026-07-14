class Solution:
    def sequentialDigits(self, low: int, high: int) -> list[int]:
        result = []
        for length in range(2, 10):
            for start in range(1, 10 - length + 1):
                num = 0
                for i in range(length):
                    num = num * 10 + (start + i)
                if low <= num <= high:
                    result.append(num)
        return sorted(result)