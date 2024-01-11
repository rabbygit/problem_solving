# Definition for a binary tree node.
from typing import Optional


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.maxDiff = 0

        def dfs(node: Optional[TreeNode], maxRoot: int, minRoot: int):
            if not node: return

            self.maxDiff = max(self.maxDiff, maxRoot - node.val,
                               node.val - minRoot)

            maxRoot = max(maxRoot, node.val)
            minRoot = min(minRoot, node.val)

            dfs(node.left, maxRoot, minRoot)
            dfs(node.right, maxRoot, minRoot)

        dfs(root, root.val, root.val)
        return self.maxDiff