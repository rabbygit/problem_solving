from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # T.C: O(n+m) and S.C: O(n)
    def modifiedList(
        self, nums: List[int], head: Optional[ListNode]
    ) -> Optional[ListNode]:
        numsMap = set(nums)
        prev = dummyHead = ListNode(0, head)
        curr = head

        while curr:
            if curr.val in numsMap:
                # skipping(deleting) the current node
                prev.next = curr.next
            else:
                prev = curr

            curr = curr.next

        return dummyHead.next
