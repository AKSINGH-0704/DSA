class Solution:
    def mapWordWeights(self, words: list[str], weights: list[int]) -> str:
        res = []
        for word in words:
            total_weight = 0
            for char in word:
                total_weight += weights[ord(char) - ord('a')]
            
            rem = total_weight % 26
            mapped_char = chr(ord('z') - rem)
            res.append(mapped_char)
            
        return "".join(res)