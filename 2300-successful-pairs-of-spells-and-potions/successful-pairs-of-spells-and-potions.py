class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        m = len(potions)
        ans = []
        for s in spells:
            need = (success + s - 1) // s
            idx = bisect_left(potions, need)
            ans.append(m - idx)
        return ans
