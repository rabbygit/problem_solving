/**
 * @param {number} target
 * @param {number[]} nums
 * @return {number}
 */
const minSubArrayLen = function (target, nums) {
  let l = 0;
  let sum = 0;
  let minLength = nums.length + 1;

  for (let r = 0; r < nums.length; r++) {
    sum += nums[r];
    while (sum >= target) {
      minLength = Math.min(minLength, r - l + 1);
      sum -= nums[l];
      l++;
    }
  }

  return minLength == nums.length + 1 ? 0 : minLength;
};
