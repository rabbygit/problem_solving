# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional


class Solution:
    # T.C & S.C: O(n)
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        curr = head

        # build the decreasing stack with filtered nodes
        while curr:
            while stack and stack[-1] < curr.val:
                stack.pop()
            stack.append(curr.val)
            curr = curr.next

        # build the linked list from the stack
        tail = dummy_head = ListNode("#")
        for val in stack:
            new_node = ListNode(val)
            tail.next = new_node
            tail = tail.next

        return dummy_head.next


class Solution2:
    # T.C: O(n) and S.C: O(1)
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(head: Optional[ListNode]) -> Optional[ListNode]:
            reversed_head, curr = None, head
            while curr:
                tmp = curr.next
                curr.next = reversed_head
                reversed_head = curr
                curr = tmp
            return reversed_head
        
        # reverse the list and filter from the right
        curr = reversed_head = reverse(head)
        curr_max = curr.val
        while curr.next:
            if curr.next.val < curr_max:
                curr.next = curr.next.next
            else:
                curr_max = curr.next.val
                curr = curr.next

        # reverse again to return the correct order
        return reverse(reversed_head)
