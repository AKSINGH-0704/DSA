class Solution:

    def stoneGameV(self, stoneValue: list[int]) -> int:
        n = len(stoneValue)
        if n == 1:
            return 0

        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] + stoneValue[i]

        dp = [[0] * n for _ in range(n)]
        maxL = [[0] * n for _ in range(n)]
        maxR = [[0] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            dp[i][i] = 0
            maxL[i][i] = pref[i + 1]
            maxR[i][i] = pref[i + 1] - pref[i]

            mid = i
            for j in range(i + 1, n):
                if 2 * stoneValue[i] > pref[j + 1] - pref[i]:
                    dp[i][j] = maxR[i + 1][j]
                else:
                    while (
                        mid + 1 <= j - 1
                        and 2 * (pref[mid + 2] - pref[i])
                        <= pref[j + 1] - pref[i]
                    ):
                        mid += 1

                    S_L = pref[mid + 1] - pref[i]
                    S_R = pref[j + 1] - pref[mid + 1]

                    if S_L < S_R:
                        v1 = maxL[i][mid] - pref[i]
                        v2 = maxR[mid + 2][j] if mid + 2 <= j else 0
                        dp[i][j] = max(v1, v2)
                    else: 
                        v1 = maxL[i][mid - 1] - pref[i] if mid - 1 >= i else 0
                        v2 = S_L + max(dp[i][mid], dp[mid + 1][j])
                        v3 = maxR[mid + 2][j] if mid + 2 <= j else 0
                        dp[i][j] = max(v1, v2, v3)

               
                maxL[i][j] = max(maxL[i][j - 1], pref[j + 1] + dp[i][j])
                maxR[i][j] = max(
                    maxR[i + 1][j], dp[i][j] + pref[j + 1] - pref[i]
                )

        return dp[0][n - 1]