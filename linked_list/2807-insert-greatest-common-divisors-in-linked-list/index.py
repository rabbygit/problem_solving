# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # T.C: O(n * log M) where M is the maximum value of the node values in the linked list.
    # S.C: O(1)
    def insertGreatestCommonDivisors(
        self, head: Optional[ListNode]
    ) -> Optional[ListNode]:
        curr = head

        while curr and curr.next:
            tmp = curr.next
            gcdValue = self.findGcd(curr.val, curr.next.val)
            curr.next = ListNode(gcdValue, curr.next)
            curr = tmp

        return head

    # O(log(min(a,b)))
    def findGcd(self, a: int, b: int) -> int:
        if b > a:
            return self.findGcd(b, a)

        while b:
            r = a % b
            a = b
            b = r

        return a
