class Solution:
    def hasIncreasingSubarrays(self, nums: list[int], k: int) -> bool:
        n = len(nums)
        if 2 * k > n:
            return False

        for i in range(n - 2 * k + 1):
            first_is_increasing = True
            for j in range(i, i + k - 1):
                if nums[j] >= nums[j + 1]:
                    first_is_increasing = False
                    break
            
            if first_is_increasing:
                second_is_increasing = True
                for j in range(i + k, i + 2 * k - 1):
                    if nums[j] >= nums[j + 1]:
                        second_is_increasing = False
                        break
                
                if second_is_increasing:
                    return True
        
        return False