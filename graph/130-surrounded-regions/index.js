/**
 * @param {character[][]} board
 * @return {void} Do not return anything, modify board in-place instead.
 */
const solve = function (board) {
    const rows = board.length
    const cols = board[0].length

    function dfs(r, c) {
        if (r < 0 || c < 0 || r === rows || c === cols || board[r][c] !== 'O') {
            return
        }

        board[r][c] = "T"

        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)
    }

    // turn "O" to "T" if it is in border and adjacent to border's "O"
    for (let r = 0; r < rows; r++) {
        for (let c = 0; c < cols; c++) {
            if (board[r][c] === "O" && ([0, rows - 1].includes(r) || [0, cols - 1].includes(c))) {
                dfs(r, c)
            }
        }
    }

    // turn rest of the "O" to "X"
    for (let r = 0; r < rows; r++) {
        for (let c = 0; c < cols; c++) {
            if (board[r][c] === 'O') {
                board[r][c] = 'X'
            }
        }
    }

    // turn "T" to "O"
    for (let r = 0; r < rows; r++) {
        for (let c = 0; c < cols; c++) {
            if (board[r][c] === 'T') {
                board[r][c] = 'O'
            }
        }
    }
};