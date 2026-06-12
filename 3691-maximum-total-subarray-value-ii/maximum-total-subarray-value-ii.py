class Solution:
    def maxTotalValue(self, nums, k):
        n = len(nums)

        lg = [0] * (n + 1)
        for i in range(2, n + 1):
            lg[i] = lg[i // 2] + 1

        m = lg[n] + 1

        mx = [[0] * n for _ in range(m)]
        mn = [[0] * n for _ in range(m)]

        for i in range(n):
            mx[0][i] = nums[i]
            mn[0][i] = nums[i]

        j = 1
        while (1 << j) <= n:
            length = 1 << j
            half = length >> 1

            for i in range(n - length + 1):
                mx[j][i] = max(mx[j - 1][i], mx[j - 1][i + half])
                mn[j][i] = min(mn[j - 1][i], mn[j - 1][i + half])

            j += 1

        def value(l, r):
            length = r - l + 1
            p = lg[length]

            maximum = max(
                mx[p][l],
                mx[p][r - (1 << p) + 1]
            )

            minimum = min(
                mn[p][l],
                mn[p][r - (1 << p) + 1]
            )

            return maximum - minimum

        heap = []

        for l in range(n):
            v = value(l, n - 1)
            heapq.heappush(heap, (-v, l, n - 1))

        ans = 0

        for _ in range(k):
            v, l, r = heapq.heappop(heap)

            ans += -v

            if r > l:
                nv = value(l, r - 1)
                heapq.heappush(heap, (-nv, l, r - 1))

        return ans