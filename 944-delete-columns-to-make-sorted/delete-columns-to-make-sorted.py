class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        count = 0
        rows = len(strs)
        cols = len(strs[0])
        
        for c in range(cols):
            for r in range(1, rows):
                if strs[r][c] < strs[r-1][c]:
                    count += 1
                    break
                    
        return count