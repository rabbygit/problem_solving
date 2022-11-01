# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        # find middle point of the list
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # cut link
        second_part = slow.next
        slow.next = None

        # reverse the last part of list
        reversed_part = None
        while second_part:
            temp = second_part.next
            second_part.next = reversed_part
            reversed_part = second_part
            second_part = temp
        
        
        # concat two list
        first_part = head
        while first_part and reversed_part:
            temp1 = first_part.next
            temp2 = reversed_part.next

            # link two list
            first_part.next = reversed_part
            reversed_part.next = temp1

            # update next pointer
            first_part = temp1
            reversed_part = temp2