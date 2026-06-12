class Solution:
    def minimumDistance(self, word: str) -> int:
        def d(a, b):
            if a == 26: return 0
            return abs(a // 6 - b // 6) + abs(a % 6 - b % 6)
            
        dp = {26: 0}
        p = 26
        
        for char in word:
            c = ord(char) - 65
            nxt = {}
            for f, v in dp.items():
                nxt[f] = min(nxt.get(f, float('inf')), v + d(p, c))
                nxt[p] = min(nxt.get(p, float('inf')), v + d(f, c))
            dp = nxt
            p = c
            
        return min(dp.values())