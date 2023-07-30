/**
 * @param {number[]} nums
 * @return {number}
 */
const pivotIndex = function (nums) {
  let leftSum = 0;
  let rightSum = 0;

  for (const num of nums) rightSum += num;

  for (let idx = 0; idx < nums.length; idx++) {
    rightSum -= nums[idx];
    if (leftSum === rightSum) return idx;
    leftSum += nums[idx];
  }

  return -1;
};
