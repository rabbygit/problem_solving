# Definition for a binary tree node.
class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode',
                             q: 'TreeNode') -> 'TreeNode':
        if not root or root.val == p.val or root.val == q.val:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root

        return right if not left else right


class Solution1:

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode',
                             q: 'TreeNode') -> 'TreeNode':
        path1 = []
        path2 = []
        idx, lca = 0, root.val

        self.findPath(root, path1, p.val)
        self.findPath(root, path2, q.val)

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