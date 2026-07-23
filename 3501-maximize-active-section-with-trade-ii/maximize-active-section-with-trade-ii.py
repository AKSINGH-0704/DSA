class SparseTable:
    def __init__(self, arr: list[int]):
        self.n = len(arr)
        if self.n == 0:
            return
        self.K = self.n.bit_length()
        self.st = [arr[:]]
        for i in range(1, self.K):
            prev = self.st[i - 1]
            half = 1 << (i - 1)
            curr = [0] * (self.n - (1 << i) + 1)
            for j in range(len(curr)):
                curr[j] = max(prev[j], prev[j + half])
            self.st.append(curr)

    def query(self, L: int, R: int) -> int:
        if L > R or self.n == 0:
            return 0
        length = R - L + 1
        k = length.bit_length() - 1
        return max(self.st[k][L], self.st[k][R - (1 << k) + 1])

class Solution:
    def maxActiveSectionsAfterTrade(self, s: str, queries: list[list[int]]) -> list[int]:
        n = len(s)
        initial_ones = s.count('1')
    
        block_start = []
        block_end = []
        i = 0
        while i < n:
            if s[i] == '0':
                start = i
                while i < n and s[i] == '0':
                    i += 1
                block_start.append(start)
                block_end.append(i - 1)
            else:
                i += 1
                
        m = len(block_start)
        if m < 2:
            return [initial_ones] * len(queries)
            
        block_size = [block_end[k] - block_start[k] + 1 for k in range(m)]
        pair_sum = [block_size[k] + block_size[k + 1] for k in range(m - 1)]
        
        st = SparseTable(pair_sum)
        ans = []
        
        for l, r in queries:
            low = bisect.bisect_left(block_end, l)
            high = bisect.bisect_right(block_start, r) - 1
            
            if low >= high:
                ans.append(initial_ones)
                continue
                
            first_len = block_end[low] - max(block_start[low], l) + 1
            last_len = min(block_end[high], r) - block_start[high] + 1
            
            if high - low == 1:
                max_pair_sum = first_len + last_len
            else:
                pair1 = first_len + block_size[low + 1]
                pair2 = block_size[high - 1] + last_len
                rmq = st.query(low + 1, high - 2)
                max_pair_sum = max(pair1, pair2, rmq)
                
            ans.append(initial_ones + max_pair_sum)
            
        return ans