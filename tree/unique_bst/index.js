/**
 * [Problem ref]{@link  https://leetcode.com/problems/unique-binary-search-trees/}
 * @description Given an integer n, return the number of structurally unique BST's (binary search trees) 
 * which has exactly n nodes of unique values from 1 to n.
 */

/**
 * @param {number} n
 * @return {number}
 */
const numTrees = function (n) {
  if (n <= 0) return 0;
  const result = [1, 1];

  /**
   * using catalan number formula
   * C0 = 1 , C(n+1) = SUM(Ci * Cn-i)
   */
  for (let root = 2; root <= n; root++) {
    let count = 0;
    for (let index = 0; index < root; index++) {
      count += result[index] * result[root - index - 1]
    }
    result[root] = count;
  }

  return result[n]
}