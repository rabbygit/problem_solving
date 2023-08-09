/**
 * @param {number[]} arr
 * @param {number} k
 * @return {number}
 */
const getWinner = function (arr, k) {
  let currMax = arr[0];
  let winCount = 0;

  for (let i = 1; i < arr.length; i++) {
    if (arr[i] > currMax) {
      currMax = arr[i];
      winCount = 0;
    }
    winCount++;
    if (winCount === k) return currMax;
  }

  return currMax;
};
