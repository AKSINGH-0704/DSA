class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        prev = 0
        total = 0
        for row in bank:
            cnt = row.count('1')
            if cnt:
                if prev:
                    total += prev * cnt
                prev = cnt
        return total
