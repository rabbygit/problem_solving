# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        reversed = None
        current = head

        while current:
            temp = current.next
            current.next = reversed
            reversed = current
            current = temp

        return reversed

    class Solution1:
        # T.C & M.C: O(n)
        # explanation: https://www.youtube.com/watch?v=KYH83T4q6Vs&ab_channel=mycodeschool
        def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
            if not head:
                return None
            
            self.reversedHead = None
            def recurse(node):
                if node.next is None:
                    self.reversedHead = node
                    return
                recurse(node.next)
                q = node.next
                q.next = node
                node.next = None
            
            recurse(head)
            return self.reversedHead