class Solution:
    def numberOfWays(self, corridor: str) -> int:
        seats = []
        for i, char in enumerate(corridor):
            if char == 'S':
                seats.append(i)
        
        if len(seats) == 0 or len(seats) % 2 != 0:
            return 0
        
        result = 1
        MOD = 10**9 + 7
        
        prev_end = seats[1]
        for i in range(2, len(seats), 2):
            curr_start = seats[i]
            result = (result * (curr_start - prev_end)) % MOD
            prev_end = seats[i+1]
            
        return result