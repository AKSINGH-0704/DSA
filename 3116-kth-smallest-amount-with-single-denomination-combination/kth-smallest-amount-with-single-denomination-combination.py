class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        coins = sorted(coins)
        filtered = []

        for c in coins:
            if not any(c % x == 0 for x in filtered):
                filtered.append(c)

        def count(x):
            total = 0
            n = len(filtered)

            for mask in range(1, 1 << n):
                lcm = 1
                bits = 0

                for i in range(n):
                    if mask & (1 << i):
                        bits += 1
                        lcm = lcm // gcd(lcm, filtered[i]) * filtered[i]
                        if lcm > x:
                            break

                if lcm <= x:
                    if bits % 2:
                        total += x // lcm
                    else:
                        total -= x // lcm

            return total

        lo = 1
        hi = min(coins) * k

        while lo < hi:
            mid = (lo + hi) // 2

            if count(mid) >= k:
                hi = mid
            else:
                lo = mid + 1

        return lo