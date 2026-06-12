class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest = 0
        last_index = len(nums) - 1
        
        for i in range(len(nums)):
            if i > farthest:
                return False
            farthest = max(farthest, i + nums[i])
            if farthest >= last_index:
                return True
        return True
