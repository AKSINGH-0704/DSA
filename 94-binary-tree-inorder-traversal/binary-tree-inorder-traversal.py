class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        
        def traverse(node):
            if node is None:
                return
            traverse(node.left)
            result.append(node.val)
            traverse(node.right)
        
        traverse(root)
        return result
