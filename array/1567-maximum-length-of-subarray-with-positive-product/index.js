/**
 * @param {number[]} nums
 * @return {number}
 */
const getMaxLen = function (nums) {
  let res = 0;
  let i = 0;

  while (i < nums.length) {
    let start = i;
    let end = i;
    let firstNegative = -1;
    let lastNegative = -1;
    let totalNegative = 0;

    // [0(start), 1, -2, -3, -4, 0(end)];
    while (start < nums.length && nums[start] === 0) start++;

    while (end < nums.length && nums[end] !== 0) {
      if (nums[end] < 0) {
        totalNegative++;
        if (firstNegative === -1) firstNegative = end;
        lastNegative = end;
      }
      end++;
    }

    if (totalNegative % 2 === 0) {
      res = Math.max(res, end - start);
    } else {
      if (firstNegative !== -1) {
        res = Math.max(res, end - firstNegative - 1);
      }
      if (lastNegative !== -1) {
        res = Math.max(res, lastNegative - start);
      }
    }

    i = end + 1;
  }

  return res;
};
