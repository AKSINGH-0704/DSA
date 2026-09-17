from typing import List

class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)
        best = [float('inf')] * n
        ans = float('inf')
        left = 0
        curr = 0
        min_len = float('inf')

        for right in range(n):
            curr += arr[right]

            while curr > target:
                curr -= arr[left]
                left += 1

            if curr == target:
                length = right - left + 1
                if left > 0 and best[left - 1] != float('inf'):
                    ans = min(ans, length + best[left - 1])
                min_len = min(min_len, length)

            best[right] = min_len

        return -1 if ans == float('inf') else ans