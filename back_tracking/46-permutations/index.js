/**
 * [Problem ref]{@link https://leetcode.com/problems/permutations/}
 * @description Given an array nums of distinct integers,
 * return all the possible permutations. You can return the answer in any order.
 */

/**
 * @param {number[]} nums
 * @return {number[][]}
 */
const permute = function (nums) {
  const result = [];
  const taken = {};
  const n = nums.length;

  function genratePermute(sub_result) {
    if (sub_result.length === n) {
      result.push([...sub_result]);
      return;
    }

    for (let index = 0; index < n; index++) {
      const element = nums[index];
      if (!taken[element]) {
        taken[element] = true;
        sub_result.push(element);
        genratePermute(sub_result);
        sub_result.pop();
        taken[element] = false;
      }
    }
  }

  genratePermute([]);

  return result;
};