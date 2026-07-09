class Solution:
    def pathExistenceQueries(self, n: int, nums: list[int], maxDiff: int, queries: list[list[int]]) -> list[bool]:
        component_id = [0] * n
        curr_id = 0
        
        for i in range(n - 1):
            component_id[i] = curr_id
            if nums[i + 1] - nums[i] > maxDiff:
                curr_id += 1
        
        component_id[n - 1] = curr_id
        
        results = []
        for u, v in queries:
            results.append(component_id[u] == component_id[v])
            
        return results
