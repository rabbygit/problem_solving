/**
 * @author Rabby Hossain
 * [Problem ref]{@link  https://leetcode.com/problems/subarray-sum-equals-k/}
 * @description Given an array of integers nums and an integer k, 
 * return the total number of subarrays whose sum equals to k.
 * A subarray is a contiguous non-empty sequence of elements within an array.
 */

/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
const subarraySum = function (nums, k) {
  let current_sum = 0
  let start_idx = 0
  let result = 0

  for (let index = 0; index < nums.length; index++) {
    current_sum += nums[index]

    while (current_sum > k && start_idx < index) {
      current_sum -= nums[start_idx++]
    }


    if (current_sum === k) {
      result++
    }
  }

  return result
};

console.log(subarraySum([1], 0))