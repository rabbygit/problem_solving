"""
Given the root of a binary tree, collect a tree's nodes as if you were doing this:

1. Collect all the leaf nodes.
2. Remove all the leaf nodes.
3. Repeat until the tree is empty.
Image: https://assets.leetcode.com/uploads/2021/03/16/remleaves-tree.jpg
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections


class Solution:

    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        nodes = collections.defaultdict(list)

        def dfs(node, level):
            if not node:
                return level

            # post order traversal
            leftMaxLevel = dfs(node.left, level)
            rightMaxLevel = dfs(node.right, level)

            maxLevel = max(leftMaxLevel, rightMaxLevel)
            nodes[maxLevel].append(node.val)

            return maxLevel + 1

        dfs(root, 0)

        return nodes.values()