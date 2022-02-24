"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root: "Optional[Node]") -> "Optional[Node]":
        level_list = {}
        if not root:
            return root

        # traverse tree and keep track of level
        def dfs(node, level):
            if not node:
                return

            # go to left sub-tree
            dfs(node.left, level + 1)

            # check if this level is already visited or not
            # if not visited yet then keep the current node as level's value
            # else update the level's node next pointer to point the current visiting node
            # and update level's value with current node for further update
            if level not in level_list:
                level_list[level] = node
            else:
                temp = level_list[level]
                temp.next = node
                level_list[level] = node

            # go to right sub-tree
            dfs(node.right, level + 1)

        dfs(root, 0)

        return root
