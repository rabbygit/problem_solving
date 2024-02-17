import heapq
from typing import List


class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        maxHeap = []

        for i in range(len(heights) - 1):
            diff = heights[i + 1] - heights[i]
            if diff <= 0:
                continue

            bricks -= diff
            heapq.heappush(maxHeap, -diff)

            if bricks < 0:
                if ladders == 0:
                    return i

                ladders -= 1
                bricks += -1 * heapq.heappop(maxHeap)

        return len(heights) - 1
