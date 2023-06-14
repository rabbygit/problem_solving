/**
 * @param {number[]} nums
 * @param {number} threshold
 * @return {number}
 */
const smallestDivisor = function (nums, threshold) {
  let l = 1;
  let r = 10e6;

  while (l <= r) {
    const divisor = l + parseInt((r - l) / 2);
    const sum = calculateSum(nums, divisor);
    sum > threshold ? (l = divisor + 1) : (r = divisor - 1);
  }

  return l;
};

const calculateSum = (nums, divisor) => {
  let sum = 0;
  for (const num of nums) {
    sum += Math.ceil(num / divisor);
  }
  return sum;
};
