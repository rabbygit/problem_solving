# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # T.C: O(n+m) and S.C: O(1)
    def mergeInBetween(
        self, list1: ListNode, a: int, b: int, list2: ListNode
    ) -> ListNode:
        curr = list1
        aNode = bNode = None

        # find the splitting points
        while curr:
            a -= 1
            b -= 1
            if a == 0:
                aNode = curr
            if b == 0:
                bNode = curr.next
            curr = curr.next

        # go to the last node of list2
        curr = list2
        while curr.next:
            curr = curr.next

        # insert list2 into list1
        aNode.next = list2
        curr.next = bNode.next

        return list1
