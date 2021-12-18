/**
 * @author Rabby Hossain
 * [Problem ref]{@link https://leetcode.com/problems/n-queens/}
 * @description The n-queens puzzle is the problem of placing n queens on 
 * an n x n chessboard such that no two queens attack each other.
 * Given an integer n, return all distinct solutions to the n-queens puzzle.
 * You may return the answer in any order.
 */

/**
 * @param {number} n
 * @return {string[][]}
 */
const solveNQueens = function (n) {
  const result = [];
  const row_track = {}; // to track if queen is already placed in a specific row
  const column_track = {}; // to track if queen is already placed in a specific column
  const diagonal_track1 = {}; // to track if queen is already placed in lower to upper right diagonal
  const diagonal_track2 = {}; // to track if queen is already placed in upper to lower right diagonal

  function back_track(column, board) {
    if (column === n) {
      const sub_result = [];
      // construct one dimensional array
      for (let index = 0; index < board.length; index++) {
        const element = board[index];
        sub_result.push(element.join(''));
      }
      // push sub_result to result
      result.push(sub_result);
      return;
    }

    // traverse row wise
    for (let row = 0; row < n; row++) {
      // determine if queen can be placed at this position
      if (canPlace(row, column, row_track, column_track, diagonal_track1, diagonal_track2)) {
        // place the queen
        board[row][column] = 'Q';

        // keep track since queen can not be placed in same row/column/diagonal
        row_track[row] = 'Q';
        column_track[column] = 'Q';
        diagonal_track1[row + column] = 'Q';
        diagonal_track2[row - column] = 'Q';

        // recurse for every column of the row
        back_track(column + 1, board);

        // back to previous state as queen can not be placed
        board[row][column] = '.';
        row_track[row] = '.';
        column_track[column] = '.';
        diagonal_track1[row + column] = '.';
        diagonal_track2[row - column] = '.';
      }
    }
  }

  // create n x n board
  const board = [];
  for (let index = 0; index < n; index++) {
    board.push(new Array(n).fill('.'));
  }

  back_track(0, board);

  // return result
  return result;
};

/**
 * 
 * @description Determine if queen can be placed or not
 * @param {*} row
 * @param {*} column
 * @param {*} row_track
 * @param {*} column_track
 * @param {*} diagonal_track
 * @returns {Boolean}
 */
const canPlace = function (row, column, row_track, column_track, diagonal_track1, diagonal_track2) {
  if (row_track[row] === 'Q'
    || column_track[column] === 'Q'
    || diagonal_track1[row + column] === 'Q'
    || diagonal_track2[row - column] === 'Q') {
    return false;
  }

  return true;
};