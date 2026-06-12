class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq = Counter(nums)
        max_freq = max(freq.values())        
       
        total_max_freq = sum(count for count in freq.values() if count == max_freq)
        
        return total_max_freq
        