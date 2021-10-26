# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        previous = None
        current = head
        is_head = True

        while current:
            # check the value whether equal
            if current.val == val:
                if  is_head:
                    # remove from head
                    head = head.next
                elif current.next is None:
                    # remove the last node
                    previous.next = None
                else:
                    # remove from middle
                    previous.next = current.next
            else:
                is_head = False # track head
                previous = current # track unmatched node
            
            current = current.next

        return head