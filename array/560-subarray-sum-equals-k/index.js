/**
 * [Problem ref]{@link  https://leetcode.com/problems/subarray-sum-equals-k/}
 * @description Given an array of integers nums and an integer k,
 * return the total number of subarrays whose sum equals to k.
 * A subarray is a contiguous non-empty sequence of elements within an array.
 */

/**
 * @description this solution works only for non-negative
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
const subarraySumNonNegative = function (nums, k) {
  let current_sum = 0;
  let start_idx = 0;
  let result = 0;

  for (let index = 0; index < nums.length; index++) {
    current_sum += nums[index];

    while (current_sum > k && start_idx < index) {
      current_sum -= nums[start_idx++];
    }

    if (current_sum === k) {
      result++;
    }
  }

  return result;
};

/**
 * @description this solution works for both positive and negative
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
const subarraySum = function (nums, k) {
  let result = 0;
  let current_sum = 0;
  let prefix_map = {}; // prefix sum as key and index will be value

  for (let index = 0; index < nums.length; index++) {
    current_sum += nums[index];

    if (current_sum === k) result++;

    if (prefix_map[current_sum - k]) {
      result += prefix_map[current_sum - k];
    }

    prefix_map[current_sum] === undefined
      ? (prefix_map[current_sum] = 1)
      : prefix_map[current_sum]++;
  }

  return result;
};
