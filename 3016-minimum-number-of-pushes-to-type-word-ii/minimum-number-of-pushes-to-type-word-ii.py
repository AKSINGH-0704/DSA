class Solution:
    def minimumPushes(self, word: str) -> int:
        freq = [0] * 26

        for ch in word:
            freq[ord(ch) - ord("a")] += 1

        freq.sort(reverse=True)

        ans = 0

        for i, count in enumerate(freq):
            if count == 0:
                break
            ans += count * (i // 8 + 1)

        return ans