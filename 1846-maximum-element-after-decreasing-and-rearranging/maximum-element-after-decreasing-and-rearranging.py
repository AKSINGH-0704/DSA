class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: list[int]) -> int:
        arr.sort()
        arr[0] = 1
        for i in range(1, len(arr)):
            if arr[i] > arr[i - 1] + 1:
                arr[i] = arr[i - 1] + 1
        return arr[-1]