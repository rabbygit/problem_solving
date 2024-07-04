from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # Time complexity: O(n)
    # Space complexity: O(n)
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        currSum = 0
        currNode = head.next
        tail = dummyHead = ListNode()

        while currNode:
            if currNode.val == 0:
                tail.next = ListNode(currSum)
                tail = tail.next
                currSum = 0

            currSum += currNode.val
            currNode = currNode.next

        return dummyHead.next


class Solution1:
    # Time complexity: O(n)
    # Space complexity: O(1)
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sumNode = currNode = head.next
        currSum = 0

        while currNode:
            if currNode.val == 0:
                sumNode.val = currSum
                sumNode.next = currNode.next
                sumNode = sumNode.next
                currSum = 0

            currSum += currNode.val
            currNode = currNode.next

        return head.next
