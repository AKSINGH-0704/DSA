class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        n = len(nums)
        total = 0
        max_steps = 200000

        def simulate(start: int, direction: int) -> bool:
            arr = nums[:] 
            curr = start
            dir = direction
            steps = 0
            while 0 <= curr < n and steps < max_steps:
                steps += 1
                if arr[curr] == 0:
                    curr += dir
                else:
                    arr[curr] -= 1
                    dir = -dir
                    curr += dir
            return all(x == 0 for x in arr)

        for i in range(n):
            if nums[i] == 0:
                if simulate(i, -1):
                    total += 1
                if simulate(i, 1):
                    total += 1
        return total
