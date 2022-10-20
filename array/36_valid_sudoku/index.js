/**
 * [Problem ref]{@link https://leetcode.com/problems/valid-sudoku/}
 * @description Determine if a 9 x 9 Sudoku board is valid
 * A sudoku solution must satisfy all of the following rules:
 *  Each of the digits 1-9 must occur exactly once in each row.
 *  Each of the digits 1-9 must occur exactly once in each column.
 *  Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
 * The '.' character indicates empty cells.
 */


/**
 * @param {character[][]} board
 * @return {boolean}
 */
const isValidSudoku = function (board) {
    const row_map = {}
    const column_map = {}
    const box_map = {}

    for (let index = 0; index < 9; index++) {
        row_map[index] = new Array(10)
        column_map[index] = new Array(10)
    }

    const check_row = (row, value) => {
        if (row_map[row][value]) return false

        // else
        row_map[row][value] = true
        return true
    }

    const check_column = (column, value) => {
        if (column_map[column][value]) return false

        // else
        column_map[column][value] = true
        return true
    }

    const check_box = (row, column, value) => {
        const x = parseInt(row / 3)
        const y = parseInt(column / 3)

        const key = `${x}${y}`
        if (box_map[key] === undefined) {
            box_map[key] = new Array(10)
        }

        if (box_map[key][value]) return false

        // else
        box_map[key][value] = true
        return true
    }

    for (let row = 0; row < 9; row++) {
        for (let column = 0; column < 9; column++) {
            let value = board[row][column]
            if (value !== '.') {
                value = parseInt(value)
                if (!check_row(row, value) ||
                    !check_column(column, value) ||
                    !check_box(row, column, value)) {
                        return false
                }
            }

        }
    }

    return true
};

