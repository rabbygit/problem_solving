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
  const total_possibility = 2 ** n

  function backtrack(subresult, i) {
    // all possible subsets found
    if (result.length === total_possibility) {
      return
    }

    // push possible subset
    result.push([...subresult])

    for (let index = i; index < n; index++) {
      subresult.push(nums[index])
      backtrack(subresult, index + 1)
      subresult.pop()
    }
  }

  backtrack([], 0)

  return result
};