/**
 * [Problem ref]{@link  https://leetcode.com/problems/3sum/}
 * @description Given an integer array nums, return all the triplets
 * [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
 */

const threeSum = function (nums) {
  const result = [];
  const len = nums.length;
  nums = nums.sort((a, b) => a - b);

  for (let i = 0; i < len; i++) {
    if (i > 0 && nums[i] === nums[i - 1]) continue;

    let left = i + 1;
    let right = len - 1;

    while (left < right) {
      const sum = nums[i] + nums[left] + nums[right];

      if (sum === 0) {
        result.push([nums[i], nums[left], nums[right]]);
        left++;
        // avoid same element
        while (left < right && nums[left] === nums[left - 1]) {
          left++;
        }
      } else if (sum > 0) {
        right--;
      } else {
        left++;
      }
    }
  }

  return result;
};
