class Solution:
    def checkDivisibility(self, n: int) -> bool:
        temp = n
        digit_sum = 0
        digit_product = 1

        while temp:
            digit = temp % 10
            digit_sum += digit
            digit_product *= digit
            temp //= 10

        return n % (digit_sum + digit_product) == 0