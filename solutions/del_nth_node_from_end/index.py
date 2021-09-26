# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        current_node = head
        previous_node = head
        i = 1
        found = False
        
        while current_node:
            temp = current_node
            
            # Loop through from the current node to end
            # check if current node is the n-th node
            for index in range(1,n+1):
                if temp.next is None:
                    found = True
                    break
                
                temp = temp.next
            
            if found == True:
              break

            # move forward and keep track of previous node
            previous_node = current_node
            current_node = current_node.next
            i += 1

        if i == 1:
          head = previous_node.next # remove from head
        else:
          previous_node.next = previous_node.next.next
        
        return head