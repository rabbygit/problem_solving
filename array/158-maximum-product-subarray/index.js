/**
 * @param {number[]} nums
 * @return {number}
 */
const maxProduct = function (nums) {
  let result = Math.max(...nums);
  let currMax = 1;
  let currMin = 1;

  for (const n of nums) {
    if (n === 0) {
      currMax = 1;
      currMin = 1;
    }

    tempMax = n * currMax;
    currMax = Math.max(tempMax, n * currMin, n);
    currMin = Math.min(tempMax, n * currMin, n);
    result = Math.max(result, currMax);
  }

  return result;
};
