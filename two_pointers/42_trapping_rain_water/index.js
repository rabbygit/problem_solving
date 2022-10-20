/**
 * [Problem ref]{@link  https://leetcode.com/problems/trapping-rain-water/}
 * @description Given n non-negative integers representing an elevation map where the width of each bar is 1,
 * compute how much water it can trap after raining.
 */

/**
 * @param {number[]} height
 * @return {number}
 */
const trap = function (height) {
  let result = 0;
  let left = 0;
  let right = height.length - 1;
  let leftMax = height[left];
  let rightMax = height[right];

  while (left < right) {
    if (leftMax < rightMax) {
      left++;
      leftMax = Math.max(leftMax, height[left]);
      result += leftMax - height[left];
    } else {
      right--;
      rightMax = Math.max(rightMax, height[right]);
      result += rightMax - height[right];
    }
  }

  return result;
};
