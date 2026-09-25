class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        ans = [0] * k
        dp = [0] * k

        for num in nums:
            new_dp = [0] * k

            r = num % k
            new_dp[r] += 1

            for rem in range(k):
                new_rem = (rem * r) % k
                new_dp[new_rem] += dp[rem]

            dp = new_dp

            for rem in range(k):
                ans[rem] += dp[rem]

        return ans