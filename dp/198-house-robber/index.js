/**
 * @param {number[]} nums
 * @return {number}
 */
const rob = function (nums) {
  nums.push(0);

  for (let i = nums.length - 3; i > -1; i--) {
    nums[i] = Math.max(nums[i] + nums[i + 2], nums[i + 1]);
  }

  return Math.max(nums[0], nums[1]);
};
