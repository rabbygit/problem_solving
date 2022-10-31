class Solution:

    def mergeTwoLists(self, l1: Optional[ListNode],
                      l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 is None:
            return l2

        if l2 is None:
            return l1

        if l2.val < l1.val:
            return self.mergeTwoLists(l2, l1)

        current1 = l1
        current2 = l2
        prev = l1  # track last point of sorted list

        while current1 and current2:
            if current2.val <= current1.val:
                # keep next node's address
                temp1 = prev.next
                temp2 = current2.next

                # prepend smaller value's node
                current2.next = temp1
                prev.next = current2

                # update next pointer
                prev = current2
                current1 = temp1
                current2 = temp2
            else:
                prev = current1
                current1 = current1.next

        # if anything left in second list
        if current2:
            prev.next = current2

        return l1

    def mergeTwoLists2(self, l1: Optional[ListNode],
                       l2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode()
        tail = dummy

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next

            tail = tail.next

        if l1:
            tail.next = l1
        elif l2:
            tail.next = l2

        return dummy.next

    def mergeTwoLists3(self, l1: Optional[ListNode],
                       l2: Optional[ListNode]) -> Optional[ListNode]:
        result = None
        reverse = None

        # if both lists have node
        while l1 and l2:
            val = 0
            if l1.val >= l2.val:
                val = l2.val
                l2 = l2.next
            else:
                val = l1.val
                l1 = l1.next

            result = ListNode(val, result)

        # if l1 list has remaining node
        while l1:
            result = ListNode(l1.val, result)
            l1 = l1.next

        # if l2 list has remaining node
        while l2:
            result = ListNode(l2.val, result)
            l2 = l2.next

        # reverse the list
        while result:
            temp = result.next
            result.next = reverse
            reverse = result
            result = temp

        return
