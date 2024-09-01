/**
 * @param {number[]} original
 * @param {number} m
 * @param {number} n
 * @return {number[][]}
 */
const construct2DArray = function (original, m, n) {
  let idx = 0;
  const result = [];

  if (m * n != original.length) return result;

  for (let i = 0; i < m; i++) {
    result[i] = new Array(n);
  }

  for (let i = 0; i < m; i++) {
    for (let j = 0; j < n; j++) {
      result[i][j] = original[idx];
      idx++;
    }
  }

  return result;
};
