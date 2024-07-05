# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        prev, curr, next = head, head.next, head.next.next
        first_critical = prev_critical = 0
        minDiff, maxDiff = float("inf"), -1
        idx = 1

        while next:
            if self.isCriticalPoint(prev, curr, next):
                if first_critical:
                    maxDiff = idx - first_critical
                    minDiff = min(minDiff, idx - prev_critical)
                else:
                    first_critical = idx
                prev_critical = idx

            prev, curr, next = curr, next, next.next
            idx += 1

        if maxDiff == -1:
            minDiff = -1

        return [minDiff, maxDiff]

    def isCriticalPoint(self, prev: ListNode, curr: ListNode, next: ListNode) -> bool:
        return prev.val < curr.val > next.val or prev.val > curr.val < next.val
