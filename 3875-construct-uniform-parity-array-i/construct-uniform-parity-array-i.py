class Solution:
    def uniformArray(self, nums1: List[int]) -> bool:
        even = sum(x % 2 == 0 for x in nums1)
        odd = len(nums1) - even

        if even == 0 or odd == 0:
            return True

        return len(nums1) > 1