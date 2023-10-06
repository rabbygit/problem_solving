/**
 * @param {number[]} nums
 * @return {number[]}
 */
const sortedSquares = function (nums) {
  let l = 0;
  let r = nums.length - 1;
  let idx = r;
  const res = new Array(nums.length).fill(0);

  while (l <= r) {
    if (Math.abs(nums[l]) > Math.abs(nums[r])) {
      res[idx] = nums[l] * nums[l];
      l++;
    } else {
      res[idx] = nums[r] * nums[r];
      r--;
    }

    idx--;
  }

  return res;
};
