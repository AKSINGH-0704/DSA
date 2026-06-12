class Solution:
    def maximumTotalDamage(self, power: list[int]) -> int:
        
        sys.setrecursionlimit(200000)

        counts = {}
        for p in power:
            if p not in counts:
                counts[p] = 0
            counts[p] += p

        unique_powers = sorted(list(counts.keys()))
        n = len(unique_powers)
        
        memo = {}

        def solve(i):
            if i >= n:
                return 0
            
            if i in memo:
                return memo[i]

            current_power = unique_powers[i]

            damage_if_skipped = solve(i + 1)
            
            next_index = i + 1
            while next_index < n and unique_powers[next_index] <= current_power + 2:
                next_index += 1
            
            damage_if_taken = counts[current_power] + solve(next_index)

            result = max(damage_if_skipped, damage_if_taken)
            memo[i] = result
            return result

        return solve(0)