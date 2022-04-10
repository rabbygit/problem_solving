# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.MIN_INT = float('-inf')

    def checkBalance(self, root):
        if root == None:
            return -1

        left_tree_height = self.checkBalance(root.left)
        if left_tree_height == self.MIN_INT:
            return self.MIN_INT

        right_tree_height = self.checkBalance(root.right)
        if right_tree_height == self.MIN_INT:
            return self.MIN_INT

        diff = abs(left_tree_height-right_tree_height)
        if diff > 1:
            return self.MIN_INT
        else:
            return max(left_tree_height,right_tree_height)+1


    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.checkBalance(root) != self.MIN_INT