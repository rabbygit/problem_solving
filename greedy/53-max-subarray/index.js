/**
 * Problem Ref: 53. https://leetcode.com/problems/maximum-subarray/
 */

/**
 * @param {number[]} nums
 * @return {number}
 */
const maxSubArray = function (nums) {
  let maxSum = nums[0];
  let currentSum = maxSum;

  for (let i = 1; i < nums.length; i++) {
    if (currentSum < 0) currentSum = 0;
    currentSum += nums[i];
    maxSum = Math.max(maxSum, currentSum);
  }

  return maxSum;
};
