# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections


class Solution:

    def pathSum(self, root, target):
        self.result = 0
        self.sumMap = collections.defaultdict(int)

        self.dfs(root, target, 0)

        return self.result

    def dfs(self, node, target, currSum):
        if not node:
            return

        currSum += node.val
        if currSum == target:
            self.result += 1

        self.result += self.sumMap.get(currSum - target, 0)
        self.sumMap[currSum] = self.sumMap.get(currSum, 0) + 1

        self.dfs(node.left, target, currSum)
        self.dfs(node.right, target, currSum)

        self.sumMap[currSum] -= 1
