/**
 * @param {number[]} nums
 * @return {boolean}
 */
const canPartition = function (nums) {
  const total = nums.reduce((a, b) => a + b);
  if (total % 2) return false;

  const target = parseInt(total / 2);
  let dp = new Map();
  dp.set(0, true);

  for (const n of nums) {
    const nextDp = new Map();
    for (const s of dp.keys()) {
      if (s + n === target) return true;
      nextDp.set(s + n, true);
      nextDp.set(s, true);
    }
    dp = nextDp;
  }

  return dp.has(target);
};
