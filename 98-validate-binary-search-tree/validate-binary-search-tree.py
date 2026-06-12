# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(node, min_bound, max_bound):
            if node is None:
                return True

            if not (min_bound < node.val < max_bound):
                return False

            is_left_valid = helper(node.left, min_bound, node.val)
            is_right_valid = helper(node.right, node.val, max_bound)
            return is_left_valid and is_right_valid

        return helper(root, float('-inf'), float('inf'))
