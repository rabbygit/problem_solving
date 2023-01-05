class Solution:

    def solveNQueens(self, n):
        board = [['.' for x in range(n)] for x in range(n)]
        result = []
        # for tracking valid queen position
        column = set()
        # (r+c) is constant for lower-left to top-right positions
        positiveDiagonal = set()
        # (r-c) is constant for upper-left to lower-right positions
        negativeDiagonal = set()

        def back_track(r):
            if r == n:
                sub_result = []
                for row in range(n):
                    sub_result.append(''.join(board[row]))

                result.append(sub_result)
                return

            for c in range(n):
                if c in column or (r + c) in positiveDiagonal or (
                        r - c) in negativeDiagonal:
                    continue

                column.add(c)
                positiveDiagonal.add(r + c)
                negativeDiagonal.add(r - c)
                board[r][c] = 'Q'

                back_track(r + 1)

                column.remove(c)
                positiveDiagonal.remove(r + c)
                negativeDiagonal.remove(r - c)
                board[r][c] = '.'

        back_track(0)

        return result