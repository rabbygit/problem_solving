import collections


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        q = collections.deque()
        q.append(root)

        while q:
            qLength = len(q)
            rightMostChild = None

            for i in range(qLength):
                node = q.popleft()

                # add to the queue's right side
                if node:
                    rightMostChild = node
                    q.append(node.left)
                    q.append(node.right)

            if rightMostChild:
                result.append(rightMostChild.val)

        return result