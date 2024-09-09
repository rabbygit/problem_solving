# Definition for singly-linked list.
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # T.C: O(m*n) and S.C: O(1)
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        matrix = [[-1 for _ in range(n)] for _ in range(m)]
        top = left = 0
        bottom, right = m - 1, n - 1
        curr = head

        while curr:
            # from top left to right
            for i in range(left, right + 1):
                if not curr:
                    break
                matrix[top][i] = curr.val
                curr = curr.next
            top += 1

            # from top right to bottom
            for i in range(top, bottom + 1):
                if not curr:
                    break
                matrix[i][right] = curr.val
                curr = curr.next
            right -= 1

            # from bottom right to left
            for i in range(right, left - 1, -1):
                if not curr:
                    break
                matrix[bottom][i] = curr.val
                curr = curr.next
            bottom -= 1

            # from bottom left to top
            for i in range(bottom, top - 1, -1):
                if not curr:
                    break
                matrix[i][left] = curr.val
                curr = curr.next
            left += 1

        return matrix
