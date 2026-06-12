class Solution:
    def countPartitions(self, nums, k):
        MOD = 10**9 + 7
        n = len(nums)
        maxd = deque()
        mind = deque()
        L = 0
        dp = [0] * (n + 1)
        pref = [0] * (n + 1)
        dp[0] = 1
        pref[0] = 1
        for i in range(n):
            x = nums[i]
            while maxd and nums[maxd[-1]] <= x:
                maxd.pop()
            maxd.append(i)
            while mind and nums[mind[-1]] >= x:
                mind.pop()
            mind.append(i)
            while nums[maxd[0]] - nums[mind[0]] > k:
                if maxd and maxd[0] == L:
                    maxd.popleft()
                if mind and mind[0] == L:
                    mind.popleft()
                L += 1
            if L == 0:
                prev = 0
            else:
                prev = pref[L-1]
            dp[i+1] = (pref[i] - prev) % MOD
            pref[i+1] = (pref[i] + dp[i+1]) % MOD
        return dp[n] % MOD
