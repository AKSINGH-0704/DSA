class Solution:
    def maximumLength(self, nums: list[int]) -> int:
        count = Counter(nums)
        ans = 1
        
        if count[1] > 0:
            if count[1] % 2 == 0:
                ans = count[1] - 1
            else:
                ans = count[1]
                
        sorted_keys = sorted(count.keys())
        
        for x in sorted_keys:
            if x == 1:
                continue
                
            curr = x
            length = 0
            
            while curr in count and count[curr] >= 2:
                length += 2
                curr = curr * curr
                
            if curr in count:
                length += 1
            else:
                length -= 1
                
            ans = max(ans, length)
            
        return ans