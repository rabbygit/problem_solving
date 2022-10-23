/**
 * [Problem ref]{@link  https://leetcode.com/problems/binary-search/}
 * @description Given an array of integers nums which is sorted in ascending order,
 * and an integer target, write a function to search target in nums.
 * If target exists, then return its index. Otherwise, return -1.
 * You must write an algorithm with O(log n) runtime complexity.
 */

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
const search = function (nums, target) {
  let start = 0;
  let end = nums.length - 1;

  while (start <= end) {
    mid = parseInt((start + end) / 2);

    if (target === nums[mid]) {
      return mid;
    } else if (target > nums[mid]) {
      start = mid + 1;
    } else {
      end = mid - 1;
    }
  }

  return -1;
};
