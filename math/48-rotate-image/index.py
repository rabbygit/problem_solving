class Solution:

    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        left, right = 0, len(matrix) - 1

        while left < right:

            for index in range(right - left):
                top, bottom = left, right

                # save top left value
                topLeft = matrix[top][left + index]

                # move bottom left to top left
                matrix[top][left + index] = matrix[bottom - index][left]

                # move bottom right to bottom left
                matrix[bottom - index][left] = matrix[bottom][right - index]

                # move top right to bottom right
                matrix[bottom][right - index] = matrix[top + index][right]

                # move top right to bottom right
                matrix[top + index][right] = topLeft

            left += 1
            right -= 1