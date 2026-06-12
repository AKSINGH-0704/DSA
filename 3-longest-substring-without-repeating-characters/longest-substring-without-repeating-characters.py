class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = {}
        start = 0
        max_len = 0
        
        for end, char in enumerate(s):
            if char in last_seen and last_seen[char] >= start:
                start = last_seen[char] + 1
            
            last_seen[char] = end
            max_len = max(max_len, end - start + 1)
            
        return max_len