from collections import deque

class Solution:
    def minOperations(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
            
        pos = -1
        for i in range(n):
            if nums[i] == 0:
                pos = i
                break
                
        is_inc = True
        for i in range(1, n):
            if nums[(pos + i) % n] != i:
                is_inc = False
                break
                
        is_dec = True
        for i in range(1, n):
            if nums[(pos + i) % n] != n - i:
                is_dec = False
                break
                
        if not is_inc and not is_dec:
            return -1
            
        start_state = pos if is_inc else pos + n
        
        dist = [-1] * (2 * n)
        dist[start_state] = 0
        q = deque([start_state])
        
        while q:
            curr = q.popleft()
            if curr == 0:
                return dist[curr]
                
            d = dist[curr]
            p = curr if curr < n else curr - n
            
            # Rotate left
            nxt_p = (p - 1) % n
            nxt_state1 = nxt_p if curr < n else nxt_p + n
            if dist[nxt_state1] == -1:
                dist[nxt_state1] = d + 1
                q.append(nxt_state1)
                
            # Reverse
            nxt_p = (n - 1 - p) % n
            nxt_state2 = nxt_p + n if curr < n else nxt_p
            if dist[nxt_state2] == -1:
                dist[nxt_state2] = d + 1
                q.append(nxt_state2)
                
        return -1