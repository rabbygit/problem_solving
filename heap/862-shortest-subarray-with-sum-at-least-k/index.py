import heapq
from typing import List


class Solution:
    # T.C: O(n logn) and S.C: O(n)
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        res = float("inf")
        currSum = 0
        minHeap = []

        for r in range(len(nums)):
            currSum += nums[r]

            if currSum >= k:
                res = min(res, r + 1)

            while minHeap and currSum - minHeap[0][0] >= k:
                _, l = heapq.heappop(minHeap)
                res = min(res, r - l)

            heapq.heappush(minHeap, (currSum, r))

        return -1 if res == float("inf") else res
