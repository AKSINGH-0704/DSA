class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        word_set = set(word)
        count = 0
        
        for char in set(word.lower()):
            if char in word_set and char.upper() in word_set:
                count += 1
                
        return count