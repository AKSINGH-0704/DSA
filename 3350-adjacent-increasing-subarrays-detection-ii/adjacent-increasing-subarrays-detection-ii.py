class Solution:
    def maxIncreasingSubarrays(self, nums: list[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0

        increasing_len = [1] * n
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                increasing_len[i] = increasing_len[i - 1] + 1
        
        max_k = 0
        low, high = 1, n // 2
        
        while low <= high:
            k = low + (high - low) // 2
            
            possible = False
            for i in range(n - 2 * k + 1):
                first_subarray_ok = (increasing_len[i + k - 1] >= k)
                second_subarray_ok = (increasing_len[i + 2 * k - 1] >= k)
                
                if first_subarray_ok and second_subarray_ok:
                    possible = True
                    break
            
            if possible:
                max_k = k
                low = k + 1
            else:
                high = k - 1
                
        return max_k