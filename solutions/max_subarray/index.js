/**
 * Problem Ref: 53. https://leetcode.com/problems/maximum-subarray/
 */

/**
 * @param {number[]} nums
 * @return {number}
 */
const maxSubArray = function(nums) {
  const length = nums.length;
  if (length === 1) return nums[0];

  let sum = 0;
  let min = 0;
  let max = nums[0];

  for (let index = 0; index < length; index++) {
      sum += nums[index];
      if (sum - min > max) max = sum - min;
      if (sum < min)  min = sum;
  }

  return max;
};