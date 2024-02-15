/**
 * @param {number[]} nums
 * @return {number}
 */
const largestPerimeter = function (nums) {
  let result = -1;
  let prefixSum = 0;
  nums.sort((a, b) => a - b);

  for (const n of nums) {
    if (prefixSum > n) {
      result = prefixSum + n;
    }
    prefixSum += n;
  }

  return result;
};
