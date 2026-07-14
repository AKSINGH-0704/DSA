import math

class Solution:
    def subsequencePairCount(self, nums: list[int]) -> int:
        MOD = 1_000_000_007
        max_num = max(nums)
        dp = [[0] * (max_num + 1) for _ in range(max_num + 1)]
        dp[0][0] = 1
        
        for num in nums:
            new_dp = [row[:] for row in dp]
            for x in range(max_num + 1):
                for y in range(max_num + 1):
                    if dp[x][y] == 0:
                        continue
                    
                    new_x = math.gcd(x, num) if x > 0 else num
                    new_dp[new_x][y] = (new_dp[new_x][y] + dp[x][y]) % MOD
                    
                    new_y = math.gcd(y, num) if y > 0 else num
                    new_dp[x][new_y] = (new_dp[x][new_y] + dp[x][y]) % MOD
            dp = new_dp
            
        ans = 0
        for g in range(1, max_num + 1):
            ans = (ans + dp[g][g]) % MOD
        return ans