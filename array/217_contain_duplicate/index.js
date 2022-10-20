/**
 * [Problem ref]{@link  https://leetcode.com/problems/contains-duplicate/}
 * @description Given an integer array nums, 
 * return true if any value appears at least twice in the array, 
 * and return false if every element is distinct.
 */

/**
 * @param {number[]} nums
 * @return {boolean}
 */
const containsDuplicate = function(nums) {
    const visited ={}

    for (let index = 0; index < nums.length; index++) {
      const element = nums[index];
      if (visited[element]) {
        return true
      }
      visited[element] = true
    }

    return false
};