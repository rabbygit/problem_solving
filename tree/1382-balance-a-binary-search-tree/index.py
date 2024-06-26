# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        return self.constructBST(self.buildInorderArray(root))

    def constructBST(self, inorder: List[int]) -> TreeNode:
        def helper(l: int, r: int) -> TreeNode:
            if l > r:
                return

            m = l + (r - l) // 2
            root = TreeNode(inorder[m])
            root.left = helper(l, m - 1)
            root.right = helper(m + 1, r)

            return root

        return helper(0, len(inorder) - 1)

    def buildInorderArray(self, root: TreeNode):
        inorder = []

        def dfs(node: TreeNode) -> None:
            if not node:
                return

            dfs(node.left)
            inorder.append(node.val)
            dfs(node.right)

        dfs(root)
        return inorder
