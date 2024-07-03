import heapq
from typing import List


class Solution:
    # T.C and S.C: O(n)
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0

        minDiff = float("inf")
        minFour = sorted(heapq.nsmallest(4, nums))
        maxFour = sorted(heapq.nlargest(4, nums))

        for i in range(4):
            minDiff = min(minDiff, maxFour[i] - minFour[i])

        return minDiff
