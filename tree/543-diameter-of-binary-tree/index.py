# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = float("-inf")

        def findMax(root):
            if root is None:
                return 0

            leftMax = findMax(root.left)
            rightMax = findMax(root.right)

            self.diameter = max(self.diameter, leftMax + rightMax)

            return 1 + max(leftMax, rightMax)

        findMax(root)

        return self.diameter
