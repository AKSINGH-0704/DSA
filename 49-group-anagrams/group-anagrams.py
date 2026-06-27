from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        ans = defaultdict(list)
        
        for s in strs:
            key = "".join(sorted(s))
            ans[key].append(s)
            
        return list(ans.values())