class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_dia = [0]

        def dfs(node):
            if node is None:
                return -1

            left_height = dfs(node.left)
            right_height = dfs(node.right)

            curr_dia = left_height + right_height + 2
            max_dia[0] = max(max_dia[0], curr_dia)

            return 1 + max(left_height, right_height)

        
        dfs(root)
        return max_dia[0]
