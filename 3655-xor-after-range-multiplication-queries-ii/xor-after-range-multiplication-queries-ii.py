class Solution:
    def xorAfterQueries(self, nums: list[int], queries: list[list[int]]) -> int:
        n = len(nums)
        M = 10**9 + 7
        s = {}
        m = [1] * n
        
        for l, r, k, v in queries:
            if k <= 300:
                s.setdefault(k, []).append((l, r, v))
            else:
                for i in range(l, r + 1, k):
                    m[i] = (m[i] * v) % M
                    
        for k, q in s.items():
            d = [1] * n
            for l, r, v in q:
                d[l] = (d[l] * v) % M
                e = l + ((r - l) // k) * k + k
                if e < n:
                    d[e] = (d[e] * pow(v, M - 2, M)) % M
                    
            for i in range(n):
                if i >= k and d[i - k] != 1:
                    d[i] = (d[i] * d[i - k]) % M
                if d[i] != 1:
                    m[i] = (m[i] * d[i]) % M
                    
        x = 0
        for i in range(n):
            x ^= (nums[i] * m[i]) % M
            
        return x