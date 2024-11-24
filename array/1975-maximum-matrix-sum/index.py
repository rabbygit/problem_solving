from typing import List


class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        res = 0
        negativeCount = 0
        minValue = float("inf")

        for i in range(n):
            for j in range(n):
                val = matrix[i][j]
                res += abs(val)
                minValue = min(minValue, abs(val))
                if val < 0:
                    negativeCount += 1

        if negativeCount % 2 == 1:
            res -= 2 * minValue

        return res
