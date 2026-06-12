class Solution:
    def findTheString(self, lcp: list[list[int]]) -> str:
        n = len(lcp)
        word = [""] * n
        curr_char = 'a'
        
        
        for i in range(n):
            if not word[i]:
                if curr_char > 'z':
                    return ""
                
                
                for j in range(i, n):
                    if lcp[i][j] > 0:
                        word[j] = curr_char
                        
                curr_char = chr(ord(curr_char) + 1)
                
        
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if word[i] == word[j]:
                    expected = 1 + (lcp[i + 1][j + 1] if i + 1 < n and j + 1 < n else 0)
                else:
                    expected = 0
                    
                if lcp[i][j] != expected:
                    return ""
                    
        return "".join(word)