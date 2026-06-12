class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        left_sum = 0
        right_sum = sum(nums)
        ans = []
        
        for num in nums:
            right_sum -= num
            ans.append(abs(left_sum - right_sum))
            left_sum += num
            
        return ans