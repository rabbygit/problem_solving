# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.currSum = 0

        def dfs(node: TreeNode):
            if not node:
                return node

            dfs(node.right)
            node.val += self.currSum
            self.currSum = node.val
            dfs(node.left)

            return node

        return dfs(root)
