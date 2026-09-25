class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        target = sum(nums) - x

        if target < 0:
            return -1

        left = 0
        curr = 0
        max_len = -1

        for right in range(len(nums)):
            curr += nums[right]

            while curr > target:
                curr -= nums[left]
                left += 1

            if curr == target:
                max_len = max(max_len, right - left + 1)

        if max_len == -1:
            return -1

        return len(nums) - max_len