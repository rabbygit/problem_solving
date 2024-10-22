# Definition for a binary tree node.
import collections
import heapq
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # T.C: O(n + k logn) and S.C: O(n)
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        levelSums = []
        q = collections.deque()
        q.append(root)

        while q:
            length = len(q)
            levelSum = 0

            for _ in range(length):
                node = q.popleft()
                levelSum += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            levelSums.append(-1 * levelSum)

        if len(levelSums) < k:
            return -1

        heapq.heapify(levelSums)
        while k:
            k -= 1
            res = heapq.heappop(levelSums)

        return res * -1
