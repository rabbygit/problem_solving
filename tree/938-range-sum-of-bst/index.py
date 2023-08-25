# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def rangeSumBST(self, root: Optional[TreeNode], low: int,
                    high: int) -> int:
        self.sum = 0

        def dfs(node):
            if not node: return

            dfs(node.left)

            if node.val >= low and node.val <= high:
                self.sum += node.val

            dfs(node.right)

        dfs(root)

        return self.sum