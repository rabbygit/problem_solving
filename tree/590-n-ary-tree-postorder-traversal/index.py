"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class RecursiveSolution:
    # T.C: O(n) and S.C: O(h)
    def postorder(self, root: "Node") -> List[int]:
        res = []

        def dfs(node):
            if not node:
                return

            for c in node.children:
                dfs(c)

            res.append(node.val)

        dfs(root)

        return res


class Solution:
    # T.C: O(n) and S.C: O(h)
    def postorder(self, root: "Node") -> List[int]:
        if not root:
            return []

        res = []
        stack = [root]
        visited = [False]

        while stack:
            node = stack.pop()

            if visited[-1]:
                res.append(node.val)
                visited.pop()
            else:
                stack.append(node)
                visited[-1] = True
                for i in range(len(node.children) - 1, -1, -1):
                    stack.append(node.children[i])
                    visited.append(False)

        return res
