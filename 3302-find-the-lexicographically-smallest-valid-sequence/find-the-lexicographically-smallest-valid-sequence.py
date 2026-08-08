class Solution:

    def validSequence(self, word1: str, word2: str) -> list[int]:
        n, m = len(word1), len(word2)

        R = [-1] * (m + 1)
        R[m] = n

        r_idx = n - 1
        for j in range(m - 1, -1, -1):
            while r_idx >= 0 and word1[r_idx] != word2[j]:
                r_idx -= 1
            if r_idx >= 0:
                R[j] = r_idx
                r_idx -= 1  

        ans = []
        curr_i = 0
        changed = False

        for j in range(m):
            found = False
            while curr_i < n:
                i = curr_i

                if word1[i] == word2[j]:
                    if not changed or i < R[j + 1]:
                        ans.append(i)
                        curr_i = i + 1
                        found = True
                        break

                elif not changed and i < R[j + 1]:
                    changed = True
                    ans.append(i)
                    curr_i = i + 1
                    found = True
                    break

                curr_i += 1

            if not found:
                return []

        return ans