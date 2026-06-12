class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        @lru_cache(None)
        def dfs(full, empty, exch):
            best = 0
            if full == 0:
                if empty >= exch:
                    return dfs(full + 1, empty - exch, exch + 1)
                return 0
            for k in range(1, full + 1):
                best = max(best, k + dfs(full - k, empty + k, exch))
            if empty >= exch:
                best = max(best, dfs(full + 1, empty - exch, exch + 1))
            return best
        return dfs(numBottles, 0, numExchange)
        