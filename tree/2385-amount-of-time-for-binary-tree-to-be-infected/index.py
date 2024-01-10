# Definition for a binary tree node.
import collections
from typing import Optional


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        self.adj = collections.defaultdict(list)
        self.buildAdjList(root)

        minutes = 0
        visited = set()
        q = collections.deque()
        q.append(start)
        visited.add(start)

        while q:
            qLength = len(q)
            infected = False

            for _ in range(qLength):
                infectedNode = q.popleft()
                for neighbor in self.adj[infectedNode]:
                    if neighbor not in visited:
                        q.append(neighbor)
                        visited.add(neighbor)
                        infected = True

            if infected == True:
                minutes += 1

        return minutes

    def buildAdjList(self, node: Optional[TreeNode]):
        if not node: return

        if node.left:
            self.adj[node.val].append(node.left.val)
            self.adj[node.left.val].append(node.val)
            self.buildAdjList(node.left)

        if node.right:
            self.adj[node.val].append(node.right.val)
            self.adj[node.right.val].append(node.val)
            self.buildAdjList(node.right)
