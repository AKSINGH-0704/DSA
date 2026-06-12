class TrieNode:
    def __init__(self, best_idx: int):
        self.children = {}
        self.best_idx = best_idx

class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        global_best = 0
        for i in range(1, len(wordsContainer)):
            if len(wordsContainer[i]) < len(wordsContainer[global_best]):
                global_best = i
                
        root = TrieNode(global_best)
        
        for i, word in enumerate(wordsContainer):
            curr = root
            for char in reversed(word):
                if char not in curr.children:
                    curr.children[char] = TrieNode(i)
                else:
                    child = curr.children[char]
                    if len(word) < len(wordsContainer[child.best_idx]):
                        child.best_idx = i
                    elif len(word) == len(wordsContainer[child.best_idx]) and i < child.best_idx:
                        child.best_idx = i
                curr = curr.children[char]
                
        ans = []
        for query in wordsQuery:
            curr = root
            for char in reversed(query):
                if char not in curr.children:
                    break
                curr = curr.children[char]
            ans.append(curr.best_idx)
            
        return ans