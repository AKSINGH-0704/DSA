from math import isqrt

class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)
        divisors = []
        for i in range(1, isqrt(n) + 1):
            if n % i == 0:
                divisors.append(i)
                if i * i != n:
                    divisors.append(n // i)
        
        ans = 0
        for k in sorted(divisors):
            valid = True
            prev_max = -float('inf')
            for i in range(0, n, k):
                block = nums[i:i+k]
                descents = 0
                for j in range(k):
                    if block[j] > block[(j + 1) % k]:
                        descents += 1
                if descents > 1:
                    valid = False
                    break
                
                if descents == 0:
                    curr_min = block[0]
                    curr_max = block[-1]
                else:
                    drop_idx = -1
                    for j in range(k):
                        if block[j] > block[(j + 1) % k]:
                            drop_idx = j
                            break
                    curr_min = block[(drop_idx + 1) % k]
                    curr_max = block[drop_idx]
                
                if curr_min < prev_max:
                    valid = False
                    break
                prev_max = curr_max
            
            if valid:
                ans += k
        return ans