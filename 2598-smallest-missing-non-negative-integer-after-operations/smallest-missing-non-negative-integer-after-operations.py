class Solution:
    def findSmallestInteger(self, nums: list[int], value: int) -> int:
        counts = [0] * value
        for num in nums:
            counts[num % value] += 1
        
        mex = 0
        while True:
            remainder_needed = mex % value
            
            if counts[remainder_needed] > 0:
                counts[remainder_needed] -= 1
                mex += 1
            else:
                break
        
        return mex