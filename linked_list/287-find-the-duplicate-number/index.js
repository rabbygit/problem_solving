/**
 * [Problem ref]{@link  https://leetcode.com/problems/find-the-duplicate-number/}
 * @description Given an array of integers nums containing n + 1 integers where
 * each integer is in the range [1, n] inclusive.
 * There is only one repeated number in nums,
 * return this repeated number.
 * You must solve the problem without modifying the array nums and uses only constant extra space.
 */

/**
 * @param {number[]} nums
 * @return {number}
 * Explaination: https://www.youtube.com/watch?v=wjYnzkAhcNk&t=336s&ab_channel=NeetCode
 */
const findDuplicate = function (nums) {
  // Solved through Floyd's algorithm
  let slow = 0;
  let fast = 0;

  while (true) {
    slow = nums[slow];
    fast = nums[nums[fast]];
    if (fast === slow) {
      break;
    }
  }

  let slow2 = 0;
  while (true) {
    slow2 = nums[slow2];
    slow = nums[slow];
    if (slow === slow2) {
      return slow;
    }
  }
};
