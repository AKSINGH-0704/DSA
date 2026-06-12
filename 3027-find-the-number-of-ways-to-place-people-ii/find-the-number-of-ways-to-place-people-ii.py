import math

class Solution:
    def numberOfPairs(self, points: list[list[int]]) -> int:
        n = len(points)
        ans = 0
        for i in range(n):
            alice_x, alice_y = points[i]
            
            candidates = []
            for j in range(n):
                if i == j:
                    continue
                
                bob_x, bob_y = points[j]
                if bob_x >= alice_x and bob_y <= alice_y:
                    candidates.append(points[j])

            if not candidates:
                continue

            candidates.sort(key=lambda p: (p[0], -p[1]))

            max_y_so_far = -math.inf
            for cand_x, cand_y in candidates:
                if cand_y > max_y_so_far:
                    ans += 1
                max_y_so_far = max(max_y_so_far, cand_y)
                
        return ans