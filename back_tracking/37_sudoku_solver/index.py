from pickletools import TAKEN_FROM_ARGUMENT4U


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        for row in range(9):
            for column in range(9):
                if board[row][column] == '.':
                    for n in range(1,10):
                        n = str(n)
                        if self.canPlace(board,row,column,n):
                            board[row][column] = n
                            
                            if(self.solveSudoku(board)):
                                return True
                            else:
                                board[row][column] = '.'
                        
                    return False

        return True

    def canPlace(self,board,row,column,n):
        for i in range(9):
            if board[row][i] == n:
                return False
        
        for i in range(9):
            if board[i][column] == n:
                return False 

        x = int(row / 3) * 3
        y = int(column / 3 ) * 3

        for i in range(3):
            for j in range(3):
                if board[x+i][y+j] == n:
                    return False

        return True 