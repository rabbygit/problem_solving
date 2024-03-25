/**
 * [Problem ref]{@link  https://leetcode.com/problems/find-all-duplicates-in-an-array/}
 * @description Given an integer array nums of length n where all the integers of nums are in the range [1, n] and
 * each integer appears once or twice, return an array of all the integers that appears twice.
 * You must write an algorithm that runs in O(n) time and uses only constant extra space
 */

/**
 * @param {number[]} nums
 * @return {number[]}
 */
const findDuplicates = function (nums) {
  const result = [];

  for (const n of nums) {
    const idx = Math.abs(n) - 1;
    if (nums[idx] < 0) {
      result.push(idx + 1);
    }
    nums[idx] = -nums[idx];
  }

  return result;
};
