from typing import List


class Solution:
    # T.C and S.C: O(n)
    def minOperations(self, nums: List[int], k: int) -> int:
        minNum = float("inf")
        numSet = set()

        for n in nums:
            if n < k:
                return -1

            if n not in numSet:
                numSet.add(n)
                minNum = min(minNum, n)

        if k == minNum:
            return len(numSet) - 1

        return len(numSet)
