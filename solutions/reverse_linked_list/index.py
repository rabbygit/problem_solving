# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        reverse_list = None
        
        # Reverse the list
        while head:
          temp = head.next
          head.next = reverse_list
          reverse_list = head
          head = temp
        
        return reverse_list