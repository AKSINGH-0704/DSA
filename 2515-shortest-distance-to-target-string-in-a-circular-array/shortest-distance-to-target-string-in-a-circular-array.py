class Solution:
    def closestTarget(self, words: list[str], target: str, startIndex: int) -> int:
        n = len(words)
        r = -1
        for i, w in enumerate(words):
            if w == target:
                d = abs(i - startIndex)
                v = min(d, n - d)
                if r < 0 or v < r:
                    r = v
        return r
