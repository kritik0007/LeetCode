from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        result = []
        queue = deque([root])
        while queue:
            level = len(queue)
            for i in range(level):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                  queue.append(node.right)
                if i == level - 1:
                   result.append(node.val)
        return result 
            
        