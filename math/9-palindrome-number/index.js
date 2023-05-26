/**
 * [Problem ref]{@link https://leetcode.com/problems/palindrome-number/}
 * @description An integer is a palindrome when it reads the same backward as forward.
 */

/**
 * @param {number} x
 * @return {boolean}
 */
const isPalindrome = function (x) {
  // filter all negative integers
  if (x < 0) return false;

  // reverse the integer
  let result = 0;
  let n = x;
  while (n) {
    const digit = n % 10; //  Get right-most digit. Ex. 123 % 10 → 3
    result = result * 10 + digit; //  Ex. 123 → 1230 + 4 → 1234
    n = parseInt(n / 10); //  Remove right-most digit. Ex. 123 → 12.3 → 12
  }

  return result == x;
};
