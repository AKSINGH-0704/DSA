class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        freq = [0] * (n + 1)
        ans = []
        common = 0
        
        for i in range(n):
            freq[A[i]] += 1
            if freq[A[i]] == 2:
                common += 1
                
            freq[B[i]] += 1
            if freq[B[i]] == 2:
                common += 1
                
            ans.append(common)
            
        return ans