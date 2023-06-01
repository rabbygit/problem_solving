class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        curry = 0
        result = ListNode()
        tail = result

        while l1 and l2:
            sum = l1.val + l2.val + curry

            if sum >= 10:
                curry = 1
                sum = sum % 10
            else:
                curry = 0

            # create node and add at end
            tail.next = ListNode(sum)
            tail = tail.next

            # move forward
            l1 = l1.next
            l2 = l2.next

        # if l1 still has element
        while l1:
            sum = l1.val + curry

            if sum >= 10:
                curry = 1
                sum = sum % 10
            else:
                curry = 0

            # create node and add at end
            tail.next = ListNode(sum)
            tail = tail.next

            # move forward
            l1 = l1.next

        # if l2 still has element
        while l2:
            sum = l2.val + curry

            if sum >= 10:
                curry = 1
                sum = sum % 10
            else:
                curry = 0

            # create node and add at end
            tail.next = ListNode(sum)
            tail = tail.next

            # move forward
            l2 = l2.next

        # if curry has 1
        if curry:
            tail.next = ListNode(curry)
            curry = 0

        return result.next