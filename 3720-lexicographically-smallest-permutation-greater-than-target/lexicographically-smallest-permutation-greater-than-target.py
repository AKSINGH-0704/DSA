class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        cnt = [0] * 26

        for c in s:
            cnt[ord(c) - ord('a')] += 1

        n = len(s)

        def build(i, greater):
            if i == n:
                return ""

            start = 0
            if not greater:
                start = ord(target[i]) - ord('a')

            for c in range(start, 26):
                if cnt[c] == 0:
                    continue

                if not greater and c < ord(target[i]) - ord('a'):
                    continue

                cnt[c] -= 1

                if greater or c > ord(target[i]) - ord('a'):
                    suffix = ''.join(chr(j + ord('a')) * cnt[j] for j in range(26))
                    cnt[c] += 1
                    return chr(c + ord('a')) + suffix

                suffix = build(i + 1, False)

                if suffix != "":
                    cnt[c] += 1
                    return chr(c + ord('a')) + suffix

                cnt[c] += 1

            return ""

        ans = build(0, False)
        return ans