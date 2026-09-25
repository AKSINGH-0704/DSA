class Solution:
    def maxNumOfSubstrings(self, s: str):
        n = len(s)
        first = [n] * 26
        last = [-1] * 26

        for i, ch in enumerate(s):
            c = ord(ch) - ord('a')
            first[c] = min(first[c], i)
            last[c] = i

        intervals = []

        for c in range(26):
            if first[c] == n:
                continue

            l, r = first[c], last[c]
            i = l
            valid = True

            while i <= r:
                x = ord(s[i]) - ord('a')

                # Character occurs before l -> invalid
                if first[x] < l:
                    valid = False
                    break

                r = max(r, last[x])
                i += 1

            if valid:
                intervals.append((r, l))

        # Earliest ending interval first
        intervals.sort()

        ans = []
        end = -1

        for r, l in intervals:
            if l > end:
                ans.append(s[l:r + 1])
                end = r

        return ans