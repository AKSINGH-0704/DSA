class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n = len(nums)
        i = n - 2
        
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
            
        if i >= 0:
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
            
        nums[i + 1:] = reversed(nums[i + 1:])