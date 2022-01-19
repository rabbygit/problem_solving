# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
      # return if list has 1 or no node
      if head is None or head.next is None:
        return head

      unique_list = None
      duplicate_value = None
      result_list = None

      while head:
        # check duplicacy with previous value and next node's value
        if head.val != duplicate_value:
          if (head.next and head.next.val != head.val) or head.next is None:
            # create new node and add the node at head
            unique_list = ListNode(head.val,unique_list)
        
        duplicate_value = head.val
        head = head.next

      # reverse the list
      while unique_list:
        temp = unique_list.next
        unique_list.next = result_list
        result_list = unique_list
        unique_list = temp
      
      return result_list