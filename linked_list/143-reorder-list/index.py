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
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # cut link
        second_part = slow.next
        slow.next = None

        # reverse the last part of list
        reversed = None
        while second_part:
            temp = second_part.next
            second_part.next = reversed
            reversed = second_part
            second_part = temp

        # merge two list
        first_part = head
        while first_part and reversed:
            temp1 = first_part.next
            temp2 = reversed.next

            # link two list
            first_part.next = reversed
            reversed.next = temp1

            # update next pointer
            first_part = temp1
            reversed = temp2