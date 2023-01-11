/**
 * [Problem ref]{@link https://leetcode.com/problems/powx-n/}
 */

/**
 * @param {number} x
 * @param {number} n
 * @return {number}
 */
const myPow = function (x, n) {
  function square(x, n) {
    if (x === 0) return 0;
    if (n === 0) return 1;

    let result = square(x, parseInt(n / 2));
    result = result * result;

    if (n % 2 === 0) return result;
    return x * result;
  }

  let pow = square(x, Math.abs(n));

  if (n >= 0) return pow;
  return 1 / pow;
};
