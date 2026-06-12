class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = []
        
        def dfs(node, remaining_sum, path):
            if not node:
                return
                
            path.append(node.val)
            
            if not node.left and not node.right and remaining_sum == node.val:
                ans.append(list(path))
            else:
                dfs(node.left, remaining_sum - node.val, path)
                dfs(node.right, remaining_sum - node.val, path)
                
            path.pop()
            
        dfs(root, targetSum, [])
        return ans