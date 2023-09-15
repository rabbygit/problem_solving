from typing import List


class Solution:

    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows, col = len(matrix), len(matrix[0])
        cache = {}

        def countSquare(r, c):
            if r >= rows or c >= col:
                return 0

            if not (r, c) in cache:
                down = countSquare(r + 1, c)
                right = countSquare(r, c + 1)
                dia = countSquare(r + 1, c + 1)

                cache[(r, c)] = 0
                if matrix[r][c] == '1':
                    cache[(r, c)] = 1 + min(down, right, dia)

            return cache[(r, c)]

        countSquare(0, 0)

        return max(cache.values())**2

    def maximalSquareDp(self, matrix: List[List[str]]) -> int:
        rows, col = len(matrix), len(matrix[0])
        maxSquareLen = 0

        def getIntValue(r, c):
            if r >= rows or c >= col:
                return 0

            return int(matrix[r][c])

        for i in range(rows - 1, -1, -1):
            for j in range(col - 1, -1, -1):
                if matrix[i][j] == '1':
                    down = getIntValue(i + 1, j)
                    right = getIntValue(i, j + 1)
                    dia = getIntValue(i + 1, j + 1)

                    matrix[i][j] = 1 + min(down, right, dia)
                    maxSquareLen = max(maxSquareLen, matrix[i][j])

        return maxSquareLen * maxSquareLen
