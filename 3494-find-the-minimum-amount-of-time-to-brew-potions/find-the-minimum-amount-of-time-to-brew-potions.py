class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        n = len(skill)
        m = len(mana)
        prev = [0] * n
        running = 0
        for i in range(n):
            running += skill[i] * mana[0]
            prev[i] = running
        offset = 0
        for j in range(1, m):
            cur = [0] * n
            running = 0
            mx = -10**18
            for i in range(n):
                running += skill[i] * mana[j]
                cur[i] = running
                left = cur[i-1] if i-1 >= 0 else 0
                diff = prev[i] - left
                if diff > mx:
                    mx = diff
            if mx < 0:
                mx = 0
            offset += mx
            prev = cur
        return offset + prev[-1]
