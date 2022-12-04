# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.isBalanced = True

        def findMaxHeight(root):
            if root is None:
                return 0

            left = findMaxHeight(root.left)
            right = findMaxHeight(root.right)

            diff = abs(left - right)
            self.isBalanced = self.isBalanced and diff <= 1

            return 1 + max(left, right)

        findMaxHeight(root)
        return self.isBalanced