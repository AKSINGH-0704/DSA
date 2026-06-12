class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result: List[List[int]] = []
        
        def backtrack(curr_permutation: List[int]) -> None:
            if len(curr_permutation) == len(nums):
                result.append(list(curr_permutation))
                return
            for number in nums:
                if number in curr_permutation:
                    continue
                curr_permutation.append(number)
                backtrack(curr_permutation)
                curr_permutation.pop()
        
        backtrack([])
        return result
