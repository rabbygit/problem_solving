class Solution:

    def exist(self, board: List[List[str]], word: str) -> bool:
        wordLength = len(word)
        row = len(board)
        col = len(board[0])

        def backtrack(r, c, i):
            if i == wordLength:
                return True
            # if r/c is out of bound, or letter doesn't match or
            # we already visited the index then return False
            if (r < 0 or c < 0 or r >= row or c >= col
                    or board[r][c] != word[i] or board[r][c] == '#'):
                return False

            # remember which path we are visiting
            tempChar = board[r][c]
            board[r][c] = '#'

            # recursive call to 4 possible direction to find the word
            found = (backtrack(r + 1, c, i + 1) or backtrack(r - 1, c, i + 1)
                     or backtrack(r, c + 1, i + 1)
                     or backtrack(r, c - 1, i + 1))

            # remove the path from visiting path
            board[r][c] = tempChar

            return found

        # call from every position of the board to find the word
        for r in range(row):
            for c in range(col):
                if board[r][c] == word[0]:
                    if backtrack(r, c, 0):
                        return True

        return False
