/**
 * @param {number[]} nums
 * @return {number}
 */
const minMoves = function (nums) {
  let res = 0;
  let minNum = Math.min(...nums);
  for (const n of nums) {
    res += n - minNum;
  }
  return res;
};
