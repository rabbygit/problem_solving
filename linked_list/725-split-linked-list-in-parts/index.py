# Definition for singly-linked list.
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def splitListToParts(
        self, head: Optional[ListNode], k: int
    ) -> List[Optional[ListNode]]:
        result = []
        length = self.findLinkedListLength(head)
        avgPartLength, extraNodes = length // k, length % k

        curr = head
        while curr:
            currPartLength = avgPartLength
            partHead = ListNode(0, curr)

            # as long as we have extraNodes, we will add 1 extra node to each part
            # because no two parts should have a size difference by more than one
            if extraNodes:
                currPartLength += 1
                extraNodes -= 1

            # we already considered the current node as a part of the current split
            # so, decrease 1 from the required node count
            currPartLength -= 1
            # go to the last node of the current split
            while currPartLength:
                curr = curr.next
                currPartLength -= 1

            # disconnect the last node of the current part 
            # from the remaining part of the list
            if curr:
                tmp = curr.next
                curr.next = None
                curr = tmp

            k -= 1
            result.append(partHead.next)

        # we don't have any node, 
        # so, fill the remaining spots with null
        while k:
            result.append(None)
            k -= 1

        return result

    def findLinkedListLength(self, head: Optional[ListNode]) -> int:
        curr = head
        length = 0
        while curr:
            curr = curr.next
            length += 1

        return length
