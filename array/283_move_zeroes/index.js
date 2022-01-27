/**
 * @author Rabby Hossain
 * [Problem ref]{@link  https://leetcode.com/problems/move-zeroes/}
 * @description Given an integer array nums, move all 0's to the end of it
 * while maintaining the relative order of the non-zero elements.
 * Note that you must do this in-place without making a copy of the array.
 */

/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
const moveZeroes = function (nums) {
  let replace_idx = 0

  for (let index = 0; index < nums.length; index++) {
    if (nums[index] !== 0) {
      if (replace_idx !== index) {
        nums[replace_idx] = nums[index]
        nums[index] = 0
      }
      replace_idx++
    }
  }
};