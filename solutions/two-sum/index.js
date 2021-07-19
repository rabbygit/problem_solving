/**
 * Problem ref: https://leetcode.com/problems/two-sum/
 */

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
 const twoSum = function(nums, target) {
  let result = [];
  let obj = {};

  for (let index = 0; index < nums.length; index++) {
    const value = target - nums[index];

    if (obj.hasOwnProperty(value)) {
      result = [obj[value],index];
      break;
    } else {
      obj[nums[index]] = index;
    }

  }

  return result;
};