class Solution:

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        m = len(matrix)
        if m == 0:
            return result
        n = len(matrix[0])

        left = 0
        top = 0
        right = n - 1
        bottom = m - 1
        direction = 0

        while left <= right and top <= bottom:

            if direction == 0:
                # move left to right
                for index in range(left, right + 1):
                    result.append(matrix[top][index])
                top += 1
            elif direction == 1:
                # move top to bottom
                for index in range(top, bottom + 1):
                    result.append(matrix[index][right])
                right -= 1
            elif direction == 2:
                # move right to left
                for index in range(right, left - 1, -1):
                    result.append(matrix[bottom][index])
                bottom -= 1
            else:
                # move bottom to top
                for index in range(bottom, top - 1, -1):
                    result.append(matrix[index][left])
                left += 1

            direction = (direction + 1) % 4

        return result