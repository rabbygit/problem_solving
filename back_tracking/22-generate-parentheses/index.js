/**
 * [Problem ref]{@link https://leetcode.com/problems/generate-parentheses/}
 * @description Given n pairs of parentheses,
 * write a function to generate all combinations of well-formed parentheses.
 */

/**
 * @param {number} n
 * @return {string[]}
 */
const generateParenthesis = function (n) {
  const result = [];

  function generate(l, r, sub_result) {
    // opening and closing parentheis are all used
    if (l === n && r === n) {
      result.push(sub_result);
      return;
    }

    // add opening parenthesis if remains
    if (l < n) generate(l + 1, r, sub_result + "(");

    // add closing parenthesis if we have more open parentheses
    if (l > r) generate(l, r + 1, sub_result + ")");
  }

  generate(0, 0, "");

  return result;
};
