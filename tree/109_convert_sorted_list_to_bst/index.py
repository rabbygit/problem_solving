# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        length = 0
        index_map = {}

        node = head
        while node:
            index_map[length] = node.val
            length += 1
            node = node.next

        def constructBST(left, right):
            if left > right:
                return None

            mid = int((left + right) / 2)

            root = TreeNode(index_map[mid])

            root.left = constructBST(left, mid - 1)
            root.right = constructBST(mid + 1, right)

            return root

        return constructBST(0, length - 1)
