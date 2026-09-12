from typing import List
from bisect import bisect_right

class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        arr = sorted(
            (l, r, w, i)
            for i, (l, r, w) in enumerate(intervals)
        )

        starts = [x[0] for x in arr]
        nxt = [0] * n
        for i in range(n):
            nxt[i] = bisect_right(starts, arr[i][1])

        dp = [[(0, ()) for _ in range(5)] for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):
            l, r, w, original_idx = arr[i]

            for k in range(1, 5):
                skip = dp[i + 1][k]

                next_score, next_indices = dp[nxt[i]][k - 1]

                take = (
                    w + next_score,
                    tuple(sorted((original_idx,) + next_indices))
                )

                if take[0] > skip[0] or (
                    take[0] == skip[0] and take[1] < skip[1]
                ):
                    dp[i][k] = take
                else:
                    dp[i][k] = skip

        return list(dp[0][4][1])