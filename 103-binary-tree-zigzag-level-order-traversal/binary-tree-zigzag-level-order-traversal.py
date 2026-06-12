class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        
        result = []
        queue = [root]
        level_no = 0

        while len(queue) > 0:
            level_size = len(queue)
            curr_level = []
            
            for i in range(level_size):
                node = queue.pop(0)
                curr_level.append(node.val)  
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            if level_no % 2 == 1:
                curr_level.reverse()
            
            result.append(curr_level)
            level_no += 1
        
        return result
