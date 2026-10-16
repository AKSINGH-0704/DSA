from typing import List

class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        s, sq, lazy = [0] * (4 * n), [0] * (4 * n), [0] * (4 * n)

        def apply(node, l, r, v):
            length = r - l + 1
            s[node], sq[node] = (
                (s[node] + v * length) % MOD,
                (sq[node] + 2 * v * s[node] + v * v * length) % MOD
            )
            lazy[node] = (lazy[node] + v) % MOD

        def push(node, l, r):
            if lazy[node] and l < r:
                m = (l + r) // 2
                apply(node * 2, l, m, lazy[node])
                apply(node * 2 + 1, m + 1, r, lazy[node])
                lazy[node] = 0

        def update(node, l, r, ql, qr):
            if ql <= l and r <= qr:
                apply(node, l, r, 1)
                return
            push(node, l, r)
            m = (l + r) // 2
            if ql <= m:
                update(node * 2, l, m, ql, qr)
            if qr > m:
                update(node * 2 + 1, m + 1, r, ql, qr)
            s[node] = (s[node * 2] + s[node * 2 + 1]) % MOD
            sq[node] = (sq[node * 2] + sq[node * 2 + 1]) % MOD

        last, ans = {}, 0

        for i, x in enumerate(nums):
            p = last.get(x, -1)
            update(1, 0, n - 1, p + 1, i)
            ans = (ans + sq[1]) % MOD
            last[x] = i

        return ans