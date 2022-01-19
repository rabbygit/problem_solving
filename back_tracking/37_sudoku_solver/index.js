/**
 * @author Rabby Hossain
 * [Problem ref]{@link https://leetcode.com/problems/sudoku-solver/}
 * @description Write a program to solve a Sudoku puzzle by filling the empty cells.
 * A sudoku solution must satisfy all of the following rules:
 *  Each of the digits 1-9 must occur exactly once in each row.
 *  Each of the digits 1-9 must occur exactly once in each column.
 *  Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
 * The '.' character indicates empty cells.
 */


/**
 * @param {character[][]} board
 * @return {void} Do not return anything, modify board in-place instead.
 */
const solveSudoku = function (board) {
    // Go to every index and find the empty place
    for (let row = 0; row < 9; row++) {
        for (let column = 0; column < 9; column++) {
            if (board[row][column] === '.') {
                // try every number(1-9) to place in this position
                for (let n = 1; n < 10; n++) {
                    n = String(n) // convert to string
                    if (canPlace(board, row, column, n)) {
                        board[row][column] = n
                        if (solveSudoku(board)) return true; // backtrack call
                        else board[row][column] = '.'
                    }
                }

                return false
            }
        }
    }

    return true
};

/**
 * @description Determines if n can be placed
 * @param {*} row 
 * @param {*} column 
 * @param {*} n 
 * @returns boolean
 */
function canPlace(board, row, column, n) {
    // check whether n is already placed in the same row or not
    for (let i = 0; i < 9; i++) {
        if (board[row][i] === n) {
            return false
        }
    }

    // check whether n is already placed in the same column or not
    for (let i = 0; i < 9; i++) {
        if (board[i][column] === n) {
            return false
        }
    }

    // check whether n is already placed in the same 3x3 square or not
    let x = parseInt(row / 3) * 3;
    let y = parseInt(column / 3) * 3;

    for (let i = 0; i < 3; i++) {
        for (let j = 0; j < 3; j++) {
            if (board[x + i][y + j] === n) return false;
        }
    }

    return true;
}