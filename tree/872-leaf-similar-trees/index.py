from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:

    def leafSimilar(self, root1: Optional[TreeNode],
                    root2: Optional[TreeNode]) -> bool:
        leafValues1 = []
        leafValues2 = []

        self.getLeafValues(root1, leafValues1)
        self.getLeafValues(root2, leafValues2)

        return leafValues1 == leafValues2

    def getLeafValues(self, node: Optional[TreeNode], leafValues: list[int]):
        if not node: return

        if not node.left and not node.right:
            leafValues.append(node.val)
            return

        self.getLeafValues(node.left, leafValues)
        self.getLeafValues(node.right, leafValues)
