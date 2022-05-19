/**
 * @author Rabby Hossain
 * [Problem ref]{@link  https://leetcode.com/problems/majority-element/}
 * @description Given an array nums of size n, return the majority element.
 * The majority element is the element that appears more than ⌊n / 2⌋ times. 
 * You may assume that the majority element always exists in the array.
 */


/**
 * @param {number[]} nums
 * @return {number}
 */
const majorityElement = function (nums) {
  /**
   * Using BOYER MOORE MAJORITY VOTE ALGORITHM
   * Time complexity: O(n)
   * Space complexity: O(1)
   */

  let count = 0
  let majority = null

  for (const num of nums) {
    // consider current element is the majority element
    if (count === 0) {
      majority = num
    }

    if (majority === num) {
      // increase majority count
      count++
    } else {
      // decrease count for anything else
      count--
    }
  }

  // It's guaranteed that majority element exists by the problem description
  return majority
};