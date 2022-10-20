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
  const result = []

  function generate(l, r, sub_result) {
    // opening and closing parentheis are all used
    if (!l && !r) {
      result.push(sub_result);
      return;
    }

    // go further when remaining opening parenthesis count is greater
    if (l > r) {
      return
    }

    // add opening parenthesis if remains
    if (l) {
      generate(l - 1, r, sub_result + '(');
    }

    // add closing parenthesis if remains
    if (r) {
      generate(l, r - 1, sub_result + ')');
    }
  }

  generate(n, n, '');

  return result;
};

console.log(generateParenthesis(3));