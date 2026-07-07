class Solution:
    def sumAndMultiply(self, n: int) -> int:
        s = str(n)
        
        non_zeros = [char for char in s if char != '0']
        if not non_zeros:
            return 0
        
        x = int("".join(non_zeros))
        digit_sum = sum(int(digit) for digit in non_zeros)
        
        return x * digit_sum