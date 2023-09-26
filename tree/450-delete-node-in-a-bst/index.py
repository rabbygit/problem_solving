# Definition for a binary tree node.
from typing import Optional

# class TreeNode:

#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:

    def deleteNode(self, root, key):
        # if root doesn't exist, just return it
        if not root:
            return root

        # if key value is less than root value, find the node in the left subtree
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        # if key value is greater than root value, find the node in right subtree
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        #if we found the node (root.value == key), start to delete it
        else:
            # if it doesn't have right children,
            # we delete the node then new root would be root.left
            if not root.right:
                return root.left
            # if it has no left children,
            # we delete the node then new root would be root.right
            if not root.left:
                return root.right

            # if the node have both left and right children
            # we replace its value with the minmimum value in the right subtree and then delete that minimum node in the right subtree
            curr = root.right
            while curr.left:
                curr = curr.left
            # replace the found node's value with the minimum value of the right subtree
            root.val = curr.val
            # delete the minimum node(duplicate) in right subtree
            root.right = self.deleteNode(root.right, root.val)

        return root
