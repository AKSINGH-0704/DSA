class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        prefixes = set()
        
        for val in arr1:
            while val > 0:
                prefixes.add(val)
                val //= 10
                
        max_len = 0
        
        for val in arr2:
            while val > 0 and str(val).__len__() > max_len:
                if val in prefixes:
                    max_len = max(max_len, len(str(val)))
                    break
                val //= 10
                
        return max_len