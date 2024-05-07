from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # T.C: O(n) and S.C: O(1)
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = curr = reversed_head = self.reverse(head)
        carry = 0

        while curr:
            d = curr.val * 2 + carry
            curr.val = d % 10
            carry = d // 10
            prev = curr
            curr = curr.next

        if carry:
            prev.next = ListNode(carry)

        return self.reverse(reversed_head)

    def reverse(self, head: Optional[ListNode]) -> Optional[ListNode]:
        reversed_head, curr = None, head
        while curr:
            tmp = curr.next
            curr.next = reversed_head
            reversed_head = curr
            curr = tmp
        return reversed_head
