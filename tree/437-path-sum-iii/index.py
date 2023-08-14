# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Explanation: https://leetcode.com/problems/path-sum-iii/solutions/141424/python-step-by-step-walk-through-easy-to-understand-two-solutions-comparison/
# https://leetcode.com/problems/path-sum-iii/solutions/141424/python-step-by-step-walk-through-easy-to-understand-two-solutions-comparison/comments/657040
class Solution:

    def pathSum(self, root, target):
        self.result, self.cache = 0, {}

        # recursive to get result
        self.dfs(root, target, 0)

        return self.result

    def dfs(self, root, target, curr_sum):
        if not root:
            return None

        curr_sum = curr_sum + root.val

        if curr_sum == target:
            self.result += 1

        if (curr_sum - target) in self.cache:
            self.result += self.cache[curr_sum - target]

        if curr_sum in self.cache:
            self.cache[curr_sum] += 1
        else:
            self.cache[curr_sum] = 1

        self.dfs(root.left, target, curr_sum)
        self.dfs(root.right, target, curr_sum)

        self.cache[curr_sum] -= 1
