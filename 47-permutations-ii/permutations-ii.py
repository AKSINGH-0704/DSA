class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        visited = [False]*len(nums)
        
        def backtrack(curr_permute):
            if len(curr_permute)==len(nums):
                result.append(list(curr_permute))
            
            for i in range(len(nums)):
                if visited[i] or (i>0 and nums[i]==nums[i-1] and not visited[i-1]):
                    continue
                
                visited[i]= True
                curr_permute.append(nums[i])
                backtrack(curr_permute)
                curr_permute.pop()
                visited[i] = False
        backtrack([])
        return result