from typing import List


class Solution:

    def countBattleships(self, board: List[List[str]]) -> int:
        r, c = len(board), len(board[0])
        result = 0

        for i in range(r):
            for j in range(c):
                if board[i][j] == 'X' and self.isNewBattleship(board, i, j):
                    result += 1

        return result

    def isNewBattleship(self, board: List[List[str]], r: int, c: int) -> bool:
        return ((r == 0 or board[r - 1][c] == '.')
                and (c == 0 or board[r][c - 1] == '.'))
