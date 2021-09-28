# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
      track_node = None
      reverse = None
      while head:
        # check unique value and add it to head
        if track_node is None or track_node.val != head.val:
          track_node = ListNode(head.val,track_node)
        head = head.next
      
      # reverse the list
      while track_node:
        temp = track_node.next
        track_node.next = reverse
        reverse = track_node
        track_node = temp

      return reverse
