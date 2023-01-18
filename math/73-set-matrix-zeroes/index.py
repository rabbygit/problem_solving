class Solution:

    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows, cols = len(matrix), len(matrix[0])
        rowZero = False

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    # first row will track which column will be zero
                    matrix[0][c] = 0

                    # first column will track which row will be zero
                    # except for the first row,
                    # because it's overlapped with first column at position [0][0]
                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        rowZero = True

        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0

        # make first column 0
        if matrix[0][0] == 0:
            for r in range(rows):
                matrix[r][0] = 0

        # make first row 0
        if rowZero:
            for c in range(cols):
                matrix[0][c] = 0