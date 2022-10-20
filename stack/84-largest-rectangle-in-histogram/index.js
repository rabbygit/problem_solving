/**
 * [Problem ref]{@link https://leetcode.com/problems/largest-rectangle-in-histogram/submissions/}
 * @description Given an array of integers heights representing the histogram's bar height where the width of each bar is 1,
 * return the area of the largest rectangle in the histogram.
 */

/**
 * @param {number[]} heights
 * @return {number}
 */
const largestRectangleArea = function (heights) {
  let maxArea = 0;
  const stack = [];

  for (let i = 0; i < heights.length; i++) {
    startIndex = i;

    while (stack.length && stack[stack.length - 1].height > heights[i]) {
      const { index, height } = stack.pop();
      maxArea = Math.max(maxArea, height * (i - index));
      startIndex = index;
    }

    stack.push({ index: startIndex, height: heights[i] });
  }

  for (let i = 0; i < stack.length; i++) {
    const { index, height } = stack[i];
    maxArea = Math.max(maxArea, height * (heights.length - index));
  }

  return maxArea;
};