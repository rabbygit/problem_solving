from typing import List


class Solution:
    # T.C: O(n) and S.C: O(1)
    def maxSatisfied(
        self, customers: List[int], grumpy: List[int], minutes: int
    ) -> int:
        tmpSum = maxSum = res = l = 0
        length = len(customers)

        for i in range(length):
            if grumpy[i] == 0:
                res += customers[i]

        for r in range(length):
            if grumpy[r]:
                tmpSum += customers[r]

            if r - l + 1 > minutes:
                if grumpy[l]:
                    tmpSum -= customers[l]
                l += 1

            maxSum = max(tmpSum, maxSum)

        return res + maxSum
