class Solution:

    def reverseEvenLengthGroups(
            self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = head
        count = 2
        while prev.next:
            curr, n = prev, 0
            while n < count and curr.next:
                curr = curr.next
                n += 1

            if n % 2 == 0:  # even
                curr = prev.next
                prev.next, curr.next = self.reverse(curr, n)

            prev = curr
            count += 1

        return head

    def reverse(self, node, k):
        rev = None
        for _ in range(k):
            tmp = node.next
            node.next = rev
            rev = node
            node = tmp
        return rev, node