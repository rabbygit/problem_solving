from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # T.C & S.C: O(n)
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        # leaf node
        if not root.left and not root.right:
            return bool(root.val)
        
        left = self.evaluateTree(root.left)
        right = self.evaluateTree(root.right)

        return left and right if root.val == 3 else left or right