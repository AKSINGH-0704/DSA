class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        MOD = 10**9 + 7
        
        dp0 = [[0] * (one + 1) for _ in range(zero + 1)]
        dp1 = [[0] * (one + 1) for _ in range(zero + 1)]
        
        for i in range(1, min(zero, limit) + 1):
            dp0[i][0] = 1
        for j in range(1, min(one, limit) + 1):
            dp1[0][j] = 1
            
        for i in range(1, zero + 1):
            # Cache the row references to avoid repeated 2D array lookups
            d0_i = dp0[i]
            d0_im1 = dp0[i - 1]
            d1_i = dp1[i]
            d1_im1 = dp1[i - 1]
            
            if i > limit:
                d1_imL = dp1[i - limit - 1]
                
                # Split the loop to completely eliminate 'if j > limit' checks
                for j in range(1, min(one, limit) + 1):
                    d0_i[j] = (d0_im1[j] + d1_im1[j] - d1_imL[j]) % MOD
                    d1_i[j] = (d0_i[j - 1] + d1_i[j - 1]) % MOD
                    
                for j in range(limit + 1, one + 1):
                    d0_i[j] = (d0_im1[j] + d1_im1[j] - d1_imL[j]) % MOD
                    d1_i[j] = (d0_i[j - 1] + d1_i[j - 1] - d0_i[j - limit - 1]) % MOD
            else:
                for j in range(1, min(one, limit) + 1):
                    d0_i[j] = (d0_im1[j] + d1_im1[j]) % MOD
                    d1_i[j] = (d0_i[j - 1] + d1_i[j - 1]) % MOD
                    
                for j in range(limit + 1, one + 1):
                    d0_i[j] = (d0_im1[j] + d1_im1[j]) % MOD
                    d1_i[j] = (d0_i[j - 1] + d1_i[j - 1] - d0_i[j - limit - 1]) % MOD
                    
        return (dp0[zero][one] + dp1[zero][one]) % MOD