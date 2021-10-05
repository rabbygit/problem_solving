# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return True

        slow = head
        fast = head
        reversed = None
        
        # find the middle of the list
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # set None to the left half
        reversed = slow
        slow = slow.next
        reversed.next = None

        # reverse the right half
        while slow:
            temp = slow.next
            slow.next = reversed
            reversed = slow
            slow = temp

        # compare two halves of the list
        while head and reversed:
            if head.val != reversed.val:
                return False
            else:
                head = head.next
                reversed = reversed.next
        
        return True