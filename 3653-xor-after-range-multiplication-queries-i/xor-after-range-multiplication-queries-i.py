class Solution:
    def xorAfterQueries(self, nums: list[int], queries: list[list[int]]) -> int:
        MOD = 10**9 + 7
        
        for query in queries:
            l = query[0]
            r = query[1]
            k = query[2]
            v = query[3]
            
            for idx in range(l, r + 1, k):
                nums[idx] = (nums[idx] * v) % MOD
                
        final_xor = 0
        for num in nums:
            final_xor ^= num
            
        return final_xor