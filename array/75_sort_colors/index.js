/**
 * @author Rabby Hossain
 * [Problem ref]{@link  https://leetcode.com/problems/sort-colors/}
 * @description Given an array nums with n objects colored red, white, or blue, 
 * sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
 * We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
 * You must solve this problem without using the library's sort function.
 */


/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
const sortColorsTwoPass = function (nums) {
  let red = 0
  let white = 0
  let blue = 0

  for (let index = 0; index < nums.length; index++) {
    if (nums[index] === 0) {
      red++
    } else if (nums[index] === 1) {
      white++
    } else {
      blue++
    }
  }

  white += red
  blue += white

  for (let index = 0; index < nums.length; index++) {
    if (index < red) {
      nums[index] = 0
    } else if (index >= red && index < white) {
      nums[index] = 1
    } else {
      nums[index] = 2
    }
  }

  return nums
};

/**
 * @description one pass
 * @param {*} nums 
 * @returns 
 */
const sortColors = function (nums) {
  let red_idx = 0
  let white_idx = 0
  let blue_idx = nums.length - 1

  while (white_idx <= blue_idx) {
    if (nums[white_idx] === 0) {
      swap(nums, red_idx, white_idx)
      red_idx++
      white_idx++
    } else if (nums[white_idx] === 1) {
      white_idx++
    } else {
      swap(nums, blue_idx, white_idx)
      blue_idx--
    }
  }

  return nums
};

/**
 * @description helper function to swap
 * @param {*} nums 
 * @param {*} a 
 * @param {*} b 
 */
const swap = (nums, a, b) => {
  let temp = nums[a]
  nums[a] = nums[b]
  nums[b] = temp
}