class Solution:
    def minInsertions(self, s: str) -> int:
        open_count = 0
        insertions = 0
        i = 0

        while i < len(s):
            if s[i] == '(':
                open_count += 1
            else:
                if i + 1 < len(s) and s[i + 1] == ')':
                    i += 1
                else:
                    insertions += 1

                if open_count > 0:
                    open_count -= 1
                else:
                    insertions += 1

            i += 1

        return insertions + 2 * open_count