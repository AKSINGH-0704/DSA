class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs)
        m = len(strs[0])
        is_sorted = [False] * (n - 1)
        delete_count = 0
        
        for j in range(m):
            to_delete = False
            for i in range(n - 1):
                if not is_sorted[i] and strs[i][j] > strs[i+1][j]:
                    to_delete = True
                    break
            
            if to_delete:
                delete_count += 1
            else:
                for i in range(n - 1):
                    if strs[i][j] < strs[i+1][j]:
                        is_sorted[i] = True
                        
        return delete_count