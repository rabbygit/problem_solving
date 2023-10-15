/**
 * [Problem ref]{@link https://leetcode.com/problems/subsets/}
 * @description Given an integer array nums of unique elements,
 * return all possible subsets (the power set).
 * The solution set must not contain duplicate subsets.
 * Return the solution in any order.
 */

/**
 * @param {number[]} nums
 * @return {number[][]}
 */
const subsets = function (nums) {
  const result = [];

  function backtrack(subresult, i) {
    // push possible subset
    result.push([...subresult]);

    for (let index = i; index < nums.length; index++) {
      subresult.push(nums[index]);
      backtrack(subresult, index + 1);
      subresult.pop();
    }
  }

  backtrack([], 0);

  return result;
};
