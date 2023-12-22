# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:

    def reverse(self, node, k):
        rev = None
        for _ in range(k):
            tmp = node.next
            node.next = rev
            rev = node
            node = tmp
        return rev, node

    def reverseKGroup(self, head: Optional[ListNode],
                      k: int) -> Optional[ListNode]:
        dummy = prev = ListNode(0, head)
        while prev.next:
            curr, n = prev, 0

            while n < k and curr.next:
                curr = curr.next
                n += 1

            if n == k:
                curr = prev.next
                prev.next, curr.next = self.reverse(curr, n)

            prev = curr

        return dummy.next
