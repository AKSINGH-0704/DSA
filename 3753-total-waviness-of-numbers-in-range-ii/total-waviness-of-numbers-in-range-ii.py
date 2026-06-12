class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        def count(N: int) -> int:
            if N < 101:
                return 0
            
            s = str(N)
            n = len(s)
            
            @lru_cache(None)
            def dp(idx, prev, pprev, is_started, is_tight):
                if idx == n:
                    return 1, 0
                
                limit = int(s[idx]) if is_tight else 9
                res_count = 0
                res_wav = 0
                
                for d in range(limit + 1):
                    next_tight = is_tight and (d == limit)
                    
                    if not is_started and d == 0:
                        sub_count, sub_wav = dp(idx + 1, -1, -1, False, next_tight)
                        res_count += sub_count
                        res_wav += sub_wav
                    else:
                        w_delta = 0
                        if is_started and pprev != -1 and prev != -1:
                            if pprev < prev > d or pprev > prev < d:
                                w_delta = 1
                                
                        sub_count, sub_wav = dp(idx + 1, d, prev, True, next_tight)
                        res_count += sub_count
                        res_wav += sub_wav + w_delta * sub_count
                        
                return res_count, res_wav
            
            return dp(0, -1, -1, False, True)[1]
            
        return count(num2) - count(num1 - 1)