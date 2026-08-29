class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)
        m = n // 2

        cnt = [0] * 26
        for ch in s:
            cnt[ord(ch) - ord('a')] += 1

        odd = [i for i in range(26) if cnt[i] % 2]

        if len(odd) > 1:
            return ""

        mid = chr(odd[0] + 97) if odd else ""


        half = [x // 2 for x in cnt]

      
        def build(left):
            left = ''.join(left)
            return left + mid + left[::-1]

        available = half[:]
        left = []
        possible = True

        for i in range(m):
            c = ord(target[i]) - 97

            if available[c] == 0:
                possible = False
                break

            left.append(target[i])
            available[c] -= 1

        if possible:
       
            pal = build(left)

            if pal > target:
                return pal

        for pos in range(m - 1, -1, -1):

            available = half[:]
            prefix = []
            possible = True

            for i in range(pos):
                c = ord(target[i]) - 97

                if available[c] == 0:
                    possible = False
                    break

                prefix.append(target[i])
                available[c] -= 1

            if not possible:
                continue

            t = ord(target[pos]) - 97

            bigger = -1

            for c in range(t + 1, 26):
                if available[c] > 0:
                    bigger = c
                    break

            if bigger == -1:
                continue

            prefix.append(chr(bigger + 97))
            available[bigger] -= 1

            
            for c in range(26):
                prefix.extend(chr(c + 97) for _ in range(available[c]))

            return build(prefix)

        return ""