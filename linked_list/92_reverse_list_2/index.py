# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        count = 1 # track start and end point to reverse
        start = None # starting node
        prev_start = None # previous node of starting point
        end = None # end node
        next_end = None # next node of ending node
        prev = None # previous node of any node
        runner = head


         # loop through until reach to the end point
        while (count <= right):
            next = runner.next # keep the next pointer

            # starting point
            if (count == left):
                start = runner
                prev_start = prev

            # middle nodes between start and end point
            # change pointer of the current node to its previous node
            if (count > left and count < right):
                runner.next = prev

            # ending point
            if (count == right):
                end = runner
                next_end = runner.next
                runner.next = prev


            prev = runner
            runner = next
            count+=1

        start.next = next_end # starting node's will point to the end node's next

        # previous node of starting point(if it's not the beginning of list) 
        # will point to the end node of reversed portion. 
        # otherwise, replace head pointer with the end node of reversed portion
        if (prev_start): prev_start.next = end
        else: head = end

        return head