from typing import List


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows, cols = len(matrix), len(matrix[0])
        self.prefixMatrix = [[0] * (cols + 1) for r in range(rows + 1)]

        for r in range(rows):
            currSum = 0
            for c in range(cols):
                currSum += matrix[r][c]
                topRight = self.prefixMatrix[r][c + 1]
                self.prefixMatrix[r + 1][c + 1] += currSum + topRight

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1, col1, row2, col2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1

        bottomRight = self.prefixMatrix[row2][col2]
        topRight = self.prefixMatrix[row1 - 1][col2]
        bottomLeft = self.prefixMatrix[row2][col1 - 1]
        topLeft = self.prefixMatrix[row1 - 1][col1 - 1]

        return bottomRight - topRight - bottomLeft + topLeft
