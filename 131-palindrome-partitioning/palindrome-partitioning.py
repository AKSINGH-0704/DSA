class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        
        def is_palindrome(word):
            return word == word[::-1]
        
        def backtrack(start_index, curr_partition):
            if start_index >= len(s):
                result.append(list(curr_partition))
                return  
        
            for i in range(start_index, len(s)):
                piece = s[start_index : i + 1]
                if is_palindrome(piece):  
                    curr_partition.append(piece)  
                    backtrack(i + 1, curr_partition)
                    curr_partition.pop()
        
        backtrack(0, [])
        return result
