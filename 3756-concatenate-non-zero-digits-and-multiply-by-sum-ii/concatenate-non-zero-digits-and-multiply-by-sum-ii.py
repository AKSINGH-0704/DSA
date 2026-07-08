class Solution:
    def sumAndMultiply(self, s: str, queries: list[list[int]]) -> list[int]:
        mod = 10**9 + 7
        n = len(s)
        nz_indices = [i for i, char in enumerate(s) if char != '0']
        k = len(nz_indices)
        
        pref_sum = [0] * (k + 1)
        for i in range(k):
            pref_sum[i+1] = pref_sum[i] + int(s[nz_indices[i]])
            
        pow10 = [1] * (k + 1)
        for i in range(1, k + 1):
            pow10[i] = (pow10[i-1] * 10) % mod
            
        pref_val = [0] * (k + 1)
        for i in range(k):
            pref_val[i+1] = (pref_val[i] * 10 + int(s[nz_indices[i]])) % mod
            
        import bisect
        results = []
        for l, r in queries:
            start = bisect.bisect_left(nz_indices, l)
            end = bisect.bisect_right(nz_indices, r) - 1
            
            if start > end:
                results.append(0)
                continue
                
            count = end - start + 1
            
            digit_sum = pref_sum[end + 1] - pref_sum[start]
            x = (pref_val[end + 1] - pref_val[start] * pow10[count]) % mod
            
            results.append((x * digit_sum) % mod)
            
        return results