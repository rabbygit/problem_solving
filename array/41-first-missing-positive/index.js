/**
 * @param {number[]} nums
 * @return {number}
 */
const firstMissingPositive = function (nums) {
  for (let i = 0; i < nums.length; i++) {
    if (nums[i] < 0) nums[i] = 0;
  }

  for (let i = 0; i < nums.length; i++) {
    const value = Math.abs(nums[i]);
    if (value >= 1 && value <= nums.length) {
      if (nums[value - 1] > 0) {
        nums[value - 1] *= -1;
      } else if (nums[value - 1] === 0) {
        nums[value - 1] = -1 * (nums.length + 1);
      }
    }
  }

  for (let i = 1; i <= nums.length; i++) {
    if (nums[i - 1] >= 0) {
      return i;
    }
  }

  return nums.length + 1;
};
