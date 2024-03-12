# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prefixSum, sumMap = 0, {}
        dummy = ListNode()
        dummy.next = head
        sumMap[prefixSum] = dummy

        while head:
            prefixSum += head.val

            if prefixSum in sumMap:
                curr = prefixSum
                node = sumMap[prefixSum].next
                while node != head:
                    curr += node.val
                    del sumMap[curr]
                    node = node.next
                sumMap[prefixSum].next = node.next
            else:
                sumMap[prefixSum] = head

            head = head.next

        return dummy.next
