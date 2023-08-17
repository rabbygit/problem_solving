from typing import List


class Solution:

    def gameOfLife(self, board: List[List[int]]) -> None:

        for i in range(len(board)):
            for j in range(len(board[0])):
                # live neighbors count
                live = self.totalAliveNeighbors(board, i, j)

                # rule 1 or rule 3
                if board[i][j] == 1 and (live < 2 or live > 3):
                    board[i][j] = -1
                # rule 4
                if board[i][j] == 0 and live == 3:
                    board[i][j] = 2

        for i in range(len(board)):
            for j in range(len(board[0])):
                board[i][j] = 1 if (board[i][j] > 0) else 0

        return board

    def totalAliveNeighbors(self, board, i, j) -> int:
        total = 0
        directions = [(1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1),
                      (0, 1), (1, 1)]

        # check and count neighbors in all directions
        for x, y in directions:
            if (i + x < len(board)
                    and i + x >= 0) and (j + y < len(board[0])
                                         and j + y >= 0) and abs(
                                             board[i + x][j + y]) == 1:
                total += 1

        return total
