/**
 * @param {number[][]} land
 * @return {number[][]}
 */
// T.C: O(m * n) and S.C: O(k)
const findFarmland = function (land) {
  const ROWS = land.length;
  const COLS = land[0].length;
  const result = [];
  let bottomRight = [];

  function dfs(r, c) {
    if (r >= ROWS || r < 0 || c >= COLS || c < 0 || land[r][c] == 0) {
      return;
    }

    bottomRight[0] = Math.max(bottomRight[0], r);
    bottomRight[1] = Math.max(bottomRight[1], c);

    land[r][c] = 0;

    dfs(r + 1, c);
    dfs(r - 1, c);
    dfs(r, c + 1);
    dfs(r, c - 1);
  }

  for (let i = 0; i < ROWS; i++) {
    for (let j = 0; j < COLS; j++) {
      if (land[i][j] == 1) {
        bottomRight = [i, j];
        dfs(i, j);
        result.push([i, j, ...bottomRight]);
      }
    }
  }

  return result;
};
