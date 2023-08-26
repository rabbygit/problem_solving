# Definition for a binary tree node.
class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode',
                             q: 'TreeNode') -> 'TreeNode':
        result = self.dfs(root, p, q)
        result1 = self.dfs(root, p, p)  # show whether p exist in tree
        result2 = self.dfs(root, q, q)  # show whether q exist in tree

        if result and result1 and result2:
            return result
        if result1 is None or result2 is None:
            return None

    def dfs(self, root: 'TreeNode', p: 'TreeNode',
            q: 'TreeNode') -> 'TreeNode':
        if not root or root.val == p.val or root.val == q.val:
            return root

        left = self.dfs(root.left, p, q)
        right = self.dfs(root.right, p, q)

        if left and right:
            return root

        return right if not left else left


class Solution1:

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode',
                             q: 'TreeNode') -> 'TreeNode':
        path1 = []
        path2 = []
        idx, lca = 0, None

        self.findPath(root, path1, p.val)
        self.findPath(root, path2, q.val)

        if not path1 or not path2:
            return lca

        while idx < len(path1) and idx < len(path2):
            if path1[idx] == path2[idx]:
                lca = path1[idx]
            idx += 1

        return TreeNode(lca)

    def findPath(self, node: 'TreeNode', arr: list[int], value: int) -> bool:
        if not node:
            return False

        arr.append(node.val)

        if node.val == value:
            return True

        if self.findPath(node.left, arr, value) or self.findPath(
                node.right, arr, value):
            return True

        arr.pop()
        return False