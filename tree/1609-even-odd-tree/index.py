import collections
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        level = 0
        q = collections.deque([root])

        while q:
            level_length = len(q)
            last_val = None

            for _ in range(level_length):
                node = q.popleft()
                if level % 2 == 0:
                    # even level
                    if node.val % 2 == 0:
                        return False
                    elif last_val != None and node.val <= last_val:
                        return False
                else:
                    # odd level
                    if node.val % 2 != 0:
                        return False
                    elif last_val != None and node.val >= last_val:
                        return False

                last_val = node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            level += 1

        return True
