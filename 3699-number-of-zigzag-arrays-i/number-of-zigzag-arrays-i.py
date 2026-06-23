class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:

        MOD = 10**9 + 7
        m = r - l + 1

        up = [0] * m
        down = [0] * m

        for v in range(m):

            up[v] = v
            down[v] = m - 1 - v

        if n == 2:
            return sum(up) + sum(down)

        for _ in range(3, n + 1):

            prefix_up = [0] * (m + 1)
            prefix_down = [0] * (m + 1)

            for i in range(m):
                prefix_up[i + 1] = (prefix_up[i] + up[i]) % MOD
                prefix_down[i + 1] = (prefix_down[i] + down[i]) % MOD

            total_up = prefix_up[m]
            total_down = prefix_down[m]

            new_up = [0] * m
            new_down = [0] * m

            for v in range(m):

                new_up[v] = prefix_down[v]

                new_down[v] = (total_up - prefix_up[v + 1]) % MOD

            up = new_up
            down = new_down

        return (sum(up) + sum(down)) % MOD