class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        memo = {}

        def helper(start_index):
            if start_index == len(s):
                return True
            if start_index in memo:
                return memo[start_index]
            for i in range(start_index, len(s)):
                prefix = s[start_index: i + 1]
                if prefix in word_set and helper(i + 1):
                    memo[start_index] = True
                    return True
            memo[start_index] = False
            return False

        return helper(0)
