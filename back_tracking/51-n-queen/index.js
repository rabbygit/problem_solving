/**
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
  const board = [];
  const result = [];

  // create n x n board
  for (let i = 0; i < n; i++) board.push(new Array(n).fill("."));

  const column = new Set(); // to track if queen is already placed in a specific column
  const bottomToTop = new Set(); // to track if queen is already placed in lower left to upper right diagonal
  const topToBottom = new Set(); // to track if queen is already placed in upper left to lower right diagonal

  function back_track(r) {
    if (r === n) {
      // construct one dimensional array
      const c = [];
      for (let i = 0; i < n; i++) c.push(board[i].join(""));
      result.push(c);
      return;
    }

    for (let c = 0; c < n; c++) {
      // determine if queen can be placed at this position
      if (column.has(c) || bottomToTop.has(r + c) || topToBottom.has(r - c)) {
        continue;
      }

      board[r][c] = "Q";
      column.add(c);
      bottomToTop.add(r + c);
      topToBottom.add(r - c);

      back_track(r + 1);

      board[r][c] = ".";
      column.delete(c);
      bottomToTop.delete(r + c);
      topToBottom.delete(r - c);
    }
  }

  back_track(0);
  return result;
};
