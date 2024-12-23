import collections
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def swapsCount(self, level: list[int]) -> int:
        res = 0
        idxMap = {n: i for i, n in enumerate(level)}
        sortedLevel = sorted(level)

        for i in range(len(level)):
            if level[i] != sortedLevel[i]:
                j = idxMap[sortedLevel[i]]
                level[i], level[j] = level[j], level[i]
                idxMap[level[j]] = j
                res += 1

        return res

    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        res = 0
        q = collections.deque([root])

        while q:
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            res += self.swapsCount(level)

        return res
