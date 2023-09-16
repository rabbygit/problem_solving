# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        minVal = [float('inf')]

        def dfs(node):
            if not node:
                return

            dfs(node.left)

            if node.val != root.val:
                minVal[0] = min(minVal[0], node.val)

            dfs(node.right)

        dfs(root)

        return -1 if minVal[0] == float('inf') else minVal[0]