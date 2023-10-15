/**
 * [Problem ref]{@link https://leetcode.com/problems/combination-sum-ii/}
 * @description Given a collection of candidate numbers (candidates) and a target number (target),
 * find all unique combinations in candidates where the candidate numbers sum to target.
 * Each number in candidates may only be used once in the combination.
 * Note: The solution set must not contain duplicate combinations.
 */

/**
 * @param {number[]} candidates
 * @param {number} target
 * @return {number[][]}
 */
const combinationSum2 = function (candidates, target) {
  const result = [];
  const n = candidates.length;
  candidates.sort();

  function backtrack(sub_result, sum, i) {
    if (sum > target) return;

    if (sum === target) {
      result.push([...sub_result]);
      return;
    }

    for (let idx = i; idx < n; idx++) {
      const num = candidates[idx];
      sub_result.push(num);
      backtrack(sub_result, sum + num, idx + 1);
      sub_result.pop();

      // avoid duplicates
      while (idx + 1 < n && num === candidates[idx + 1]) {
        idx++;
      }
    }
  }

  backtrack([], 0, 0);
  return result;
};
