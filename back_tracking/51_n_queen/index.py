class Solution:
    def solveNQueens(self, n):
        self.result = []
        self.row_track = {}  # to track if queen is already placed in a specific row
        self.column_track = {}  # to track if queen is already placed in a specific column
        # to track if queen is already placed in lower to upper right diagonal
        self.diagonal_track1 = {}
        # to track if queen is already placed in upper to lower right diagonal
        self.diagonal_track2 = {}

        def back_track(column, board):
            if column == n:
                sub_result = []
                # construct one dimensional array
                for i in range(n):
                    sub_result.append(''.join(board[i]))

                # push sub_result to result
                self.result.append(sub_result)
                return

            # traverse row wise
            for row in range(n):
                # determine if queen can be placed at this position
                if self.canPlace(row, column, self.row_track, self.column_track, self.diagonal_track1, self.diagonal_track2):
                    # place the queen
                    board[row][column] = 'Q'

                    # keep track since queen can not be placed in same row/column/diagonal
                    self.row_track[row] = 'Q'
                    self.column_track[column] = 'Q'
                    self.diagonal_track1[row+column] = 'Q'
                    self.diagonal_track2[row-column] = 'Q'

                    # recurse for every column of the row
                    back_track(column+1, board)

                    # back to previous state as queen can not be placed
                    board[row][column] = '.'
                    self.row_track[row] = '.'
                    self.column_track[column] = '.'
                    self.diagonal_track1[row+column] = '.'
                    self.diagonal_track2[row-column] = '.'

        # create n x n board
        board = [['.' for x in range(n)] for x in range(n)]
        back_track(0, board)

        return self.result

    def canPlace(self, row, column, row_track, column_track, diagonal_track1, diagonal_track2):
        if ((row in row_track and row_track[row] == 'Q') or
                (column in column_track and column_track[column] == 'Q') or
                ((row + column) in diagonal_track1 and diagonal_track1[row + column] == 'Q') or
                ((row-column) in diagonal_track2 and diagonal_track2[row - column] == 'Q')):
            return False

        return True
