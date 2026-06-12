class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        transitions = {}
        for s in allowed:
            key = s[0] + s[1]
            if key not in transitions:
                transitions[key] = []
            transitions[key].append(s[2])
            
        memo = {}
        
        def solve(row, next_row):
            if len(row) == 1:
                return True
            
            if len(next_row) == len(row) - 1:
                if next_row in memo:
                    return memo[next_row]
                result = solve(next_row, "")
                memo[next_row] = result
                return result
            
            idx = len(next_row)
            key = row[idx] + row[idx + 1]
            
            if key in transitions:
                for val in transitions[key]:
                    if solve(row, next_row + val):
                        return True
            
            return False
            
        return solve(bottom, "")