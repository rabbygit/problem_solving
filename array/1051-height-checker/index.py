from typing import List


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        excepted = heights.copy()
        excepted.sort()
        res = 0

        for i in range(len(heights)):
            if heights[i] != excepted[i]:
                res += 1

        return res