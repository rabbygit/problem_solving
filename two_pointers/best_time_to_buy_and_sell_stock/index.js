/**
 * @param {number[]} prices
 * @return {number}
 * Complexity: Time:- O(n) , Space:- O(n)
 */
const maxProfit = function (prices) {
  let diff = 0;
  const rightMaxArray = new Array(prices.length);
  let rightMax = prices[prices.length - 1];

  for (let index = prices.length - 1; index > -1; index--) {
    rightMax = Math.max(rightMax, prices[index]);
    rightMaxArray[index] = rightMax;
  }

  for (let index = 0; index < prices.length - 1; index++) {
    diff = Math.max(diff, rightMaxArray[index + 1] - prices[index]);
  }

  return diff;
};

/**
 * @param {number[]} prices
 * @return {number}
 * Complexity: Time:- O(n) , Space:- O(1)
 */
const maxProfit1 = function (prices) {
  let left = 0;
  let right = 1;
  let max = 0;

  while (left < prices.length) {
    if (prices[left] < prices[right]) {
      max = Math.max(max, prices[right] - prices[left]);
    } else {
      left = right;
    }

    right++;
  }

  return max;
};
