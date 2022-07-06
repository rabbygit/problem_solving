/**
 * @author Rabby Hossain
 * [Problem ref]{@link  https://leetcode.com/problems/container-with-most-water/}
 * @description You are given an integer array height of length n.
 * There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
 * Find two lines that together with the x-axis form a container, such that the container contains the most water.
 * Return the maximum amount of water a container can store.
 */

/**
 * @param {number[]} height
 * @return {number}
 */
const maxArea = function (height) {
  let largest_area = 0;
  let left = 0;
  let right = height.length - 1;

  while (left < right) {
    if (height[left] < height[right]) {
      largest_area = Math.max(largest_area, height[left] * (right - left));
      left++;
    } else {
      largest_area = Math.max(largest_area, height[right] * (right - left));
      right--;
    }
  }

  return largest_area;
};
