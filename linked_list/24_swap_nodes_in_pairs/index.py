# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # return if list has one or no node
        if not head or not head.next:
            return head

        # two pointer; one is ahead of another
        slow = head
        fast = head.next
        prev = None

        while slow and fast:
            temp = fast.next

            # swap head nodes
            if not prev:
                head = fast
                head.next = slow
                head.next.next = temp
            else:
                # swap nodes from middle
                prev.next = fast
                prev.next.next = slow 
                slow.next = temp

            # keep track of previous node for swaping from the middle of the list
            prev = slow

            # update the pointers to next
            slow = temp
            if slow:
                fast = slow.next

        return head