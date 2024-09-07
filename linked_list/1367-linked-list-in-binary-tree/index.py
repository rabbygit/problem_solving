# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # T.C: O(n * m)
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        def dfs(node: Optional[TreeNode], curr: Optional[ListNode]):
            if not curr:
                return True
            if not node or curr.val != node.val:
                return False

            return dfs(node.left, curr.next) or dfs(node.right, curr.next)

        if not root:
            return False
        if dfs(root, head):
            return True

        return self.isSubPath(head, root.left) or self.isSubPath(head, root.right)
