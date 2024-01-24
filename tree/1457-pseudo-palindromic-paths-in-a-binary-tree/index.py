import collections
from typing import Optional


# Definition for a binary tree node.
class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:
        self.count = self.frequency = 0
        self.countMap = collections.defaultdict(int)
        self.dfs(root)
        return self.count

    def dfs(self, node):
        if not node: return

        # track frequency
        self.countMap[node.val] += 1
        odd_change = -1
        if self.countMap[node.val] % 2 == 1:
            odd_change = 1
        self.frequency += odd_change

        # check whether it's a leaf node 
        # and does only 1 node has an odd frequency
        if not node.left and not node.right and self.frequency < 2:
            self.count += 1

        # visit child nodes recursively
        self.dfs(node.left)
        self.dfs(node.right)

        # undone changes
        self.countMap[node.val] -= 1
        self.frequency -= odd_change