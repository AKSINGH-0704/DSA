class Solution:
    def countMajoritySubarrays(self, nums: list[int], target: int) -> int:
        n = len(nums)
        transformed = [1 if x == target else -1 for x in nums]
        
        prefix_sums = [0] * (n + 1)
        for i in range(n):
            prefix_sums[i+1] = prefix_sums[i] + transformed[i]
        count = 0
        for i in range(n + 1):
            for j in range(i + 1, n + 1):
                if prefix_sums[j] > prefix_sums[i]:
                    count += 1
                    
        return count