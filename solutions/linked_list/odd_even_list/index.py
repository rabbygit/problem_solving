# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #If list contains no nodes or only two nodes
        if not head or not head.next:
            return head;

        prev_odd = head; # 1st node
        prev_even = head.next; # 2nd node

        current_odd = None;
        current_even = None;
        first_even = head.next;

        if prev_even.next:
            current_odd = prev_even.next; # 3rd node
    

        if current_odd and current_odd.next:
            current_even = current_odd.next; # 4th node

        while current_odd or current_even: 

            # link current odd and even position node with
            # previous odd and even nodes
            prev_odd.next = current_odd;
            prev_even.next = current_even;

            # move forward the prevous odd position's node
            prev_odd = prev_odd.next;
            # move forward the prevous even position's node
            prev_even = prev_even.next;

            # move forward the current odd position
            if current_odd.next and current_odd.next.next:
                current_odd = current_odd.next.next
            else: 
                current_odd = None;
        
            # move forward the current even position
            if current_even and current_even.next and current_even.next.next: 
                current_even = current_even.next.next;
            else:
                current_even = None;

        
        # link last odd node to first even node
        prev_odd.next = first_even;

        # return ordered head
        return head;
        
    
    