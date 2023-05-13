/**
 * @param {number[]} nums
 * @return {boolean}
 */
const canJump = function (nums) {
  let des = nums.length - 1;

  for (let index = nums.length - 1; index > -1; index--) {
    if (index + nums[index] >= des) {
      des = index;
    }
  }

  return des === 0 ? true : false;
};
