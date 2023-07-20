/**
 * [Problem ref]{@link https://leetcode.com/problems/combination-sum/}
 * @description Given an array of distinct integers candidates and a target integer target,
 * return a list of all unique combinations of candidates where the chosen numbers sum to target.
 *  You may return the combinations in any order.
 */

/**
 * @param {number[]} candidates
 * @param {number} target
 * @return {number[][]}
 */
const combinationSum = function (candidates, target) {
  const result = [];

  function dfs(sub_result, sum, i) {
    if (sum === target) {
      result.push([...sub_result]);
      return;
    }

    if (sum > target) return;

    for (let idx = i; idx < candidates.length; idx++) {
      const num = candidates[idx];
      sub_result.push(num);
      dfs(sub_result, sum + num, i);
      sub_result.pop();
    }
  }

  dfs([], 0, 0);

  return result;
};
