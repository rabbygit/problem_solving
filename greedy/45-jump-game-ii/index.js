/**
 * @param {number[]} nums
 * @return {number}
 */
const jump = function (nums) {
  let left = 0;
  let right = 0;
  let result = 0;

  while (right < nums.length - 1) {
    let farthest = 0;

    for (let i = left; i < right + 1; i++) {
      farthest = Math.max(farthest, i + nums[i]);
    }

    left = right + 1;
    right = farthest;
    result++;
  }

  return result;
};
