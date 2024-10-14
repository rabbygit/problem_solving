import math
import heapq
from typing import List


class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        score = 0
        maxheap = [n * -1 for n in nums]
        heapq.heapify(maxheap)

        for _ in range(k):
            s = -1 * heapq.heappop(maxheap)
            score += s
            heapq.heappush(maxheap, -1 * math.ceil(s / 3))

        return score
