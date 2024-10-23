# Definition for a binary tree node.
import collections
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # T.C and S.C: O(n)
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        levelSum = []
        q = collections.deque([root])
        while q:
            currTotal = 0
            for _ in range(len(q)):
                node = q.popleft()
                currTotal += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            levelSum.append(currTotal)

        q = collections.deque([root])
        root.val = 0
        level = 0
        while q:
            for _ in range(len(q)):
                node = q.popleft()

                siblingSum = 0
                if node.left:
                    siblingSum += node.left.val
                if node.right:
                    siblingSum += node.right.val

                if node.left:
                    node.left.val = levelSum[level + 1] - siblingSum
                    q.append(node.left)
                if node.right:
                    node.right.val = levelSum[level + 1] - siblingSum
                    q.append(node.right)
            level += 1

        return root
