class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ans = []
        for num in nums:
            for digit in str(num):
                ans.append(int(digit))
        return ans