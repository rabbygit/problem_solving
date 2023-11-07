from typing import List


class Solution:

    def tictactoe(self, moves: List[List[int]]) -> str:
        board = [[' '] * 3 for _ in range(3)]
        possible_res = [
            [(0, 0), (0, 1), (0, 2)],
            [(1, 0), (1, 1), (1, 2)],
            [(2, 0), (2, 1), (2, 2)],
            [(0, 0), (1, 0), (2, 0)],
            [(0, 1), (1, 1), (2, 1)],
            [(0, 2), (1, 2), (2, 2)],
            [(0, 0), (1, 1), (2, 2)],
            [(0, 2), (1, 1), (2, 0)],
        ]
        
        for i in range(len(moves)):
            r, c = moves[i]
            if i % 2 == 0:
                board[r][c] = 'X'
            else:
                board[r][c] = 'O'

        for i in range(len(possible_res)):
            count = 1
            r1, c1 = possible_res[i][0]
            first_move = board[r1][c1]
            if first_move != ' ':
                for j in range(1, 3):
                    r, c = possible_res[i][j]
                    if board[r][c] == first_move:
                        count += 1
            
            if count == 3:
                return 'A' if first_move == 'X' else 'B'

        return 'Draw' if len(moves) == 9 else 'Pending'
