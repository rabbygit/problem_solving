/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[][]}
 */
const divideArray = function (nums, k) {
  const res = [];
  nums.sort((a, b) => a - b);

  for (let i = 0; i < nums.length / 3; i++) {
    let idx = i * 3;
    if (nums[idx + 2] - sub[idx] > k) return [];
    res.push(nums.slice(idx, idx + 3));
  }

  return res;
};
