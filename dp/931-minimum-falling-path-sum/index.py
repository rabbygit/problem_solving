from typing import List


class Solution:

    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)

        def validValue(i, j):
            if 0 <= i < n and 0 <= j < n:
                return matrix[i][j]
            return float('inf')

        for i in range(n - 2, -1, -1):
            for j in range(n):
                below = validValue(i + 1, j)
                left_di = validValue(i + 1, j - 1)
                right_di = validValue(i + 1, j + 1)
                matrix[i][j] += min(below, left_di, right_di)

        return min(matrix[0])