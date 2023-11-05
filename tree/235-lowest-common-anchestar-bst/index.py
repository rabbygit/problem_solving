# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:

    def lowestCommonAncestor(self, root: "TreeNode", p: "TreeNode",
                             q: "TreeNode") -> "TreeNode":
        curr = root

        while curr:
            # if both p and q's values are greater than the current node, it means need to move right sub tree
            # else to left sub tree
            # otherwise, p or q must exist in left or right subtree and this current node is the ancestor
            if p.val > curr.val and q.val > curr.val:
                curr = curr.right
            elif p.val < curr.val and q.val < curr.val:
                curr = curr.left
            else:
                return curr
