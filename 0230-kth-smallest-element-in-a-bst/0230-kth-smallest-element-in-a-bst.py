from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.c = 0
        self.ans = None

        def inord(root):
            if not root or self.ans is not None:
                return
            
            inord(root.left)

            self.c += 1
            if self.c == k:
                self.ans = root.val
                return

            inord(root.right)

        inord(root)
        return self.ans