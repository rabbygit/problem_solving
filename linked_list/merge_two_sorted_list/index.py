# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = None
        reverse = None
        
        # if both lists have node
        while l1 and l2:
          val = 0
          if l1.val >= l2.val:
            val = l2.val
            l2 = l2.next
          else:
            val = l1.val
            l1 = l1.next
          
          result = ListNode(val,result)
        
        # if l1 list has remaining node
        while l1:
          result = ListNode(l1.val,result)
          l1 = l1.next
        
        # if l2 list has remaining node
        while l2:
          result = ListNode(l2.val,result)
          l2 = l2.next

        # reverse the list
        while result:
          temp = result.next
          result.next = reverse
          reverse = result
          result = temp
        
        return reverse