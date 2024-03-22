from typing import Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        reversed = None

        # find the middle of the list
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse the right half
        while slow:
            temp = slow.next
            slow.next = reversed
            reversed = slow
            slow = temp

        # compare two halves of the list
        while reversed:
            if head.val != reversed.val:
                return False
            else:
                head = head.next
                reversed = reversed.next

        return True
