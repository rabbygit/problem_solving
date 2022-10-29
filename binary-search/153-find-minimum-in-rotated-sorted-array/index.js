/**
 * [Problem ref]{@link  https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/}
 */

/**
 * @param {number[]} nums
 * @return {number}
 */
const findMin = function (nums) {
  let left = 0;
  let right = nums.length - 1;
  let minNum = Number.POSITIVE_INFINITY;

  while (left <= right) {
    const mid = parseInt((left + right) / 2);

    minNum = Math.min(minNum, nums[mid]);

    if (nums[left] <= nums[mid]) {
      if (nums[right] < nums[mid]) {
        left = mid + 1;
      } else {
        right = mid - 1;
      }
    } else {
      if (nums[right] > nums[mid] || nums[right] > nums[left]) {
        right = mid - 1;
      } else {
        left = mid + 1;
      }
    }
  }

  return minNum;
};
