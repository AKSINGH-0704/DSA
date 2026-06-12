class Solution:
    def totalMoney(self, n: int) -> int:
        total = 0
        for i in range(n):
            
            week = i // 7
            day_of_week = i % 7
            
            
            deposit = (week + 1) + day_of_week
            total += deposit
            
        return total