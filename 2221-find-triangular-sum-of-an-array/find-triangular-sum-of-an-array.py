class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        while len(nums) > 1:
            new_nums = []
            for i in range(len(nums) - 1):
                val = (nums[i] + nums[i+1]) % 10
                new_nums.append(val)
            nums = new_nums
            
        return nums[0]