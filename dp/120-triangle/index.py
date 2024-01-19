from typing import List


class Solution:

    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for r in range(len(triangle) - 2, -1, -1):
            cols = len(triangle[r])
            for c in range(cols):
                triangle[r][c] += min(triangle[r + 1][c],
                                      triangle[r + 1][c + 1])

        return triangle[0][0]