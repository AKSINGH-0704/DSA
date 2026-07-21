class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        initial_ones = s.count('1')
        t = '1' + s + '1'
        blocks = []
        curr_char = t[0]
        curr_len = 0
        
        for ch in t:
            if ch == curr_char:
                curr_len += 1
            else:
                blocks.append(curr_len)
                curr_char = ch
                curr_len = 1
        blocks.append(curr_len)
        
        num_blocks = len(blocks)
        k = (num_blocks - 1) // 2
        
        if k < 2:
            return initial_ones
            
        Z = [blocks[2 * i + 1] for i in range(k)]      
        L = [blocks[2 * i + 2] for i in range(k - 1)]  
        
        pref_max = [0] * k
        pref_max[0] = Z[0]
        for i in range(1, k):
            pref_max[i] = max(pref_max[i - 1], Z[i])
            
        suff_max = [0] * k
        suff_max[-1] = Z[-1]
        for i in range(k - 2, -1, -1):
            suff_max[i] = max(suff_max[i + 1], Z[i])
            
        max_ones = initial_ones
        
        for i in range(k - 1):
            M_i = Z[i] + L[i] + Z[i + 1]
            
            left_max = pref_max[i - 1] if i - 1 >= 0 else 0
            right_max = suff_max[i + 2] if i + 2 < k else 0
            
            best_0_block = max(M_i, left_max, right_max)
            current_ones = initial_ones - L[i] + best_0_block
            max_ones = max(max_ones, current_ones)
            
        return max_ones