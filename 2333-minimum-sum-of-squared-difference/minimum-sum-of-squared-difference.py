class Solution:
    def minSumSquareDiff(self, nums1, nums2, k1, k2):
        k = k1 + k2

        diff = [abs(a - b) for a, b in zip(nums1, nums2)]

        if sum(diff) <= k:
            return 0

        left, right = 0, max(diff)

        while left < right:
            mid = (left + right) // 2

            ops = sum(max(0, d - mid) for d in diff)

            if ops <= k:
                right = mid
            else:
                left = mid + 1

        x = left

        remaining = k

        for i in range(len(diff)):
            if diff[i] > x:
                remaining -= diff[i] - x
                diff[i] = x

        for i in range(len(diff)):
            if remaining > 0 and diff[i] == x:
                diff[i] -= 1
                remaining -= 1

        return sum(d * d for d in diff)