class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7
        dp = 1
        last = [0] * 26

        for ch in s:
            i = ord(ch) - ord('a')
            new_dp = (dp * 2 - last[i]) % MOD
            last[i] = dp
            dp = new_dp

        return (dp - 1) % MOD