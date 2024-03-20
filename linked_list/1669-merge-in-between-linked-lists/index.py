# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(
        self, list1: ListNode, a: int, b: int, list2: ListNode
    ) -> ListNode:
        curr = list1
        aNode = bNode = None

        while curr:
            a -= 1
            b -= 1
            if a == 0:
                aNode = curr
            if b == 0:
                bNode = curr.next
            curr = curr.next

        aNode.next = list2
        while list2.next:
            list2 = list2.next
        list2.next = bNode.next
        
        return list1
