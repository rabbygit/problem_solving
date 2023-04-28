/**
 * @param {number[]} nums
 * @return {number}
 */
const missingNumber = function (nums) {
  let result = nums.length;

  for (let index = 0; index < nums.length; index++) {
    result = result ^ index ^ nums[index];
  }

  return result;
};
