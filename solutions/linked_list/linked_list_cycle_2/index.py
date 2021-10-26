# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
      if head is None or head.next is None:
          return None
        
      slow = head
      fast = head
        
      while slow:
        if fast and fast.next:
          slow = slow.next
          fast = fast.next.next
        else:
          return None
          
        if slow == fast:
          break;
          
      slow2 = head
      
      while slow2 != slow:
        slow2 = slow2.next
        slow = slow.next
      
      return slow2
          
      
          
        