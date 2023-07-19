import collections
import heapq
from typing import List


class Solution:

    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        numMap = collections.Counter(arr)
        minHeap = [(numMap[num], num) for num in numMap]
        heapq.heapify(minHeap)

        while k:
            occ, num = minHeap[0]
            if occ >= k:
                occ = occ - k
                k = 0
            else:
                k = k - occ
                occ = 0

            heapq.heappop(minHeap)
            if occ > 0:
                heapq.heappush(minHeap, (occ, num))

        return len(minHeap)