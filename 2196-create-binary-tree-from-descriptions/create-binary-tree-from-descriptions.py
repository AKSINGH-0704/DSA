class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodes = {}
        children = set()
        
        for p, c, is_left in descriptions:
            if p not in nodes:
                nodes[p] = TreeNode(p)
            if c not in nodes:
                nodes[c] = TreeNode(c)
                
            if is_left == 1:
                nodes[p].left = nodes[c]
            else:
                nodes[p].right = nodes[c]
                
            children.add(c)
            
        for p, _, _ in descriptions:
            if p not in children:
                return nodes[p]
                
        return None