# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def traverse(root, level):
            if root is None:
                return level

            leftMaxDepth = traverse(root.left, level + 1)
            rightMaxDepth = traverse(root.right, level + 1)

            return max(leftMaxDepth, rightMaxDepth)

        return traverse(root, 0)
