# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        reversed = None
        current = head

        while current:
            temp = current.next
            current.next = reversed
            reversed = current
            current = temp

        return reversed

    def reverseListRecurse(self,
                           head: Optional[ListNode]) -> Optional[ListNode]:
        reversedHead = None

        def recurse(current):
            if current.next is None:
                nonlocal reversedHead
                reversedHead = current
                return

            recurse(current.next)
            temp = current.next
            temp.next = current
            current.next = None

        if head:
            recurse(head)

        return reversedHead
