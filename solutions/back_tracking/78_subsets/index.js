/**
 * @author Rabby Hossain
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
  const result = []
  const n = nums.length

  function backtrack(subresult, i) {
    for (let index = i; index < n; index++) {
      const element = nums[index]
      subresult.push(element)
      backtrack(subresult, index + 1)
    }
  }
};