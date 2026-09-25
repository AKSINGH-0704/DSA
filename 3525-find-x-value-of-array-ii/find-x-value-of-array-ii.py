class Solution:
    def resultArray(self, nums, k, queries):
        n = len(nums)
        tree = [[0] * (k + 1) for _ in range(4 * n)]

        def merge(left, right):
            res = [0] * (k + 1)

            # Product of entire segment
            res[0] = (left[0] * right[0]) % k

            # Prefixes entirely inside left segment
            for r in range(k):
                res[r + 1] += left[r + 1]

            # Prefixes that extend into right segment
            shift = left[0]

            for r in range(k):
                new_r = (shift * r) % k
                res[new_r + 1] += right[r + 1]

            return res

        def build(node, l, r):
            if l == r:
                p = nums[l] % k
                tree[node][0] = p
                tree[node][p + 1] = 1
                return

            mid = (l + r) // 2

            build(node * 2, l, mid)
            build(node * 2 + 1, mid + 1, r)

            tree[node] = merge(
                tree[node * 2],
                tree[node * 2 + 1]
            )

        def update(node, l, r, idx, value):
            if l == r:
                p = value % k

                tree[node] = [0] * (k + 1)
                tree[node][0] = p
                tree[node][p + 1] = 1
                return

            mid = (l + r) // 2

            if idx <= mid:
                update(node * 2, l, mid, idx, value)
            else:
                update(node * 2 + 1, mid + 1, r, idx, value)

            tree[node] = merge(
                tree[node * 2],
                tree[node * 2 + 1]
            )

        def query(node, l, r, ql):
            if ql <= l:
                return tree[node]

            mid = (l + r) // 2

            if ql > mid:
                return query(node * 2 + 1, mid + 1, r, ql)

            left_part = query(node * 2, l, mid, ql)
            right_part = tree[node * 2 + 1]

            return merge(left_part, right_part)

        build(1, 0, n - 1)

        ans = []

        for index, value, start, x in queries:
            update(1, 0, n - 1, index, value)

            result = query(1, 0, n - 1, start)

            ans.append(result[x + 1])

        return ans