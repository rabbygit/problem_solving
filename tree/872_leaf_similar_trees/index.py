# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        root1_leaf = self.leafNodes(root1)
        root2_leaf = self.leafNodes(root2)

        if len(root1_leaf) != len(root2_leaf):
            return False

        # compare the two array
        for index in range(len(root1_leaf)):
            if root1_leaf[index] != root2_leaf[index]:
                return False

        return True

    def leafNodes(self, root):
        list = []

        if root == None:
            return list

        if root.left == None and root.right == None:
            list.append(root.val)
            return list

        l_nodes = self.leafNodes(root.left)
        r_nodes = self.leafNodes(root.right)

        list = l_nodes + r_nodes

        return list
