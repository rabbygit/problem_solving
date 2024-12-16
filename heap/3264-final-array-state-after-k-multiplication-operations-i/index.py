import heapq
from typing import List


class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        minHeap = [[nums[i], i] for i in range(len(nums))]
        heapq.heapify(minHeap)

        while k:
            val, idx = heapq.heappop(minHeap)
            val *= multiplier
            heapq.heappush(minHeap, [val, idx])
            nums[idx] = val
            k -= 1

        return nums
