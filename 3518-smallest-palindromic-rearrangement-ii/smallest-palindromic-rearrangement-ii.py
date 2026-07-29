class Solution:

    def smallestPalindrome(self, s: str, k: int) -> str:
        n = len(s)
        half_len = n // 2
        MAX_K = 10**6 + 1

        counts = [0] * 26
        for char in s[:half_len]:
            counts[ord(char) - ord("a")] += 1

        def count_arrangements(c_list: list[int]) -> int:
            rem_len = sum(c_list)
            res = 1
            for count in c_list:
                if count > 0:
                    res *= math.comb(rem_len, count)
                    rem_len -= count
                    if res >= MAX_K:
                        return MAX_K
            return res

        if count_arrangements(counts) < k:
            return ""

        left_half = []

        for _ in range(half_len):
            for i in range(26):
                if counts[i] > 0:
                    counts[i] -= 1
                    ways = count_arrangements(counts)

                    if k <= ways:
                        left_half.append(chr(ord("a") + i))
                        break
                    else:
                     
                        k -= ways
                        counts[i] += 1  

        left_str = "".join(left_half)
        middle = s[half_len] if n % 2 != 0 else ""

        return left_str + middle + left_str[::-1]