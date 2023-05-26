from collections import Counter
import heapq
from typing import List


class Solution:

    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        minHeap = []
        result = []
        for idx, n in enumerate(nums):
            heapq.heappush(minHeap, (n, idx))
            if len(minHeap) > k:
                heapq.heappop(minHeap)

        minHeap.sort(key=lambda k: k[1])
        for n in minHeap:
            result.append(n[0])

        return result

    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        sortedNums = nums.copy()
        sortedNums.sort()
        numsCounter = Counter(sortedNums[-k:])
        result = []

        for n in nums:
            if numsCounter[n] > 0:
                result.append(n)
                numsCounter[n] -= 1

        return result
