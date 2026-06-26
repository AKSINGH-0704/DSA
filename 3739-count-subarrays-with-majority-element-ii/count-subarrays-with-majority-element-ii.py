class Solution:
    def countMajoritySubarrays(self, nums: list[int], target: int) -> int:
        n = len(nums)
        arr = [1 if x == target else -1 for x in nums]
        
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] + arr[i]
            
        sorted_pref = sorted(list(set(pref)))
        rank = {val: i + 1 for i, val in enumerate(sorted_pref)}
        
        bit = [0] * (len(sorted_pref) + 1)
        
        def update(i, delta):
            while i < len(bit):
                bit[i] += delta
                i += i & (-i)
                
        def query(i):
            s = 0
            while i > 0:
                s += bit[i]
                i -= i & (-i)
            return s
            
        ans = 0
        for x in pref:
            ans += query(rank[x] - 1)
            update(rank[x], 1)
            
        return ans