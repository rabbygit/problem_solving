/**
 * @param {character[][]} board
 * @param {string} word
 * @return {boolean}
 */
const exist = function (board, word) {
  const rows = board.length - 1;
  const cols = board[0].length - 1;

  function isInvalidPath(r, c, i) {
    return (
      r < 0 ||
      r > rows ||
      c < 0 ||
      c > cols ||
      board[r][c] !== word[i] ||
      board[r][c] === "#"
    );
  }

  function dfs(r, c, i) {
    if (i === word.length) return true;
    if (isInvalidPath(r, c, i)) return false;

    const tmp = board[r][c];
    board[r][c] = "#";
    const found =
      dfs(r + 1, c, i + 1) ||
      dfs(r - 1, c, i + 1) ||
      dfs(r, c + 1, i + 1) ||
      dfs(r, c - 1, i + 1);

    board[r][c] = tmp;
    return found;
  }

  for (let r = 0; r <= rows; r++) {
    for (let c = 0; c <= cols; c++) {
      if (board[r][c] !== word[0]) continue;
      if (dfs(r, c, 0)) return true;
    }
  }

  return false;
};
