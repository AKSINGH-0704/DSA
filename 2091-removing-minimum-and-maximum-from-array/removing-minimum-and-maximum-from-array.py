class Solution:
    def minimumDeletions(self, nums):
        n = len(nums)

        min_index = nums.index(min(nums))
        max_index = nums.index(max(nums))

        left = min(min_index, max_index)
        right = max(min_index, max_index)

        remove_from_left = right + 1
        remove_from_right = n - left
        remove_both = left + 1 + n - right

        return min(remove_from_left, remove_from_right, remove_both)