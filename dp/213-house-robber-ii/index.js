/**
 * @param {number[]} nums
 * @return {number}
 */
const rob = function (nums) {
  if (nums.length === 1) {
    return nums[0];
  }

  return Math.max(findMaxRob(nums.slice(1)), findMaxRob(nums.slice(0, -1)));
};

function findMaxRob(nums) {
  nums.push(0);

  for (let i = nums.length - 3; i > -1; i--) {
    nums[i] = Math.max(nums[i] + nums[i + 2], nums[i + 1]);
  }

  return Math.max(nums[0], nums[1]);
}
