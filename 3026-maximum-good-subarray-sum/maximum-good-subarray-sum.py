class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        prefix = 0
        ans = float('-inf')
        mp = {}
        found = False

        for num in nums:
            if num - k in mp:
                ans = max(ans, prefix + num - mp[num - k])
                found = True
            if num + k in mp:
                ans = max(ans, prefix + num - mp[num + k])
                found = True

            if num in mp:
                mp[num] = min(mp[num], prefix)
            else:
                mp[num] = prefix

            prefix += num

        return ans if found else 0

        