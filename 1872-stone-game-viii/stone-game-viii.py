class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        prefix = [0] * len(stones)
        prefix[0] = stones[0]

        for i in range(1, len(stones)):
            prefix[i] = prefix[i - 1] + stones[i]

        ans = prefix[-1]

        for i in range(len(stones) - 2, 0, -1):
            ans = max(ans, prefix[i] - ans)

        return ans