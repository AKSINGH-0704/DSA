class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        from functools import lru_cache

        @lru_cache(None)
        def solve(left, right):
            if left == right:
                return nums[left]

            take_left = nums[left] - solve(left + 1, right)
            take_right = nums[right] - solve(left, right - 1)

            return max(take_left, take_right)

        return solve(0, len(nums) - 1) >= 0