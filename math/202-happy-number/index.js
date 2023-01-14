/**
 * [Problem ref]{@link https://leetcode.com/problems/happy-number/description/}
 */

/**
 * @param {number} n
 * @return {boolean}
 */
const isHappy = function (n) {
  const visited = new Map();

  while (!visited.get(n)) {
    visited.set(n, true);
    n = calculateSum(n);
    if (n === 1) {
      return true;
    }
  }

  return false;
};

function calculateSum(n) {
  let sum = 0;

  while (n) {
    const digit = n % 10;
    sum += Math.pow(digit, 2);
    n = parseInt(n / 10);
  }

  return sum;
}
