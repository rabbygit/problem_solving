/**
 * @param {number[]} nums
 * @return {number}
 */
const arraySign = function (nums) {
  let total_negative = 0;
  for (const n of nums) {
    if (n === 0) {
      return 0;
    } else if (n < 0) {
      total_negative++;
    }
  }

  if (total_negative % 2 === 0) {
    return 1;
  }

  return -1;
};
