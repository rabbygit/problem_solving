import math
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1 , max(piles)
        k = right

        while left <= right:
            mid = (left + right) // 2

            total_hours = 0
            for p in piles:
                total_hours += math.ceil(p / mid)

            if total_hours <= h:
                k = min(k , mid)
                right = mid - 1
            else:
                left = mid + 1

        
        return k