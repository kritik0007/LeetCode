class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        def getLeaves(root):
            leaves = []
            
            def dfs(node):
                if not node:
                    return
                
                if not node.left and not node.right:
                    leaves.append(node.val)
                
                dfs(node.left)
                dfs(node.right)
            
            dfs(root)
            return leaves
        
        return getLeaves(root1) == getLeaves(root2)