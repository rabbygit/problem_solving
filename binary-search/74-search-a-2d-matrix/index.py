from typing import List


class Solution:

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix[0]) - 1
        foundRow = None

        for row in range(len(matrix)):
            if target <= matrix[row][n]:
                foundRow = row
                break

        if foundRow == None:
            return False

        return self.search(matrix, target, foundRow)

    # iterative approach
    def search(self, matrix: List[List[int]], target: int,
               foundRow: int) -> int:
        start = 0
        end = len(matrix[0]) - 1

        while end >= start:
            mid = (end + start) // 2

            if matrix[foundRow][mid] == target:
                return True
            elif target > matrix[foundRow][mid]:
                start = mid + 1
            else:
                end = mid - 1

        return False